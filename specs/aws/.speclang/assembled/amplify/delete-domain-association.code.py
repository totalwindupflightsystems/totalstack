def handler(store, request: dict) -> dict:
    record = store.delete_domain_association(request["appId"], request["domainName"])
    return {"domainAssociation": record.to_dict()}
