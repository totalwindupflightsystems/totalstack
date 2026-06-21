---
id: "@specs/aws/lightsail/get_buckets"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_GetBuckets"
---

# GetBuckets

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/get_buckets
> **spec:implements:** @kind:operation GetBuckets
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_GetBuckets.spec.md

Returns information about one or more Amazon Lightsail buckets. The information returned includes the synchronization status of the Amazon Simple Storage Service (Amazon S3) account-level block public access feature for your Lightsail buckets. For more information about buckets, see Buckets in Amazon Lightsail in the Amazon Lightsail Developer Guide .

## Input Shape: GetBucketsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| bucketName | Any  # complex shape |  | The name of the bucket for which to return information. When omitted, the response includes all of your buckets in the A |
| includeConnectedResources | Any  # complex shape |  | A Boolean value that indicates whether to include Lightsail instances that were given access to the bucket using the Set |
| includeCors | Any  # complex shape |  | A Boolean value that indicates whether to include Lightsail bucket CORS configuration in the response. For more informat |
| pageToken | Any  # complex shape |  | The token to advance to the next page of results from your request. To get a page token, perform an initial GetBuckets r |

## Output Shape: GetBucketsResult

- **accountLevelBpaSync** (Any  # complex shape): An object that describes the synchronization status of the Amazon S3 account-level block public access feature for your 
- **buckets** (list[Any  # complex shape]): An array of objects that describe buckets.
- **nextPageToken** (Any  # complex shape): The token to advance to the next page of results from your request. A next page token is not returned if there are no mo

## Errors
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 
- **NotFoundException**: Lightsail throws this exception when it cannot find a resource.
- **ServiceException**: A general service exception.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.
- **RegionSetupInProgressException**: Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.

## Implementation

```speclang
def get_buckets(store, request: dict) -> dict:
    """Returns information about one or more Amazon Lightsail buckets. The information returned includes the synchronization status of the Amazon Simple Storage Service (Amazon S3) account-level block public"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
