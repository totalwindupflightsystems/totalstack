def handler(store, r: dict) -> dict:
    return store.put_record(r["StreamName"], r["Data"], r["PartitionKey"])