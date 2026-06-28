def handler(store, request):
    source = request["source"]
    destination = request["destination"]
    profileName = request["profileName"]
    clientRequestToken = request["clientRequestToken"]
    profileOwner = request.get("profileOwner")
    job = store.start_job(source, destination, profileName, clientRequestToken, profileOwner)
    return {"jobId": job.jobId, "jobOwner": job.jobOwner}
