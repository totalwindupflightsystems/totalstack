# spec:trace: aws/textract/CreateAdapterVersion.spec.py.md#implementation
# spec:id: @specs/aws/textract/createadapterversion
# spec:generated: DO NOT EDIT — edit the spec instead

import uuid

def execute_create_adapter_version(store, request: dict) -> dict:
    adapter_id = request.get("AdapterId")
    if not adapter_id:
        raise InvalidParameterException("AdapterId is required")

    a = store.get_adapter(adapter_id)  # validates existence

    version = str(uuid.uuid4())[:8]
    v_record = AdapterVersionRecord(
        adapter_version=version,
        creation_time=time.time(),
        status="CREATING",
        feature_types=a.feature_types,
    )
    a.versions[version] = v_record
    # Auto-complete in local dev
    v_record.status = "ACTIVE"

    tags = request.get("Tags", {})
    if tags:
        arn = f"arn:aws:textract:us-east-1:000000000000:adapter/{adapter_id}/version/{version}"
        store.tag_resource(arn, {t["Key"]: t["Value"] for t in tags})

    return {"AdapterId": adapter_id, "AdapterVersion": version}

