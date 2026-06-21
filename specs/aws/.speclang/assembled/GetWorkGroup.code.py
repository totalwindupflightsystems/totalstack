// spec:trace spec=/home/kara/totalstack/specs/aws/athena/GetWorkGroup.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

def get_work_group(store: 'AthenaStore', request: dict) -> dict:
    """Get an Athena workgroup by name."""
    name = request.get('WorkGroup')
    if not name:
        raise InvalidRequestException('WorkGroup is required')
    if name not in store.work_groups:
        raise ResourceNotFoundException(f'Workgroup {name} not found')
    return {'WorkGroup': dict(store.work_groups[name])}