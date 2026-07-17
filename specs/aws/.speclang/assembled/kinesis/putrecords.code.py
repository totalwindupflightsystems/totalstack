def handler(store, r: dict) -> dict:
    return store.put_records(r["StreamName"], r["Records"])