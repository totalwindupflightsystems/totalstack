---
id: "@specs/aws/iam/list_policy_versions"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_ListPolicyVersions"
---

# ListPolicyVersions

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/list_policy_versions
> **spec:implements:** @kind:operation ListPolicyVersions
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_ListPolicyVersions.spec.md

Lists information about the versions of the specified managed policy, including the version that is currently set as the policy's default version. For more information about managed policies, see Managed policies and inline policies in the IAM User Guide .

## Input Shape: ListPolicyVersionsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Marker | Any  # complex shape |  | Use this parameter only when paginating results and only after you receive a response indicating that the results are tr |
| MaxItems | Any  # complex shape |  | Use this only when paginating results to indicate the maximum number of items you want in the response. If additional it |
| PolicyArn | Any  # complex shape | ✓ | The Amazon Resource Name (ARN) of the IAM policy for which you want the versions. For more information about ARNs, see A |

## Output Shape: ListPolicyVersionsResponse

- **IsTruncated** (Any  # complex shape): A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent 
- **Marker** (Any  # complex shape): When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequen
- **Versions** (Any  # complex shape): A list of policy versions. For more information about managed policy versions, see Versioning for managed policies in th

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def list_policy_versions(store, request: dict) -> dict:
    """Lists information about the versions of the specified managed policy, including the version that is currently set as the policy's default version. For more information about managed policies, see Mana"""
    policy_arn = request.get("PolicyArn", "").strip() if isinstance(request.get("PolicyArn"), str) else request.get("PolicyArn")
    if not policy_arn:
        raise ValidationException("PolicyArn is required")

    items = store.list_policy_versionss()
    return {"Versions": list(items.values())}
```
