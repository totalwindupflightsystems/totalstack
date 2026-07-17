def handler(store, r: dict) -> dict:
    return store.get_shard_iterator(r["StreamName"], r["ShardId"], r["ShardIteratorType"])