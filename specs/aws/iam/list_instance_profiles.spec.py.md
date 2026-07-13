---
id: "@specs/aws/iam/list_instance_profiles"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_ListInstanceProfiles"
---

# ListInstanceProfiles

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/list_instance_profiles
> **spec:implements:** @kind:operation ListInstanceProfiles
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_ListInstanceProfiles.spec.md

Lists the instance profiles that have the specified path prefix. If there are none, the operation returns an empty list. For more information about instance profiles, see Using instance profiles in the IAM User Guide . IAM resource-listing operations return a subset of the available attributes for the resource. For example, this operation does not return tags, even though they are an attribute of the returned object. To view all of the information for an instance profile, see GetInstanceProfile . You can paginate the results using the MaxItems and Marker parameters.

## Input Shape: ListInstanceProfilesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Marker | Any  # complex shape |  | Use this parameter only when paginating results and only after you receive a response indicating that the results are tr |
| MaxItems | Any  # complex shape |  | Use this only when paginating results to indicate the maximum number of items you want in the response. If additional it |
| PathPrefix | Any  # complex shape |  | The path prefix for filtering the results. For example, the prefix /application_abc/component_xyz/ gets all instance pro |

## Output Shape: ListInstanceProfilesResponse

- **InstanceProfiles** (Any  # complex shape): A list of instance profiles.
- **IsTruncated** (Any  # complex shape): A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent 
- **Marker** (Any  # complex shape): When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequen

## Errors
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def list_instance_profiles(store, request: dict) -> dict:
    """Lists the instance profiles that have the specified path prefix. If there are none, the operation returns an empty list. For more information about instance profiles, see Using instance profiles in th"""

    items = store.list_instance_profiless()
    return {"InstanceProfiles": list(items.values())}
```
