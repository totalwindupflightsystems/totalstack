def handler(store, request: dict) -> dict:
    arn = request["ResourceARN"]
    record = _find_by_arn(store, arn)
    for t in request.get("Tags", []):
        record.Tags[t["Key"]] = t["Value"]
    return {}
