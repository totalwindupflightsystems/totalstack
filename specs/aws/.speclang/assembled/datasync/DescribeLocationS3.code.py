def describe_location(store, request: dict) -> dict:
    return store.describe_location(LocationArn=request["LocationArn"])
