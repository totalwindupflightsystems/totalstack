---
id: "@specs/aws/rekognition/detect_moderation_labels"
target_lang: py
version: 1.0.0
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/rekognition/plan"
---

# DetectModerationLabels

Detects unsafe content in a specified JPEG or PNG format image. Use DetectModerationLabels to moderate images depending on your requirements. For example, you might want to filter images that contain nudity, but not images containing suggestive content. To filter images, use the labels returned by DetectModerationLabels to determine which types of content are appropriate. For information about moderation labels, see Detecting Unsafe Content in the Amazon Rekognition Developer Guide. You pass the input image either as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes is not supported. The image must be either a PNG or JPEG formatted file. You can specify an adapter to use when retrieving label predictions by providing a ProjectVersionArn to the ProjectVersion argument.

## Input Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `HumanLoopConfig` | HumanLoopConfig | No | Sets up the configuration for human evaluation, including the FlowDefinition the image will be sent  |
| `Image` | Image | Yes | The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekog |
| `MinConfidence` | Percent | No | Specifies the minimum confidence level for the labels to return. Amazon Rekognition doesn't return a |
| `ProjectVersion` | ProjectVersionId | No | Identifier for the custom adapter. Expects the ProjectVersionArn as a value. Use the CreateProject o |

## Errors
- `AccessDeniedException`
- `HumanLoopQuotaExceededException`
- `ImageTooLargeException`
- `InternalServerError`
- `InvalidImageFormatException`
- `InvalidParameterException`
- `InvalidS3ObjectException`
- `ProvisionedThroughputExceededException`
- `ResourceNotFoundException`
- `ResourceNotReadyException`
- `ThrottlingException`

## Output Members
- `ContentTypes`
- `HumanLoopActivationOutput`
- `ModerationLabels`
- `ModerationModelVersion`
- `ProjectVersion`

## Implementation

```speclang
@dataclass
@kind: operation
def execute_detect_moderation_labels(store, request):
    """Detects unsafe content in a specified JPEG or PNG format image. Use DetectModerationLabels to moderate images depending on your requirements. For example, you might want to filter images that contain nudity, but not images containing suggestive content. To filter images, use the labels returned by DetectModerationLabels to determine which types of content are appropriate. For information about moderation labels, see Detecting Unsafe Content in the Amazon Rekognition Developer Guide. You pass the input image either as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes is not supported. The image must be either a PNG or JPEG formatted file. You can specify an adapter to use when retrieving label predictions by providing a ProjectVersionArn to the ProjectVersion argument."""
    if not request.get("Image"):
        raise InvalidParameterException(f"{fname} is required")
    # Return mock moderationlabels results
    return {
        "ModerationLabels": []
    }
```
