def handler(store, r: dict) -> dict:
    return store.tag_stream(r["StreamName"], r["Tags"])