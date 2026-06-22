def update_topic(store, request: dict) -> dict:
    topic_args = {}
    for k in ("NumPartitions", "ReplicationFactor", "ConfigEntries"):
        if k in request:
            topic_args[k] = request[k]
    return store.update_topic(request["ClusterArn"], request["TopicName"], **topic_args)
