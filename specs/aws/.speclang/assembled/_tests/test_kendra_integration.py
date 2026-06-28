"""Integration test for Kendra — real store."""
import pytest
import os
import importlib.util
import types
import time as _time
import uuid as _uuid

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'kendra')

models_spec = importlib.util.spec_from_file_location(
    'models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

KendraStore = models_mod.KendraStore
IndexRecord = models_mod.IndexRecord
DataSourceRecord = models_mod.DataSourceRecord
FaqRecord = models_mod.FaqRecord
ThesaurusRecord = models_mod.ThesaurusRecord
ExperienceRecord = models_mod.ExperienceRecord
InvalidParameterException = models_mod.InvalidParameterException
ResourceNotFoundException = models_mod.ResourceNotFoundException
ConflictException = models_mod.ConflictException
ValidationException = models_mod.ValidationException

skip_names = {'dataclass', 'time', 'uuid', '<lambda>'}


def _load_handler(op_name, globals_inject=None):
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    for cls in [InvalidParameterException, ResourceNotFoundException,
                 ConflictException, ValidationException,
                 IndexRecord, DataSourceRecord, FaqRecord,
                 ThesaurusRecord, ExperienceRecord]:
        setattr(mod, cls.__name__, cls)
    mod.time = _time
    mod.uuid = _uuid
    mod.dataclass = lambda f: f
    if globals_inject:
        for name, value in globals_inject.items():
            setattr(mod, name, value)
    spec.loader.exec_module(mod)
    handler = None
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
                and not v.__name__.startswith('_')
                and v.__name__ not in skip_names):
            handler = v
            break
    return handler


# ══════════════════════════════════════════════════════

class TestIndex:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = KendraStore()
        return self._store

    def test_create_index_happy(self):
        h = _load_handler('create-index')
        resp = h(self.store, {'Name': 'test-index', 'RoleArn': 'arn:aws:iam::000000000000:role/kendra'})
        assert resp is not None
        assert 'Id' in resp
        assert resp['Name'] == 'test-index'
        assert resp['Status'] == 'ACTIVE'

    def test_create_index_with_edition(self):
        h = _load_handler('create-index')
        resp = h(self.store, {'Name': 'dev-index', 'RoleArn': 'arn:aws:iam::000000000000:role/kendra',
                               'Edition': 'DEVELOPER_EDITION'})
        assert resp['Edition'] == 'DEVELOPER_EDITION'

    def test_describe_index(self):
        create = _load_handler('create-index')
        describe = _load_handler('describe-index')
        c = create(self.store, {'Name': 'desc-idx', 'RoleArn': 'arn:aws:iam::000000000000:role/r'})
        resp = describe(self.store, {'Id': c['Id']})
        assert resp['Id'] == c['Id']

    def test_describe_index_not_found(self):
        h = _load_handler('describe-index')
        with pytest.raises(ResourceNotFoundException):
            h(self.store, {'Id': 'nonexistent'})

    def test_delete_index(self):
        create = _load_handler('create-index')
        delete = _load_handler('delete-index')
        describe = _load_handler('describe-index')
        c = create(self.store, {'Name': 'del-idx', 'RoleArn': 'arn:aws:iam::000000000000:role/r'})
        delete(self.store, {'Id': c['Id']})
        with pytest.raises(ResourceNotFoundException):
            describe(self.store, {'Id': c['Id']})

    def test_list_indices(self):
        create = _load_handler('create-index')
        list_h = _load_handler('list-indices')
        create(self.store, {'Name': 'i1', 'RoleArn': 'arn:aws:iam::000000000000:role/r'})
        create(self.store, {'Name': 'i2', 'RoleArn': 'arn:aws:iam::000000000000:role/r'})
        resp = list_h(self.store, {})
        assert resp is not None


class TestDataSource:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = KendraStore()
        return self._store

    def _create_index(self):
        h = _load_handler('create-index')
        return h(self.store, {'Name': 'ds-idx', 'RoleArn': 'arn:aws:iam::000000000000:role/r'})

    def test_create_data_source(self):
        idx = self._create_index()
        h = _load_handler('create-data-source')
        resp = h(self.store, {'IndexId': idx['Id'], 'Name': 's3-ds', 'Type': 'S3'})
        assert resp is not None
        assert resp['Name'] == 's3-ds'

    def test_describe_data_source(self):
        idx = self._create_index()
        create = _load_handler('create-data-source')
        describe = _load_handler('describe-data-source')
        c = create(self.store, {'IndexId': idx['Id'], 'Name': 'ds1', 'Type': 'S3'})
        resp = describe(self.store, {'Id': c['Id'], 'IndexId': idx['Id']})
        assert resp['Id'] == c['Id']

    def test_delete_data_source(self):
        idx = self._create_index()
        create = _load_handler('create-data-source')
        delete = _load_handler('delete-data-source')
        describe = _load_handler('describe-data-source')
        c = create(self.store, {'IndexId': idx['Id'], 'Name': 'ds-del', 'Type': 'S3'})
        delete(self.store, {'Id': c['Id'], 'IndexId': idx['Id']})
        with pytest.raises(ResourceNotFoundException):
            describe(self.store, {'Id': c['Id'], 'IndexId': idx['Id']})

    def test_list_data_sources(self):
        idx = self._create_index()
        create = _load_handler('create-data-source')
        list_h = _load_handler('list-data-sources')
        create(self.store, {'IndexId': idx['Id'], 'Name': 'ds-a', 'Type': 'S3'})
        resp = list_h(self.store, {'IndexId': idx['Id']})
        assert 'SummaryItems' in resp


class TestFaq:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = KendraStore()
        return self._store

    def _create_index(self):
        h = _load_handler('create-index')
        return h(self.store, {'Name': 'faq-idx', 'RoleArn': 'arn:aws:iam::000000000000:role/r'})

    def test_create_faq(self):
        idx = self._create_index()
        h = _load_handler('create-faq')
        resp = h(self.store, {
            'IndexId': idx['Id'], 'Name': 'test-faq',
            'S3Path': {'Bucket': 'my-bucket', 'Key': 'faq.csv'},
            'RoleArn': 'arn:aws:iam::000000000000:role/r',
        })
        assert resp is not None
        assert resp['Name'] == 'test-faq'

    def test_describe_faq(self):
        idx = self._create_index()
        create = _load_handler('create-faq')
        describe = _load_handler('describe-faq')
        c = create(self.store, {
            'IndexId': idx['Id'], 'Name': 'f1',
            'S3Path': {'Bucket': 'b', 'Key': 'k.csv'},
            'RoleArn': 'arn:aws:iam::000000000000:role/r',
        })
        resp = describe(self.store, {'Id': c['Id'], 'IndexId': idx['Id']})
        assert resp['Id'] == c['Id']

    def test_delete_faq(self):
        idx = self._create_index()
        create = _load_handler('create-faq')
        delete = _load_handler('delete-faq')
        describe = _load_handler('describe-faq')
        c = create(self.store, {
            'IndexId': idx['Id'], 'Name': 'f-del',
            'S3Path': {'Bucket': 'b', 'Key': 'k.csv'},
            'RoleArn': 'arn:aws:iam::000000000000:role/r',
        })
        delete(self.store, {'Id': c['Id'], 'IndexId': idx['Id']})
        with pytest.raises(ResourceNotFoundException):
            describe(self.store, {'Id': c['Id'], 'IndexId': idx['Id']})

    def test_list_faqs(self):
        idx = self._create_index()
        create = _load_handler('create-faq')
        list_h = _load_handler('list-faqs')
        create(self.store, {
            'IndexId': idx['Id'], 'Name': 'faq1',
            'S3Path': {'Bucket': 'b', 'Key': 'k.csv'},
            'RoleArn': 'arn:aws:iam::000000000000:role/r',
        })
        resp = list_h(self.store, {'IndexId': idx['Id']})
        assert 'FaqSummaryItems' in resp


class TestThesaurus:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = KendraStore()
        return self._store

    def _create_index(self):
        h = _load_handler('create-index')
        return h(self.store, {'Name': 'th-idx', 'RoleArn': 'arn:aws:iam::000000000000:role/r'})

    def test_create_thesaurus(self):
        idx = self._create_index()
        h = _load_handler('create-thesaurus')
        resp = h(self.store, {
            'IndexId': idx['Id'], 'Name': 'test-th',
            'RoleArn': 'arn:aws:iam::000000000000:role/r',
            'SourceS3Path': {'Bucket': 'b', 'Key': 'th.txt'},
        })
        assert resp is not None
        assert resp['Name'] == 'test-th'

    def test_describe_thesaurus(self):
        idx = self._create_index()
        create = _load_handler('create-thesaurus')
        describe = _load_handler('describe-thesaurus')
        c = create(self.store, {
            'IndexId': idx['Id'], 'Name': 'th1',
            'RoleArn': 'arn:aws:iam::000000000000:role/r',
            'SourceS3Path': {'Bucket': 'b', 'Key': 'th.txt'},
        })
        resp = describe(self.store, {'Id': c['Id'], 'IndexId': idx['Id']})
        assert resp['Id'] == c['Id']

    def test_delete_thesaurus(self):
        idx = self._create_index()
        create = _load_handler('create-thesaurus')
        delete = _load_handler('delete-thesaurus')
        describe = _load_handler('describe-thesaurus')
        c = create(self.store, {
            'IndexId': idx['Id'], 'Name': 'th-del',
            'RoleArn': 'arn:aws:iam::000000000000:role/r',
            'SourceS3Path': {'Bucket': 'b', 'Key': 'th.txt'},
        })
        delete(self.store, {'Id': c['Id'], 'IndexId': idx['Id']})
        with pytest.raises(ResourceNotFoundException):
            describe(self.store, {'Id': c['Id'], 'IndexId': idx['Id']})


class TestExperience:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = KendraStore()
        return self._store

    def _create_index(self):
        h = _load_handler('create-index')
        return h(self.store, {'Name': 'exp-idx', 'RoleArn': 'arn:aws:iam::000000000000:role/r'})

    def test_create_experience(self):
        idx = self._create_index()
        h = _load_handler('create-experience')
        resp = h(self.store, {'IndexId': idx['Id'], 'Name': 'test-exp'})
        assert resp is not None
        assert resp['Name'] == 'test-exp'

    def test_describe_experience(self):
        idx = self._create_index()
        create = _load_handler('create-experience')
        describe = _load_handler('describe-experience')
        c = create(self.store, {'IndexId': idx['Id'], 'Name': 'exp1'})
        resp = describe(self.store, {'Id': c['Id'], 'IndexId': idx['Id']})
        assert resp['Id'] == c['Id']

    def test_delete_experience(self):
        idx = self._create_index()
        create = _load_handler('create-experience')
        delete = _load_handler('delete-experience')
        describe = _load_handler('describe-experience')
        c = create(self.store, {'IndexId': idx['Id'], 'Name': 'exp-del'})
        delete(self.store, {'Id': c['Id'], 'IndexId': idx['Id']})
        with pytest.raises(ResourceNotFoundException):
            describe(self.store, {'Id': c['Id'], 'IndexId': idx['Id']})

    def test_list_experiences(self):
        idx = self._create_index()
        create = _load_handler('create-experience')
        list_h = _load_handler('list-experiences')
        create(self.store, {'IndexId': idx['Id'], 'Name': 'exp-a'})
        resp = list_h(self.store, {'IndexId': idx['Id']})
        assert 'SummaryItems' in resp


class TestTags:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = KendraStore()
        return self._store

    def _create_index_with_tags(self):
        h = _load_handler('create-index')
        return h(self.store, {
            'Name': 'tagged-idx',
            'RoleArn': 'arn:aws:iam::000000000000:role/r',
            'tags': [{'Key': 'env', 'Value': 'test'}],
        })

    def test_list_tags(self):
        idx = self._create_index_with_tags()
        h = _load_handler('list-tags-for-resource')
        resp = h(self.store, {'ResourceARN': f'arn:aws:kendra:us-east-1:000000000000:index/{idx["Id"]}'})
        assert 'Tags' in resp

    def test_tag_resource(self):
        idx = self._create_index_with_tags()
        h = _load_handler('tag-resource')
        h(self.store, {
            'ResourceARN': f'arn:aws:kendra:us-east-1:000000000000:index/{idx["Id"]}',
            'Tags': [{'Key': 'team', 'Value': 'search'}],
        })
        list_tags = _load_handler('list-tags-for-resource')
        resp = list_tags(self.store, {'ResourceARN': f'arn:aws:kendra:us-east-1:000000000000:index/{idx["Id"]}'})
        assert resp is not None

    def test_untag_resource(self):
        idx = self._create_index_with_tags()
        h = _load_handler('untag-resource')
        h(self.store, {
            'ResourceARN': f'arn:aws:kendra:us-east-1:000000000000:index/{idx["Id"]}',
            'TagKeys': ['env'],
        })
        list_tags = _load_handler('list-tags-for-resource')
        resp = list_tags(self.store, {'ResourceARN': f'arn:aws:kendra:us-east-1:000000000000:index/{idx["Id"]}'})
        assert resp is not None


class TestQuery:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = KendraStore()
        return self._store

    def test_query(self):
        create = _load_handler('create-index')
        idx = create(self.store, {'Name': 'q-idx', 'RoleArn': 'arn:aws:iam::000000000000:role/r'})
        h = _load_handler('query')
        resp = h(self.store, {'IndexId': idx['Id'], 'QueryText': 'what is dynamodb'})
        assert resp is not None
        assert 'ResultItems' in resp
        assert 'TotalNumberOfResults' in resp

    def test_query_nonexistent_index(self):
        h = _load_handler('query')
        with pytest.raises(ResourceNotFoundException):
            h(self.store, {'IndexId': 'nonexistent', 'QueryText': 'test'})
