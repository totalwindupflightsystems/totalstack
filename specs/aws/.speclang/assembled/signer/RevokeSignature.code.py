def handler(store, request):
    jobId = request["jobId"]
    reason = request["reason"]
    jobOwner = request.get("jobOwner")
    store.revoke_signature(jobId, reason, jobOwner)
    return {}
