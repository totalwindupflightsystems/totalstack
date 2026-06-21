"""Handler for CreateIPSet — AWS WAFv2."""
def handler(store, request):
    name = request.get("Name")
    scope = request.get("Scope")
    if not name:
        raise WAFInvalidParameterException("Name is required")
    if not scope:
        raise WAFInvalidParameterException("Scope is required")
    if not request.get("IPAddressVersion"):
        raise WAFInvalidParameterException("IPAddressVersion is required")
    if not request.get("Addresses"):
        raise WAFInvalidParameterException("Addresses is required")
    return store.create_ip_set(
        name=name,
        scope=scope,
        ip_address_version=request["IPAddressVersion"],
        addresses=request["Addresses"],
        description=request.get("Description", ""),
        tags=request.get("Tags"))
