def handler(store, request: dict):
    return store.delete_contact(request["ContactListName"], request["EmailAddress"])
