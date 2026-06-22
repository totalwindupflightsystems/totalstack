def handler(store, request: dict):
    return store.get_contact(request["ContactListName"], request["EmailAddress"])
