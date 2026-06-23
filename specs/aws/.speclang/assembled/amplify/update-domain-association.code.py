def handler(store, request: dict) -> dict:
    record = store.update_domain_association(request["appId"], request["domainName"], **{k: v for k, v in request.items() if k not in ("appId", "domainName")})
    return {"domainAssociation": record.to_dict()}
