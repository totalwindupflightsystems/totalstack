def handler(store, request: dict) -> dict:
    record = store.delete_branch(request["appId"], request["branchName"])
    return {"branch": record.to_dict()}
