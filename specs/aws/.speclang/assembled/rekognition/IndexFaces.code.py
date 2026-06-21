# spec:trace: aws/rekognition/IndexFaces.spec.py.md#implementation
# spec:id: @specs/aws/rekognition/indexfaces
# spec:generated: DO NOT EDIT — edit the spec instead

@dataclass
def execute_index_faces(store, request):
    """Detects faces in the input image and adds them to the specified collection. Amazon Rekognition doesn't save the actual faces that are detected. Instead, the underlying detection algorithm first detects the faces in the input image. For each face, the algorithm extracts facial features into a feature vector, and stores it in the backend database. Amazon Rekognition uses feature vectors when it performs face match and search operations using the SearchFaces and SearchFacesByImage operations. For more information, see Adding faces to a collection in the Amazon Rekognition Developer Guide. To get the number of faces in a collection, call DescribeCollection. If you're using version 1.0 of the face detection model, IndexFaces indexes the 15 largest faces in the input image. Later versions of the face detection model index the 100 largest faces in the input image. If you're using version 4 or later of the face model, image orientation information is not returned in the OrientationCorrection field. To determine which version of the model you're using, call DescribeCollection and supply the collection ID. You can also get the model version from the value of FaceModelVersion in the response from IndexFaces For more information, see Model Versioning in the Amazon Rekognition Developer Guide. If you provide the optional ExternalImageId for the input image you provided, Amazon Rekognition associates this ID with all faces that it detects. When you call the ListFaces operation, the response returns the external ID. You can use this external image ID to create a client-side index to associate the faces with each image. You can then use the index to find all faces in an image. You can specify the maximum number of faces to index with the MaxFaces input parameter. This is useful when you want to index the largest faces in an image and don't want to index smaller faces, such as those belonging to people standing in the background. The QualityFilter input parameter allows you to filter out detected faces that don’t meet a required quality bar. The quality bar is based on a variety of common use cases. By default, IndexFaces chooses the quality bar that's used to filter faces. You can also explicitly choose the quality bar. Use QualityFilter, to set the quality bar by specifying LOW, MEDIUM, or HIGH. If you do not want to filter detected faces, specify NONE. To use quality filtering, you need a collection associated with version 3 of the face model or higher. To get the version of the face model associated with a collection, call DescribeCollection. Information about faces detected in an image, but not indexed, is returned in an array of UnindexedFace objects, UnindexedFaces. Faces aren't indexed for reasons such as: The number of faces detected exceeds the value of the MaxFaces request parameter. The face is too small compared to the image dimensions. The face is too blurry. The image is too dark. The face has an extreme pose. The face doesn’t have enough detail to be suitable for face search. In response, the IndexFaces operation returns an array of metadata for all detected faces, FaceRecords. This includes: The bounding box, BoundingBox, of the detected face. A confidence value, Confidence, which indicates the confidence that the bounding box contains a face. A face ID, FaceId, assigned by the service for each face that's detected and stored. An image ID, ImageId, assigned by the service for the input image. If you request ALL or specific facial attributes (e.g., FACE_OCCLUDED) by using the detectionAttributes parameter, Amazon Rekognition returns detailed facial attributes, such as facial landmarks (for example, location of eye and mouth), facial occlusion, and other facial attributes. If you provide the same image, specify the same collection, and use the same external ID in the IndexFaces operation, Amazon Rekognition doesn't save duplicate face metadata. The input image is passed either as base64-encoded image bytes, or as a reference to an image in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes isn't supported. The image must be formatted as a PNG or JPEG file. This operation requires permissions to perform the rekognition:IndexFaces action."""
    if not request.get("CollectionId"):
        raise InvalidParameterException(f"{fname} is required")
    if not request.get("Image"):
        raise InvalidParameterException(f"{fname} is required")
    collection_id = request["CollectionId"]
    if collection_id not in store.collections:
        raise ResourceNotFoundException(f"Collection {collection_id} not found")
    
    max_faces = request.get("MaxFaces", 1)
    face_records = []
    for i in range(min(max_faces, 5)):
        face_id = str(uuid.uuid4())[:8]
        face_record = {
            "FaceId": face_id,
            "BoundingBox": {"Width": 0.3, "Height": 0.4, "Left": 0.2 + i * 0.1, "Top": 0.1},
            "ImageId": str(uuid.uuid4())[:8],
            "Confidence": 99.0
        }
        store.faces[face_id] = face_record
        store.collection_faces[collection_id].add(face_id)
        face_records.append(face_record)
    
    store.collections[collection_id]["FaceCount"] = len(store.collection_faces[collection_id])
    
    return {
        "FaceRecords": [{"Face": fr, "FaceDetail": fr} for fr in face_records],
        "FaceModelVersion": "7.0"
    }

