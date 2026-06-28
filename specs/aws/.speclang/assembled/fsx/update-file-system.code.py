def handler(store, request: dict) -> dict:
    kwargs = {k: v for k, v in request.items()
              if k != "FileSystemId" and v is not None}
    record = store.update_file_system(request["FileSystemId"], **kwargs)
    return record.to_dict()
