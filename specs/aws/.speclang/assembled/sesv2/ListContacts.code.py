def handler(store, request: dict):
    return store.list_contacts(request["ContactListName"])
