def handler(store, request: dict) -> dict:
    return store.delete_data_source(
        request["knowledgeBaseId"], request["dataSourceId"])
