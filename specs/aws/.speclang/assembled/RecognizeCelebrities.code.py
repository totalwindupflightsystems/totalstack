// spec:trace spec=/home/kara/totalstack/specs/aws/rekognition/RecognizeCelebrities.spec.py.md#input-fields
// spec:generated DO NOT EDIT — edit the spec instead

def execute_recognize_celebrities(store, request):
    """Returns an array of celebrities recognized in the input image. For more information, see Recognizing celebrities in the Amazon Rekognition Developer Guide. RecognizeCelebrities returns the 64 largest faces in the image. It lists the recognized celebrities in the CelebrityFaces array and any unrecognized faces in the UnrecognizedFaces array. RecognizeCelebrities doesn't return celebrities whose faces aren't among the largest 64 faces in the image. For each celebrity recognized, RecognizeCelebrities returns a Celebrity object. The Celebrity object contains the celebrity name, ID, URL links to additional information, match confidence, and a ComparedFace object that you can use to locate the celebrity's face on the image. Amazon Rekognition doesn't retain information about which images a celebrity has been recognized in. Your application must store this information and use the Celebrity ID property as a unique identifier for the celebrity. If you don't store the celebrity name or additional information URLs returned by RecognizeCelebrities, you will need the ID to identify the celebrity in a call to the GetCelebrityInfo operation. You pass the input image either as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes is not supported. The image must be either a PNG or JPEG formatted file. For an example, see Recognizing celebrities in an image in the Amazon Rekognition Developer Guide. This operation requires permissions to perform the rekognition:RecognizeCelebrities operation."""
    if not request.get("Image"):
        raise InvalidParameterException(f"{fname} is required")
    # Return mock celebrity recognition results
    return {
        "CelebrityFaces": [
            {
                "Name": "Celebrity One",
                "Id": "celebrity-1",
                "MatchConfidence": 99.0,
                "Face": {
                    "BoundingBox": {"Width": 0.3, "Height": 0.4, "Left": 0.2, "Top": 0.1},
                    "Confidence": 99.0,
                    "Landmarks": [{"Type": "eyeLeft", "X": 0.3, "Y": 0.2}]
                }
            }
        ],
        "UnrecognizedFaces": []
    }