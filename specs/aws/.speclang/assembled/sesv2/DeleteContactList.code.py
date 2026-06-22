def handler(store, request: dict):
    return store.delete_contact_list(request["ContactListName"])
