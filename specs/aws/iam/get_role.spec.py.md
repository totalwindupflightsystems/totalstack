---
id: "@specs/aws/iam/get_role"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_GetRole"
---

# GetRole

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/get_role
> **spec:implements:** @kind:operation GetRole
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_GetRole.spec.md

Retrieves information about the specified role, including the role's path, GUID, ARN, and the role's trust policy that grants permission to assume the role. For more information about roles, see IAM roles in the IAM User Guide . Policies returned by this operation are URL-encoded compliant with RFC 3986 . You can use a URL decoding method to convert the policy back to plain JSON text. For example, if you use Java, you can use the decode method of the java.net.URLDecoder utility class in the Java SDK. Other languages and SDKs provide similar functionality, and some SDKs do this decoding automatically.

## Input Shape: GetRoleRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| RoleName | Any  # complex shape | ✓ | The name of the IAM role to get information about. This parameter allows (through its regex pattern ) a string of charac |

## Output Shape: GetRoleResponse

- **Role** (Any  # complex shape): A structure containing details about the IAM role.

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def get_role(store, request: dict) -> dict:
    """Retrieves information about the specified role, including the role's path, GUID, ARN, and the role's trust policy that grants permission to assume the role. For more information about roles, see IAM r"""
    role_name = request.get("RoleName", "").strip() if isinstance(request.get("RoleName"), str) else request.get("RoleName")
    if not role_name:
        raise ValidationException("RoleName is required")

    resource = store.roles(role_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource role_name not found")
    return {"RoleName": role_name, **resource}
```
