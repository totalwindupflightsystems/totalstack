def delete_volume(store, request: dict) -> dict:
    return store.delete_volume(VolumeARN=request["VolumeARN"])
