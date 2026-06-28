def delete_location(store, request: dict) -> dict:
    return store.delete_location(LocationArn=request["LocationArn"])
