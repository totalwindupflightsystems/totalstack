def list_experiments(store, request: dict) -> dict:
    exps = store.list_experiments()
    return {"experiments": exps}
