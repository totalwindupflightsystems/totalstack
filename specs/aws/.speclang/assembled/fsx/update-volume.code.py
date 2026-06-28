def handler(store, request: dict) -> dict:
    kwargs = {k: v for k, v in request.items()
              if k != "VolumeId" and v is not None}
    record = store.update_volume(request["VolumeId"], **kwargs)
    return record.to_dict()
