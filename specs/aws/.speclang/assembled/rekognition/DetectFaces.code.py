# spec:trace: aws/rekognition/DetectFaces.spec.py.md#implementation
# spec:id: @specs/aws/rekognition/detectfaces
# spec:generated: DO NOT EDIT — edit the spec instead

def execute_detect_faces(store, request):
    """Detects faces within an image that is provided as input. DetectFaces detects the 100 largest faces in the image. For each face detected, the operation returns face details. These details include a bounding box of the face, a confidence value (that the bounding box contains a face), and a fixed set of attributes such as facial landmarks (for example, coordinates of eye and mouth), pose, presence of facial occlusion, and so on. The face-detection algorithm is most effective on frontal faces. For non-frontal or obscured faces, the algorithm might not detect the faces or might detect faces with lower confidence. You pass the input image either as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes is not supported. The image must be either a PNG or JPEG formatted file. This is a stateless API operation. That is, the operation does not persist any data. This operation requires permissions to perform the rekognition:DetectFaces action."""
    if not request.get("Image"):
        raise InvalidParameterException(f"{fname} is required")
    # Return mock facedetails results
    return {
        "FaceDetails": []
    }

