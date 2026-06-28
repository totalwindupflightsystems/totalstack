def create_smb_file_share(store, request: dict) -> dict:
    kw = {k: v for k, v in request.items()
          if k not in ("GatewayARN", "Role", "LocationARN")}
    return store.create_smb_file_share(
        GatewayARN=request["GatewayARN"],
        Role=request["Role"],
        LocationARN=request["LocationARN"],
        ClientList=request.get("ClientList"),
        FileShareName=request.get("FileShareName"),
        Tags=request.get("Tags"),
        **kw)
