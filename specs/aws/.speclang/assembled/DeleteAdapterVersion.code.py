// spec:trace spec=/home/kara/totalstack/specs/aws/textract/DeleteAdapterVersion.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

def execute_delete_adapter_version(store, request: dict) -> dict:
    adapter_id = request.get("AdapterId")
    version = request.get("AdapterVersion")
    if not adapter_id or not version:
        raise InvalidParameterException("AdapterId and AdapterVersion are required")

    a = store.get_adapter(adapter_id)
    if version not in a.versions:
        raise ResourceNotFoundException(f"AdapterVersion {version} not found")
    del a.versions[version]
    return {}