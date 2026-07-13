---
id: "@specs/aws/iam/get_user_policy"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_GetUserPolicy"
---

# GetUserPolicy

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/get_user_policy
> **spec:implements:** @kind:operation GetUserPolicy
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_GetUserPolicy.spec.md

Retrieves the specified inline policy document that is embedded in the specified IAM user. Policies returned by this operation are URL-encoded compliant with RFC 3986 . You can use a URL decoding method to convert the policy back to plain JSON text. For example, if you use Java, you can use the decode method of the java.net.URLDecoder utility class in the Java SDK. Other languages and SDKs provide similar functionality, and some SDKs do this decoding automatically. An IAM user can also have managed policies attached to it. To retrieve a managed policy document that is attached to a user, use GetPolicy to determine the policy's default version. Then use GetPolicyVersion to retrieve the policy document. For more information about policies, see Managed policies and inline policies in the IAM User Guide .

## Input Shape: GetUserPolicyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| PolicyName | Any  # complex shape | ✓ | The name of the policy document to get. This parameter allows (through its regex pattern ) a string of characters consis |
| UserName | Any  # complex shape | ✓ | The name of the user who the policy is associated with. This parameter allows (through its regex pattern ) a string of c |

## Output Shape: GetUserPolicyResponse

- **PolicyDocument** (Any  # complex shape): The policy document. IAM stores policies in JSON format. However, resources that were created using CloudFormation templ
- **PolicyName** (Any  # complex shape): The name of the policy.
- **UserName** (Any  # complex shape): The user the policy is associated with.

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def get_user_policy(store, request: dict) -> dict:
    """Retrieves the specified inline policy document that is embedded in the specified IAM user. Policies returned by this operation are URL-encoded compliant with RFC 3986 . You can use a URL decoding meth"""
    policy_name = request.get("PolicyName", "").strip() if isinstance(request.get("PolicyName"), str) else request.get("PolicyName")
    if not policy_name:
        raise ValidationException("PolicyName is required")
    user_name = request.get("UserName", "").strip() if isinstance(request.get("UserName"), str) else request.get("UserName")
    if not user_name:
        raise ValidationException("UserName is required")

    resource = store.user_policys(user_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource user_name not found")
    return {"UserName": user_name, **resource}
```
