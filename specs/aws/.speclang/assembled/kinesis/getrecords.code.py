def handler(store, r: dict) -> dict:
    return store.get_records(r["ShardIterator"], r.get("Limit", 10))