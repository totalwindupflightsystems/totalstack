def handler(store, r: dict) -> dict:
    return store.describe_parameters(r.get("Filters"), r.get("MaxResults", 50))