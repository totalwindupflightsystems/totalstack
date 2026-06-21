"""Integration test for MediaConvert — real store, 4 entities + tags."""
import pytest
import os
import sys
import importlib.util
import types
import time as _time
import uuid as _uuid

# ── Setup ───────────────────────────────────────────────────────
ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'mediaconvert')

# Load models module
models_spec = importlib.util.spec_from_file_location(
    'models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

# Pull out needed names
MediaConvertStore = models_mod.MediaConvertStore
JobRecord = models_mod.JobRecord
JobTemplateRecord = models_mod.JobTemplateRecord
PresetRecord = models_mod.PresetRecord
QueueRecord = models_mod.QueueRecord
InvalidParameterException = models_mod.InvalidParameterException
ResourceNotFoundException = models_mod.ResourceNotFoundException
ConflictException = models_mod.ConflictException

# ── Module Loaders ──────────────────────────────────────────────

skip_names = {'dataclass', 'time', 'uuid', '<lambda>'}
STDLIB_INJECT = {
    'time': _time,
    'uuid': _uuid,
    'dataclass': lambda f: f,
}

def _load_handler(op_name, globals_inject=None):
    """Load a single-handler .code.py file — returns the handler function."""
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    # Inject exception classes + stdlib + record classes
    mod.InvalidParameterException = InvalidParameterException
    mod.ResourceNotFoundException = ResourceNotFoundException
    mod.ConflictException = ConflictException
    mod.JobRecord = JobRecord
    mod.JobTemplateRecord = JobTemplateRecord
    mod.PresetRecord = PresetRecord
    mod.QueueRecord = QueueRecord
    inject = dict(STDLIB_INJECT)
    if globals_inject:
        inject.update(globals_inject)
    for name, value in inject.items():
        setattr(mod, name, value)
    spec.loader.exec_module(mod)
    # Find handler function (skip injected names and lambdas)
    handler = None
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
                and not v.__name__.startswith('_')
                and v.__name__ not in skip_names):
            handler = v
            break
    return handler


def _load_module(op_name, globals_inject=None):
    """Load a multi-handler .code.py module."""
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    mod.InvalidParameterException = InvalidParameterException
    mod.ResourceNotFoundException = ResourceNotFoundException
    mod.ConflictException = ConflictException
    mod.JobRecord = JobRecord
    mod.JobTemplateRecord = JobTemplateRecord
    mod.PresetRecord = PresetRecord
    mod.QueueRecord = QueueRecord
    inject = dict(STDLIB_INJECT)
    if globals_inject:
        inject.update(globals_inject)
    for name, value in inject.items():
        setattr(mod, name, value)
    spec.loader.exec_module(mod)
    return mod


# ── Job Tests ───────────────────────────────────────────────────

class TestJobIntegration:
    @pytest.fixture
    def store(self):
        return MediaConvertStore()

    def test_create_job_happy_path(self, store):
        handler = _load_handler('CreateJob')
        request = {
            'Role': 'arn:aws:iam::000000000000:role/MediaConvertRole',
            'Settings': {'Inputs': [{'FileInput': 's3://bucket/input.mp4'}]}
        }
        response = handler(store, request)
        assert 'Job' in response
        job = response['Job']
        assert 'Id' in job
        assert job['Role'] == request['Role']
        assert job['Status'] == 'SUBMITTED'

    def test_create_job_missing_role(self, store):
        handler = _load_handler('CreateJob')
        with pytest.raises(InvalidParameterException):
            handler(store, {'Settings': {}})

    def test_create_job_missing_settings(self, store):
        handler = _load_handler('CreateJob')
        with pytest.raises(InvalidParameterException):
            handler(store, {'Role': 'arn:aws:iam::role'})

    def test_get_job_happy_path(self, store):
        create = _load_handler('CreateJob')
        get = _load_handler('GetJob')
        created = create(store, {
            'Role': 'arn:aws:iam::role',
            'Settings': {'Inputs': [{'FileInput': 's3://b/input.mp4'}]}
        })
        job_id = created['Job']['Id']
        response = get(store, {'Id': job_id})
        assert response['Job']['Id'] == job_id

    def test_get_job_nonexistent(self, store):
        handler = _load_handler('GetJob')
        with pytest.raises(ResourceNotFoundException):
            handler(store, {'Id': 'nonexistent'})

    def test_list_jobs_happy_path(self, store):
        create = _load_handler('CreateJob')
        for i in range(3):
            create(store, {
                'Role': 'arn:aws:iam::role',
                'Settings': {'Inputs': [{'FileInput': f's3://b/input{i}.mp4'}]}
            })
        list_handler = _load_handler('ListJobs')
        response = list_handler(store, {})
        assert 'Jobs' in response
        assert len(response['Jobs']) == 3

    def test_list_jobs_pagination(self, store):
        create = _load_handler('CreateJob')
        for i in range(5):
            create(store, {
                'Role': 'arn:aws:iam::role',
                'Settings': {'Inputs': [{'FileInput': f's3://b/input{i}.mp4'}]}
            })
        list_handler = _load_handler('ListJobs')
        page1 = list_handler(store, {'MaxResults': 2})
        assert len(page1['Jobs']) == 2
        assert 'NextToken' in page1
        page2 = list_handler(store, {'MaxResults': 2, 'NextToken': page1['NextToken']})
        assert len(page2['Jobs']) == 2

    def test_cancel_job_happy_path(self, store):
        create = _load_handler('CreateJob')
        cancel = _load_handler('CancelJob')
        created = create(store, {
            'Role': 'arn:aws:iam::role',
            'Settings': {'Inputs': [{'FileInput': 's3://b/input.mp4'}]}
        })
        job_id = created['Job']['Id']
        response = cancel(store, {'Id': job_id})
        assert response['Job']['Status'] == 'CANCELED'

    def test_cancel_job_nonexistent(self, store):
        handler = _load_handler('CancelJob')
        with pytest.raises(ResourceNotFoundException):
            handler(store, {'Id': 'nonexistent'})


# ── JobTemplate Tests ────────────────────────────────────────────

class TestJobTemplateIntegration:
    @pytest.fixture
    def store(self):
        return MediaConvertStore()

    def test_create_template_happy_path(self, store):
        handler = _load_handler('CreateJobTemplate')
        request = {
            'Name': 'my-template',
            'Settings': {'Inputs': [{'FileInput': 's3://b/input.mp4'}]}
        }
        response = handler(store, request)
        assert response['JobTemplate']['Name'] == 'my-template'

    def test_create_template_duplicate(self, store):
        handler = _load_handler('CreateJobTemplate')
        request = {
            'Name': 'my-template',
            'Settings': {'Inputs': [{'FileInput': 's3://b/input.mp4'}]}
        }
        handler(store, request)
        with pytest.raises(ConflictException):
            handler(store, request)

    def test_get_template_happy_path(self, store):
        create = _load_handler('CreateJobTemplate')
        get = _load_handler('GetJobTemplate')
        create(store, {
            'Name': 'my-template',
            'Settings': {'Inputs': [{'FileInput': 's3://b/input.mp4'}]}
        })
        response = get(store, {'Name': 'my-template'})
        assert response['JobTemplate']['Name'] == 'my-template'

    def test_get_template_nonexistent(self, store):
        handler = _load_handler('GetJobTemplate')
        with pytest.raises(ResourceNotFoundException):
            handler(store, {'Name': 'nonexistent'})

    def test_list_templates_happy_path(self, store):
        create = _load_handler('CreateJobTemplate')
        for i in range(3):
            create(store, {
                'Name': f'template-{i}',
                'Settings': {'Inputs': [{'FileInput': f's3://b/input{i}.mp4'}]}
            })
        list_handler = _load_handler('ListJobTemplates')
        response = list_handler(store, {})
        assert len(response['JobTemplates']) == 3

    def test_update_template_happy_path(self, store):
        create = _load_handler('CreateJobTemplate')
        update = _load_handler('UpdateJobTemplate')
        create(store, {
            'Name': 'my-template',
            'Settings': {'Inputs': [{'FileInput': 's3://b/old.mp4'}]}
        })
        response = update(store, {
            'Name': 'my-template',
            'Description': 'Updated description'
        })
        assert response['JobTemplate']['Description'] == 'Updated description'

    def test_update_template_nonexistent(self, store):
        handler = _load_handler('UpdateJobTemplate')
        with pytest.raises(ResourceNotFoundException):
            handler(store, {'Name': 'nonexistent'})

    def test_delete_template_happy_path(self, store):
        create = _load_handler('CreateJobTemplate')
        delete = _load_handler('DeleteJobTemplate')
        get = _load_handler('GetJobTemplate')
        create(store, {
            'Name': 'my-template',
            'Settings': {'Inputs': [{'FileInput': 's3://b/input.mp4'}]}
        })
        delete(store, {'Name': 'my-template'})
        with pytest.raises(ResourceNotFoundException):
            get(store, {'Name': 'my-template'})


# ── Preset Tests ─────────────────────────────────────────────────

class TestPresetIntegration:
    @pytest.fixture
    def store(self):
        return MediaConvertStore()

    def test_create_preset_happy_path(self, store):
        handler = _load_handler('CreatePreset')
        response = handler(store, {
            'Name': 'my-preset',
            'Settings': {'Description': 'H.264 1080p'}
        })
        assert response['Preset']['Name'] == 'my-preset'

    def test_create_preset_duplicate(self, store):
        handler = _load_handler('CreatePreset')
        req = {'Name': 'my-preset', 'Settings': {'Description': 'H.264 1080p'}}
        handler(store, req)
        with pytest.raises(ConflictException):
            handler(store, req)

    def test_get_preset_nonexistent(self, store):
        handler = _load_handler('GetPreset')
        with pytest.raises(ResourceNotFoundException):
            handler(store, {'Name': 'nonexistent'})

    def test_list_presets_happy_path(self, store):
        create = _load_handler('CreatePreset')
        for i in range(3):
            create(store, {'Name': f'preset-{i}', 'Settings': {'Description': f'Preset {i}'}})
        list_handler = _load_handler('ListPresets')
        response = list_handler(store, {})
        assert len(response['Presets']) == 3

    def test_update_preset(self, store):
        create = _load_handler('CreatePreset')
        update = _load_handler('UpdatePreset')
        create(store, {'Name': 'my-preset', 'Settings': {'Description': 'Old'}})
        response = update(store, {
            'Name': 'my-preset',
            'Description': 'Updated'
        })
        assert response['Preset']['Description'] == 'Updated'

    def test_delete_preset(self, store):
        create = _load_handler('CreatePreset')
        delete = _load_handler('DeletePreset')
        get = _load_handler('GetPreset')
        create(store, {'Name': 'my-preset', 'Settings': {'Description': 'Old'}})
        delete(store, {'Name': 'my-preset'})
        with pytest.raises(ResourceNotFoundException):
            get(store, {'Name': 'my-preset'})


# ── Queue Tests ──────────────────────────────────────────────────

class TestQueueIntegration:
    @pytest.fixture
    def store(self):
        return MediaConvertStore()

    def test_create_queue_happy_path(self, store):
        handler = _load_handler('CreateQueue')
        response = handler(store, {'Name': 'my-queue'})
        assert response['Queue']['Name'] == 'my-queue'
        assert response['Queue']['Status'] == 'ACTIVE'

    def test_create_queue_duplicate(self, store):
        handler = _load_handler('CreateQueue')
        handler(store, {'Name': 'my-queue'})
        with pytest.raises(ConflictException):
            handler(store, {'Name': 'my-queue'})

    def test_get_queue_nonexistent(self, store):
        handler = _load_handler('GetQueue')
        with pytest.raises(ResourceNotFoundException):
            handler(store, {'Name': 'nonexistent'})

    def test_list_queues_happy_path(self, store):
        create = _load_handler('CreateQueue')
        for i in range(3):
            create(store, {'Name': f'queue-{i}'})
        list_handler = _load_handler('ListQueues')
        response = list_handler(store, {})
        assert len(response['Queues']) == 3

    def test_update_queue(self, store):
        create = _load_handler('CreateQueue')
        update = _load_handler('UpdateQueue')
        create(store, {'Name': 'my-queue'})
        response = update(store, {
            'Name': 'my-queue',
            'Status': 'PAUSED',
            'Description': 'paused queue'
        })
        assert response['Queue']['Status'] == 'PAUSED'
        assert response['Queue']['Description'] == 'paused queue'

    def test_delete_queue(self, store):
        create = _load_handler('CreateQueue')
        delete = _load_handler('DeleteQueue')
        get = _load_handler('GetQueue')
        create(store, {'Name': 'my-queue'})
        delete(store, {'Name': 'my-queue'})
        with pytest.raises(ResourceNotFoundException):
            get(store, {'Name': 'my-queue'})


# ── Tag Tests ────────────────────────────────────────────────────

class TestTagIntegration:
    @pytest.fixture
    def store(self):
        return MediaConvertStore()

    def test_tag_resource_happy_path(self, store):
        tag_ops = _load_module('TagOperations')
        tag_ops.execute_tag_resource(store, {
            'Arn': 'arn:aws:mediaconvert:us-east-1:000000000000:job/abc123',
            'Tags': {'Environment': 'prod', 'Team': 'media'}
        })
        response = tag_ops.execute_list_tags_for_resource(store, {
            'Arn': 'arn:aws:mediaconvert:us-east-1:000000000000:job/abc123'
        })
        tags = response['ResourceTags']['Tags']
        assert tags['Environment'] == 'prod'
        assert tags['Team'] == 'media'

    def test_untag_resource(self, store):
        tag_ops = _load_module('TagOperations')
        arn = 'arn:aws:mediaconvert:us-east-1:000000000000:preset/my-preset'
        tag_ops.execute_tag_resource(store, {
            'Arn': arn,
            'Tags': {'Key1': 'Val1', 'Key2': 'Val2'}
        })
        tag_ops.execute_untag_resource(store, {
            'Arn': arn,
            'TagKeys': ['Key1']
        })
        response = tag_ops.execute_list_tags_for_resource(store, {'Arn': arn})
        tags = response['ResourceTags']['Tags']
        assert 'Key1' not in tags
        assert tags['Key2'] == 'Val2'

    def test_list_tags_empty(self, store):
        tag_ops = _load_module('TagOperations')
        response = tag_ops.execute_list_tags_for_resource(store, {
            'Arn': 'arn:aws:mediaconvert:us-east-1:000000000000:job/none'
        })
        assert response['ResourceTags']['Tags'] == {}

    def test_tag_missing_arn(self, store):
        tag_ops = _load_module('TagOperations')
        with pytest.raises(InvalidParameterException):
            tag_ops.execute_tag_resource(store, {'Tags': {'A': 'B'}})
