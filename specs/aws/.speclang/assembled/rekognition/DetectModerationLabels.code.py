# spec:trace: aws/rekognition/DetectModerationLabels.spec.py.md#implementation
# spec:id: @specs/aws/rekognition/detectmoderationlabels
# spec:generated: DO NOT EDIT — edit the spec instead

@dataclass
def execute_detect_moderation_labels(store, request):
    """Detects unsafe content in a specified JPEG or PNG format image. Use DetectModerationLabels to moderate images depending on your requirements. For example, you might want to filter images that contain nudity, but not images containing suggestive content. To filter images, use the labels returned by DetectModerationLabels to determine which types of content are appropriate. For information about moderation labels, see Detecting Unsafe Content in the Amazon Rekognition Developer Guide. You pass the input image either as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes is not supported. The image must be either a PNG or JPEG formatted file. You can specify an adapter to use when retrieving label predictions by providing a ProjectVersionArn to the ProjectVersion argument."""
    if not request.get("Image"):
        raise InvalidParameterException(f"{fname} is required")
    # Return mock moderationlabels results
    return {
        "ModerationLabels": []
    }

