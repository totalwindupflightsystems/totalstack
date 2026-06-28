def list_components(store, request: dict) -> dict:
    comps = store.list_components()
    return {"components": comps}
