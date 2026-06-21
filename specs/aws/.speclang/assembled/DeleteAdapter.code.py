// spec:trace spec=/home/kara/totalstack/specs/aws/textract/DeleteAdapter.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

def execute_delete_adapter(store, request: dict) -> dict:
    adapter_id = request.get("AdapterId")
    if not adapter_id:
        raise InvalidParameterException("AdapterId is required")
    store.delete_adapter(adapter_id)
    return {}