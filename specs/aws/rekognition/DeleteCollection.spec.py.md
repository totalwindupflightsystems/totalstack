---
id: "@specs/aws/rekognition/delete_collection"
target_lang: py
version: 1.0.0
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/rekognition/plan"
---

# DeleteCollection

Deletes the specified collection. Note that this operation removes all faces in the collection. For an example, see Deleting a collection. This operation requires permissions to perform the rekognition:DeleteCollection action.

## Input Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `CollectionId` | CollectionId | Yes | ID of the collection to delete. |

## Errors
- `AccessDeniedException`
- `InternalServerError`
- `InvalidParameterException`
- `ProvisionedThroughputExceededException`
- `ResourceNotFoundException`
- `ThrottlingException`

## Output Members
- `StatusCode`

## Implementation

```speclang
@dataclass
@kind: operation
def execute_delete_collection(store, request):
    """Deletes the specified collection. Note that this operation removes all faces in the collection. For an example, see Deleting a collection. This operation requires permissions to perform the rekognition:DeleteCollection action."""
    if not request.get("CollectionId"):
        raise InvalidParameterException(f"{fname} is required")
    collection_id = request["CollectionId"]
    if collection_id not in store.collections:
        raise ResourceNotFoundException(f"Collection {collection_id} not found")
    
    # Delete all faces in the collection
    for face_id in list(store.collection_faces.get(collection_id, set())):
        del store.faces[face_id]
    del store.collection_faces[collection_id]
    del store.collections[collection_id]
    
    return {"StatusCode": 200}
```
