def handler(store, request: dict):
    return store.create_email_identity(request["EmailIdentity"], **{k: v for k, v in request.items() if k != "EmailIdentity"})
