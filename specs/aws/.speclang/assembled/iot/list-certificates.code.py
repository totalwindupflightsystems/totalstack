def list_certificates(store, request: dict) -> dict:
    certs = store.list_certificates()
    return {"certificates": certs}
