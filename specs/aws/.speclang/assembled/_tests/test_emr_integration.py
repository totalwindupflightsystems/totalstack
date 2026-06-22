"""Integration test for EMR — real store with generated handlers."""
import pytest
import os
import importlib.util
import types

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'emr')

models_spec = importlib.util.spec_from_file_location(
    'models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

EMRStore = models_mod.EMRStore
ClusterRecord = models_mod.ClusterRecord
ClusterNotFoundFault = models_mod.ClusterNotFoundFault
InvalidRequestException = models_mod.InvalidRequestException
AlreadyExistsException = models_mod.AlreadyExistsException


def _load_handler(op_name):
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    mod.ClusterNotFoundFault = ClusterNotFoundFault
    mod.InvalidRequestException = InvalidRequestException
    mod.AlreadyExistsException = AlreadyExistsException
    spec.loader.exec_module(mod)
    skip_names = {'dataclass', 'time', 'uuid', '<lambda>'}
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
                and not v.__name__.startswith('_')
                and v.__name__ not in skip_names):
            return v


# ─── Cluster Tests ────────────────────────────────────────────────────────────

class TestCluster:
    @pytest.fixture
    def store(self):
        return EMRStore()

    def test_run_job_flow(self, store):
        handler = _load_handler('RunJobFlow')
        response = handler(store, {
            "Name": "test-cluster",
            "Instances": {"MasterInstanceType": "m5.xlarge", "InstanceCount": 1},
            "ReleaseLabel": "emr-7.0.0",
        })
        assert "JobFlowId" in response
        assert response["JobFlowId"].startswith("j-")

    def test_describe_cluster(self, store):
        create = _load_handler('RunJobFlow')
        r = create(store, {"Name": "my-cluster", "Instances": {}})
        handler = _load_handler('DescribeCluster')
        response = handler(store, {"ClusterId": r["JobFlowId"]})
        assert response["Cluster"]["Name"] == "my-cluster"

    def test_describe_nonexistent(self, store):
        handler = _load_handler('DescribeCluster')
        with pytest.raises(ClusterNotFoundFault):
            handler(store, {"ClusterId": "j-nonexistent"})

    def test_list_clusters(self, store):
        create = _load_handler('RunJobFlow')
        create(store, {"Name": "c1", "Instances": {}})
        create(store, {"Name": "c2", "Instances": {}})
        handler = _load_handler('ListClusters')
        response = handler(store, {})
        assert len(response["Clusters"]) == 2

    def test_terminate_job_flows(self, store):
        create = _load_handler('RunJobFlow')
        r = create(store, {"Name": "kill-me", "Instances": {}})
        handler = _load_handler('TerminateJobFlows')
        handler(store, {"JobFlowIds": [r["JobFlowId"]]})
        c = store.clusters(r["JobFlowId"])
        assert c.Status["State"] == "TERMINATED"


# ─── Instance Fleet Tests ─────────────────────────────────────────────────────

class TestInstanceFleet:
    @pytest.fixture
    def store(self):
        s = EMRStore()
        r = s.run_job_flow("fleet-cluster", Instances={})
        return s, r

    def test_add_happy(self, store):
        s, cluster = store
        handler = _load_handler('AddInstanceFleet')
        response = handler(s, {
            "ClusterId": cluster.Id,
            "InstanceFleet": {"Name": "master-fleet", "InstanceFleetType": "MASTER",
                              "TargetOnDemandCapacity": 1, "TargetSpotCapacity": 0},
        })
        assert response["InstanceFleetId"].startswith("if-")

    def test_add_nonexistent_cluster(self, store):
        s, _ = store
        handler = _load_handler('AddInstanceFleet')
        with pytest.raises(ClusterNotFoundFault):
            handler(s, {"ClusterId": "j-no", "InstanceFleet": {}})

    def test_list(self, store):
        s, cluster = store
        handler = _load_handler('AddInstanceFleet')
        handler(s, {"ClusterId": cluster.Id, "InstanceFleet": {"Name": "f1"}})
        lst = _load_handler('ListInstanceFleets')
        response = lst(s, {"ClusterId": cluster.Id})
        assert len(response["InstanceFleets"]) == 1


# ─── Instance Group Tests ─────────────────────────────────────────────────────

class TestInstanceGroup:
    @pytest.fixture
    def store(self):
        s = EMRStore()
        r = s.run_job_flow("group-cluster", Instances={})
        return s, r

    def test_add_happy(self, store):
        s, cluster = store
        handler = _load_handler('AddInstanceGroups')
        response = handler(s, {
            "JobFlowId": cluster.Id,
            "InstanceGroups": [
                {"Name": "master", "InstanceRole": "MASTER",
                 "InstanceType": "m5.xlarge", "InstanceCount": 1},
                {"Name": "core", "InstanceRole": "CORE",
                 "InstanceType": "m5.xlarge", "InstanceCount": 2},
            ],
        })
        assert len(response["InstanceGroupIds"]) == 2

    def test_list(self, store):
        s, cluster = store
        add = _load_handler('AddInstanceGroups')
        add(s, {"JobFlowId": cluster.Id, "InstanceGroups": [
            {"Name": "master", "InstanceRole": "MASTER", "InstanceType": "m5.xlarge", "InstanceCount": 1}]})
        lst = _load_handler('ListInstanceGroups')
        response = lst(s, {"ClusterId": cluster.Id})
        assert len(response["InstanceGroups"]) == 1


# ─── Step Tests ───────────────────────────────────────────────────────────────

class TestStep:
    @pytest.fixture
    def store(self):
        s = EMRStore()
        r = s.run_job_flow("step-cluster", Instances={})
        return s, r

    def test_add_happy(self, store):
        s, cluster = store
        handler = _load_handler('AddJobFlowSteps')
        response = handler(s, {
            "JobFlowId": cluster.Id,
            "Steps": [{"Name": "test-step",
                       "HadoopJarStep": {"Jar": "s3://bucket/hadoop.jar"}}],
        })
        assert len(response["StepIds"]) == 1
        assert response["StepIds"][0].startswith("s-")

    def test_describe_and_list(self, store):
        s, cluster = store
        add = _load_handler('AddJobFlowSteps')
        r = add(s, {"JobFlowId": cluster.Id,
                     "Steps": [{"Name": "my-step",
                                "HadoopJarStep": {"Jar": "s3://x/jar"}}]})
        desc = _load_handler('DescribeStep')
        d = desc(s, {"ClusterId": cluster.Id, "StepId": r["StepIds"][0]})
        assert d["Step"]["Name"] == "my-step"
        lst = _load_handler('ListSteps')
        ls = lst(s, {"ClusterId": cluster.Id})
        assert len(ls["Steps"]) == 1

    def test_cancel(self, store):
        s, cluster = store
        add = _load_handler('AddJobFlowSteps')
        r = add(s, {"JobFlowId": cluster.Id,
                     "Steps": [{"Name": "cancel-me",
                                "HadoopJarStep": {"Jar": "s3://x/jar"}}]})
        handler = _load_handler('CancelSteps')
        handler(s, {"ClusterId": cluster.Id, "StepIds": r["StepIds"]})


# ─── Security Configuration Tests ─────────────────────────────────────────────

class TestSecurityConfiguration:
    @pytest.fixture
    def store(self):
        return EMRStore()

    def test_create_happy(self, store):
        handler = _load_handler('CreateSecurityConfiguration')
        response = handler(store, {
            "Name": "test-sec-config",
            "SecurityConfiguration": '{"EncryptionConfiguration": {}}',
        })
        assert response["Name"] == "test-sec-config"

    def test_create_duplicate(self, store):
        handler = _load_handler('CreateSecurityConfiguration')
        handler(store, {"Name": "dup", "SecurityConfiguration": "{}"})
        with pytest.raises(AlreadyExistsException):
            handler(store, {"Name": "dup", "SecurityConfiguration": "{}"})

    def test_describe(self, store):
        create = _load_handler('CreateSecurityConfiguration')
        create(store, {"Name": "my-config", "SecurityConfiguration": "{}"})
        desc = _load_handler('DescribeSecurityConfiguration')
        response = desc(store, {"Name": "my-config"})
        assert response["Name"] == "my-config"

    def test_describe_nonexistent(self, store):
        handler = _load_handler('DescribeSecurityConfiguration')
        with pytest.raises(InvalidRequestException):
            handler(store, {"Name": "no-such"})

    def test_list(self, store):
        create = _load_handler('CreateSecurityConfiguration')
        create(store, {"Name": "c1", "SecurityConfiguration": "{}"})
        create(store, {"Name": "c2", "SecurityConfiguration": "{}"})
        lst = _load_handler('ListSecurityConfigurations')
        response = lst(store, {})
        assert len(response["SecurityConfigurations"]) == 2

    def test_delete(self, store):
        create = _load_handler('CreateSecurityConfiguration')
        create(store, {"Name": "del-me", "SecurityConfiguration": "{}"})
        handler = _load_handler('DeleteSecurityConfiguration')
        handler(store, {"Name": "del-me"})
        desc = _load_handler('DescribeSecurityConfiguration')
        with pytest.raises(InvalidRequestException):
            desc(store, {"Name": "del-me"})


# ─── Studio Tests ─────────────────────────────────────────────────────────────

class TestStudio:
    @pytest.fixture
    def store(self):
        return EMRStore()

    def test_create_happy(self, store):
        handler = _load_handler('CreateStudio')
        response = handler(store, {
            "Name": "test-studio",
            "AuthMode": "SSO",
            "VpcId": "vpc-abc",
            "SubnetIds": ["subnet-1"],
            "ServiceRole": "arn:aws:iam::123456789012:role/EMRStudio",
        })
        assert response["StudioId"].startswith("es-")

    def test_describe(self, store):
        create = _load_handler('CreateStudio')
        r = create(store, {"Name": "my-studio", "AuthMode": "SSO",
                           "VpcId": "vpc-abc", "SubnetIds": ["subnet-1"],
                           "ServiceRole": "arn:aws:iam::123456789012:role/EMRStudio"})
        desc = _load_handler('DescribeStudio')
        response = desc(store, {"StudioId": r["StudioId"]})
        assert response["Studio"]["Name"] == "my-studio"

    def test_describe_nonexistent(self, store):
        handler = _load_handler('DescribeStudio')
        with pytest.raises(InvalidRequestException):
            handler(store, {"StudioId": "es-nonexistent"})

    def test_list(self, store):
        create = _load_handler('CreateStudio')
        create(store, {"Name": "s1", "AuthMode": "SSO",
                       "VpcId": "vpc-abc", "SubnetIds": ["subnet-1"],
                       "ServiceRole": "arn:aws:iam::123456789012:role/EMRStudio"})
        create(store, {"Name": "s2", "AuthMode": "SSO",
                       "VpcId": "vpc-abc", "SubnetIds": ["subnet-1"],
                       "ServiceRole": "arn:aws:iam::123456789012:role/EMRStudio"})
        lst = _load_handler('ListStudios')
        response = lst(store, {})
        assert len(response["Studios"]) == 2

    def test_update(self, store):
        create = _load_handler('CreateStudio')
        r = create(store, {"Name": "upd-studio", "AuthMode": "SSO",
                           "VpcId": "vpc-abc", "SubnetIds": ["subnet-1"],
                           "ServiceRole": "arn:aws:iam::123456789012:role/EMRStudio"})
        handler = _load_handler('UpdateStudio')
        handler(store, {"StudioId": r["StudioId"], "Description": "Updated"})

    def test_delete(self, store):
        create = _load_handler('CreateStudio')
        r = create(store, {"Name": "del-studio", "AuthMode": "SSO",
                           "VpcId": "vpc-abc", "SubnetIds": ["subnet-1"],
                           "ServiceRole": "arn:aws:iam::123456789012:role/EMRStudio"})
        handler = _load_handler('DeleteStudio')
        handler(store, {"StudioId": r["StudioId"]})
        desc = _load_handler('DescribeStudio')
        with pytest.raises(InvalidRequestException):
            desc(store, {"StudioId": r["StudioId"]})
