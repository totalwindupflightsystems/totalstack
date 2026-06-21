"""Integration test for Athena — real AthenaStore."""
import pytest
import os
import sys
import importlib.util
import types

ASSEMBLED_DIR = os.path.dirname(__file__)
ATHENA_DIR = os.path.join(ASSEMBLED_DIR, '..', 'athena')
sys.path.insert(0, os.path.join(ASSEMBLED_DIR, '..'))

from athena import AthenaStore, InvalidRequestException, ResourceNotFoundException, InternalServerException


def _load_handler(op_name, suffix=''):
    """Load generated code.py from assembled/athena directory."""
    path = os.path.join(ATHENA_DIR, op_name + suffix + '.code.py')
    if not os.path.exists(path):
        path = os.path.join(ATHENA_DIR, op_name + '.code.py')
    if not os.path.exists(path):
        raise FileNotFoundError(f'Cannot find {path}')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    # Inject exceptions into the module namespace since generated code
    # references them without explicit imports
    mod.InvalidRequestException = InvalidRequestException
    mod.ResourceNotFoundException = ResourceNotFoundException
    mod.InternalServerException = InternalServerException
    spec.loader.exec_module(mod)
    return mod


def _get_handler(mod):
    """Get the first non-private function from a module using types.FunctionType."""
    handlers = [v for k, v in mod.__dict__.items()
                if isinstance(v, types.FunctionType) and not k.startswith('_')]
    return handlers[0] if handlers else None


# ── DataCatalogs ──────────────────────────────────────────────

class TestDataCatalogIntegration:

    @pytest.fixture
    def store(self):
        return AthenaStore()

    def test_create_happy_path(self, store):
        mod = _load_handler('CreateDataCatalog')
        handler = _get_handler(mod)
        response = handler(store, {'Name': 'test-catalog', 'Type': 'HIVE', 'Description': 'test'})
        assert response is not None
        assert response['DataCatalog']['Name'] == 'test-catalog'
        assert response['DataCatalog']['Type'] == 'HIVE'

    def test_create_missing_name(self, store):
        mod = _load_handler('CreateDataCatalog')
        handler = _get_handler(mod)
        with pytest.raises(InvalidRequestException):
            handler(store, {'Type': 'HIVE'})

    def test_create_duplicate(self, store):
        mod = _load_handler('CreateDataCatalog')
        handler = _get_handler(mod)
        handler(store, {'Name': 'dup', 'Type': 'HIVE'})
        with pytest.raises(InvalidRequestException):
            handler(store, {'Name': 'dup', 'Type': 'GLUE'})

    def test_get_happy_path(self, store):
        _get_handler(_load_handler('CreateDataCatalog'))(store, {'Name': 'get-test', 'Type': 'LAMBDA'})
        mod = _load_handler('GetDataCatalog')
        handler = _get_handler(mod)
        response = handler(store, {'Name': 'get-test'})
        assert response['DataCatalog']['Name'] == 'get-test'

    def test_get_nonexistent(self, store):
        mod = _load_handler('GetDataCatalog')
        handler = _get_handler(mod)
        with pytest.raises(ResourceNotFoundException):
            handler(store, {'Name': 'nonexistent'})

    def test_list_pagination(self, store):
        mod = _load_handler('ListDataCatalogs')
        handler = _get_handler(mod)
        # Create 3 catalogs
        for i in range(3):
            _get_handler(_load_handler('CreateDataCatalog'))(store, {'Name': f'cat-{i}', 'Type': 'HIVE'})
        response = handler(store, {'MaxResults': 2})
        assert len(response['DataCatalogsSummary']) == 2
        assert 'NextToken' in response

    def test_update_happy_path(self, store):
        _get_handler(_load_handler('CreateDataCatalog'))(store, {'Name': 'update-me', 'Type': 'HIVE'})
        mod = _load_handler('UpdateDataCatalog')
        handler = _get_handler(mod)
        response = handler(store, {'Name': 'update-me', 'Type': 'GLUE', 'Description': 'updated'})
        assert response['DataCatalog']['Type'] == 'GLUE'
        assert response['DataCatalog']['Description'] == 'updated'

    def test_delete_happy_path(self, store):
        _get_handler(_load_handler('CreateDataCatalog'))(store, {'Name': 'to-delete', 'Type': 'HIVE'})
        mod = _load_handler('DeleteDataCatalog')
        handler = _get_handler(mod)
        handler(store, {'Name': 'to-delete'})
        assert 'to-delete' not in store.data_catalogs


# ── WorkGroups ─────────────────────────────────────────────────

class TestWorkGroupIntegration:

    @pytest.fixture
    def store(self):
        return AthenaStore()

    def test_create_happy_path(self, store):
        mod = _load_handler('CreateWorkGroup')
        handler = _get_handler(mod)
        response = handler(store, {'Name': 'test-wg', 'Description': 'test'})
        assert response['WorkGroup']['Name'] == 'test-wg'
        assert response['WorkGroup']['State'] == 'ENABLED'

    def test_create_missing_name(self, store):
        mod = _load_handler('CreateWorkGroup')
        handler = _get_handler(mod)
        with pytest.raises(InvalidRequestException):
            handler(store, {})

    def test_create_duplicate(self, store):
        mod = _load_handler('CreateWorkGroup')
        handler = _get_handler(mod)
        handler(store, {'Name': 'dup-wg'})
        with pytest.raises(InvalidRequestException):
            handler(store, {'Name': 'dup-wg'})

    def test_get_happy_path(self, store):
        _get_handler(_load_handler('CreateWorkGroup'))(store, {'Name': 'get-wg'})
        mod = _load_handler('GetWorkGroup')
        handler = _get_handler(mod)
        response = handler(store, {'WorkGroup': 'get-wg'})
        assert response['WorkGroup']['Name'] == 'get-wg'

    def test_get_nonexistent(self, store):
        mod = _load_handler('GetWorkGroup')
        handler = _get_handler(mod)
        with pytest.raises(ResourceNotFoundException):
            handler(store, {'WorkGroup': 'nope'})

    def test_list_and_delete(self, store):
        _get_handler(_load_handler('CreateWorkGroup'))(store, {'Name': 'wg-1'})
        _get_handler(_load_handler('CreateWorkGroup'))(store, {'Name': 'wg-2'})
        mod = _load_handler('ListWorkGroups')
        handler = _get_handler(mod)
        response = handler(store, {})
        assert len(response['WorkGroups']) == 2

        _get_handler(_load_handler('DeleteWorkGroup'))(store, {'WorkGroup': 'wg-1'})
        assert 'wg-1' not in store.work_groups

    def test_update_happy_path(self, store):
        _get_handler(_load_handler('CreateWorkGroup'))(store, {'Name': 'update-wg'})
        mod = _load_handler('UpdateWorkGroup')
        handler = _get_handler(mod)
        response = handler(store, {'WorkGroup': 'update-wg', 'Description': 'new desc'})
        assert response['WorkGroup']['Description'] == 'new desc'


# ── NamedQueries ───────────────────────────────────────────────

class TestNamedQueryIntegration:

    @pytest.fixture
    def store(self):
        s = AthenaStore()
        s.work_groups['primary'] = {'Name': 'primary', 'State': 'ENABLED', 'Description': '', 'Configuration': {}}
        return s

    def test_create_happy_path(self, store):
        mod = _load_handler('CreateNamedQuery')
        handler = _get_handler(mod)
        response = handler(store, {'Name': 'my-query', 'Database': 'mydb', 'QueryString': 'SELECT 1'})
        assert 'NamedQueryId' in response
        qid = response['NamedQueryId']
        assert qid in store.named_queries

    def test_create_missing_fields(self, store):
        mod = _load_handler('CreateNamedQuery')
        handler = _get_handler(mod)
        with pytest.raises(InvalidRequestException):
            handler(store, {'Name': 'q'})

    def test_get_happy_path(self, store):
        create_resp = _get_handler(_load_handler('CreateNamedQuery'))(store, {'Name': 'q1', 'Database': 'db', 'QueryString': 'SELECT * FROM t'})
        qid = create_resp['NamedQueryId']
        mod = _load_handler('GetNamedQuery')
        handler = _get_handler(mod)
        response = handler(store, {'NamedQueryId': qid})
        assert response['NamedQuery']['Name'] == 'q1'

    def test_get_nonexistent(self, store):
        mod = _load_handler('GetNamedQuery')
        handler = _get_handler(mod)
        with pytest.raises(ResourceNotFoundException):
            handler(store, {'NamedQueryId': 'nonexistent'})

    def test_list_and_delete(self, store):
        h = _get_handler(_load_handler('CreateNamedQuery'))
        h(store, {'Name': 'q-a', 'Database': 'db', 'QueryString': 'SELECT 1'})
        h(store, {'Name': 'q-b', 'Database': 'db', 'QueryString': 'SELECT 2'})
        r = _get_handler(_load_handler('ListNamedQueries'))(store, {})
        assert len(r['NamedQueryIds']) == 2
        # Delete first
        _get_handler(_load_handler('DeleteNamedQuery'))(store, {'NamedQueryId': r['NamedQueryIds'][0]})
        r2 = _get_handler(_load_handler('ListNamedQueries'))(store, {})
        assert len(r2['NamedQueryIds']) == 1

    def test_batch_get(self, store):
        h = _get_handler(_load_handler('CreateNamedQuery'))
        r1 = h(store, {'Name': 'batch-1', 'Database': 'db', 'QueryString': 'Q1'})
        r2 = h(store, {'Name': 'batch-2', 'Database': 'db', 'QueryString': 'Q2'})
        mod = _load_handler('BatchGetNamedQuery')
        handler = _get_handler(mod)
        resp = handler(store, {'NamedQueryIds': [r1['NamedQueryId'], r2['NamedQueryId'], 'fake-id']})
        assert len(resp['NamedQueries']) == 2
        assert len(resp.get('UnprocessedNamedQueryIds', [])) == 1


# ── QueryExecutions ────────────────────────────────────────────

class TestQueryExecutionIntegration:

    @pytest.fixture
    def store(self):
        s = AthenaStore()
        s.work_groups['primary'] = {'Name': 'primary', 'State': 'ENABLED', 'Description': '', 'Configuration': {}}
        return s

    def test_start_happy_path(self, store):
        mod = _load_handler('StartQueryExecution')
        handler = _get_handler(mod)
        response = handler(store, {'QueryString': 'SELECT 1'})
        assert 'QueryExecutionId' in response
        qid = response['QueryExecutionId']
        assert qid in store.query_executions
        assert store.query_executions[qid]['Status']['State'] == 'SUCCEEDED'

    def test_start_missing_query(self, store):
        mod = _load_handler('StartQueryExecution')
        handler = _get_handler(mod)
        with pytest.raises(InvalidRequestException):
            handler(store, {})

    def test_get_happy_path(self, store):
        r = _get_handler(_load_handler('StartQueryExecution'))(store, {'QueryString': 'SELECT 2'})
        mod = _load_handler('GetQueryExecution')
        handler = _get_handler(mod)
        response = handler(store, {'QueryExecutionId': r['QueryExecutionId']})
        assert response['QueryExecution']['Query'] == 'SELECT 2'

    def test_get_nonexistent(self, store):
        mod = _load_handler('GetQueryExecution')
        handler = _get_handler(mod)
        with pytest.raises(ResourceNotFoundException):
            handler(store, {'QueryExecutionId': 'none'})

    def test_stop_happy_path(self, store):
        r = _get_handler(_load_handler('StartQueryExecution'))(store, {'QueryString': 'SELECT 3'})
        mod = _load_handler('StopQueryExecution')
        handler = _get_handler(mod)
        handler(store, {'QueryExecutionId': r['QueryExecutionId']})
        assert store.query_executions[r['QueryExecutionId']]['Status']['State'] == 'CANCELLED'

    def test_get_results(self, store):
        mod = _load_handler('GetQueryResults')
        handler = _get_handler(mod)
        r = _get_handler(_load_handler('StartQueryExecution'))(store, {'QueryString': 'SELECT 1'})
        response = handler(store, {'QueryExecutionId': r['QueryExecutionId']})
        assert 'ResultSet' in response

    def test_list_and_batch(self, store):
        h = _get_handler(_load_handler('StartQueryExecution'))
        h(store, {'QueryString': 'Q1'})
        h(store, {'QueryString': 'Q2'})
        r = _get_handler(_load_handler('ListQueryExecutions'))(store, {})
        assert len(r['QueryExecutionIds']) == 2
        mod = _load_handler('BatchGetQueryExecution')
        handler = _get_handler(mod)
        resp = handler(store, {'QueryExecutionIds': r['QueryExecutionIds']})
        assert len(resp['QueryExecutions']) == 2


# ── PreparedStatements ─────────────────────────────────────────

class TestPreparedStatementIntegration:

    @pytest.fixture
    def store(self):
        s = AthenaStore()
        s.work_groups['primary'] = {'Name': 'primary', 'State': 'ENABLED', 'Description': '', 'Configuration': {}}
        return s

    def test_create_happy_path(self, store):
        mod = _load_handler('CreatePreparedStatement')
        handler = _get_handler(mod)
        handler(store, {'StatementName': 'ps1', 'WorkGroup': 'primary', 'QueryStatement': 'SELECT ?'})
        assert ('primary', 'ps1') in store.prepared_statements

    def test_create_missing_fields(self, store):
        mod = _load_handler('CreatePreparedStatement')
        handler = _get_handler(mod)
        with pytest.raises(InvalidRequestException):
            handler(store, {'StatementName': 'ps'})

    def test_create_duplicate(self, store):
        mod = _load_handler('CreatePreparedStatement')
        handler = _get_handler(mod)
        handler(store, {'StatementName': 'dup', 'WorkGroup': 'primary', 'QueryStatement': 'SELECT 1'})
        with pytest.raises(InvalidRequestException):
            handler(store, {'StatementName': 'dup', 'WorkGroup': 'primary', 'QueryStatement': 'SELECT 2'})

    def test_get_happy_path(self, store):
        _get_handler(_load_handler('CreatePreparedStatement'))(store, {'StatementName': 'ps-get', 'WorkGroup': 'primary', 'QueryStatement': 'X'})
        mod = _load_handler('GetPreparedStatement')
        handler = _get_handler(mod)
        r = handler(store, {'StatementName': 'ps-get', 'WorkGroup': 'primary'})
        assert r['PreparedStatement']['StatementName'] == 'ps-get'

    def test_get_nonexistent(self, store):
        mod = _load_handler('GetPreparedStatement')
        handler = _get_handler(mod)
        with pytest.raises(ResourceNotFoundException):
            handler(store, {'StatementName': 'nope', 'WorkGroup': 'primary'})

    def test_list_update_delete(self, store):
        h = _get_handler(_load_handler('CreatePreparedStatement'))
        h(store, {'StatementName': 'a', 'WorkGroup': 'primary', 'QueryStatement': '1'})
        h(store, {'StatementName': 'b', 'WorkGroup': 'primary', 'QueryStatement': '2'})
        r = _get_handler(_load_handler('ListPreparedStatements'))(store, {'WorkGroup': 'primary'})
        assert len(r['PreparedStatements']) == 2

        _get_handler(_load_handler('UpdatePreparedStatement'))(store, {'StatementName': 'a', 'WorkGroup': 'primary', 'QueryStatement': 'NEW'})
        assert store.prepared_statements[('primary', 'a')]['QueryStatement'] == 'NEW'

        _get_handler(_load_handler('DeletePreparedStatement'))(store, {'StatementName': 'a', 'WorkGroup': 'primary'})
        assert ('primary', 'a') not in store.prepared_statements


# ── Databases & Tables ────────────────────────────────────────

class TestDatabaseTableIntegration:

    @pytest.fixture
    def store(self):
        s = AthenaStore()
        s.databases[('AwsDataCatalog', 'testdb')] = {'Name': 'testdb', 'Description': 'Test DB'}
        s.table_metadata[('AwsDataCatalog', 'testdb', 'testtbl')] = {'Name': 'testtbl', 'TableType': 'EXTERNAL_TABLE'}
        return s

    def test_get_database(self, store):
        mod = _load_handler('GetDatabase')
        handler = _get_handler(mod)
        r = handler(store, {'DatabaseName': 'testdb'})
        assert r['Database']['Name'] == 'testdb'

    def test_get_database_nonexistent(self, store):
        mod = _load_handler('GetDatabase')
        handler = _get_handler(mod)
        with pytest.raises(ResourceNotFoundException):
            handler(store, {'DatabaseName': 'nope'})

    def test_list_databases(self, store):
        mod = _load_handler('ListDatabases')
        handler = _get_handler(mod)
        r = handler(store, {})
        assert len(r['DatabaseList']) == 1

    def test_get_table_metadata(self, store):
        mod = _load_handler('GetTableMetadata')
        handler = _get_handler(mod)
        r = handler(store, {'DatabaseName': 'testdb', 'TableName': 'testtbl'})
        assert r['TableMetadata']['Name'] == 'testtbl'

    def test_list_table_metadata(self, store):
        mod = _load_handler('ListTableMetadata')
        handler = _get_handler(mod)
        r = handler(store, {'DatabaseName': 'testdb'})
        assert len(r['TableMetadataList']) == 1


# ── Tags ───────────────────────────────────────────────────────

class TestTagsIntegration:

    @pytest.fixture
    def store(self):
        return AthenaStore()

    def test_tag_untag_list(self, store):
        arn = 'arn:aws:athena:us-east-1:000000000000:workgroup/test-wg'
        _get_handler(_load_handler('TagResource'))(store, {
            'ResourceARN': arn,
            'Tags': [{'Key': 'env', 'Value': 'dev'}, {'Key': 'team', 'Value': 'backend'}]
        })
        r = _get_handler(_load_handler('ListTagsForResource'))(store, {'ResourceARN': arn})
        assert len(r['Tags']) == 2

        _get_handler(_load_handler('UntagResource'))(store, {
            'ResourceARN': arn, 'TagKeys': ['env']
        })
        r2 = _get_handler(_load_handler('ListTagsForResource'))(store, {'ResourceARN': arn})
        assert len(r2['Tags']) == 1
        assert r2['Tags'][0]['Key'] == 'team'
