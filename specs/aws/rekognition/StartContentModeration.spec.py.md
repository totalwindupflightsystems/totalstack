---
id: "@specs/aws/rekognition/start_content_moderation"
target_lang: py
version: 1.0.0
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/rekognition/plan"
---

# StartContentModeration

Starts asynchronous detection of inappropriate, unwanted, or offensive content in a stored video. For a list of moderation labels in Amazon Rekognition, see Using the image and video moderation APIs. Amazon Rekognition Video can moderate content in a video stored in an Amazon S3 bucket. Use Video to specify the bucket name and the filename of the video. StartContentModeration returns a job identifier (JobId) which you use to get the results of the analysis. When content analysis is finished, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic that you specify in NotificationChannel. To get the results of the content analysis, first check that the status value published to the Amazon SNS topic is SUCCEEDED. If so, call GetContentModeration and pass the job identifier (JobId) from the initial call to StartContentModeration. For more information, see Moderating content in the Amazon Rekognition Developer Guide.

## Input Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `ClientRequestToken` | ClientRequestToken | No | Idempotent token used to identify the start request. If you use the same token with multiple StartCo |
| `JobTag` | JobTag | No | An identifier you specify that's returned in the completion notification that's published to your Am |
| `MinConfidence` | Percent | No | Specifies the minimum confidence that Amazon Rekognition must have in order to return a moderated co |
| `NotificationChannel` | NotificationChannel | No | The Amazon SNS topic ARN that you want Amazon Rekognition Video to publish the completion status of  |
| `Video` | Video | Yes | The video in which you want to detect inappropriate, unwanted, or offensive content. The video must  |

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
def execute_start_content_moderation(store, request):
    """Starts asynchronous detection of inappropriate, unwanted, or offensive content in a stored video. For a list of moderation labels in Amazon Rekognition, see Using the image and video moderation APIs. Amazon Rekognition Video can moderate content in a video stored in an Amazon S3 bucket. Use Video to specify the bucket name and the filename of the video. StartContentModeration returns a job identifier (JobId) which you use to get the results of the analysis. When content analysis is finished, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic that you specify in NotificationChannel. To get the results of the content analysis, first check that the status value published to the Amazon SNS topic is SUCCEEDED. If so, call GetContentModeration and pass the job identifier (JobId) from the initial call to StartContentModeration. For more information, see Moderating content in the Amazon Rekognition Developer Guide."""
    if not request.get("Video"):
        raise InvalidParameterException(f"{fname} is required")
    job_id = str(uuid.uuid4())
    store.video_jobs[job_id] = {
        "JobId": job_id,
        "Status": "SUCCEEDED",
        "API": "StartContentModeration",
        "Video": request.get("Video", {}),
        "CreatedTimestamp": time.time(),
        "Results": []
    }
    return {"JobId": job_id}
```
