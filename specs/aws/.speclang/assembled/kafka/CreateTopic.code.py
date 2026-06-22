def create_topic(store, request: dict) -> dict:
    ca = request["ClusterArn"]
    return store.create_topic(ca, TopicName=request["TopicName"],
        NumPartitions=request.get("NumPartitions", 1),
        ReplicationFactor=request.get("ReplicationFactor", 3),
        ConfigEntries=request.get("ConfigEntries", {}))
