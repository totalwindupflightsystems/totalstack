// spec:trace spec=/home/kara/totalstack/specs/aws/rekognition/SearchFacesByImage.spec.py.md#input-fields
// spec:generated DO NOT EDIT — edit the spec instead

def execute_search_faces_by_image(store, request):
    """For a given input image, first detects the largest face in the image, and then searches the specified collection for matching faces. The operation compares the features of the input face with faces in the specified collection. To search for all faces in an input image, you might first call the IndexFaces operation, and then use the face IDs returned in subsequent calls to the SearchFaces operation. You can also call the DetectFaces operation and use the bounding boxes in the response to make face crops, which then you can pass in to the SearchFacesByImage operation. You pass the input image either as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes is not supported. The image must be either a PNG or JPEG formatted file. The response returns an array of faces that match, ordered by similarity score with the highest similarity first. More specifically, it is an array of metadata for each face match found. Along with the metadata, the response also includes a similarity indicating how similar the face is to the input face. In the response, the operation also returns the bounding box (and a confidence level that the bounding box contains a face) of the face that Amazon Rekognition used for the input image. If no faces are detected in the input image, SearchFacesByImage returns an InvalidParameterException error. For an example, Searching for a Face Using an Image in the Amazon Rekognition Developer Guide. The QualityFilter input parameter allows you to filter out detected faces that don’t meet a required quality bar. The quality bar is based on a variety of common use cases. Use QualityFilter to set the quality bar for filtering by specifying LOW, MEDIUM, or HIGH. If you do not want to filter detected faces, specify NONE. The default value is NONE. To use quality filtering, you need a collection associated with version 3 of the face model or higher. To get the version of the face model associated with a collection, call DescribeCollection. This operation requires permissions to perform the rekognition:SearchFacesByImage action."""
    if not request.get("CollectionId"):
        raise InvalidParameterException(f"{fname} is required")
    if not request.get("Image"):
        raise InvalidParameterException(f"{fname} is required")
    collection_id = request["CollectionId"]
    if collection_id not in store.collections:
        raise ResourceNotFoundException(f"Collection {collection_id} not found")
    
    return {
        "FaceMatches": [],
        "SearchedFaceId": request.get("FaceId"),
        "FaceModelVersion": "7.0"
    }