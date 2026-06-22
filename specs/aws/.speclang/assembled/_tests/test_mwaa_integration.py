"""Integration test for MWAA — real store with generated handlers."""
import os
import types
import importlib.util

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'mwaa')

# Dynamically load models.code.py
models_spec = importlib.util.spec_from_file_location(
    'models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

MWAAStore = models_mod.MWAAStore
EnvironmentRecord = models_mod.EnvironmentRecord
NetworkConfiguration = models_mod.NetworkConfiguration
LoggingConfiguration = models_mod.LoggingConfiguration
ModuleLoggingConfiguration = models_mod.ModuleLoggingConfiguration
ResourceNotFoundException = models_mod.ResourceNotFoundException
ValidationException = models_mod.ValidationException
InternalServerException = models_mod.InternalServerException
AccessDeniedException = models_mod.AccessDeniedException
RestApiClientException = models_mod.RestApiClientException
RestApiServerException = models_mod.RestApiServerException


def _load_handler(op_name):
    """Load a single-handler .code.py file."""
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    # Inject exceptions
    mod.ResourceNotFoundException = ResourceNotFoundException
    mod.ValidationException = ValidationException
    mod.InternalServerException = InternalServerException
    mod.AccessDeniedException = AccessDeniedException
    mod.RestApiClientException = RestApiClientException
    mod.RestApiServerException = RestApiServerException
    # Inject records
    mod.EnvironmentRecord = EnvironmentRecord
    mod.NetworkConfiguration = NetworkConfiguration
    mod.LoggingConfiguration = LoggingConfiguration
    mod.ModuleLoggingConfiguration = ModuleLoggingConfiguration
    # Inject stdlib
    mod.time = __import__('time')
    mod.uuid = __import__('uuid')
    spec.loader.exec_module(mod)
    # Find the handler (not exceptions, not records)
    skip_names = {'ResourceNotFoundException', 'ValidationException',
                  'InternalServerException', 'AccessDeniedException',
                  'RestApiClientException', 'RestApiServerException',
                  'EnvironmentRecord', 'NetworkConfiguration',
                  'LoggingConfiguration', 'ModuleLoggingConfiguration',
                  'time', 'uuid'}
    handler = None
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
                and not v.__name__.startswith('_')
                and v.__name__ not in skip_names):
            handler = v
            break
    return handler


class TestMWAAEnvironment:
    """Core environment CRUD operations."""

    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = MWAAStore()
        return self._store

    def test_create_environment_happy(self):
        handler = _load_handler('CreateEnvironment')
        resp = handler(self.store, {
            "Name": "test-env",
            "ExecutionRoleArn": "arn:aws:iam::000000000000:role/mwaa",
            "SourceBucketArn": "arn:aws:s3:::my-bucket",
            "DagS3Path": "dags/",
            "NetworkConfiguration": {
                "SecurityGroupIds": ["sg-12345"],
                "SubnetIds": ["subnet-abc", "subnet-def"],
            },
        })
        assert resp is not None
        assert "Arn" in resp
        assert "test-env" in resp["Arn"]

    def test_create_environment_with_all_fields(self):
        handler = _load_handler('CreateEnvironment')
        resp = handler(self.store, {
            "Name": "full-env",
            "ExecutionRoleArn": "arn:aws:iam::000000000000:role/mwaa",
            "SourceBucketArn": "arn:aws:s3:::my-bucket",
            "DagS3Path": "dags/",
            "NetworkConfiguration": {
                "SecurityGroupIds": ["sg-12345"],
                "SubnetIds": ["subnet-abc"],
            },
            "EnvironmentClass": "mw1.medium",
            "MaxWorkers": 25,
            "MinWorkers": 2,
            "Schedulers": 3,
            "AirflowVersion": "2.10.1",
            "WebserverAccessMode": "PUBLIC_ONLY",
            "Tags": {"env": "test", "team": "platform"},
        })
        assert resp is not None

    def test_create_environment_missing_required(self):
        handler = _load_handler('CreateEnvironment')
        try:
            handler(self.store, {})
            raise AssertionError("Expected ValidationException")
        except (ValidationException, TypeError):
            pass  # Missing required fields

    def test_create_environment_duplicate(self):
        handler = _load_handler('CreateEnvironment')
        handler(self.store, {
            "Name": "dup-env",
            "ExecutionRoleArn": "arn:aws:iam::000000000000:role/mwaa",
            "SourceBucketArn": "arn:aws:s3:::my-bucket",
            "DagS3Path": "dags/",
            "NetworkConfiguration": {"SecurityGroupIds": ["sg-1"], "SubnetIds": ["sub-1"]},
        })
        try:
            handler(self.store, {
                "Name": "dup-env",
                "ExecutionRoleArn": "arn:aws:iam::000000000000:role/mwaa",
                "SourceBucketArn": "arn:aws:s3:::my-bucket",
                "DagS3Path": "dags/",
                "NetworkConfiguration": {"SecurityGroupIds": ["sg-1"], "SubnetIds": ["sub-1"]},
            })
            raise AssertionError("Expected ValidationException for duplicate")
        except ValidationException:
            pass

    def test_get_environment_happy(self):
        create = _load_handler('CreateEnvironment')
        create(self.store, {
            "Name": "get-env",
            "ExecutionRoleArn": "arn:aws:iam::000000000000:role/mwaa",
            "SourceBucketArn": "arn:aws:s3:::my-bucket",
            "DagS3Path": "dags/",
            "NetworkConfiguration": {"SecurityGroupIds": ["sg-1"], "SubnetIds": ["sub-1"]},
        })
        handler = _load_handler('GetEnvironment')
        resp = handler(self.store, {"Name": "get-env"})
        assert "Environment" in resp
        assert resp["Environment"]["Name"] == "get-env"
        assert resp["Environment"]["Status"] == "CREATING"

    def test_get_environment_nonexistent(self):
        handler = _load_handler('GetEnvironment')
        try:
            handler(self.store, {"Name": "nonexistent"})
            raise AssertionError("Expected ResourceNotFoundException")
        except ResourceNotFoundException:
            pass

    def test_list_environments(self):
        create = _load_handler('CreateEnvironment')
        for i in range(3):
            create(self.store, {
                "Name": f"env-{i}",
                "ExecutionRoleArn": "arn:aws:iam::000000000000:role/mwaa",
                "SourceBucketArn": "arn:aws:s3:::my-bucket",
                "DagS3Path": "dags/",
                "NetworkConfiguration": {"SecurityGroupIds": ["sg-1"], "SubnetIds": ["sub-1"]},
            })
        handler = _load_handler('ListEnvironments')
        resp = handler(self.store, {})
        assert "Environments" in resp
        assert len(resp["Environments"]) == 3

    def test_update_environment_happy(self):
        create = _load_handler('CreateEnvironment')
        create(self.store, {
            "Name": "update-env",
            "ExecutionRoleArn": "arn:aws:iam::000000000000:role/mwaa",
            "SourceBucketArn": "arn:aws:s3:::my-bucket",
            "DagS3Path": "dags/",
            "NetworkConfiguration": {"SecurityGroupIds": ["sg-1"], "SubnetIds": ["sub-1"]},
        })
        update = _load_handler('UpdateEnvironment')
        resp = update(self.store, {
            "Name": "update-env",
            "MinWorkers": 5,
            "MaxWorkers": 50,
            "EnvironmentClass": "mw1.large",
        })
        assert resp is not None
        assert "Arn" in resp

    def test_update_environment_nonexistent(self):
        handler = _load_handler('UpdateEnvironment')
        try:
            handler(self.store, {"Name": "nonexistent", "MinWorkers": 5})
            raise AssertionError("Expected ResourceNotFoundException")
        except ResourceNotFoundException:
            pass

    def test_delete_environment_happy(self):
        create = _load_handler('CreateEnvironment')
        create(self.store, {
            "Name": "delete-env",
            "ExecutionRoleArn": "arn:aws:iam::000000000000:role/mwaa",
            "SourceBucketArn": "arn:aws:s3:::my-bucket",
            "DagS3Path": "dags/",
            "NetworkConfiguration": {"SecurityGroupIds": ["sg-1"], "SubnetIds": ["sub-1"]},
        })
        handler = _load_handler('DeleteEnvironment')
        resp = handler(self.store, {"Name": "delete-env"})
        assert resp == {}

    def test_delete_environment_nonexistent(self):
        handler = _load_handler('DeleteEnvironment')
        try:
            handler(self.store, {"Name": "nonexistent"})
            raise AssertionError("Expected ResourceNotFoundException")
        except ResourceNotFoundException:
            pass


class TestMWAATokens:
    """CLI and Web login token operations."""

    _store = None

    @property
    def store(self):
        if self._store is None:
            s = MWAAStore()
            handler = _load_handler('CreateEnvironment')
            handler(s, {
                "Name": "token-env",
                "ExecutionRoleArn": "arn:aws:iam::000000000000:role/mwaa",
                "SourceBucketArn": "arn:aws:s3:::my-bucket",
                "DagS3Path": "dags/",
                "NetworkConfiguration": {"SecurityGroupIds": ["sg-1"], "SubnetIds": ["sub-1"]},
            })
            TestMWAATokens._store = s
        return self._store

    def test_create_cli_token_happy(self):
        handler = _load_handler('CreateCliToken')
        resp = handler(self.store, {"Name": "token-env"})
        assert "CliToken" in resp
        assert "WebServerHostname" in resp
        assert len(resp["CliToken"]) > 0

    def test_create_cli_token_nonexistent(self):
        handler = _load_handler('CreateCliToken')
        try:
            handler(self.store, {"Name": "nonexistent"})
            raise AssertionError("Expected ResourceNotFoundException")
        except ResourceNotFoundException:
            pass

    def test_create_web_login_token_happy(self):
        handler = _load_handler('CreateWebLoginToken')
        resp = handler(self.store, {"Name": "token-env"})
        assert "WebToken" in resp
        assert "WebServerHostname" in resp
        assert "IamIdentity" in resp
        assert "AirflowIdentity" in resp

    def test_create_web_login_token_nonexistent(self):
        handler = _load_handler('CreateWebLoginToken')
        try:
            handler(self.store, {"Name": "nonexistent"})
            raise AssertionError("Expected ResourceNotFoundException")
        except ResourceNotFoundException:
            pass

    def test_invoke_rest_api_happy(self):
        handler = _load_handler('InvokeRestApi')
        resp = handler(self.store, {
            "Name": "token-env",
            "Path": "/api/v1/dags",
            "Method": "GET",
        })
        assert "RestApiStatusCode" in resp
        assert "RestApiResponse" in resp
        assert resp["RestApiStatusCode"] == 200

    def test_invoke_rest_api_nonexistent(self):
        handler = _load_handler('InvokeRestApi')
        try:
            handler(self.store, {
                "Name": "nonexistent",
                "Path": "/api/v1/dags",
                "Method": "GET",
            })
            raise AssertionError("Expected ResourceNotFoundException")
        except ResourceNotFoundException:
            pass


class TestMWAATags:
    """Tag operations."""

    _store = None
    _arn = None

    @property
    def store(self):
        if self._store is None:
            s = MWAAStore()
            handler = _load_handler('CreateEnvironment')
            resp = handler(s, {
                "Name": "tag-env",
                "ExecutionRoleArn": "arn:aws:iam::000000000000:role/mwaa",
                "SourceBucketArn": "arn:aws:s3:::my-bucket",
                "DagS3Path": "dags/",
                "NetworkConfiguration": {"SecurityGroupIds": ["sg-1"], "SubnetIds": ["sub-1"]},
                "Tags": {"env": "test"},
            })
            TestMWAATags._store = s
            TestMWAATags._arn = resp["Arn"]
        return self._store

    def test_list_tags_for_resource(self):
        handler = _load_handler('ListTagsForResource')
        resp = handler(self.store, {"ResourceArn": self._arn})
        assert "Tags" in resp
        assert resp["Tags"]["env"] == "test"

    def test_tag_resource(self):
        handler = _load_handler('TagResource')
        resp = handler(self.store, {
            "ResourceArn": self._arn,
            "Tags": {"team": "platform", "cost": "low"},
        })
        assert resp == {}
        # Verify
        list_handler = _load_handler('ListTagsForResource')
        resp2 = list_handler(self.store, {"ResourceArn": self._arn})
        assert resp2["Tags"]["team"] == "platform"
        assert resp2["Tags"]["cost"] == "low"

    def test_untag_resource(self):
        tag_handler = _load_handler('TagResource')
        tag_handler(self.store, {
            "ResourceArn": self._arn,
            "Tags": {"temp": "remove-me"},
        })
        handler = _load_handler('UntagResource')
        resp = handler(self.store, {
            "ResourceArn": self._arn,
            "tagKeys": ["temp"],
        })
        assert resp == {}
        list_handler = _load_handler('ListTagsForResource')
        resp2 = list_handler(self.store, {"ResourceArn": self._arn})
        assert "temp" not in resp2["Tags"]
        assert resp2["Tags"]["env"] == "test"  # original tag preserved

    def test_list_tags_nonexistent(self):
        handler = _load_handler('ListTagsForResource')
        try:
            handler(self.store, {"ResourceArn": "arn:aws:airflow:us-east-1:000000000000:environment/nonexistent"})
            raise AssertionError("Expected ResourceNotFoundException")
        except ResourceNotFoundException:
            pass

    def test_tag_resource_nonexistent(self):
        handler = _load_handler('TagResource')
        try:
            handler(self.store, {
                "ResourceArn": "arn:aws:airflow:us-east-1:000000000000:environment/nonexistent",
                "Tags": {"key": "val"},
            })
            raise AssertionError("Expected ResourceNotFoundException")
        except ResourceNotFoundException:
            pass


class TestMWAAMetrics:
    """PublishMetrics operation."""

    _store = None

    @property
    def store(self):
        if self._store is None:
            s = MWAAStore()
            handler = _load_handler('CreateEnvironment')
            handler(s, {
                "Name": "metrics-env",
                "ExecutionRoleArn": "arn:aws:iam::000000000000:role/mwaa",
                "SourceBucketArn": "arn:aws:s3:::my-bucket",
                "DagS3Path": "dags/",
                "NetworkConfiguration": {"SecurityGroupIds": ["sg-1"], "SubnetIds": ["sub-1"]},
            })
            TestMWAAMetrics._store = s
        return self._store

    def test_publish_metrics_happy(self):
        handler = _load_handler('PublishMetrics')
        resp = handler(self.store, {
            "EnvironmentName": "metrics-env",
            "MetricData": [
                {
                    "MetricName": "SchedulerHeartbeat",
                    "Timestamp": 1700000000,
                    "Value": 1.0,
                    "Unit": "Count",
                },
            ],
        })
        assert resp == {}

    def test_publish_metrics_nonexistent(self):
        handler = _load_handler('PublishMetrics')
        try:
            handler(self.store, {
                "EnvironmentName": "nonexistent",
                "MetricData": [],
            })
            raise AssertionError("Expected ResourceNotFoundException")
        except ResourceNotFoundException:
            pass
