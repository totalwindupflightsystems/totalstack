# spec:trace: aws/rekognition/DeleteFaces.spec.py.md#implementation
# spec:id: @specs/aws/rekognition/deletefaces
# spec:generated: DO NOT EDIT — edit the spec instead

@dataclass
def execute_delete_faces(store, request):
    """Deletes faces from a collection. You specify a collection ID and an array of face IDs to remove from the collection. This operation requires permissions to perform the rekognition:DeleteFaces action."""
    if not request.get("CollectionId"):
        raise InvalidParameterException(f"{fname} is required")
    if not request.get("FaceIds"):
        raise InvalidParameterException(f"{fname} is required")
    collection_id = request["CollectionId"]
    face_ids = request.get("FaceIds", [])
    
    if collection_id not in store.collections:
        raise ResourceNotFoundException(f"Collection {collection_id} not found")
    
    deleted = []
    for face_id in face_ids:
        if face_id in store.faces:
            del store.faces[face_id]
            store.collection_faces[collection_id].discard(face_id)
            deleted.append(face_id)
    
    return {"DeletedFaces": deleted}

