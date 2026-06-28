def handler(store, request: dict) -> dict:
    arn = request["ResourceARN"]
    record = _find_by_arn(store, arn)
    for k in request.get("TagKeys", []):
        record.Tags.pop(k, None)
    return {}
