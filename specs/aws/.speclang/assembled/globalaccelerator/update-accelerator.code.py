def handler(store, request: dict) -> dict:
    return store.update_accelerator(
        AcceleratorArn=request["AcceleratorArn"],
        Name=request.get("Name"),
        Enabled=request.get("Enabled"),
        IpAddressType=request.get("IpAddressType"),
        IpAddresses=request.get("IpAddresses"),
    )
