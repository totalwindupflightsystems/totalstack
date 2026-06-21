"""Integration tests for CodeDeploy — real in-memory stores via generated handlers."""
import sys
import os
import types
import importlib.util
import pytest

# ── Paths ────────────────────────────────────────────────────
ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'codedeploy')

# ── Load models module ───────────────────────────────────────
models_spec = importlib.util.spec_from_file_location(
    'models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

# Pull out needed names
CodeDeployStore = models_mod.CodeDeployStore
ApplicationRecord = models_mod.ApplicationRecord
DeploymentConfigRecord = models_mod.DeploymentConfigRecord
DeploymentGroupRecord = models_mod.DeploymentGroupRecord
DeploymentRecord = models_mod.DeploymentRecord

# Exception classes
InvalidInputException = models_mod.InvalidInputException
ApplicationNameRequiredException = models_mod.ApplicationNameRequiredException
InvalidApplicationNameException = models_mod.InvalidApplicationNameException
ApplicationDoesNotExistException = models_mod.ApplicationDoesNotExistException
ApplicationAlreadyExistsException = models_mod.ApplicationAlreadyExistsException
ApplicationLimitExceededException = models_mod.ApplicationLimitExceededException
DeploymentConfigNameRequiredException = models_mod.DeploymentConfigNameRequiredException
InvalidDeploymentConfigNameException = models_mod.InvalidDeploymentConfigNameException
DeploymentConfigDoesNotExistException = models_mod.DeploymentConfigDoesNotExistException
DeploymentConfigAlreadyExistsException = models_mod.DeploymentConfigAlreadyExistsException
DeploymentConfigInUseException = models_mod.DeploymentConfigInUseException
DeploymentGroupNameRequiredException = models_mod.DeploymentGroupNameRequiredException
InvalidDeploymentGroupNameException = models_mod.InvalidDeploymentGroupNameException
DeploymentGroupDoesNotExistException = models_mod.DeploymentGroupDoesNotExistException
DeploymentGroupAlreadyExistsException = models_mod.DeploymentGroupAlreadyExistsException
DeploymentIdRequiredException = models_mod.DeploymentIdRequiredException
InvalidDeploymentIdException = models_mod.InvalidDeploymentIdException
DeploymentDoesNotExistException = models_mod.DeploymentDoesNotExistException
DeploymentAlreadyCompletedException = models_mod.DeploymentAlreadyCompletedException
InvalidRevisionException = models_mod.InvalidRevisionException
InvalidMinimumHealthyHostValueException = models_mod.InvalidMinimumHealthyHostValueException
InvalidComputePlatformException = models_mod.InvalidComputePlatformException
InvalidRoleException = models_mod.InvalidRoleException
RoleRequiredException = models_mod.RoleRequiredException
DeploymentLimitExceededException = models_mod.DeploymentLimitExceededException
InvalidNextTokenException = models_mod.InvalidNextTokenException

# ── Handler loader ───────────────────────────────────────────
SKIP_NAMES = {'dataclass', 'time', 'uuid', '<lambda>'}


def _load_handler(op_name, globals_inject=None):
    """Load a single-handler .code.py file — returns the handler function."""
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    # Inject exceptions that generated code references without imports
    mod.InvalidInputException = InvalidInputException
    mod.ApplicationNameRequiredException = ApplicationNameRequiredException
    mod.InvalidApplicationNameException = InvalidApplicationNameException
    mod.ApplicationDoesNotExistException = ApplicationDoesNotExistException
    mod.ApplicationAlreadyExistsException = ApplicationAlreadyExistsException
    mod.ApplicationLimitExceededException = ApplicationLimitExceededException
    mod.DeploymentConfigNameRequiredException = DeploymentConfigNameRequiredException
    mod.InvalidDeploymentConfigNameException = InvalidDeploymentConfigNameException
    mod.DeploymentConfigDoesNotExistException = DeploymentConfigDoesNotExistException
    mod.DeploymentConfigAlreadyExistsException = DeploymentConfigAlreadyExistsException
    mod.DeploymentConfigInUseException = DeploymentConfigInUseException
    mod.DeploymentGroupNameRequiredException = DeploymentGroupNameRequiredException
    mod.InvalidDeploymentGroupNameException = InvalidDeploymentGroupNameException
    mod.DeploymentGroupDoesNotExistException = DeploymentGroupDoesNotExistException
    mod.DeploymentGroupAlreadyExistsException = DeploymentGroupAlreadyExistsException
    mod.DeploymentIdRequiredException = DeploymentIdRequiredException
    mod.InvalidDeploymentIdException = InvalidDeploymentIdException
    mod.DeploymentDoesNotExistException = DeploymentDoesNotExistException
    mod.DeploymentAlreadyCompletedException = DeploymentAlreadyCompletedException
    mod.InvalidRevisionException = InvalidRevisionException
    mod.InvalidMinimumHealthyHostValueException = InvalidMinimumHealthyHostValueException
    mod.InvalidComputePlatformException = InvalidComputePlatformException
    mod.InvalidRoleException = InvalidRoleException
    mod.RoleRequiredException = RoleRequiredException
    mod.DeploymentLimitExceededException = DeploymentLimitExceededException
    mod.InvalidNextTokenException = InvalidNextTokenException
    if globals_inject:
        for name, value in globals_inject.items():
            setattr(mod, name, value)
    spec.loader.exec_module(mod)
    # Find the handler function
    handler = None
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
                and not v.__name__.startswith('_')
                and v.__name__ not in SKIP_NAMES):
            handler = v
            break
    return handler


# ═══════════════════════════════════════════════════════════════
#  APPLICATION TESTS
# ═══════════════════════════════════════════════════════════════

class TestApplicationIntegration:

    @pytest.fixture
    def store(self):
        return CodeDeployStore()

    def test_create_application_happy_path(self, store):
        handler = _load_handler('CreateApplication')
        response = handler(store, {'applicationName': 'MyApp', 'computePlatform': 'Server'})
        assert response is not None
        assert 'applicationId' in response
        assert len(response['applicationId']) > 0

        # Verify store state
        app = store.applications.get_application('MyApp')
        assert app.applicationName == 'MyApp'
        assert app.computePlatform == 'Server'

    def test_create_application_missing_name(self, store):
        handler = _load_handler('CreateApplication')
        with pytest.raises(ApplicationNameRequiredException):
            handler(store, {})

    def test_create_application_duplicate(self, store):
        handler = _load_handler('CreateApplication')
        handler(store, {'applicationName': 'MyApp'})
        with pytest.raises(ApplicationAlreadyExistsException):
            handler(store, {'applicationName': 'MyApp'})

    def test_get_application_happy_path(self, store):
        create = _load_handler('CreateApplication')
        get = _load_handler('GetApplication')
        create(store, {'applicationName': 'MyApp'})
        response = get(store, {'applicationName': 'MyApp'})
        assert response['application']['applicationName'] == 'MyApp'

    def test_get_application_nonexistent(self, store):
        get = _load_handler('GetApplication')
        with pytest.raises(ApplicationDoesNotExistException):
            get(store, {'applicationName': 'Nonexistent'})

    def test_list_applications_happy_path(self, store):
        create = _load_handler('CreateApplication')
        list_handler = _load_handler('ListApplications')
        create(store, {'applicationName': 'AppB'})
        create(store, {'applicationName': 'AppA'})
        response = list_handler(store, {})
        assert response['applications'] == ['AppA', 'AppB']

    def test_delete_application_happy_path(self, store):
        create = _load_handler('CreateApplication')
        delete = _load_handler('DeleteApplication')
        get = _load_handler('GetApplication')
        create(store, {'applicationName': 'MyApp'})
        delete(store, {'applicationName': 'MyApp'})
        with pytest.raises(ApplicationDoesNotExistException):
            get(store, {'applicationName': 'MyApp'})

    def test_update_application_rename(self, store):
        create = _load_handler('CreateApplication')
        update = _load_handler('UpdateApplication')
        get = _load_handler('GetApplication')
        create(store, {'applicationName': 'OldName'})
        update(store, {'applicationName': 'OldName', 'newApplicationName': 'NewName'})
        response = get(store, {'applicationName': 'NewName'})
        assert response['application']['applicationName'] == 'NewName'

    def test_batch_get_applications(self, store):
        create = _load_handler('CreateApplication')
        batch = _load_handler('BatchGetApplications')
        create(store, {'applicationName': 'App1'})
        create(store, {'applicationName': 'App2'})
        response = batch(store, {'applicationNames': ['App1', 'App2', 'Missing']})
        assert len(response['applicationsInfo']) == 2


# ═══════════════════════════════════════════════════════════════
#  DEPLOYMENT CONFIG TESTS
# ═══════════════════════════════════════════════════════════════

class TestDeploymentConfigIntegration:

    @pytest.fixture
    def store(self):
        return CodeDeployStore()

    def test_create_deployment_config_happy_path(self, store):
        handler = _load_handler('CreateDeploymentConfig')
        response = handler(store, {
            'deploymentConfigName': 'MyConfig',
            'minimumHealthyHosts': {'type': 'HOST_COUNT', 'value': 2}
        })
        assert response is not None
        assert 'deploymentConfigId' in response
        assert len(response['deploymentConfigId']) > 0

    def test_create_deployment_config_missing_name(self, store):
        handler = _load_handler('CreateDeploymentConfig')
        with pytest.raises(DeploymentConfigNameRequiredException):
            handler(store, {})

    def test_create_deployment_config_duplicate(self, store):
        handler = _load_handler('CreateDeploymentConfig')
        handler(store, {'deploymentConfigName': 'MyConfig'})
        with pytest.raises(DeploymentConfigAlreadyExistsException):
            handler(store, {'deploymentConfigName': 'MyConfig'})

    def test_get_deployment_config_happy_path(self, store):
        get = _load_handler('GetDeploymentConfig')
        response = get(store, {'deploymentConfigName': 'CodeDeployDefault.OneAtATime'})
        assert response['deploymentConfigInfo']['deploymentConfigName'] == 'CodeDeployDefault.OneAtATime'

    def test_get_deployment_config_nonexistent(self, store):
        get = _load_handler('GetDeploymentConfig')
        with pytest.raises(DeploymentConfigDoesNotExistException):
            get(store, {'deploymentConfigName': 'NoSuchConfig'})

    def test_list_deployment_configs(self, store):
        create = _load_handler('CreateDeploymentConfig')
        list_handler = _load_handler('ListDeploymentConfigs')
        create(store, {'deploymentConfigName': 'ZZZCustom'})
        response = list_handler(store, {})
        assert 'CodeDeployDefault.AllAtOnce' in response['deploymentConfigsList']
        assert 'ZZZCustom' in response['deploymentConfigsList']

    def test_delete_deployment_config_custom(self, store):
        create = _load_handler('CreateDeploymentConfig')
        delete = _load_handler('DeleteDeploymentConfig')
        get = _load_handler('GetDeploymentConfig')
        create(store, {'deploymentConfigName': 'ToDelete'})
        delete(store, {'deploymentConfigName': 'ToDelete'})
        with pytest.raises(DeploymentConfigDoesNotExistException):
            get(store, {'deploymentConfigName': 'ToDelete'})

    def test_delete_predefined_config_fails(self, store):
        delete = _load_handler('DeleteDeploymentConfig')
        with pytest.raises(InvalidDeploymentConfigNameException):
            delete(store, {'deploymentConfigName': 'CodeDeployDefault.OneAtATime'})


# ═══════════════════════════════════════════════════════════════
#  DEPLOYMENT GROUP TESTS
# ═══════════════════════════════════════════════════════════════

class TestDeploymentGroupIntegration:

    @pytest.fixture
    def store(self):
        s = CodeDeployStore()
        # Pre-create an application
        s.applications.create_application('TestApp')
        return s

    def test_create_deployment_group_happy_path(self, store):
        handler = _load_handler('CreateDeploymentGroup')
        response = handler(store, {
            'applicationName': 'TestApp',
            'deploymentGroupName': 'MyGroup',
            'serviceRoleArn': 'arn:aws:iam::123456789012:role/CodeDeployRole',
        })
        assert response is not None
        assert 'deploymentGroupId' in response

    def test_create_deployment_group_missing_role(self, store):
        handler = _load_handler('CreateDeploymentGroup')
        with pytest.raises(RoleRequiredException):
            handler(store, {
                'applicationName': 'TestApp',
                'deploymentGroupName': 'MyGroup',
            })

    def test_create_deployment_group_missing_name(self, store):
        handler = _load_handler('CreateDeploymentGroup')
        with pytest.raises(DeploymentGroupNameRequiredException):
            handler(store, {
                'applicationName': 'TestApp',
                'serviceRoleArn': 'arn:aws:iam::123456789012:role/Test',
            })

    def test_create_deployment_group_nonexistent_app(self, store):
        handler = _load_handler('CreateDeploymentGroup')
        with pytest.raises(ApplicationDoesNotExistException):
            handler(store, {
                'applicationName': 'NoSuchApp',
                'deploymentGroupName': 'MyGroup',
                'serviceRoleArn': 'arn:aws:iam::123456789012:role/Test',
            })

    def test_get_deployment_group_happy_path(self, store):
        create = _load_handler('CreateDeploymentGroup')
        get = _load_handler('GetDeploymentGroup')
        create(store, {
            'applicationName': 'TestApp',
            'deploymentGroupName': 'MyGroup',
            'serviceRoleArn': 'arn:aws:iam::123456789012:role/Test',
        })
        response = get(store, {
            'applicationName': 'TestApp',
            'deploymentGroupName': 'MyGroup',
        })
        assert response['deploymentGroupInfo']['deploymentGroupName'] == 'MyGroup'

    def test_get_deployment_group_nonexistent(self, store):
        get = _load_handler('GetDeploymentGroup')
        with pytest.raises(DeploymentGroupDoesNotExistException):
            get(store, {
                'applicationName': 'TestApp',
                'deploymentGroupName': 'NoGroup',
            })

    def test_list_deployment_groups(self, store):
        create = _load_handler('CreateDeploymentGroup')
        list_handler = _load_handler('ListDeploymentGroups')
        create(store, {
            'applicationName': 'TestApp',
            'deploymentGroupName': 'GroupB',
            'serviceRoleArn': 'arn:aws:iam::123456789012:role/Test',
        })
        create(store, {
            'applicationName': 'TestApp',
            'deploymentGroupName': 'GroupA',
            'serviceRoleArn': 'arn:aws:iam::123456789012:role/Test',
        })
        response = list_handler(store, {'applicationName': 'TestApp'})
        assert response['deploymentGroups'] == ['GroupA', 'GroupB']

    def test_delete_deployment_group_happy_path(self, store):
        create = _load_handler('CreateDeploymentGroup')
        delete = _load_handler('DeleteDeploymentGroup')
        get = _load_handler('GetDeploymentGroup')
        create(store, {
            'applicationName': 'TestApp',
            'deploymentGroupName': 'ToDelete',
            'serviceRoleArn': 'arn:aws:iam::123456789012:role/Test',
        })
        delete(store, {
            'applicationName': 'TestApp',
            'deploymentGroupName': 'ToDelete',
        })
        with pytest.raises(DeploymentGroupDoesNotExistException):
            get(store, {
                'applicationName': 'TestApp',
                'deploymentGroupName': 'ToDelete',
            })


# ═══════════════════════════════════════════════════════════════
#  DEPLOYMENT TESTS
# ═══════════════════════════════════════════════════════════════

class TestDeploymentIntegration:

    @pytest.fixture
    def store(self):
        s = CodeDeployStore()
        s.applications.create_application('TestApp')
        s.deployment_groups.create_deployment_group(
            'TestApp', 'TestGroup', 'arn:aws:iam::123456789012:role/Test')
        return s

    def test_create_deployment_happy_path(self, store):
        handler = _load_handler('CreateDeployment')
        response = handler(store, {
            'applicationName': 'TestApp',
            'deploymentGroupName': 'TestGroup',
            'revision': {
                'revisionType': 'S3',
                's3Location': {
                    'bucket': 'my-bucket',
                    'key': 'my-app.zip',
                    'bundleType': 'zip',
                }
            }
        })
        assert response is not None
        assert 'deploymentId' in response
        assert response['deploymentId'].startswith('d-')

    def test_create_deployment_missing_app(self, store):
        handler = _load_handler('CreateDeployment')
        with pytest.raises(ApplicationNameRequiredException):
            handler(store, {})

    def test_create_deployment_nonexistent_app(self, store):
        handler = _load_handler('CreateDeployment')
        with pytest.raises(ApplicationDoesNotExistException):
            handler(store, {'applicationName': 'NoSuchApp'})

    def test_get_deployment_happy_path(self, store):
        create = _load_handler('CreateDeployment')
        get = _load_handler('GetDeployment')
        result = create(store, {
            'applicationName': 'TestApp',
            'revision': {'revisionType': 'S3', 's3Location': {'bucket': 'b', 'key': 'k', 'bundleType': 'zip'}}
        })
        response = get(store, {'deploymentId': result['deploymentId']})
        assert response['deploymentInfo']['deploymentId'] == result['deploymentId']
        assert response['deploymentInfo']['applicationName'] == 'TestApp'

    def test_get_deployment_nonexistent(self, store):
        get = _load_handler('GetDeployment')
        with pytest.raises(DeploymentDoesNotExistException):
            get(store, {'deploymentId': 'd-NONEXISTENT'})

    def test_stop_deployment_happy_path(self, store):
        create = _load_handler('CreateDeployment')
        stop = _load_handler('StopDeployment')
        get = _load_handler('GetDeployment')
        result = create(store, {
            'applicationName': 'TestApp',
            'revision': {'revisionType': 'S3', 's3Location': {'bucket': 'b', 'key': 'k', 'bundleType': 'zip'}}
        })
        stop(store, {'deploymentId': result['deploymentId']})
        response = get(store, {'deploymentId': result['deploymentId']})
        assert response['deploymentInfo']['status'] == 'Stopped'

    def test_list_deployments_filtered(self, store):
        create = _load_handler('CreateDeployment')
        list_handler = _load_handler('ListDeployments')
        create(store, {
            'applicationName': 'TestApp',
            'revision': {'revisionType': 'S3', 's3Location': {'bucket': 'b', 'key': 'k', 'bundleType': 'zip'}}
        })
        create(store, {
            'applicationName': 'TestApp',
            'revision': {'revisionType': 'S3', 's3Location': {'bucket': 'b2', 'key': 'k2', 'bundleType': 'zip'}}
        })
        response = list_handler(store, {'applicationName': 'TestApp'})
        assert len(response['deployments']) == 2

    def test_batch_get_deployments(self, store):
        create = _load_handler('CreateDeployment')
        batch = _load_handler('BatchGetDeployments')
        r1 = create(store, {
            'applicationName': 'TestApp',
            'revision': {'revisionType': 'S3', 's3Location': {'bucket': 'b', 'key': 'k', 'bundleType': 'zip'}}
        })
        r2 = create(store, {
            'applicationName': 'TestApp',
            'revision': {'revisionType': 'S3', 's3Location': {'bucket': 'b2', 'key': 'k2', 'bundleType': 'zip'}}
        })
        response = batch(store, {'deploymentIds': [r1['deploymentId'], r2['deploymentId'], 'd-MISSING']})
        assert len(response['deploymentsInfo']) == 2
