def delete_topic(store, request: dict) -> dict:
    return store.delete_topic(request["ClusterArn"], request["TopicName"])
