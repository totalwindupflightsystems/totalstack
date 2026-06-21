# spec:trace: aws/athena/CreatePreparedStatement.spec.py.md#implementation
# spec:id: @specs/aws/athena/createpreparedstatement
# spec:generated: DO NOT EDIT — edit the spec instead

def create_prepared_statement(store: 'AthenaStore', request: dict) -> dict:
    """Create a prepared statement."""
    name = request.get('StatementName')
    workgroup = request.get('WorkGroup')
    query = request.get('QueryStatement')
    if not name:
        raise InvalidRequestException('StatementName is required')
    if not workgroup:
        raise InvalidRequestException('WorkGroup is required')
    if not query:
        raise InvalidRequestException('QueryStatement is required')

    key = (workgroup, name)
    if key in store.prepared_statements:
        raise InvalidRequestException(f'Prepared statement {name} already exists in workgroup {workgroup}')

    store.prepared_statements[key] = {
        'StatementName': name,
        'WorkGroupName': workgroup,
        'QueryStatement': query,
        'Description': request.get('Description', ''),
    }
    return {}

