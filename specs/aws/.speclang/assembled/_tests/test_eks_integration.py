"""Integration test for EKS — real EKSStore against generated handlers."""
import pytest
import os
import importlib.util
import types

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'eks')

# Load models module
models_spec = importlib.util.spec_from_file_location(
    'models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

EKSStore = models_mod.EKSStore
ResourceNotFoundException = models_mod.ResourceNotFoundException
ResourceInUseException = models_mod.ResourceInUseException
InvalidParameterException = models_mod.InvalidParameterException

SKIP_NAMES = {'<lambda>'}
HANDLER_DIR = SERVICE_DIR


def _load_handler(op_name):
    """Load a single-handler .code.py file."""
    path = os.path.join(HANDLER_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
            and not v.__name__.startswith('_')
            and v.__name__ not in SKIP_NAMES):
            return v
    raise RuntimeError(f"No handler found in {op_name}")


# ── Cluster Tests ──────────────────────────────────────────────

class TestClusterIntegration:

    @pytest.fixture
    def store(self):
        return EKSStore()

    def test_create_cluster_happy(self, store):
        h = _load_handler('CreateCluster')
        resp = h(store, {
            "name": "test-cluster",
            "roleArn": "arn:aws:iam::123456789012:role/EKSClusterRole",
            "resourcesVpcConfig": {
                "subnetIds": ["subnet-abc123"],
                "securityGroupIds": ["sg-abc123"]
            }
        })
        assert resp is not None
        assert "cluster" in resp
        assert resp["cluster"]["name"] == "test-cluster"
        assert resp["cluster"]["status"] == "ACTIVE"
        assert resp["cluster"]["arn"].startswith("arn:aws:eks:")

    def test_create_cluster_duplicate(self, store):
        h = _load_handler('CreateCluster')
        h(store, {"name": "dup-cluster", "roleArn": "arn:aws:iam::123456789012:role/R",
                  "resourcesVpcConfig": {"subnetIds": ["subnet-1"]}})
        with pytest.raises(ResourceInUseException):
            h(store, {"name": "dup-cluster", "roleArn": "arn:aws:iam::123456789012:role/R",
                      "resourcesVpcConfig": {"subnetIds": ["subnet-1"]}})

    def test_describe_cluster_happy(self, store):
        create = _load_handler('CreateCluster')
        create(store, {"name": "desc-cluster", "roleArn": "arn:aws:iam::123456789012:role/R",
                       "resourcesVpcConfig": {"subnetIds": ["subnet-1"]}})
        h = _load_handler('DescribeCluster')
        resp = h(store, {"name": "desc-cluster"})
        assert resp["cluster"]["name"] == "desc-cluster"
        assert "version" in resp["cluster"]

    def test_describe_cluster_notfound(self, store):
        h = _load_handler('DescribeCluster')
        with pytest.raises(ResourceNotFoundException):
            h(store, {"name": "nonexistent"})

    def test_list_clusters(self, store):
        create = _load_handler('CreateCluster')
        create(store, {"name": "c1", "roleArn": "arn:aws:iam::123456789012:role/R",
                       "resourcesVpcConfig": {"subnetIds": ["subnet-1"]}})
        create(store, {"name": "c2", "roleArn": "arn:aws:iam::123456789012:role/R",
                       "resourcesVpcConfig": {"subnetIds": ["subnet-1"]}})
        h = _load_handler('ListClusters')
        resp = h(store, {})
        assert "clusters" in resp
        assert "c1" in resp["clusters"]
        assert "c2" in resp["clusters"]

    def test_delete_cluster_happy(self, store):
        create = _load_handler('CreateCluster')
        create(store, {"name": "del-me", "roleArn": "arn:aws:iam::123456789012:role/R",
                       "resourcesVpcConfig": {"subnetIds": ["subnet-1"]}})
        h = _load_handler('DeleteCluster')
        resp = h(store, {"name": "del-me"})
        assert resp["cluster"]["status"] == "DELETING"

        # Verify gone
        desc = _load_handler('DescribeCluster')
        with pytest.raises(ResourceNotFoundException):
            desc(store, {"name": "del-me"})

    def test_delete_cluster_notfound(self, store):
        h = _load_handler('DeleteCluster')
        with pytest.raises(ResourceNotFoundException):
            h(store, {"name": "no-such-cluster"})

    def test_update_cluster_config(self, store):
        create = _load_handler('CreateCluster')
        create(store, {"name": "upd-cluster", "roleArn": "arn:aws:iam::123456789012:role/R",
                       "resourcesVpcConfig": {"subnetIds": ["subnet-1"]}})
        h = _load_handler('UpdateClusterConfig')
        resp = h(store, {
            "name": "upd-cluster",
            "logging": {"clusterLogging": [{"types": ["api"], "enabled": True}]}
        })
        assert "update" in resp
        assert resp["update"]["status"] == "Successful"

    def test_update_cluster_version(self, store):
        create = _load_handler('CreateCluster')
        create(store, {"name": "ver-cluster", "roleArn": "arn:aws:iam::123456789012:role/R",
                       "resourcesVpcConfig": {"subnetIds": ["subnet-1"]}})
        h = _load_handler('UpdateClusterVersion')
        resp = h(store, {"name": "ver-cluster", "version": "1.33"})
        assert resp["update"]["status"] == "Successful"


# ── Nodegroup Tests ─────────────────────────────────────────────

class TestNodegroupIntegration:

    @pytest.fixture
    def store(self):
        s = EKSStore()
        s.create_cluster(name="ng-cluster", roleArn="arn:aws:iam::123456789012:role/R",
                         resourcesVpcConfig={"subnetIds": ["subnet-1"]})
        return s

    def test_create_nodegroup_happy(self, store):
        h = _load_handler('CreateNodegroup')
        resp = h(store, {
            "clusterName": "ng-cluster",
            "nodegroupName": "ng-1",
            "subnets": ["subnet-1"]
        })
        assert resp["nodegroup"]["nodegroupName"] == "ng-1"
        assert resp["nodegroup"]["status"] == "ACTIVE"

    def test_create_nodegroup_missing_cluster(self, store):
        h = _load_handler('CreateNodegroup')
        with pytest.raises(ResourceNotFoundException):
            h(store, {"clusterName": "no-such", "nodegroupName": "ng-1",
                      "subnets": ["subnet-1"]})

    def test_create_nodegroup_duplicate(self, store):
        h = _load_handler('CreateNodegroup')
        h(store, {"clusterName": "ng-cluster", "nodegroupName": "ng-dup",
                  "subnets": ["subnet-1"]})
        with pytest.raises(ResourceInUseException):
            h(store, {"clusterName": "ng-cluster", "nodegroupName": "ng-dup",
                      "subnets": ["subnet-1"]})

    def test_describe_nodegroup(self, store):
        create = _load_handler('CreateNodegroup')
        create(store, {"clusterName": "ng-cluster", "nodegroupName": "ng-desc",
                       "subnets": ["subnet-1"]})
        h = _load_handler('DescribeNodegroup')
        resp = h(store, {"clusterName": "ng-cluster", "nodegroupName": "ng-desc"})
        assert resp["nodegroup"]["nodegroupName"] == "ng-desc"

    def test_describe_nodegroup_notfound(self, store):
        h = _load_handler('DescribeNodegroup')
        with pytest.raises(ResourceNotFoundException):
            h(store, {"clusterName": "ng-cluster", "nodegroupName": "no-such-ng"})

    def test_list_nodegroups(self, store):
        create = _load_handler('CreateNodegroup')
        create(store, {"clusterName": "ng-cluster", "nodegroupName": "ng-a", "subnets": ["subnet-1"]})
        create(store, {"clusterName": "ng-cluster", "nodegroupName": "ng-b", "subnets": ["subnet-1"]})
        h = _load_handler('ListNodegroups')
        resp = h(store, {"clusterName": "ng-cluster"})
        assert "ng-a" in resp["nodegroups"]
        assert "ng-b" in resp["nodegroups"]

    def test_delete_nodegroup(self, store):
        create = _load_handler('CreateNodegroup')
        create(store, {"clusterName": "ng-cluster", "nodegroupName": "ng-del",
                       "subnets": ["subnet-1"]})
        h = _load_handler('DeleteNodegroup')
        resp = h(store, {"clusterName": "ng-cluster", "nodegroupName": "ng-del"})
        assert resp["nodegroup"]["status"] == "DELETING"


# ── Fargate Profile Tests ───────────────────────────────────────

class TestFargateProfileIntegration:

    @pytest.fixture
    def store(self):
        s = EKSStore()
        s.create_cluster(name="fg-cluster", roleArn="arn:aws:iam::123456789012:role/R",
                         resourcesVpcConfig={"subnetIds": ["subnet-1"]})
        return s

    def test_create_fargate_happy(self, store):
        h = _load_handler('CreateFargateProfile')
        resp = h(store, {
            "clusterName": "fg-cluster",
            "fargateProfileName": "fp-1",
            "podExecutionRoleArn": "arn:aws:iam::123456789012:role/FargatePodRole"
        })
        assert resp["fargateProfile"]["fargateProfileName"] == "fp-1"
        assert resp["fargateProfile"]["status"] == "ACTIVE"

    def test_create_fargate_missing_cluster(self, store):
        h = _load_handler('CreateFargateProfile')
        with pytest.raises(ResourceNotFoundException):
            h(store, {"clusterName": "no-such", "fargateProfileName": "fp-1",
                      "podExecutionRoleArn": "arn:aws:iam::123456789012:role/R"})

    def test_describe_fargate(self, store):
        create = _load_handler('CreateFargateProfile')
        create(store, {"clusterName": "fg-cluster", "fargateProfileName": "fp-desc",
                       "podExecutionRoleArn": "arn:aws:iam::123456789012:role/R"})
        h = _load_handler('DescribeFargateProfile')
        resp = h(store, {"clusterName": "fg-cluster", "fargateProfileName": "fp-desc"})
        assert resp["fargateProfile"]["fargateProfileName"] == "fp-desc"

    def test_describe_fargate_notfound(self, store):
        h = _load_handler('DescribeFargateProfile')
        with pytest.raises(ResourceNotFoundException):
            h(store, {"clusterName": "fg-cluster", "fargateProfileName": "no-such-fp"})

    def test_list_fargate_profiles(self, store):
        create = _load_handler('CreateFargateProfile')
        create(store, {"clusterName": "fg-cluster", "fargateProfileName": "fp-a",
                       "podExecutionRoleArn": "arn:aws:iam::123456789012:role/R"})
        create(store, {"clusterName": "fg-cluster", "fargateProfileName": "fp-b",
                       "podExecutionRoleArn": "arn:aws:iam::123456789012:role/R"})
        h = _load_handler('ListFargateProfiles')
        resp = h(store, {"clusterName": "fg-cluster"})
        assert "fp-a" in resp["fargateProfileNames"]
        assert "fp-b" in resp["fargateProfileNames"]

    def test_delete_fargate(self, store):
        create = _load_handler('CreateFargateProfile')
        create(store, {"clusterName": "fg-cluster", "fargateProfileName": "fp-del",
                       "podExecutionRoleArn": "arn:aws:iam::123456789012:role/R"})
        h = _load_handler('DeleteFargateProfile')
        resp = h(store, {"clusterName": "fg-cluster", "fargateProfileName": "fp-del"})
        assert resp["fargateProfile"]["status"] == "DELETING"


# ── Addon Tests ─────────────────────────────────────────────────

class TestAddonIntegration:

    @pytest.fixture
    def store(self):
        s = EKSStore()
        s.create_cluster(name="addon-cluster", roleArn="arn:aws:iam::123456789012:role/R",
                         resourcesVpcConfig={"subnetIds": ["subnet-1"]})
        return s

    def test_create_addon_happy(self, store):
        h = _load_handler('CreateAddon')
        resp = h(store, {"clusterName": "addon-cluster", "addonName": "vpc-cni",
                         "addonVersion": "v1.15.0-eksbuild.1"})
        assert resp["addon"]["addonName"] == "vpc-cni"
        assert resp["addon"]["status"] == "ACTIVE"

    def test_create_addon_missing_cluster(self, store):
        h = _load_handler('CreateAddon')
        with pytest.raises(ResourceNotFoundException):
            h(store, {"clusterName": "no-such", "addonName": "vpc-cni"})

    def test_describe_addon(self, store):
        create = _load_handler('CreateAddon')
        create(store, {"clusterName": "addon-cluster", "addonName": "kube-proxy"})
        h = _load_handler('DescribeAddon')
        resp = h(store, {"clusterName": "addon-cluster", "addonName": "kube-proxy"})
        assert resp["addon"]["addonName"] == "kube-proxy"

    def test_list_addons(self, store):
        create = _load_handler('CreateAddon')
        create(store, {"clusterName": "addon-cluster", "addonName": "vpc-cni"})
        create(store, {"clusterName": "addon-cluster", "addonName": "coredns"})
        h = _load_handler('ListAddons')
        resp = h(store, {"clusterName": "addon-cluster"})
        assert "coredns" in resp["addons"]
        assert "vpc-cni" in resp["addons"]

    def test_delete_addon(self, store):
        create = _load_handler('CreateAddon')
        create(store, {"clusterName": "addon-cluster", "addonName": "del-addon"})
        h = _load_handler('DeleteAddon')
        resp = h(store, {"clusterName": "addon-cluster", "addonName": "del-addon"})
        assert resp["addon"]["status"] == "DELETING"


# ── Access Entry Tests ──────────────────────────────────────────

class TestAccessEntryIntegration:

    @pytest.fixture
    def store(self):
        s = EKSStore()
        s.create_cluster(name="ae-cluster", roleArn="arn:aws:iam::123456789012:role/R",
                         resourcesVpcConfig={"subnetIds": ["subnet-1"]})
        return s

    def test_create_access_entry_happy(self, store):
        h = _load_handler('CreateAccessEntry')
        resp = h(store, {"clusterName": "ae-cluster",
                         "principalArn": "arn:aws:iam::123456789012:user/dev"})
        assert resp["accessEntry"]["principalArn"] == "arn:aws:iam::123456789012:user/dev"

    def test_create_access_entry_duplicate(self, store):
        h = _load_handler('CreateAccessEntry')
        h(store, {"clusterName": "ae-cluster", "principalArn": "arn:aws:iam::123456789012:user/dup"})
        with pytest.raises(ResourceInUseException):
            h(store, {"clusterName": "ae-cluster", "principalArn": "arn:aws:iam::123456789012:user/dup"})

    def test_describe_access_entry(self, store):
        create = _load_handler('CreateAccessEntry')
        create(store, {"clusterName": "ae-cluster", "principalArn": "arn:aws:iam::123456789012:user/dev"})
        h = _load_handler('DescribeAccessEntry')
        resp = h(store, {"clusterName": "ae-cluster", "principalArn": "arn:aws:iam::123456789012:user/dev"})
        assert resp["accessEntry"]["principalArn"] == "arn:aws:iam::123456789012:user/dev"

    def test_list_access_entries(self, store):
        create = _load_handler('CreateAccessEntry')
        create(store, {"clusterName": "ae-cluster", "principalArn": "arn:aws:iam::123456789012:user/a"})
        create(store, {"clusterName": "ae-cluster", "principalArn": "arn:aws:iam::123456789012:user/b"})
        h = _load_handler('ListAccessEntries')
        resp = h(store, {"clusterName": "ae-cluster"})
        assert len(resp["accessEntries"]) == 2

    def test_delete_access_entry(self, store):
        create = _load_handler('CreateAccessEntry')
        create(store, {"clusterName": "ae-cluster", "principalArn": "arn:aws:iam::123456789012:user/del"})
        h = _load_handler('DeleteAccessEntry')
        h(store, {"clusterName": "ae-cluster", "principalArn": "arn:aws:iam::123456789012:user/del"})
        # Verify deleted
        desc = _load_handler('DescribeAccessEntry')
        with pytest.raises(ResourceNotFoundException):
            desc(store, {"clusterName": "ae-cluster", "principalArn": "arn:aws:iam::123456789012:user/del"})


# ── Tag Tests ───────────────────────────────────────────────────

class TestTagIntegration:

    @pytest.fixture
    def store(self):
        s = EKSStore()
        s.create_cluster(name="tag-cluster", roleArn="arn:aws:iam::123456789012:role/R",
                         resourcesVpcConfig={"subnetIds": ["subnet-1"]})
        return s

    def test_tag_and_list(self, store):
        cluster_arn = store._clusters["tag-cluster"].arn
        tag_h = _load_handler('TagResource')
        tag_h(store, {"resourceArn": cluster_arn, "tags": {"env": "prod", "team": "platform"}})
        list_h = _load_handler('ListTagsForResource')
        resp = list_h(store, {"resourceArn": cluster_arn})
        assert resp["tags"]["env"] == "prod"
        assert resp["tags"]["team"] == "platform"

    def test_untag(self, store):
        cluster_arn = store._clusters["tag-cluster"].arn
        tag_h = _load_handler('TagResource')
        tag_h(store, {"resourceArn": cluster_arn, "tags": {"env": "prod", "team": "platform"}})
        untag_h = _load_handler('UntagResource')
        untag_h(store, {"resourceArn": cluster_arn, "tagKeys": ["team"]})
        list_h = _load_handler('ListTagsForResource')
        resp = list_h(store, {"resourceArn": cluster_arn})
        assert "env" in resp["tags"]
        assert "team" not in resp["tags"]

    def test_tag_nonexistent_resource(self, store):
        h = _load_handler('TagResource')
        with pytest.raises(ResourceNotFoundException):
            h(store, {"resourceArn": "arn:aws:eks:us-east-1:123456789012:cluster/no-such",
                      "tags": {"k": "v"}})


# ── Update Tests ────────────────────────────────────────────────

class TestUpdateIntegration:

    @pytest.fixture
    def store(self):
        s = EKSStore()
        s.create_cluster(name="upd-cluster", roleArn="arn:aws:iam::123456789012:role/R",
                         resourcesVpcConfig={"subnetIds": ["subnet-1"]})
        return s

    def test_list_updates(self, store):
        # Trigger an update
        upd = _load_handler('UpdateClusterVersion')
        upd(store, {"name": "upd-cluster", "version": "1.33"})
        h = _load_handler('ListUpdates')
        resp = h(store, {"name": "upd-cluster"})
        assert len(resp["updateIds"]) >= 1

    def test_describe_update(self, store):
        upd = _load_handler('UpdateClusterVersion')
        result = upd(store, {"name": "upd-cluster", "version": "1.34"})
        uid = result["update"]["id"]
        h = _load_handler('DescribeUpdate')
        resp = h(store, {"name": "upd-cluster", "updateId": uid})
        assert resp["update"]["id"] == uid
        assert resp["update"]["status"] == "Successful"


# ── Access Policy Tests ─────────────────────────────────────────

class TestAccessPolicyIntegration:

    @pytest.fixture
    def store(self):
        s = EKSStore()
        s.create_cluster(name="ap-cluster", roleArn="arn:aws:iam::123456789012:role/R",
                         resourcesVpcConfig={"subnetIds": ["subnet-1"]})
        s.create_access_entry(clusterName="ap-cluster",
                              principalArn="arn:aws:iam::123456789012:user/dev")
        return s

    def test_associate_and_list_policies(self, store):
        assoc = _load_handler('AssociateAccessPolicy')
        assoc(store, {"clusterName": "ap-cluster",
                      "principalArn": "arn:aws:iam::123456789012:user/dev",
                      "policyArn": "arn:aws:eks::aws:cluster-access-policy/AmazonEKSClusterAdminPolicy"})
        list_p = _load_handler('ListAssociatedAccessPolicies')
        resp = list_p(store, {"clusterName": "ap-cluster",
                              "principalArn": "arn:aws:iam::123456789012:user/dev"})
        assert len(resp["associatedAccessPolicies"]) == 1
        assert "AmazonEKSClusterAdminPolicy" in resp["associatedAccessPolicies"][0]["policyArn"]

    def test_disassociate_policy(self, store):
        assoc = _load_handler('AssociateAccessPolicy')
        assoc(store, {"clusterName": "ap-cluster",
                      "principalArn": "arn:aws:iam::123456789012:user/dev",
                      "policyArn": "arn:aws:eks::aws:cluster-access-policy/AmazonEKSClusterAdminPolicy"})
        dis = _load_handler('DisassociateAccessPolicy')
        dis(store, {"clusterName": "ap-cluster",
                    "principalArn": "arn:aws:iam::123456789012:user/dev",
                    "policyArn": "arn:aws:eks::aws:cluster-access-policy/AmazonEKSClusterAdminPolicy"})
        list_p = _load_handler('ListAssociatedAccessPolicies')
        resp = list_p(store, {"clusterName": "ap-cluster",
                              "principalArn": "arn:aws:iam::123456789012:user/dev"})
        assert len(resp["associatedAccessPolicies"]) == 0


# ── Error path: delete cluster with node groups ─────────────────

class TestDeleteConstraints:

    @pytest.fixture
    def store(self):
        s = EKSStore()
        s.create_cluster(name="busy-cluster", roleArn="arn:aws:iam::123456789012:role/R",
                         resourcesVpcConfig={"subnetIds": ["subnet-1"]})
        s.create_nodegroup(clusterName="busy-cluster", nodegroupName="ng-1",
                           subnets=["subnet-1"])
        return s

    def test_delete_cluster_with_nodegroups_fails(self, store):
        h = _load_handler('DeleteCluster')
        with pytest.raises(ResourceInUseException):
            h(store, {"name": "busy-cluster"})
