def handler(store, request: dict):
    return store.list_email_identities()
