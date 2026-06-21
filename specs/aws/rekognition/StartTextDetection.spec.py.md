---
id: "@specs/aws/rekognition/start_text_detection"
target_lang: py
version: 1.0.0
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/rekognition/plan"
---

# StartTextDetection

Starts asynchronous detection of text in a stored video. Amazon Rekognition Video can detect text in a video stored in an Amazon S3 bucket. Use Video to specify the bucket name and the filename of the video. StartTextDetection returns a job identifier (JobId) which you use to get the results of the operation. When text detection is finished, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic that you specify in NotificationChannel. To get the results of the text detection operation, first check that the status value published to the Amazon SNS topic is SUCCEEDED. if so, call GetTextDetection and pass the job identifier (JobId) from the initial call to StartTextDetection.

## Input Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `ClientRequestToken` | ClientRequestToken | No | Idempotent token used to identify the start request. If you use the same token with multiple StartTe |
| `Filters` | StartTextDetectionFilters | No | Optional parameters that let you set criteria the text must meet to be included in your response. |
| `JobTag` | JobTag | No | An identifier returned in the completion status published by your Amazon Simple Notification Service |
| `NotificationChannel` | NotificationChannel | No |  |
| `Video` | Video | Yes |  |

## Errors
- `AccessDeniedException`
- `IdempotentParameterMismatchException`
- `InternalServerError`
- `InvalidParameterException`
- `InvalidS3ObjectException`
- `LimitExceededException`
- `ProvisionedThroughputExceededException`
- `ThrottlingException`
- `VideoTooLargeException`

## Output Members
- `JobId`

## Implementation

```speclang
@dataclass
@kind: operation
def execute_start_text_detection(store, request):
    """Starts asynchronous detection of text in a stored video. Amazon Rekognition Video can detect text in a video stored in an Amazon S3 bucket. Use Video to specify the bucket name and the filename of the video. StartTextDetection returns a job identifier (JobId) which you use to get the results of the operation. When text detection is finished, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic that you specify in NotificationChannel. To get the results of the text detection operation, first check that the status value published to the Amazon SNS topic is SUCCEEDED. if so, call GetTextDetection and pass the job identifier (JobId) from the initial call to StartTextDetection."""
    if not request.get("Video"):
        raise InvalidParameterException(f"{fname} is required")
    job_id = str(uuid.uuid4())
    store.video_jobs[job_id] = {
        "JobId": job_id,
        "Status": "SUCCEEDED",
        "API": "StartTextDetection",
        "Video": request.get("Video", {}),
        "CreatedTimestamp": time.time(),
        "Results": []
    }
    return {"JobId": job_id}
```
