# spec:trace: aws/athena/CreateWorkGroup.spec.py.md#implementation
# spec:id: @specs/aws/athena/createworkgroup
# spec:generated: DO NOT EDIT — edit the spec instead

def create_work_group(store: 'AthenaStore', request: dict) -> dict:
    """Create a new Athena workgroup."""
    name = request.get('Name')
    if not name:
        raise InvalidRequestException('Name is required')
    if name in store.work_groups:
        raise InvalidRequestException(f'Workgroup {name} already exists')

    wg = {
        'Name': name,
        'State': 'ENABLED',
        'Description': request.get('Description', ''),
        'Configuration': request.get('Configuration', {}),
    }
    store.work_groups[name] = wg

    tags = request.get('Tags', [])
    if tags:
        arn = f'arn:aws:athena:us-east-1:000000000000:workgroup/{name}'
        store.tags[arn] = {t['Key']: t['Value'] for t in tags}

    return {}

