def handler(store, request: dict):
    return store.create_contact(request["ContactListName"], request["EmailAddress"], **{k: v for k, v in request.items() if k not in ("ContactListName", "EmailAddress")})
