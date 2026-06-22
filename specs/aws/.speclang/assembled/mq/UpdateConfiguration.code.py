def handler(store, request: dict) -> dict:
    return store.update_configuration(
        ConfigurationId=request["ConfigurationId"],
        Data=request.get("Data", ""),
        Description=request.get("Description"))
