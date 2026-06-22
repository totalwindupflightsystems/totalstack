def handler(store, request: dict) -> dict:
    return store.get_shard_iterator(
        StreamArn=request["StreamArn"],
        ShardId=request["ShardId"],
        ShardIteratorType=request["ShardIteratorType"],
        SequenceNumber=request.get("SequenceNumber"),
    )
