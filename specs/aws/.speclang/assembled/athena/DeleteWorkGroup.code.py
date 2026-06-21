# spec:trace: aws/athena/DeleteWorkGroup.spec.py.md#implementation
# spec:id: @specs/aws/athena/deleteworkgroup
# spec:generated: DO NOT EDIT — edit the spec instead

def delete_work_group(store: 'AthenaStore', request: dict) -> dict:
    """Delete an Athena workgroup."""
    name = request.get('WorkGroup')
    if not name:
        raise InvalidRequestException('WorkGroup is required')
    if name not in store.work_groups:
        raise ResourceNotFoundException(f'Workgroup {name} not found')
    del store.work_groups[name]
    return {}

