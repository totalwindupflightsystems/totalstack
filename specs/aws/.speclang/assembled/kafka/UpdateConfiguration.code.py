def update_configuration(store, request: dict) -> dict:
    config_args = {}
    for k in ("ServerProperties", "Description", "KafkaVersions"):
        if k in request:
            config_args[k] = request[k]
    return store.update_configuration(request["Arn"], **config_args)
