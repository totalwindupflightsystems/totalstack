---
id: "@specs/aws/iam/get_group_policy"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_GetGroupPolicy"
---

# GetGroupPolicy

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/get_group_policy
> **spec:implements:** @kind:operation GetGroupPolicy
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_GetGroupPolicy.spec.md

Retrieves the specified inline policy document that is embedded in the specified IAM group. Policies returned by this operation are URL-encoded compliant with RFC 3986 . You can use a URL decoding method to convert the policy back to plain JSON text. For example, if you use Java, you can use the decode method of the java.net.URLDecoder utility class in the Java SDK. Other languages and SDKs provide similar functionality, and some SDKs do this decoding automatically. An IAM group can also have managed policies attached to it. To retrieve a managed policy document that is attached to a group, use GetPolicy to determine the policy's default version, then use GetPolicyVersion to retrieve the policy document. For more information about policies, see Managed policies and inline policies in the IAM User Guide .

## Input Shape: GetGroupPolicyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| GroupName | Any  # complex shape | ✓ | The name of the group the policy is associated with. This parameter allows (through its regex pattern ) a string of char |
| PolicyName | Any  # complex shape | ✓ | The name of the policy document to get. This parameter allows (through its regex pattern ) a string of characters consis |

## Output Shape: GetGroupPolicyResponse

- **GroupName** (Any  # complex shape): The group the policy is associated with.
- **PolicyDocument** (Any  # complex shape): The policy document. IAM stores policies in JSON format. However, resources that were created using CloudFormation templ
- **PolicyName** (Any  # complex shape): The name of the policy.

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def get_group_policy(store, request: dict) -> dict:
    """Retrieves the specified inline policy document that is embedded in the specified IAM group. Policies returned by this operation are URL-encoded compliant with RFC 3986 . You can use a URL decoding met"""
    group_name = request.get("GroupName", "").strip() if isinstance(request.get("GroupName"), str) else request.get("GroupName")
    if not group_name:
        raise ValidationException("GroupName is required")
    policy_name = request.get("PolicyName", "").strip() if isinstance(request.get("PolicyName"), str) else request.get("PolicyName")
    if not policy_name:
        raise ValidationException("PolicyName is required")

    resource = store.group_policys(group_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource group_name not found")
    return {"GroupName": group_name, **resource}
```
