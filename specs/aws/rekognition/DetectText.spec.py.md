---
id: "@specs/aws/rekognition/detect_text"
target_lang: py
version: 1.0.0
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/rekognition/plan"
---

# DetectText

Detects text in the input image and converts it into machine-readable text. Pass the input image as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, you must pass it as a reference to an image in an Amazon S3 bucket. For the AWS CLI, passing image bytes is not supported. The image must be either a .png or .jpeg formatted file. The DetectText operation returns text in an array of TextDetection elements, TextDetections. Each TextDetection element provides information about a single word or line of text that was detected in the image. A word is one or more script characters that are not separated by spaces. DetectText can detect up to 100 words in an image. A line is a string of equally spaced words. A line isn't necessarily a complete sentence. For example, a driver's license number is detected as a line. A line ends when there is no aligned text after it. Also, a line ends when there is a large gap between words, relative to the length of the words. This means, depending on the gap between words, Amazon Rekognition may detect multiple lines in text aligned in the same direction. Periods don't represent the end of a line. If a sentence spans multiple lines, the DetectText operation returns multiple lines. To determine whether a TextDetection element is a line of text or a word, use the TextDetection object Type field. To be detected, text must be within +/- 90 degrees orientation of the horizontal axis. For more information, see Detecting text in the Amazon Rekognition Developer Guide.

## Input Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `Filters` | DetectTextFilters | No | Optional parameters that let you set the criteria that the text must meet to be included in your res |
| `Image` | Image | Yes | The input image as base64-encoded bytes or an Amazon S3 object. If you use the AWS CLI to call Amazo |

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
- `TextDetections`
- `TextModelVersion`

## Implementation

```speclang
@dataclass
@kind: operation
def execute_detect_text(store, request):
    """Detects text in the input image and converts it into machine-readable text. Pass the input image as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, you must pass it as a reference to an image in an Amazon S3 bucket. For the AWS CLI, passing image bytes is not supported. The image must be either a .png or .jpeg formatted file. The DetectText operation returns text in an array of TextDetection elements, TextDetections. Each TextDetection element provides information about a single word or line of text that was detected in the image. A word is one or more script characters that are not separated by spaces. DetectText can detect up to 100 words in an image. A line is a string of equally spaced words. A line isn't necessarily a complete sentence. For example, a driver's license number is detected as a line. A line ends when there is no aligned text after it. Also, a line ends when there is a large gap between words, relative to the length of the words. This means, depending on the gap between words, Amazon Rekognition may detect multiple lines in text aligned in the same direction. Periods don't represent the end of a line. If a sentence spans multiple lines, the DetectText operation returns multiple lines. To determine whether a TextDetection element is a line of text or a word, use the TextDetection object Type field. To be detected, text must be within +/- 90 degrees orientation of the horizontal axis. For more information, see Detecting text in the Amazon Rekognition Developer Guide."""
    if not request.get("Image"):
        raise InvalidParameterException(f"{fname} is required")
    # Return mock textdetections results
    return {
        "TextDetections": []
    }
```
