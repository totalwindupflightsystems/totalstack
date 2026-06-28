def handler(store, request: dict) -> dict:
    return store.create_accelerator(
        Name=request["Name"],
        IdempotencyToken=request.get("IdempotencyToken"),
        Enabled=request.get("Enabled", True),
        IpAddressType=request.get("IpAddressType"),
        IpAddresses=request.get("IpAddresses"),
        Tags=request.get("Tags"),
    )
