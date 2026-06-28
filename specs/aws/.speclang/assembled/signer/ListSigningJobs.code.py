def handler(store, request):
    job_list = store.jobs()
    maxResults = request.get("maxResults", 100)
    jobs_data = [j.to_dict() for j in job_list[:maxResults]]
    return {"jobs": jobs_data, "nextToken": None}
