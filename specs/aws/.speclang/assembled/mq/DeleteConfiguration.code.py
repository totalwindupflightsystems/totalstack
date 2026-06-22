def handler(store, request: dict) -> dict:
    return store.delete_configuration(ConfigurationId=request["ConfigurationId"])
