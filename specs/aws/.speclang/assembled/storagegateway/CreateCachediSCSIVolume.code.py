def create_cached_iscsi_volume(store, request: dict) -> dict:
    kw = {k: v for k, v in request.items()
          if k not in ("GatewayARN", "VolumeSizeInBytes", "TargetName")}
    return store.create_cached_iscsi_volume(
        GatewayARN=request["GatewayARN"],
        VolumeSizeInBytes=request["VolumeSizeInBytes"],
        TargetName=request["TargetName"],
        SnapshotId=request.get("SnapshotId"),
        DiskId=request.get("DiskId"),
        Tags=request.get("Tags"),
        **kw)
