"""Integration test for DataSync — real store."""
import pytest
import os
import importlib.util
import types
import time as _time
import uuid as _uuid

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'datasync')

# Load models
models_spec = importlib.util.spec_from_file_location(
    'models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

DataSyncStore = models_mod.DataSyncStore
InvalidRequestException = models_mod.InvalidRequestException
ResourceNotFoundException = models_mod.ResourceNotFoundException
AgentRecord = models_mod.AgentRecord
LocationRecord = models_mod.LocationRecord
TaskRecord = models_mod.TaskRecord
TaskExecutionRecord = models_mod.TaskExecutionRecord


def _load_handler(op_name, globals_inject=None):
    """Load a handler .code.py file — injects names and returns handler function."""
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    mod.InvalidRequestException = InvalidRequestException
    mod.ResourceNotFoundException = ResourceNotFoundException
    mod.AgentRecord = AgentRecord
    mod.LocationRecord = LocationRecord
    mod.TaskRecord = TaskRecord
    mod.TaskExecutionRecord = TaskExecutionRecord
    mod.time = _time
    mod.uuid = _uuid
    mod.dataclass = lambda f: f
    if globals_inject:
        for name, value in globals_inject.items():
            setattr(mod, name, value)
    spec.loader.exec_module(mod)
    skip_names = {'dataclass', 'time', 'uuid', '<lambda>'}
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
                and not v.__name__.startswith('_')
                and v.__name__ not in skip_names):
            return v
    return None


class TestAgent:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = DataSyncStore()
        return self._store

    def test_create_agent_happy(self):
        handler = _load_handler('CreateAgent')
        resp = handler(self.store, {"ActivationKey": "KEY12345"})
        assert "AgentArn" in resp

    def test_create_agent_with_optional_fields(self):
        handler = _load_handler('CreateAgent')
        resp = handler(self.store, {
            "ActivationKey": "KEY67890",
            "AgentName": "test-agent",
            "Tags": [{"Key": "env", "Value": "test"}],
        })
        assert "AgentArn" in resp

    def test_create_agent_missing_required(self):
        handler = _load_handler('CreateAgent')
        with pytest.raises(KeyError):
            handler(self.store, {})

    def test_describe_agent_happy(self):
        handler = _load_handler('CreateAgent')
        resp = handler(self.store, {"ActivationKey": "KEY-AAA"})
        arn = resp["AgentArn"]
        desc_handler = _load_handler('DescribeAgent')
        desc = desc_handler(self.store, {"AgentArn": arn})
        assert desc["AgentArn"] == arn

    def test_describe_agent_nonexistent(self):
        handler = _load_handler('DescribeAgent')
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {"AgentArn": "arn:aws:datasync:us-east-1:000000000000:agent/agent-none"})

    def test_list_agents(self):
        handler = _load_handler('ListAgents')
        resp = handler(self.store, {})
        assert "Agents" in resp

    def test_delete_agent_happy(self):
        create = _load_handler('CreateAgent')
        resp = create(self.store, {"ActivationKey": "KEY-DEL"})
        arn = resp["AgentArn"]
        dhandler = _load_handler('DeleteAgent')
        result = dhandler(self.store, {"AgentArn": arn})
        assert result == {}
        dhandler2 = _load_handler('DescribeAgent')
        with pytest.raises(ResourceNotFoundException):
            dhandler2(self.store, {"AgentArn": arn})

    def test_delete_agent_nonexistent(self):
        handler = _load_handler('DeleteAgent')
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {"AgentArn": "arn:nonexistent"})

    def test_update_agent_happy(self):
        create = _load_handler('CreateAgent')
        resp = create(self.store, {"ActivationKey": "KEY-UPD", "AgentName": "old-name"})
        arn = resp["AgentArn"]
        uhandler = _load_handler('UpdateAgent')
        uhandler(self.store, {"AgentArn": arn, "Name": "new-name"})
        dhandler = _load_handler('DescribeAgent')
        desc = dhandler(self.store, {"AgentArn": arn})
        assert desc["AgentName"] == "new-name"


class TestLocation:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = DataSyncStore()
        return self._store

    def test_create_location_s3_happy(self):
        handler = _load_handler('CreateLocationS3')
        resp = handler(self.store, {
            "S3BucketArn": "arn:aws:s3:::my-test-bucket",
            "S3Config": {"BucketAccessRoleArn": "arn:aws:iam::000000000000:role/TestRole"},
        })
        assert "LocationArn" in resp

    def test_create_location_nfs_happy(self):
        handler = _load_handler('CreateLocationNfs')
        resp = handler(self.store, {
            "Subdirectory": "/export/test",
            "ServerHostname": "nfs.example.com",
            "OnPremConfig": {"AgentArns": ["arn:aws:datasync:us-east-1:000000000000:agent/agent-abc"]},
        })
        assert "LocationArn" in resp

    def test_create_location_s3_missing_required(self):
        handler = _load_handler('CreateLocationS3')
        with pytest.raises(KeyError):
            handler(self.store, {})

    def test_list_locations(self):
        handler = _load_handler('ListLocations')
        resp = handler(self.store, {})
        assert "Locations" in resp

    def test_delete_location_happy(self):
        create = _load_handler('CreateLocationS3')
        resp = create(self.store, {
            "S3BucketArn": "arn:aws:s3:::delete-me",
            "S3Config": {"BucketAccessRoleArn": "arn:aws:iam::000000000000:role/TestRole"},
        })
        arn = resp["LocationArn"]
        dhandler = _load_handler('DeleteLocation')
        result = dhandler(self.store, {"LocationArn": arn})
        assert result == {}

    def test_delete_location_nonexistent(self):
        handler = _load_handler('DeleteLocation')
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {"LocationArn": "arn:nonexistent"})

    def test_describe_location_s3_happy(self):
        create = _load_handler('CreateLocationS3')
        resp = create(self.store, {
            "S3BucketArn": "arn:aws:s3:::desc-me",
            "S3Config": {"BucketAccessRoleArn": "arn:aws:iam::000000000000:role/TestRole"},
        })
        arn = resp["LocationArn"]
        dhandler = _load_handler('DescribeLocationS3')
        desc = dhandler(self.store, {"LocationArn": arn})
        assert desc["LocationArn"] == arn


class TestTask:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = DataSyncStore()
        return self._store

    def _create_source_location(self):
        create_loc = _load_handler('CreateLocationS3')
        resp = create_loc(self.store, {
            "S3BucketArn": "arn:aws:s3:::source-bucket",
            "S3Config": {"BucketAccessRoleArn": "arn:aws:iam::000000000000:role/TaskRole"},
        })
        return resp["LocationArn"]

    def _create_dest_location(self):
        create_loc = _load_handler('CreateLocationNfs')
        resp = create_loc(self.store, {
            "Subdirectory": "/export/dest",
            "ServerHostname": "nfs.dest.com",
            "OnPremConfig": {"AgentArns": ["arn:aws:datasync:us-east-1:000000000000:agent/agent-xyz"]},
        })
        return resp["LocationArn"]

    def test_create_task_happy(self):
        src = self._create_source_location()
        dst = self._create_dest_location()
        handler = _load_handler('CreateTask')
        resp = handler(self.store, {
            "SourceLocationArn": src,
            "DestinationLocationArn": dst,
            "Name": "test-task",
        })
        assert "TaskArn" in resp

    def test_create_task_missing_required(self):
        handler = _load_handler('CreateTask')
        with pytest.raises(TypeError):
            handler(self.store, {})

    def test_describe_task_happy(self):
        src = self._create_source_location()
        dst = self._create_dest_location()
        create = _load_handler('CreateTask')
        resp = create(self.store, {
            "SourceLocationArn": src,
            "DestinationLocationArn": dst,
        })
        arn = resp["TaskArn"]
        dhandler = _load_handler('DescribeTask')
        desc = dhandler(self.store, {"TaskArn": arn})
        assert desc["TaskArn"] == arn

    def test_describe_task_nonexistent(self):
        handler = _load_handler('DescribeTask')
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {"TaskArn": "arn:nonexistent"})

    def test_list_tasks(self):
        handler = _load_handler('ListTasks')
        resp = handler(self.store, {})
        assert "Tasks" in resp

    def test_delete_task_happy(self):
        src = self._create_source_location()
        dst = self._create_dest_location()
        create = _load_handler('CreateTask')
        resp = create(self.store, {
            "SourceLocationArn": src,
            "DestinationLocationArn": dst,
        })
        arn = resp["TaskArn"]
        dhandler = _load_handler('DeleteTask')
        result = dhandler(self.store, {"TaskArn": arn})
        assert result == {}

    def test_delete_task_nonexistent(self):
        handler = _load_handler('DeleteTask')
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {"TaskArn": "arn:nonexistent"})

    def test_update_task_happy(self):
        src = self._create_source_location()
        dst = self._create_dest_location()
        create = _load_handler('CreateTask')
        resp = create(self.store, {
            "SourceLocationArn": src,
            "DestinationLocationArn": dst,
            "Name": "old-task-name",
        })
        arn = resp["TaskArn"]
        uhandler = _load_handler('UpdateTask')
        uhandler(self.store, {"TaskArn": arn, "Name": "updated-task-name"})
        dhandler = _load_handler('DescribeTask')
        desc = dhandler(self.store, {"TaskArn": arn})
        assert desc["Name"] == "updated-task-name"


class TestTaskExecution:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = DataSyncStore()
        return self._store

    def _create_task(self):
        create_loc_s3 = _load_handler('CreateLocationS3')
        src = create_loc_s3(self.store, {
            "S3BucketArn": "arn:aws:s3:::exec-source",
            "S3Config": {"BucketAccessRoleArn": "arn:aws:iam::000000000000:role/ExecRole"},
        })["LocationArn"]
        create_loc_nfs = _load_handler('CreateLocationNfs')
        dst = create_loc_nfs(self.store, {
            "Subdirectory": "/export/exec-dest",
            "ServerHostname": "nfs.exec.com",
            "OnPremConfig": {"AgentArns": ["arn:aws:datasync:us-east-1:000000000000:agent/agent-exec"]},
        })["LocationArn"]
        create = _load_handler('CreateTask')
        return create(self.store, {
            "SourceLocationArn": src,
            "DestinationLocationArn": dst,
        })["TaskArn"]

    def test_start_task_execution_happy(self):
        task_arn = self._create_task()
        handler = _load_handler('StartTaskExecution')
        resp = handler(self.store, {"TaskArn": task_arn})
        assert "TaskExecutionArn" in resp

    def test_start_task_execution_nonexistent_task(self):
        handler = _load_handler('StartTaskExecution')
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {"TaskArn": "arn:nonexistent"})

    def test_describe_task_execution_happy(self):
        task_arn = self._create_task()
        start = _load_handler('StartTaskExecution')
        resp = start(self.store, {"TaskArn": task_arn})
        exec_arn = resp["TaskExecutionArn"]
        dhandler = _load_handler('DescribeTaskExecution')
        desc = dhandler(self.store, {"TaskExecutionArn": exec_arn})
        assert desc["TaskExecutionArn"] == exec_arn
        assert desc["TaskArn"] == task_arn

    def test_describe_task_execution_nonexistent(self):
        handler = _load_handler('DescribeTaskExecution')
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {"TaskExecutionArn": "arn:nonexistent"})


class TestTags:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = DataSyncStore()
        return self._store

    def _create_agent(self):
        create = _load_handler('CreateAgent')
        return create(self.store, {"ActivationKey": "TAGKEY"})["AgentArn"]

    def test_tag_resource_happy(self):
        arn = self._create_agent()
        handler = _load_handler('TagResource')
        result = handler(self.store, {
            "ResourceArn": arn,
            "Tags": [{"Key": "env", "Value": "production"}],
        })
        assert result == {}

    def test_tag_resource_nonexistent(self):
        handler = _load_handler('TagResource')
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {
                "ResourceArn": "arn:nonexistent",
                "Tags": [{"Key": "x", "Value": "y"}],
            })

    def test_list_tags_for_resource_happy(self):
        arn = self._create_agent()
        tag_handler = _load_handler('TagResource')
        tag_handler(self.store, {
            "ResourceArn": arn,
            "Tags": [{"Key": "env", "Value": "test"}, {"Key": "team", "Value": "data"}],
        })
        list_handler = _load_handler('ListTagsForResource')
        resp = list_handler(self.store, {"ResourceArn": arn})
        assert "Tags" in resp
        assert len(resp["Tags"]) == 2
        keys = {t["Key"] for t in resp["Tags"]}
        assert "env" in keys
        assert "team" in keys

    def test_list_tags_for_resource_nonexistent(self):
        handler = _load_handler('ListTagsForResource')
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {"ResourceArn": "arn:nonexistent"})
