def handler(store, request: dict) -> dict:
    record = store.get_knowledge_base(request["knowledgeBaseId"])
    return {"knowledgeBase": record.to_dict()}
