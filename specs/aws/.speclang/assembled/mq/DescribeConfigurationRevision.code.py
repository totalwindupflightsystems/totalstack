def handler(store, request: dict) -> dict:
    return store.describe_configuration_revision(
        ConfigurationId=request["ConfigurationId"],
        ConfigurationRevision=request["ConfigurationRevision"])
