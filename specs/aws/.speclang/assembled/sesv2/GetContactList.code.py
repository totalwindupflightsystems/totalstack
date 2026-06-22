def handler(store, request: dict):
    return store.get_contact_list(request["ContactListName"])
