def handler(store, request: dict) -> dict:
    record = store.create_branch(request["appId"], request["branchName"], **{k: v for k, v in request.items() if k not in ("appId", "branchName")})
    return {"branch": record.to_dict()}
