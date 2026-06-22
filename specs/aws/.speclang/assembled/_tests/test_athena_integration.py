"""Integration test for Athena — generated handlers against real AthenaStore."""
import os, sys, types, importlib.util

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'athena')

# Load models first
models_spec = importlib.util.spec_from_file_location(
    'models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)
AthenaStore = models_mod.AthenaStore
InvalidRequestException = models_mod.InvalidRequestException
ResourceNotFoundException = models_mod.ResourceNotFoundException


def _load_handler(op_name):
    """Load a generated handler, injecting exceptions."""
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    mod.AthenaStore = AthenaStore
    mod.InvalidRequestException = InvalidRequestException
    mod.ResourceNotFoundException = ResourceNotFoundException
    spec.loader.exec_module(mod)
    # Find the handler function
    handler = None
    for v in mod.__dict__.values():
        if isinstance(v, types.FunctionType) and not v.__name__.startswith('_'):
            handler = v
            break
    return handler


def test_create_workgroup_happy_path():
    store = AthenaStore()
    handler = _load_handler('CreateWorkGroup')
    resp = handler(store, {'Name': 'test-wg', 'Description': 'A test workgroup'})
    assert resp['WorkGroup']['Name'] == 'test-wg'
    assert 'test-wg' in store.work_groups
    assert store.work_groups['test-wg']['State'] == 'ENABLED'


def test_create_workgroup_missing_name():
    store = AthenaStore()
    handler = _load_handler('CreateWorkGroup')
    try:
        handler(store, {})
        assert False, "Should have raised"
    except InvalidRequestException:
        pass


def test_create_workgroup_duplicate():
    store = AthenaStore()
    handler = _load_handler('CreateWorkGroup')
    handler(store, {'Name': 'dup-wg'})
    try:
        handler(store, {'Name': 'dup-wg'})
        assert False, "Should have raised"
    except InvalidRequestException:
        pass


def test_get_workgroup():
    store = AthenaStore()
    create = _load_handler('CreateWorkGroup')
    get = _load_handler('GetWorkGroup')
    create(store, {'Name': 'fetch-wg', 'Description': 'Fetch test'})
    resp = get(store, {'WorkGroup': 'fetch-wg'})
    assert resp['WorkGroup']['Name'] == 'fetch-wg'


def test_get_workgroup_nonexistent():
    store = AthenaStore()
    handler = _load_handler('GetWorkGroup')
    try:
        handler(store, {'WorkGroup': 'nonexistent'})
        assert False, "Should have raised"
    except ResourceNotFoundException:
        pass


def test_start_query_execution():
    store = AthenaStore()
    handler = _load_handler('StartQueryExecution')
    resp = handler(store, {'QueryString': 'SELECT 1'})
    assert 'QueryExecutionId' in resp
    assert resp['QueryExecutionId'] in store.query_executions
    qe = store.query_executions[resp['QueryExecutionId']]
    assert qe['Status']['State'] == 'SUCCEEDED'


if __name__ == '__main__':
    import traceback
    tests = [
        test_create_workgroup_happy_path,
        test_create_workgroup_missing_name,
        test_create_workgroup_duplicate,
        test_get_workgroup,
        test_get_workgroup_nonexistent,
        test_start_query_execution,
    ]
    passed = 0
    for t in tests:
        try:
            t()
            print(f'  ✅ {t.__name__}')
            passed += 1
        except Exception as e:
            print(f'  ❌ {t.__name__}: {e}')
            traceback.print_exc()
    print(f'\n{passed}/{len(tests)} passed')
