def delete_file_share(store, request: dict) -> dict:
    return store.delete_file_share(FileShareARN=request["FileShareARN"])
