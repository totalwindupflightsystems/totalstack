def handler(store, request: dict) -> dict:
    record = store.get_domain_association(request["appId"], request["domainName"])
    return {"domainAssociation": record.to_dict()}
