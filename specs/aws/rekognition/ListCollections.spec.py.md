---
id: "@specs/aws/rekognition/list_collections"
target_lang: py
version: 1.0.0
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/rekognition/plan"
---

# ListCollections

Returns list of collection IDs in your account. If the result is truncated, the response also provides a NextToken that you can use in the subsequent request to fetch the next set of collection IDs. For an example, see Listing collections in the Amazon Rekognition Developer Guide. This operation requires permissions to perform the rekognition:ListCollections action.

## Input Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `MaxResults` | PageSize | No | Maximum number of collection IDs to return. |
| `NextToken` | PaginationToken | No | Pagination token from the previous response. |

## Errors
- `AccessDeniedException`
- `InternalServerError`
- `InvalidPaginationTokenException`
- `InvalidParameterException`
- `ProvisionedThroughputExceededException`
- `ResourceNotFoundException`
- `ThrottlingException`

## Output Members
- `CollectionIds`
- `FaceModelVersions`
- `NextToken`

## Implementation

```speclang
@dataclass
@kind: operation
def execute_list_collections(store, request):
    """Returns list of collection IDs in your account. If the result is truncated, the response also provides a NextToken that you can use in the subsequent request to fetch the next set of collection IDs. For an example, see Listing collections in the Amazon Rekognition Developer Guide. This operation requires permissions to perform the rekognition:ListCollections action."""
    pass  # No required fields
    all_collections = list(store.collections.keys())
    max_results = request.get("MaxResults", 1000)
    next_token = request.get("NextToken", None)
    
    start = 0
    if next_token:
        try:
            start = int(next_token)
        except ValueError:
            pass
    
    page = all_collections[start:start + max_results]
    result = {
        "CollectionIds": page,
        "FaceModelVersions": ["7.0"] * len(page)
    }
    if start + max_results < len(all_collections):
        result["NextToken"] = str(start + max_results)
    return result
```
