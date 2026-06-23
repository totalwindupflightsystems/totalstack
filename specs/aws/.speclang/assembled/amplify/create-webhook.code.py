def handler(store, request: dict) -> dict:
    record = store.create_webhook(request["appId"], request["branchName"], **{k: v for k, v in request.items() if k not in ("appId", "branchName")})
    return {"webhook": record.to_dict()}
