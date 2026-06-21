"""Handler for GetIPSet — AWS WAFv2."""
def handler(store, request):
    record = store.get_ip_set(
        id=request.get("Id"),
        name=request.get("Name"),
        scope=request["Scope"])
    return {
        "IPSet": {
            "Id": record.id, "Name": record.name, "ARN": record.arn,
            "IPAddressVersion": record.ip_address_version,
            "Addresses": record.addresses,
            "Description": record.description,
            "LockToken": record.lock_token,
        }
    }
