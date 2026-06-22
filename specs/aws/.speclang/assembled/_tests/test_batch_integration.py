"""Integration tests for AWS Batch — real store, generated handlers."""
import pytest
import os
import importlib.util
import types

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'batch')

# ── Load models ──
models_spec = importlib.util.spec_from_file_location(
    'models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

BatchStore = models_mod.BatchStore
ClientException = models_mod.ClientException

# ── Handler loader ──
def _load_handler(op_name):
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    mod.ClientException = ClientException
    spec.loader.exec_module(mod)
    skip = {'ClientException'}
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
                and not v.__name__.startswith('_')
                and v.__name__ not in skip):
            return v
    raise RuntimeError(f"No handler in {op_name}")


# ═══════════════════════════════════════════════════════════════════════
# Compute Environments
# ═══════════════════════════════════════════════════════════════════════

class TestComputeEnvironments:
    @pytest.fixture
    def store(self):
        return BatchStore()

    def test_create_ce_happy(self, store):
        h = _load_handler('CreateComputeEnvironment')
        resp = h(store, {
            "computeEnvironmentName": "test-ce",
            "type": "MANAGED",
            "serviceRole": "arn:aws:iam::000000000000:role/test",
        })
        assert resp["computeEnvironmentName"] == "test-ce"
        assert "computeEnvironmentArn" in resp

    def test_create_duplicate_fails(self, store):
        h = _load_handler('CreateComputeEnvironment')
        h(store, {"computeEnvironmentName": "test-ce2", "type": "MANAGED",
                   "serviceRole": "arn:aws:iam::000000000000:role/test"})
        with pytest.raises(ClientException):
            h(store, {"computeEnvironmentName": "test-ce2", "type": "MANAGED",
                       "serviceRole": "arn:aws:iam::000000000000:role/test"})

    def test_describe_ce(self, store):
        create = _load_handler('CreateComputeEnvironment')
        desc = _load_handler('DescribeComputeEnvironments')
        create(store, {"computeEnvironmentName": "test-ce3", "type": "MANAGED",
                        "serviceRole": "arn:aws:iam::000000000000:role/test"})
        resp = desc(store, {"computeEnvironments": ["test-ce3"]})
        assert len(resp["computeEnvironments"]) == 1

    def test_describe_all_ces(self, store):
        create = _load_handler('CreateComputeEnvironment')
        desc = _load_handler('DescribeComputeEnvironments')
        create(store, {"computeEnvironmentName": "ce-a", "type": "MANAGED",
                        "serviceRole": "arn:aws:iam::000000000000:role/test"})
        create(store, {"computeEnvironmentName": "ce-b", "type": "MANAGED",
                        "serviceRole": "arn:aws:iam::000000000000:role/test"})
        resp = desc(store, {})
        assert len(resp["computeEnvironments"]) == 2

    def test_update_ce(self, store):
        create = _load_handler('CreateComputeEnvironment')
        update = _load_handler('UpdateComputeEnvironment')
        desc = _load_handler('DescribeComputeEnvironments')
        create(store, {"computeEnvironmentName": "ce-upd", "type": "MANAGED",
                        "serviceRole": "arn:aws:iam::000000000000:role/test"})
        update(store, {"computeEnvironment": "ce-upd", "state": "DISABLED"})
        resp = desc(store, {"computeEnvironments": ["ce-upd"]})
        assert resp["computeEnvironments"][0]["state"] == "DISABLED"

    def test_delete_ce(self, store):
        create = _load_handler('CreateComputeEnvironment')
        delete = _load_handler('DeleteComputeEnvironment')
        desc = _load_handler('DescribeComputeEnvironments')
        create(store, {"computeEnvironmentName": "ce-del", "type": "MANAGED",
                        "serviceRole": "arn:aws:iam::000000000000:role/test"})
        delete(store, {"computeEnvironment": "ce-del"})
        resp = desc(store, {"computeEnvironments": ["ce-del"]})
        assert len(resp["computeEnvironments"]) == 0


# ═══════════════════════════════════════════════════════════════════════
# Job Queues
# ═══════════════════════════════════════════════════════════════════════

class TestJobQueues:
    @pytest.fixture
    def store(self):
        return BatchStore()

    def test_create_jq_happy(self, store):
        h = _load_handler('CreateJobQueue')
        resp = h(store, {
            "jobQueueName": "test-jq",
            "computeEnvironmentOrder": [{
                "computeEnvironment": "test-ce",
                "order": 1,
            }],
        })
        assert resp["jobQueueName"] == "test-jq"

    def test_describe_jq(self, store):
        create = _load_handler('CreateJobQueue')
        desc = _load_handler('DescribeJobQueues')
        create(store, {"jobQueueName": "jq1", "computeEnvironmentOrder": [
            {"computeEnvironment": "ce", "order": 1}]})
        resp = desc(store, {"jobQueues": ["jq1"]})
        assert len(resp["jobQueues"]) == 1

    def test_update_jq(self, store):
        create = _load_handler('CreateJobQueue')
        update = _load_handler('UpdateJobQueue')
        desc = _load_handler('DescribeJobQueues')
        create(store, {"jobQueueName": "jq-upd", "computeEnvironmentOrder": [
            {"computeEnvironment": "ce", "order": 1}]})
        update(store, {"jobQueue": "jq-upd", "state": "DISABLED"})
        resp = desc(store, {"jobQueues": ["jq-upd"]})
        assert resp["jobQueues"][0]["state"] == "DISABLED"

    def test_delete_jq(self, store):
        create = _load_handler('CreateJobQueue')
        delete = _load_handler('DeleteJobQueue')
        desc = _load_handler('DescribeJobQueues')
        create(store, {"jobQueueName": "jq-del", "computeEnvironmentOrder": [
            {"computeEnvironment": "ce", "order": 1}]})
        delete(store, {"jobQueue": "jq-del"})
        resp = desc(store, {"jobQueues": ["jq-del"]})
        assert len(resp["jobQueues"]) == 0


# ═══════════════════════════════════════════════════════════════════════
# Job Definitions
# ═══════════════════════════════════════════════════════════════════════

class TestJobDefinitions:
    @pytest.fixture
    def store(self):
        return BatchStore()

    def test_register_jd(self, store):
        h = _load_handler('RegisterJobDefinition')
        resp = h(store, {
            "jobDefinitionName": "test-jd",
            "type": "container",
            "containerProperties": {"image": "busybox", "vcpus": 1, "memory": 128},
        })
        assert resp["jobDefinitionName"] == "test-jd"
        assert resp["revision"] == 1

    def test_register_multiple_revisions(self, store):
        h = _load_handler('RegisterJobDefinition')
        h(store, {"jobDefinitionName": "test-jd2", "type": "container",
                   "containerProperties": {"image": "busybox", "vcpus": 1, "memory": 128}})
        resp = h(store, {"jobDefinitionName": "test-jd2", "type": "container",
                          "containerProperties": {"image": "busybox", "vcpus": 2, "memory": 256}})
        assert resp["revision"] == 2

    def test_describe_jd(self, store):
        register = _load_handler('RegisterJobDefinition')
        desc = _load_handler('DescribeJobDefinitions')
        register(store, {"jobDefinitionName": "test-jd3", "type": "container",
                          "containerProperties": {"image": "busybox", "vcpus": 1, "memory": 128}})
        resp = desc(store, {"jobDefinitionName": "test-jd3"})
        assert len(resp["jobDefinitions"]) == 1

    def test_deregister_jd(self, store):
        register = _load_handler('RegisterJobDefinition')
        deregister = _load_handler('DeregisterJobDefinition')
        register(store, {"jobDefinitionName": "test-jd4", "type": "container",
                          "containerProperties": {"image": "busybox", "vcpus": 1, "memory": 128}})
        deregister(store, {
            "jobDefinition": "arn:aws:batch:us-east-1:000000000000:job-definition/test-jd4:1",
        })
        # Should not raise
        assert True


# ═══════════════════════════════════════════════════════════════════════
# Jobs
# ═══════════════════════════════════════════════════════════════════════

class TestJobs:
    @pytest.fixture
    def store(self):
        return BatchStore()

    def test_submit_job(self, store):
        h = _load_handler('SubmitJob')
        resp = h(store, {
            "jobName": "test-job",
            "jobQueue": "test-queue",
            "jobDefinition": "test-jd:1",
        })
        assert "jobId" in resp
        assert resp["jobName"] == "test-job"

    def test_describe_jobs(self, store):
        submit = _load_handler('SubmitJob')
        desc = _load_handler('DescribeJobs')
        result = submit(store, {"jobName": "job1", "jobQueue": "q1",
                                 "jobDefinition": "jd:1"})
        resp = desc(store, {"jobs": [result["jobId"]]})
        assert len(resp["jobs"]) == 1
        assert resp["jobs"][0]["jobName"] == "job1"

    def test_list_jobs(self, store):
        submit = _load_handler('SubmitJob')
        list_j = _load_handler('ListJobs')
        submit(store, {"jobName": "job-a", "jobQueue": "qa", "jobDefinition": "jd:1"})
        submit(store, {"jobName": "job-b", "jobQueue": "qa", "jobDefinition": "jd:1"})
        resp = list_j(store, {"jobQueue": "qa"})
        assert len(resp["jobSummaryList"]) == 2

    def test_cancel_job(self, store):
        submit = _load_handler('SubmitJob')
        cancel = _load_handler('CancelJob')
        desc = _load_handler('DescribeJobs')
        result = submit(store, {"jobName": "job-c", "jobQueue": "q", "jobDefinition": "jd:1"})
        cancel(store, {"jobId": result["jobId"], "reason": "testing"})
        resp = desc(store, {"jobs": [result["jobId"]]})
        assert resp["jobs"][0]["status"] == "FAILED"

    def test_terminate_job(self, store):
        submit = _load_handler('SubmitJob')
        terminate = _load_handler('TerminateJob')
        desc = _load_handler('DescribeJobs')
        result = submit(store, {"jobName": "job-t", "jobQueue": "q", "jobDefinition": "jd:1"})
        terminate(store, {"jobId": result["jobId"], "reason": "testing"})
        resp = desc(store, {"jobs": [result["jobId"]]})
        assert resp["jobs"][0]["status"] == "FAILED"

    def test_describe_nonexistent_job(self, store):
        h = _load_handler('DescribeJobs')
        resp = h(store, {"jobs": ["nonexistent"]})
        assert len(resp["jobs"]) == 0


# ═══════════════════════════════════════════════════════════════════════
# Scheduling Policies
# ═══════════════════════════════════════════════════════════════════════

class TestSchedulingPolicies:
    @pytest.fixture
    def store(self):
        return BatchStore()

    def test_create_sp(self, store):
        h = _load_handler('CreateSchedulingPolicy')
        resp = h(store, {"name": "test-sp", "fairsharePolicy": {
            "shareDecaySeconds": 300, "computeReservation": 50}})
        assert resp["name"] == "test-sp"
        assert "arn" in resp

    def test_describe_sp(self, store):
        create = _load_handler('CreateSchedulingPolicy')
        desc = _load_handler('DescribeSchedulingPolicies')
        result = create(store, {"name": "sp-desc", "fairsharePolicy": {}})
        resp = desc(store, {"arns": [result["arn"]]})
        assert len(resp["schedulingPolicies"]) == 1

    def test_list_sp(self, store):
        create = _load_handler('CreateSchedulingPolicy')
        list_sp = _load_handler('ListSchedulingPolicies')
        create(store, {"name": "sp-a", "fairsharePolicy": {}})
        create(store, {"name": "sp-b", "fairsharePolicy": {}})
        resp = list_sp(store, {})
        assert len(resp["schedulingPolicies"]) == 2

    def test_update_sp(self, store):
        create = _load_handler('CreateSchedulingPolicy')
        update = _load_handler('UpdateSchedulingPolicy')
        desc = _load_handler('DescribeSchedulingPolicies')
        result = create(store, {"name": "sp-upd", "fairsharePolicy": {
            "shareDecaySeconds": 300}})
        update(store, {"arn": result["arn"], "fairsharePolicy": {
            "shareDecaySeconds": 600}})
        resp = desc(store, {"arns": [result["arn"]]})
        assert resp["schedulingPolicies"][0]["fairsharePolicy"]["shareDecaySeconds"] == 600

    def test_delete_sp(self, store):
        create = _load_handler('CreateSchedulingPolicy')
        delete = _load_handler('DeleteSchedulingPolicy')
        desc = _load_handler('DescribeSchedulingPolicies')
        result = create(store, {"name": "sp-del", "fairsharePolicy": {}})
        delete(store, {"arn": result["arn"]})
        resp = desc(store, {"arns": [result["arn"]]})
        assert len(resp["schedulingPolicies"]) == 0


# ═══════════════════════════════════════════════════════════════════════
# Tags
# ═══════════════════════════════════════════════════════════════════════

class TestTags:
    @pytest.fixture
    def store(self):
        return BatchStore()

    def test_tag_resource(self, store):
        tag = _load_handler('TagResource')
        list_t = _load_handler('ListTagsForResource')
        tag(store, {"resourceArn": "arn:aws:batch:...", "tags": {"env": "test"}})
        resp = list_t(store, {"resourceArn": "arn:aws:batch:..."})
        assert resp["tags"]["env"] == "test"

    def test_untag_resource(self, store):
        tag = _load_handler('TagResource')
        untag = _load_handler('UntagResource')
        list_t = _load_handler('ListTagsForResource')
        tag(store, {"resourceArn": "arn:aws:batch:...", "tags": {"env": "test", "team": "x"}})
        untag(store, {"resourceArn": "arn:aws:batch:...", "tagKeys": ["env"]})
        resp = list_t(store, {"resourceArn": "arn:aws:batch:..."})
        assert "env" not in resp["tags"]
        assert resp["tags"]["team"] == "x"
