---
id: "@specs/aws/rekognition/create_collection"
target_lang: py
version: 1.0.0
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/rekognition/plan"
---

# CreateCollection

Creates a collection in an AWS Region. You can add faces to the collection using the IndexFaces operation. For example, you might create collections, one for each of your application users. A user can then index faces using the IndexFaces operation and persist results in a specific collection. Then, a user can search the collection for faces in the user-specific container. When you create a collection, it is associated with the latest version of the face model version. Collection names are case-sensitive. This operation requires permissions to perform the rekognition:CreateCollection action. If you want to tag your collection, you also require permission to perform the rekognition:TagResource operation.

## Input Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `CollectionId` | CollectionId | Yes | ID for the collection that you are creating. |
| `Tags` | TagMap | No | A set of tags (key-value pairs) that you want to attach to the collection. |

## Errors
- `AccessDeniedException`
- `InternalServerError`
- `InvalidParameterException`
- `ProvisionedThroughputExceededException`
- `ResourceAlreadyExistsException`
- `ServiceQuotaExceededException`
- `ThrottlingException`

## Output Members
- `CollectionArn`
- `FaceModelVersion`
- `StatusCode`

## Implementation

```speclang
@dataclass
@kind: operation
def execute_create_collection(store, request):
    """Creates a collection in an AWS Region. You can add faces to the collection using the IndexFaces operation. For example, you might create collections, one for each of your application users. A user can then index faces using the IndexFaces operation and persist results in a specific collection. Then, a user can search the collection for faces in the user-specific container. When you create a collection, it is associated with the latest version of the face model version. Collection names are case-sensitive. This operation requires permissions to perform the rekognition:CreateCollection action. If you want to tag your collection, you also require permission to perform the rekognition:TagResource operation."""
    if not request.get("CollectionId"):
        raise InvalidParameterException(f"{fname} is required")
    collection_id = request["CollectionId"]
    if collection_id in store.collections:
        raise ResourceInUseException(f"Collection {collection_id} already exists")
    
    store.collections[collection_id] = {
        "CollectionId": collection_id,
        "FaceCount": 0,
        "CreatedTimestamp": time.time()
    }
    store.collection_faces[collection_id] = set()
    store.collection_users[collection_id] = set()
    
    return {
        "StatusCode": 200,
        "CollectionArn": f"aws:rekognition:us-east-1:123456789012:collection/{collection_id}",
        "FaceModelVersion": "7.0"
    }
```
