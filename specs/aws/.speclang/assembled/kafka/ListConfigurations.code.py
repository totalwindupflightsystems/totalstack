def list_configurations(store, request: dict) -> dict:
    return {"Configurations": store.list_configurations(**request)}
