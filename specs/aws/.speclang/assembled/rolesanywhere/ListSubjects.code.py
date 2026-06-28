def handler(store, request):
    items = store.subjects()
    subs = [{"subjectId": s.get("subjectId", str(i)), "enabled": True}
            for i, s in enumerate(items)] if items else []
    return {"subjects": subs}
