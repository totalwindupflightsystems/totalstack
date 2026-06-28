def list_experiment_templates(store, request: dict) -> dict:
    tmps = store.list_experiment_templates()
    return {"experimentTemplates": tmps}
