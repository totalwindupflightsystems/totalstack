def handler(store, request: dict) -> dict:
    kwargs = {k: v for k, v in request.items()
              if k != "FileCacheId" and v is not None}
    record = store.update_file_cache(
        request["FileCacheId"], **kwargs)
    return record.to_dict()
