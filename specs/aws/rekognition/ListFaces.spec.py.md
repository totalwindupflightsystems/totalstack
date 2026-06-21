---
id: "@specs/aws/rekognition/list_faces"
target_lang: py
version: 1.0.0
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/rekognition/plan"
---

# ListFaces

Returns metadata for faces in the specified collection. This metadata includes information such as the bounding box coordinates, the confidence (that the bounding box contains a face), and face ID. For an example, see Listing Faces in a Collection in the Amazon Rekognition Developer Guide. This operation requires permissions to perform the rekognition:ListFaces action.

## Input Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `CollectionId` | CollectionId | Yes | ID of the collection from which to list the faces. |
| `FaceIds` | FaceIdList | No | An array of face IDs to filter results with when listing faces in a collection. |
| `MaxResults` | PageSize | No | Maximum number of faces to return. |
| `NextToken` | PaginationToken | No | If the previous response was incomplete (because there is more data to retrieve), Amazon Rekognition |
| `UserId` | UserId | No | An array of user IDs to filter results with when listing faces in a collection. |

## Errors
- `AccessDeniedException`
- `InternalServerError`
- `InvalidPaginationTokenException`
- `InvalidParameterException`
- `ProvisionedThroughputExceededException`
- `ResourceNotFoundException`
- `ThrottlingException`

## Output Members
- `FaceModelVersion`
- `Faces`
- `NextToken`

## Implementation

```speclang
@dataclass
@kind: operation
def execute_list_faces(store, request):
    """Returns metadata for faces in the specified collection. This metadata includes information such as the bounding box coordinates, the confidence (that the bounding box contains a face), and face ID. For an example, see Listing Faces in a Collection in the Amazon Rekognition Developer Guide. This operation requires permissions to perform the rekognition:ListFaces action."""
    if not request.get("CollectionId"):
        raise InvalidParameterException(f"{fname} is required")
    collection_id = request["CollectionId"]
    if collection_id not in store.collections:
        raise ResourceNotFoundException(f"Collection {collection_id} not found")
    
    face_ids = sorted(store.collection_faces.get(collection_id, set()))
    max_results = request.get("MaxResults", 1000)
    next_token = request.get("NextToken", None)
    
    start = 0
    if next_token:
        try:
            start = int(next_token)
        except ValueError:
            pass
    
    page_ids = face_ids[start:start + max_results]
    faces = []
    for fid in page_ids:
        face = store.faces.get(fid, {})
        faces.append({
            "FaceId": fid,
            "BoundingBox": face.get("BoundingBox", {}),
            "ImageId": face.get("ImageId", ""),
            "IndexFacesModelVersion": "7.0"
        })
    
    result = {"Faces": faces}
    if start + max_results < len(face_ids):
        result["NextToken"] = str(start + max_results)
    return result
```
