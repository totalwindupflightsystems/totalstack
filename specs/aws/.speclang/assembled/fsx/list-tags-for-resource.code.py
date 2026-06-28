def handler(store, request: dict) -> dict:
    arn = request["ResourceARN"]
    record = _find_by_arn(store, arn)
    tags = record.Tags
    return {"Tags": [{"Key": k, "Value": v} for k, v in tags.items()]}
