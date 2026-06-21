---
id: "@specs/aws/rekognition/compare_faces"
target_lang: py
version: 1.0.0
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/rekognition/plan"
---

# CompareFaces

Compares a face in the source input image with each of the 100 largest faces detected in the target input image. If the source image contains multiple faces, the service detects the largest face and compares it with each face detected in the target image. CompareFaces uses machine learning algorithms, which are probabilistic. A false negative is an incorrect prediction that a face in the target image has a low similarity confidence score when compared to the face in the source image. To reduce the probability of false negatives, we recommend that you compare the target image against multiple source images. If you plan to use CompareFaces to make a decision that impacts an individual's rights, privacy, or access to services, we recommend that you pass the result to a human for review and further validation before taking action. You pass the input and target images either as base64-encoded image bytes or as references to images in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes isn't supported. The image must be formatted as a PNG or JPEG file. In response, the operation returns an array of face matches ordered by similarity score in descending order. For each face match, the response provides a bounding box of the face, facial landmarks, pose details (pitch, roll, and yaw), quality (brightness and sharpness), and confidence value (indicating the level of confidence that the bounding box contains a face). The response also provides a similarity score, which indicates how closely the faces match. By default, only faces with a similarity score of greater than or equal to 80% are returned in the response. You can change this value by specifying the SimilarityThreshold parameter. CompareFaces also returns an array of faces that don't match the source image. For each face, it returns a bounding box, confidence value, landmarks, pose details, and quality. The response also returns information about the face in the source image, including the bounding box of the face and confidence value. The QualityFilter input parameter allows you to filter out detected faces that don’t meet a required quality bar. The quality bar is based on a variety of common use cases. Use QualityFilter to set the quality bar by specifying LOW, MEDIUM, or HIGH. If you do not want to filter detected faces, specify NONE. The default value is NONE. If the image doesn't contain Exif metadata, CompareFaces returns orientation information for the source and target images. Use these values to display the images with the correct image orientation. If no faces are detected in the source or target images, CompareFaces returns an InvalidParameterException error. This is a stateless API operation. That is, data returned by this operation doesn't persist. For an example, see Comparing Faces in Images in the Amazon Rekognition Developer Guide. This operation requires permissions to perform the rekognition:CompareFaces action.

## Input Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `QualityFilter` | QualityFilter | No | A filter that specifies a quality bar for how much filtering is done to identify faces. Filtered fac |
| `SimilarityThreshold` | Percent | No | The minimum level of confidence in the face matches that a match must meet to be included in the Fac |
| `SourceImage` | Image | Yes | The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekog |
| `TargetImage` | Image | Yes | The target image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Reko |

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
- `FaceMatches`
- `SourceImageFace`
- `SourceImageOrientationCorrection`
- `TargetImageOrientationCorrection`
- `UnmatchedFaces`

## Implementation

```speclang
@dataclass
@kind: operation
def execute_compare_faces(store, request):
    """Compares a face in the source input image with each of the 100 largest faces detected in the target input image. If the source image contains multiple faces, the service detects the largest face and compares it with each face detected in the target image. CompareFaces uses machine learning algorithms, which are probabilistic. A false negative is an incorrect prediction that a face in the target image has a low similarity confidence score when compared to the face in the source image. To reduce the probability of false negatives, we recommend that you compare the target image against multiple source images. If you plan to use CompareFaces to make a decision that impacts an individual's rights, privacy, or access to services, we recommend that you pass the result to a human for review and further validation before taking action. You pass the input and target images either as base64-encoded image bytes or as references to images in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes isn't supported. The image must be formatted as a PNG or JPEG file. In response, the operation returns an array of face matches ordered by similarity score in descending order. For each face match, the response provides a bounding box of the face, facial landmarks, pose details (pitch, roll, and yaw), quality (brightness and sharpness), and confidence value (indicating the level of confidence that the bounding box contains a face). The response also provides a similarity score, which indicates how closely the faces match. By default, only faces with a similarity score of greater than or equal to 80% are returned in the response. You can change this value by specifying the SimilarityThreshold parameter. CompareFaces also returns an array of faces that don't match the source image. For each face, it returns a bounding box, confidence value, landmarks, pose details, and quality. The response also returns information about the face in the source image, including the bounding box of the face and confidence value. The QualityFilter input parameter allows you to filter out detected faces that don’t meet a required quality bar. The quality bar is based on a variety of common use cases. Use QualityFilter to set the quality bar by specifying LOW, MEDIUM, or HIGH. If you do not want to filter detected faces, specify NONE. The default value is NONE. If the image doesn't contain Exif metadata, CompareFaces returns orientation information for the source and target images. Use these values to display the images with the correct image orientation. If no faces are detected in the source or target images, CompareFaces returns an InvalidParameterException error. This is a stateless API operation. That is, data returned by this operation doesn't persist. For an example, see Comparing Faces in Images in the Amazon Rekognition Developer Guide. This operation requires permissions to perform the rekognition:CompareFaces action."""
    if not request.get("SourceImage"):
        raise InvalidParameterException(f"{fname} is required")
    if not request.get("TargetImage"):
        raise InvalidParameterException(f"{fname} is required")
    # Return mock face comparison
    return {
        "FaceMatches": [],
        "UnmatchedFaces": [],
        "SourceImageFace": {
            "BoundingBox": {"Width": 0.3, "Height": 0.4, "Left": 0.2, "Top": 0.1},
            "Confidence": 99.0
        }
    }
```
