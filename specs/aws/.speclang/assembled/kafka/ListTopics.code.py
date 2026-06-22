def list_topics(store, request: dict) -> dict:
    return {"TopicInfoList": store.list_topics(request["ClusterArn"])}
