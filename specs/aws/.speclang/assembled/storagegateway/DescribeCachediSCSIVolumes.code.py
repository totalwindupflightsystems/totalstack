def describe_cached_iscsi_volumes(store, request: dict) -> dict:
    return store.describe_cached_iscsi_volumes(VolumeARNs=request["VolumeARNs"])
