def handler(store, r: dict) -> dict:
    return store.describe_stream(r["StreamName"], r.get("Limit", 10), r.get("ExclusiveStartShardId"))