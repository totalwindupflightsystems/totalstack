---
id: "@specs/aws/iam/get_role_policy"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_GetRolePolicy"
---

# GetRolePolicy

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/get_role_policy
> **spec:implements:** @kind:operation GetRolePolicy
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_GetRolePolicy.spec.md

Retrieves the specified inline policy document that is embedded with the specified IAM role. Policies returned by this operation are URL-encoded compliant with RFC 3986 . You can use a URL decoding method to convert the policy back to plain JSON text. For example, if you use Java, you can use the decode method of the java.net.URLDecoder utility class in the Java SDK. Other languages and SDKs provide similar functionality, and some SDKs do this decoding automatically. An IAM role can also have managed policies attached to it. To retrieve a managed policy document that is attached to a role, use GetPolicy to determine the policy's default version, then use GetPolicyVersion to retrieve the policy document. For more information about policies, see Managed policies and inline policies in the IAM User Guide . For more information about roles, see IAM roles in the IAM User Guide .

## Input Shape: GetRolePolicyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| PolicyName | Any  # complex shape | ✓ | The name of the policy document to get. This parameter allows (through its regex pattern ) a string of characters consis |
| RoleName | Any  # complex shape | ✓ | The name of the role associated with the policy. This parameter allows (through its regex pattern ) a string of characte |

## Output Shape: GetRolePolicyResponse

- **PolicyDocument** (Any  # complex shape): The policy document. IAM stores policies in JSON format. However, resources that were created using CloudFormation templ
- **PolicyName** (Any  # complex shape): The name of the policy.
- **RoleName** (Any  # complex shape): The role the policy is associated with.

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def get_role_policy(store, request: dict) -> dict:
    """Retrieves the specified inline policy document that is embedded with the specified IAM role. Policies returned by this operation are URL-encoded compliant with RFC 3986 . You can use a URL decoding me"""
    policy_name = request.get("PolicyName", "").strip() if isinstance(request.get("PolicyName"), str) else request.get("PolicyName")
    if not policy_name:
        raise ValidationException("PolicyName is required")
    role_name = request.get("RoleName", "").strip() if isinstance(request.get("RoleName"), str) else request.get("RoleName")
    if not role_name:
        raise ValidationException("RoleName is required")

    resource = store.role_policys(policy_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource policy_name not found")
    return {"PolicyName": policy_name, **resource}
```
