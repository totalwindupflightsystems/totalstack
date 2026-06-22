
def delete_work_group(store: 'AthenaStore', request: dict) -> dict:
    """Delete an Athena workgroup."""
    name = request.get('WorkGroup')
    if not name:
        raise InvalidRequestException('WorkGroup is required')
    if name not in store.work_groups:
        raise ResourceNotFoundException(f'Workgroup {name} not found')
    del store.work_groups[name]
    return {}
