# spec:trace: aws/athena/DeletePreparedStatement.spec.py.md#implementation
# spec:id: @specs/aws/athena/deletepreparedstatement
# spec:generated: DO NOT EDIT — edit the spec instead

def delete_prepared_statement(store: 'AthenaStore', request: dict) -> dict:
    """Delete a prepared statement."""
    name = request.get('StatementName')
    workgroup = request.get('WorkGroup')
    if not name or not workgroup:
        raise InvalidRequestException('StatementName and WorkGroup are required')
    key = (workgroup, name)
    if key not in store.prepared_statements:
        raise ResourceNotFoundException(f'Prepared statement {name} not found in workgroup {workgroup}')
    del store.prepared_statements[key]
    return {}

