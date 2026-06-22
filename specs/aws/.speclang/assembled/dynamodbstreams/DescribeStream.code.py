def handler(store, request: dict) -> dict:
    return store.describe_stream(
        StreamArn=request["StreamArn"],
        Limit=request.get("Limit"),
        ExclusiveStartShardId=request.get("ExclusiveStartShardId"),
    )
