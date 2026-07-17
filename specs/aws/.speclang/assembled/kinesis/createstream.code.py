def handler(store, r: dict) -> dict:
    return store.create_stream(r["StreamName"], r.get("ShardCount", 1))