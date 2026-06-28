def describe_nfs_file_shares(store, request: dict) -> dict:
    return store.describe_nfs_file_shares(FileShareARNList=request["FileShareARNList"])
