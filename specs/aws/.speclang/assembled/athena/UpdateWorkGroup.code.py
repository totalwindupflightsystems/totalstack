# spec:trace: aws/athena/UpdateWorkGroup.spec.py.md#implementation
# spec:id: @specs/aws/athena/updateworkgroup
# spec:generated: DO NOT EDIT — edit the spec instead

def update_work_group(store: 'AthenaStore', request: dict) -> dict:
    """Update an Athena workgroup."""
    name = request.get('WorkGroup')
    if not name:
        raise InvalidRequestException('WorkGroup is required')
    if name not in store.work_groups:
        raise ResourceNotFoundException(f'Workgroup {name} not found')
    wg = store.work_groups[name]
    if 'Description' in request:
        wg['Description'] = request['Description']
    if 'ConfigurationUpdates' in request:
        wg['Configuration'].update(request['ConfigurationUpdates'])
    if 'State' in request:
        wg['State'] = request['State']
    return {'WorkGroup': dict(wg)}

