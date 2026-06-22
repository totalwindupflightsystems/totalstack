def handler(store, request: dict) -> dict:
    record = store.create_knowledge_base(request)
    return {"knowledgeBase": record.to_dict()}
