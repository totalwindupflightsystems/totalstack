def handler(store, request: dict) -> dict:
    return store.delete_knowledge_base(request["knowledgeBaseId"])
