def describe_topic(store, request: dict) -> dict:
    return store.describe_topic(request["ClusterArn"], request["TopicName"])
