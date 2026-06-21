def handler(store, request):
    log_bucket = request.get("LogBucket")
    return store.disassociate_drt_log_bucket(log_bucket=log_bucket)
