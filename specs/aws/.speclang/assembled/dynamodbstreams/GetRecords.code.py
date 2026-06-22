def handler(store, request: dict) -> dict:
    return store.get_records(
        ShardIterator=request["ShardIterator"],
        Limit=request.get("Limit"),
    )
