def handler(store, request: dict) -> dict:
    record = store.get_branch(request["appId"], request["branchName"])
    return {"branch": record.to_dict()}
