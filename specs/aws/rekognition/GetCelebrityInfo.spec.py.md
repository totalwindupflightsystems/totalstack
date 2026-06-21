---
id: "@specs/aws/rekognition/get_celebrity_info"
target_lang: py
version: 1.0.0
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/rekognition/plan"
---

# GetCelebrityInfo

Gets the name and additional information about a celebrity based on their Amazon Rekognition ID. The additional information is returned as an array of URLs. If there is no additional information about the celebrity, this list is empty. For more information, see Getting information about a celebrity in the Amazon Rekognition Developer Guide. This operation requires permissions to perform the rekognition:GetCelebrityInfo action.

## Input Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `Id` | RekognitionUniqueId | Yes | The ID for the celebrity. You get the celebrity ID from a call to the RecognizeCelebrities operation |

## Errors
- `AccessDeniedException`
- `InternalServerError`
- `InvalidParameterException`
- `ProvisionedThroughputExceededException`
- `ResourceNotFoundException`
- `ThrottlingException`

## Output Members
- `KnownGender`
- `Name`
- `Urls`

## Implementation

```speclang
@dataclass
@kind: operation
def execute_get_celebrity_info(store, request):
    """Gets the name and additional information about a celebrity based on their Amazon Rekognition ID. The additional information is returned as an array of URLs. If there is no additional information about the celebrity, this list is empty. For more information, see Getting information about a celebrity in the Amazon Rekognition Developer Guide. This operation requires permissions to perform the rekognition:GetCelebrityInfo action."""
    if not request.get("Id"):
        raise InvalidParameterException(f"{fname} is required")
    celeb_id = request["Id"]
    if celeb_id not in store.celebrity_db:
        raise ResourceNotFoundException(f"Celebrity {celeb_id} not found")
    
    celeb = store.celebrity_db[celeb_id]
    return {
        "Name": celeb["Name"],
        "Urls": celeb.get("Urls", []),
        "KnownGender": celeb.get("KnownGender", {})
    }
```
