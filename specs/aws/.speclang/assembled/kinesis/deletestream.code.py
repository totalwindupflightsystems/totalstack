def handler(store, r: dict) -> dict:
    return store.delete_stream(r["StreamName"], r.get("EnforceConsumerDeletion", False))