# spec:trace: aws/textract/UpdateAdapter.spec.py.md#implementation
# spec:id: @specs/aws/textract/updateadapter
# spec:generated: DO NOT EDIT — edit the spec instead

def execute_update_adapter(store, request: dict) -> dict:
    adapter_id = request.get("AdapterId")
    if not adapter_id:
        raise InvalidParameterException("AdapterId is required")
    a = store.get_adapter(adapter_id)

    if "AdapterName" in request:
        a.adapter_name = request["AdapterName"]
    if "Description" in request:
        a.description = request["Description"]
    if "AutoUpdate" in request:
        a.auto_update = request["AutoUpdate"]

    return {
        "AdapterId": a.adapter_id,
        "AdapterName": a.adapter_name,
        "FeatureTypes": a.feature_types,
        "Description": a.description,
        "AutoUpdate": a.auto_update,
        "CreationTime": a.creation_time,
        "Status": a.status,
    }

