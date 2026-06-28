def handler(store, request: dict) -> dict:
    store.untag_resource(request["ResourceArn"], request["TagKeys"])
    return {"RequestId": "", "Status": 200}
