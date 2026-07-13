---
id: "@specs/aws/iam/get_policy"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_GetPolicy"
---

# GetPolicy

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/get_policy
> **spec:implements:** @kind:operation GetPolicy
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_GetPolicy.spec.md

Retrieves information about the specified managed policy, including the policy's default version and the total number of IAM users, groups, and roles to which the policy is attached. To retrieve the list of the specific users, groups, and roles that the policy is attached to, use ListEntitiesForPolicy . This operation returns metadata about the policy. To retrieve the actual policy document for a specific version of the policy, use GetPolicyVersion . This operation retrieves information about managed policies. To retrieve information about an inline policy that is embedded with an IAM user, group, or role, use GetUserPolicy , GetGroupPolicy , or GetRolePolicy . For more information about policies, see Managed policies and inline policies in the IAM User Guide .

## Input Shape: GetPolicyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| PolicyArn | Any  # complex shape | ✓ | The Amazon Resource Name (ARN) of the managed policy that you want information about. For more information about ARNs, s |

## Output Shape: GetPolicyResponse

- **Policy** (Any  # complex shape): A structure containing details about the policy.

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def get_policy(store, request: dict) -> dict:
    """Retrieves information about the specified managed policy, including the policy's default version and the total number of IAM users, groups, and roles to which the policy is attached. To retrieve the l"""
    policy_arn = request.get("PolicyArn", "").strip() if isinstance(request.get("PolicyArn"), str) else request.get("PolicyArn")
    if not policy_arn:
        raise ValidationException("PolicyArn is required")

    resource = store.policys(policy_arn)
    if not resource:
        raise ResourceNotFoundException(f"Resource policy_arn not found")
    return {"PolicyArn": policy_arn, **resource}
```
