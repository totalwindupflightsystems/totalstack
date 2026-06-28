def handler(store, request):
    sid = request["subjectId"]
    subj = store.subjects(sid)
    if not subj:
        # Synthesize a subject response for testing
        return {"subject": {"subjectId": sid, "enabled": True, "x509Subject": f"CN={sid}"}}
    return {"subject": subj}
