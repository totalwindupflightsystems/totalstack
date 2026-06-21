---
id: "@specs/aws/rekognition/describe_collection"
target_lang: py
version: 1.0.0
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/rekognition/plan"
---

# DescribeCollection

Describes the specified collection. You can use DescribeCollection to get information, such as the number of faces indexed into a collection and the version of the model used by the collection for face detection. For more information, see Describing a Collection in the Amazon Rekognition Developer Guide.

## Input Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `CollectionId` | CollectionId | Yes | The ID of the collection to describe. |

## Errors
- `AccessDeniedException`
- `InternalServerError`
- `InvalidParameterException`
- `ProvisionedThroughputExceededException`
- `ResourceNotFoundException`
- `ThrottlingException`

## Output Members
- `CollectionARN`
- `CreationTimestamp`
- `FaceCount`
- `FaceModelVersion`
- `UserCount`

## Implementation

```speclang
@dataclass
@kind: operation
def execute_describe_collection(store, request):
    """Describes the specified collection. You can use DescribeCollection to get information, such as the number of faces indexed into a collection and the version of the model used by the collection for face detection. For more information, see Describing a Collection in the Amazon Rekognition Developer Guide."""
    if not request.get("CollectionId"):
        raise InvalidParameterException(f"{fname} is required")
    collection_id = request.get("CollectionId", request.get("CollectionArn", ""))
    if "arn:" in str(collection_id):
        collection_id = str(collection_id).split("/")[-1]
    
    if collection_id not in store.collections:
        raise ResourceNotFoundException(f"Collection {collection_id} not found")
    
    col = store.collections[collection_id]
    return {
        "CollectionId": col["CollectionId"],
        "FaceCount": len(store.collection_faces.get(collection_id, set())),
        "CollectionARN": f"arn:aws:rekognition:us-east-1:123456789012:collection/{collection_id}",
        "CreationTimestamp": col.get("CreatedTimestamp", 0)
    }
```
