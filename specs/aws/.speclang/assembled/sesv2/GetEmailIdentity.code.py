def handler(store, request: dict):
    return store.get_email_identity(request["EmailIdentity"])
