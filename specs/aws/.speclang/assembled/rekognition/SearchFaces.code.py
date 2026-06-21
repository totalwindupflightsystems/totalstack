# spec:trace: aws/rekognition/SearchFaces.spec.py.md#implementation
# spec:id: @specs/aws/rekognition/searchfaces
# spec:generated: DO NOT EDIT — edit the spec instead

@dataclass
def execute_search_faces(store, request):
    """For a given input face ID, searches for matching faces in the collection the face belongs to. You get a face ID when you add a face to the collection using the IndexFaces operation. The operation compares the features of the input face with faces in the specified collection. You can also search faces without indexing faces by using the SearchFacesByImage operation. The operation response returns an array of faces that match, ordered by similarity score with the highest similarity first. More specifically, it is an array of metadata for each face match that is found. Along with the metadata, the response also includes a confidence value for each face match, indicating the confidence that the specific face matches the input face. For an example, see Searching for a face using its face ID in the Amazon Rekognition Developer Guide. This operation requires permissions to perform the rekognition:SearchFaces action."""
    if not request.get("CollectionId"):
        raise InvalidParameterException(f"{fname} is required")
    if not request.get("FaceId"):
        raise InvalidParameterException(f"{fname} is required")
    collection_id = request["CollectionId"]
    if collection_id not in store.collections:
        raise ResourceNotFoundException(f"Collection {collection_id} not found")
    
    return {
        "FaceMatches": [],
        "SearchedFaceId": request.get("FaceId"),
        "FaceModelVersion": "7.0"
    }

