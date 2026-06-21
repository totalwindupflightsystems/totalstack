---
id: "@specs/aws/rekognition/delete_faces"
target_lang: py
version: 1.0.0
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/rekognition/plan"
---

# DeleteFaces

Deletes faces from a collection. You specify a collection ID and an array of face IDs to remove from the collection. This operation requires permissions to perform the rekognition:DeleteFaces action.

## Input Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `CollectionId` | CollectionId | Yes | Collection from which to remove the specific faces. |
| `FaceIds` | FaceIdList | Yes | An array of face IDs to delete. |

## Errors
- `AccessDeniedException`
- `InternalServerError`
- `InvalidParameterException`
- `ProvisionedThroughputExceededException`
- `ResourceNotFoundException`
- `ThrottlingException`

## Output Members
- `DeletedFaces`
- `UnsuccessfulFaceDeletions`

## Implementation

```speclang
@dataclass
@kind: operation
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
```
