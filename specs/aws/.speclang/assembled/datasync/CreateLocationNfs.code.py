def create_location_nfs(store, request: dict) -> dict:
    return store.create_location_nfs(
        Subdirectory=request["Subdirectory"],
        ServerHostname=request["ServerHostname"],
        OnPremConfig=request["OnPremConfig"],
        MountOptions=request.get("MountOptions"),
        Tags=request.get("Tags"),
    )
