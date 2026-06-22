def handler(store, request: dict) -> dict:
    record = store.update_knowledge_base(request)
    return {"knowledgeBase": record.to_dict()}
