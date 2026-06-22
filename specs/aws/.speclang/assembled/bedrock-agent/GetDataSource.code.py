def handler(store, request: dict) -> dict:
    record = store.get_data_source(
        request["knowledgeBaseId"], request["dataSourceId"])
    return {"dataSource": record.to_dict()}
