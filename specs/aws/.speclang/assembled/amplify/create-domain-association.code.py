def handler(store, request: dict) -> dict:
    record = store.create_domain_association(request["appId"], request["domainName"], request["subDomainSettings"], **{k: v for k, v in request.items() if k not in ("appId", "domainName", "subDomainSettings")})
    return {"domainAssociation": record.to_dict()}
