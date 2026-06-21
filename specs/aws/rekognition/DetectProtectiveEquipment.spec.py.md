---
id: "@specs/aws/rekognition/detect_protective_equipment"
target_lang: py
version: 1.0.0
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/rekognition/plan"
---

# DetectProtectiveEquipment

Detects Personal Protective Equipment (PPE) worn by people detected in an image. Amazon Rekognition can detect the following types of PPE. Face cover Hand cover Head cover You pass the input image as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. The image must be either a PNG or JPG formatted file. DetectProtectiveEquipment detects PPE worn by up to 15 persons detected in an image. For each person detected in the image the API returns an array of body parts (face, head, left-hand, right-hand). For each body part, an array of detected items of PPE is returned, including an indicator of whether or not the PPE covers the body part. The API returns the confidence it has in each detection (person, PPE, body part and body part coverage). It also returns a bounding box (BoundingBox) for each detected person and each detected item of PPE. You can optionally request a summary of detected PPE items with the SummarizationAttributes input parameter. The summary provides the following information. The persons detected as wearing all of the types of PPE that you specify. The persons detected as not wearing all of the types PPE that you specify. The persons detected where PPE adornment could not be determined. This is a stateless API operation. That is, the operation does not persist any data. This operation requires permissions to perform the rekognition:DetectProtectiveEquipment action.

## Input Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `Image` | Image | Yes | The image in which you want to detect PPE on detected persons. The image can be passed as image byte |
| `SummarizationAttributes` | ProtectiveEquipmentSummarizationAttributes | No | An array of PPE types that you want to summarize. |

## Errors
- `AccessDeniedException`
- `ImageTooLargeException`
- `InternalServerError`
- `InvalidImageFormatException`
- `InvalidParameterException`
- `InvalidS3ObjectException`
- `ProvisionedThroughputExceededException`
- `ThrottlingException`

## Output Members
- `Persons`
- `ProtectiveEquipmentModelVersion`
- `Summary`

## Implementation

```speclang
@dataclass
@kind: operation
def execute_detect_protective_equipment(store, request):
    """Detects Personal Protective Equipment (PPE) worn by people detected in an image. Amazon Rekognition can detect the following types of PPE. Face cover Hand cover Head cover You pass the input image as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. The image must be either a PNG or JPG formatted file. DetectProtectiveEquipment detects PPE worn by up to 15 persons detected in an image. For each person detected in the image the API returns an array of body parts (face, head, left-hand, right-hand). For each body part, an array of detected items of PPE is returned, including an indicator of whether or not the PPE covers the body part. The API returns the confidence it has in each detection (person, PPE, body part and body part coverage). It also returns a bounding box (BoundingBox) for each detected person and each detected item of PPE. You can optionally request a summary of detected PPE items with the SummarizationAttributes input parameter. The summary provides the following information. The persons detected as wearing all of the types of PPE that you specify. The persons detected as not wearing all of the types PPE that you specify. The persons detected where PPE adornment could not be determined. This is a stateless API operation. That is, the operation does not persist any data. This operation requires permissions to perform the rekognition:DetectProtectiveEquipment action."""
    if not request.get("Image"):
        raise InvalidParameterException(f"{fname} is required")
    # Return mock protectiveequipment results
    return {
        "ProtectiveEquipment": []
    }
```
