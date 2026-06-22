def handler(store, request: dict) -> dict:
    return store.delete_user(BrokerId=request["BrokerId"], Username=request["Username"])
