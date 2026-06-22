
def execute_get_text_detection(store, request):
    """Gets the text detection results of a Amazon Rekognition Video analysis started by StartTextDetection. Text detection with Amazon Rekognition Video is an asynchronous operation. You start text detection by calling StartTextDetection which returns a job identifier (JobId) When the text detection operation finishes, Amazon Rekognition publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to StartTextDetection. To get the results of the text detection operation, first check that the status value published to the Amazon SNS topic is SUCCEEDED. if so, call GetTextDetection and pass the job identifier (JobId) from the initial call of StartLabelDetection. GetTextDetection returns an array of detected text (TextDetections) sorted by the time the text was detected, up to 100 words per frame of video. Each element of the array includes the detected text, the precentage confidence in the acuracy of the detected text, the time the text was detected, bounding box information for where the text was located, and unique identifiers for words and their lines. Use MaxResults parameter to limit the number of text detections returned. If there are more results than specified in MaxResults, the value of NextToken in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call GetTextDetection and populate the NextToken request parameter with the token value returned from the previous call to GetTextDetection."""
    if not request.get("JobId"):
        raise InvalidParameterException(f"{fname} is required")
    job_id = request["JobId"]
    if job_id not in store.video_jobs:
        raise ResourceNotFoundException(f"Job {job_id} not found")

    job = store.video_jobs[job_id]
    return {
        "JobStatus": job.get("Status", "SUCCEEDED"),
        "JobId": job_id,
        "text_detection": job.get("Results", [])
    }
