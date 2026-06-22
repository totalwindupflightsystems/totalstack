def handler(store, request: dict):
    return store.create_contact_list(request["ContactListName"], **{k: v for k, v in request.items() if k != "ContactListName"})
