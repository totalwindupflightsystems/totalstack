"""Integration tests for CodeBuild — real CodeBuildStore with generated handlers."""
import os
import sys
import types
import importlib.util
import pytest


# ═══════════════════════════════════════════════════════════════
# Dynamic loader utilities (greenfield service pattern)
# ═══════════════════════════════════════════════════════════════

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'codebuild')

# Load the models module first
models_spec = importlib.util.spec_from_file_location(
    'models', os.path.join(SERVICE_DIR, 'models.code.py')
)
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

# Pull out needed names
CodeBuildStore = models_mod.CodeBuildStore
InvalidInputException = models_mod.InvalidInputException
ResourceNotFoundException = models_mod.ResourceNotFoundException
ResourceAlreadyExistsException = models_mod.ResourceAlreadyExistsException
AccountLimitExceededException = models_mod.AccountLimitExceededException

import time as _time
import uuid as _uuid

SKIP_NAMES = {}


def _load_handler(op_name, globals_inject=None):
    """Load a single-handler .code.py file, injecting exceptions and stdlib."""
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    if not os.path.exists(path):
        pytest.skip(f"Handler file not found: {path}")
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    mod.InvalidInputException = InvalidInputException
    mod.ResourceNotFoundException = ResourceNotFoundException
    mod.ResourceAlreadyExistsException = ResourceAlreadyExistsException
    mod.AccountLimitExceededException = AccountLimitExceededException
    mod.time = _time
    mod.uuid = _uuid
    if globals_inject:
        for name, value in globals_inject.items():
            setattr(mod, name, value)
    spec.loader.exec_module(mod)

    # Find the handler function — exclude stdlib injects, lambdas
    skip_names = {name for name in (
        'time', 'uuid', 'InvalidInputException', 'ResourceNotFoundException',
        'ResourceAlreadyExistsException', 'AccountLimitExceededException'
    )}
    handler = None
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
                and not v.__name__.startswith('_')
                and v.__name__ not in skip_names):
            handler = v
            break
    if handler is None:
        raise RuntimeError(f"No handler function found in {op_name}.code.py")
    return handler


# ═══════════════════════════════════════════════════════════════
# Fixtures
# ═══════════════════════════════════════════════════════════════

@pytest.fixture
def store():
    return CodeBuildStore()


@pytest.fixture
def project(store):
    """Create a test project for build-dependent tests."""
    handler = _load_handler('CreateProject')
    response = handler(store, {
        'name': 'test-project',
        'source': {'type': 'S3', 'location': 'bucket/path.zip'},
        'environment': {
            'type': 'LINUX_CONTAINER',
            'image': 'aws/codebuild/standard:5.0',
            'computeType': 'BUILD_GENERAL1_SMALL',
        },
        'artifacts': {'type': 'NO_ARTIFACTS'},
        'serviceRole': 'arn:aws:iam::123456789012:role/CodeBuildServiceRole',
    })
    return response


# ═══════════════════════════════════════════════════════════════
# CreateProject Tests
# ═══════════════════════════════════════════════════════════════

class TestCreateProject:
    """Happy path + error paths for CreateProject."""

    def test_create_project_happy_path(self, store):
        handler = _load_handler('CreateProject')
        response = handler(store, {
            'name': 'my-project',
            'source': {'type': 'S3', 'location': 'mybucket/source.zip'},
            'environment': {
                'type': 'LINUX_CONTAINER',
                'image': 'aws/codebuild/standard:5.0',
                'computeType': 'BUILD_GENERAL1_SMALL',
            },
            'artifacts': {'type': 'NO_ARTIFACTS'},
            'serviceRole': 'arn:aws:iam::123456789012:role/CodeBuildRole',
            'description': 'Test project',
        })
        assert response is not None
        assert 'project' in response
        proj = response['project']
        assert proj['name'] == 'my-project'
        assert proj['arn'].startswith('arn:aws:codebuild:')

    def test_create_project_missing_name(self, store):
        handler = _load_handler('CreateProject')
        with pytest.raises(InvalidInputException):
            handler(store, {'source': {'type': 'S3', 'location': 'x/y.zip'}})

    def test_create_project_invalid_source_type(self, store):
        handler = _load_handler('CreateProject')
        with pytest.raises(InvalidInputException):
            handler(store, {
                'name': 'bad-project',
                'source': {'type': 'INVALID_TYPE', 'location': 'x/y.zip'},
                'environment': {
                    'type': 'LINUX_CONTAINER',
                    'image': 'aws/codebuild/standard:5.0',
                    'computeType': 'BUILD_GENERAL1_SMALL',
                },
                'artifacts': {'type': 'NO_ARTIFACTS'},
                'serviceRole': 'arn:aws:iam::123456789012:role/CodeBuildRole',
            })

    def test_create_duplicate_project(self, store):
        handler = _load_handler('CreateProject')
        args = {
            'name': 'dup-project',
            'source': {'type': 'S3', 'location': 'x/y.zip'},
            'environment': {
                'type': 'LINUX_CONTAINER',
                'image': 'aws/codebuild/standard:5.0',
                'computeType': 'BUILD_GENERAL1_SMALL',
            },
            'artifacts': {'type': 'NO_ARTIFACTS'},
            'serviceRole': 'arn:aws:iam::123456789012:role/CodeBuildRole',
        }
        handler(store, args)  # first — succeeds
        with pytest.raises(ResourceAlreadyExistsException):
            handler(store, args)  # duplicate — fails


# ═══════════════════════════════════════════════════════════════
# DeleteProject Tests
# ═══════════════════════════════════════════════════════════════

class TestDeleteProject:
    """Happy path + error paths for DeleteProject."""

    def test_delete_project_happy_path(self, store):
        # Create first
        create = _load_handler('CreateProject')
        create(store, {
            'name': 'delete-me',
            'source': {'type': 'S3', 'location': 'x/y.zip'},
            'environment': {
                'type': 'LINUX_CONTAINER',
                'image': 'aws/codebuild/standard:5.0',
                'computeType': 'BUILD_GENERAL1_SMALL',
            },
            'artifacts': {'type': 'NO_ARTIFACTS'},
            'serviceRole': 'arn:aws:iam::123456789012:role/CodeBuildRole',
        })

        delete = _load_handler('DeleteProject')
        response = delete(store, {'name': 'delete-me'})
        assert response == {}

        # Verify deleted — BatchGetProjects returns not_found
        get = _load_handler('BatchGetProjects')
        result = get(store, {'names': ['delete-me']})
        assert 'projectsNotFound' in result
        assert 'delete-me' in result['projectsNotFound']

    def test_delete_nonexistent_project(self, store):
        handler = _load_handler('DeleteProject')
        with pytest.raises(ResourceNotFoundException):
            handler(store, {'name': 'nonexistent'})

    def test_delete_missing_name(self, store):
        handler = _load_handler('DeleteProject')
        with pytest.raises(InvalidInputException):
            handler(store, {})


# ═══════════════════════════════════════════════════════════════
# StartBuild Tests
# ═══════════════════════════════════════════════════════════════

class TestStartBuild:
    """Happy path + error paths for StartBuild."""

    def test_start_build_happy_path(self, store, project):
        handler = _load_handler('StartBuild')
        response = handler(store, {'projectName': 'test-project'})
        assert response is not None
        assert 'build' in response
        build = response['build']
        assert build['projectName'] == 'test-project'
        assert build['buildStatus'] == 'IN_PROGRESS'
        assert 'id' in build
        assert 'arn' in build

    def test_start_build_nonexistent_project(self, store):
        handler = _load_handler('StartBuild')
        with pytest.raises(ResourceNotFoundException):
            handler(store, {'projectName': 'nonexistent'})

    def test_start_build_missing_project_name(self, store):
        handler = _load_handler('StartBuild')
        with pytest.raises(InvalidInputException):
            handler(store, {})


# ═══════════════════════════════════════════════════════════════
# StopBuild Tests
# ═══════════════════════════════════════════════════════════════

class TestStopBuild:

    def test_stop_build_happy_path(self, store, project):
        # Start a build first
        start = _load_handler('StartBuild')
        build_resp = start(store, {'projectName': 'test-project'})
        build_id = build_resp['build']['id']

        stop = _load_handler('StopBuild')
        response = stop(store, {'id': build_id})
        assert response['build']['buildStatus'] == 'STOPPED'

    def test_stop_nonexistent_build(self, store):
        handler = _load_handler('StopBuild')
        with pytest.raises(ResourceNotFoundException):
            handler(store, {'id': 'nonexistent-build-id'})


# ═══════════════════════════════════════════════════════════════
# BatchGetBuilds Tests
# ═══════════════════════════════════════════════════════════════

class TestBatchGetBuilds:

    def test_batch_get_builds_partial_not_found(self, store, project):
        # Create one build
        start = _load_handler('StartBuild')
        build_resp = start(store, {'projectName': 'test-project'})
        build_id = build_resp['build']['id']

        handler = _load_handler('BatchGetBuilds')
        result = handler(store, {'ids': [build_id, 'nonexistent']})
        assert len(result['builds']) == 1
        assert result['builds'][0]['id'] == build_id
        assert 'buildsNotFound' in result
        assert 'nonexistent' in result['buildsNotFound']


# ═══════════════════════════════════════════════════════════════
# ListProjects Tests
# ═══════════════════════════════════════════════════════════════

class TestListProjects:

    def test_list_projects_empty(self, store):
        handler = _load_handler('ListProjects')
        result = handler(store, {})
        assert result['projects'] == []

    def test_list_projects_with_items(self, store):
        create = _load_handler('CreateProject')
        base = {
            'source': {'type': 'S3', 'location': 'x/y.zip'},
            'environment': {
                'type': 'LINUX_CONTAINER',
                'image': 'aws/codebuild/standard:5.0',
                'computeType': 'BUILD_GENERAL1_SMALL',
            },
            'artifacts': {'type': 'NO_ARTIFACTS'},
            'serviceRole': 'arn:aws:iam::123456789012:role/CodeBuildRole',
        }
        create(store, {**base, 'name': 'proj-b'})
        create(store, {**base, 'name': 'proj-a'})
        create(store, {**base, 'name': 'proj-c'})

        handler = _load_handler('ListProjects')
        result = handler(store, {})
        assert result['projects'] == ['proj-a', 'proj-b', 'proj-c']


# ═══════════════════════════════════════════════════════════════
# BatchGetProjects Tests
# ═══════════════════════════════════════════════════════════════

class TestBatchGetProjects:

    def test_batch_get_partial_not_found(self, store, project):
        handler = _load_handler('BatchGetProjects')
        result = handler(store, {'names': ['test-project', 'nonexistent']})
        assert len(result['projects']) == 1
        assert result['projects'][0]['name'] == 'test-project'
        assert 'projectsNotFound' in result
