---
id: "@specs/aws/rekognition/get_content_moderation"
target_lang: py
version: 1.0.0
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/rekognition/plan"
---

# GetContentModeration

Gets the inappropriate, unwanted, or offensive content analysis results for a Amazon Rekognition Video analysis started by StartContentModeration. For a list of moderation labels in Amazon Rekognition, see Using the image and video moderation APIs. Amazon Rekognition Video inappropriate or offensive content detection in a stored video is an asynchronous operation. You start analysis by calling StartContentModeration which returns a job identifier (JobId). When analysis finishes, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to StartContentModeration. To get the results of the content analysis, first check that the status value published to the Amazon SNS topic is SUCCEEDED. If so, call GetContentModeration and pass the job identifier (JobId) from the initial call to StartContentModeration. For more information, see Working with Stored Videos in the Amazon Rekognition Devlopers Guide. GetContentModeration returns detected inappropriate, unwanted, or offensive content moderation labels, and the time they are detected, in an array, ModerationLabels, of ContentModerationDetection objects. By default, the moderated labels are returned sorted by time, in milliseconds from the start of the video. You can also sort them by moderated label by specifying NAME for the SortBy input parameter. Since video analysis can return a large number of results, use the MaxResults parameter to limit the number of labels returned in a single call to GetContentModeration. If there are more results than specified in MaxResults, the value of NextToken in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call GetContentModeration and populate the NextToken request parameter with the value of NextToken returned from the previous call to GetContentModeration. For more information, see moderating content in the Amazon Rekognition Developer Guide.

## Input Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `AggregateBy` | ContentModerationAggregateBy | No | Defines how to aggregate results of the StartContentModeration request. Default aggregation option i |
| `JobId` | JobId | Yes | The identifier for the inappropriate, unwanted, or offensive content moderation job. Use JobId to id |
| `MaxResults` | MaxResults | No | Maximum number of results to return per paginated call. The largest value you can specify is 1000. I |
| `NextToken` | PaginationToken | No | If the previous response was incomplete (because there is more data to retrieve), Amazon Rekognition |
| `SortBy` | ContentModerationSortBy | No | Sort to use for elements in the ModerationLabelDetections array. Use TIMESTAMP to sort array element |

## Errors
- `AccessDeniedException`
- `InternalServerError`
- `InvalidPaginationTokenException`
- `InvalidParameterException`
- `ProvisionedThroughputExceededException`
- `ResourceNotFoundException`
- `ThrottlingException`

## Output Members
- `GetRequestMetadata`
- `JobId`
- `JobStatus`
- `JobTag`
- `ModerationLabels`
- `ModerationModelVersion`
- `NextToken`
- `StatusMessage`
- `Video`
- `VideoMetadata`

## Implementation

```speclang
@dataclass
@kind: operation
def execute_get_content_moderation(store, request):
    """Gets the inappropriate, unwanted, or offensive content analysis results for a Amazon Rekognition Video analysis started by StartContentModeration. For a list of moderation labels in Amazon Rekognition, see Using the image and video moderation APIs. Amazon Rekognition Video inappropriate or offensive content detection in a stored video is an asynchronous operation. You start analysis by calling StartContentModeration which returns a job identifier (JobId). When analysis finishes, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to StartContentModeration. To get the results of the content analysis, first check that the status value published to the Amazon SNS topic is SUCCEEDED. If so, call GetContentModeration and pass the job identifier (JobId) from the initial call to StartContentModeration. For more information, see Working with Stored Videos in the Amazon Rekognition Devlopers Guide. GetContentModeration returns detected inappropriate, unwanted, or offensive content moderation labels, and the time they are detected, in an array, ModerationLabels, of ContentModerationDetection objects. By default, the moderated labels are returned sorted by time, in milliseconds from the start of the video. You can also sort them by moderated label by specifying NAME for the SortBy input parameter. Since video analysis can return a large number of results, use the MaxResults parameter to limit the number of labels returned in a single call to GetContentModeration. If there are more results than specified in MaxResults, the value of NextToken in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call GetContentModeration and populate the NextToken request parameter with the value of NextToken returned from the previous call to GetContentModeration. For more information, see moderating content in the Amazon Rekognition Developer Guide."""
    if not request.get("JobId"):
        raise InvalidParameterException(f"{fname} is required")
    return {"__status": "implemented", "__operation": "GetContentModeration"}
```
