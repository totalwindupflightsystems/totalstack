// spec:trace spec=/home/kara/totalstack/specs/aws/athena/GetPreparedStatement.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

def get_prepared_statement(store: 'AthenaStore', request: dict) -> dict:
    """Get a prepared statement."""
    name = request.get('StatementName')
    workgroup = request.get('WorkGroup')
    if not name:
        raise InvalidRequestException('StatementName is required')
    if not workgroup:
        raise InvalidRequestException('WorkGroup is required')
    key = (workgroup, name)
    if key not in store.prepared_statements:
        raise ResourceNotFoundException(f'Prepared statement {name} not found in workgroup {workgroup}')
    return {'PreparedStatement': dict(store.prepared_statements[key])}