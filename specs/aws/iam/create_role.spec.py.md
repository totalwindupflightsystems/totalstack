---
id: "@specs/aws/iam/create_role"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_CreateRole"
---

# CreateRole

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/create_role
> **spec:implements:** @kind:operation CreateRole
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_CreateRole.spec.md

Creates a new role for your Amazon Web Services account. For more information about roles, see IAM roles in the IAM User Guide . For information about quotas for role names and the number of roles you can create, see IAM and STS quotas in the IAM User Guide .

## Input Shape: CreateRoleRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AssumeRolePolicyDocument | Any  # complex shape | ✓ | The trust relationship policy document that grants an entity permission to assume the role. In IAM, you must provide a J |
| Description | Any  # complex shape |  | A description of the role. |
| MaxSessionDuration | Any  # complex shape |  | The maximum session duration (in seconds) that you want to set for the specified role. If you do not specify a value for |
| Path | Any  # complex shape |  | The path to the role. For more information about paths, see IAM Identifiers in the IAM User Guide . This parameter is op |
| PermissionsBoundary | Any  # complex shape |  | The ARN of the managed policy that is used to set the permissions boundary for the role. A permissions boundary policy d |
| RoleName | Any  # complex shape | ✓ | The name of the role to create. IAM user, group, role, and policy names must be unique within the account. Names are not |
| Tags | Any  # complex shape |  | A list of tags that you want to attach to the new role. Each tag consists of a key name and an associated value. For mor |

## Output Shape: CreateRoleResponse

- **Role** (Any  # complex shape): A structure containing details about the new role.

## Errors
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
- **EntityAlreadyExistsException**: The request was rejected because it attempted to create a resource that already exists.
- **MalformedPolicyDocumentException**: The request was rejected because the policy document was malformed. The error message describes the specific error.
- **ConcurrentModificationException**: The request was rejected because multiple requests to change this object were submitted simultaneously. Wait a few minutes and submit your request again.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def create_role(store, request: dict) -> dict:
    """Creates a new role for your Amazon Web Services account. For more information about roles, see IAM roles in the IAM User Guide . For information about quotas for role names and the number of roles you"""
    assume_role_policy_document = request.get("AssumeRolePolicyDocument", "").strip() if isinstance(request.get("AssumeRolePolicyDocument"), str) else request.get("AssumeRolePolicyDocument")
    if not assume_role_policy_document:
        raise ValidationException("AssumeRolePolicyDocument is required")
    role_name = request.get("RoleName", "").strip() if isinstance(request.get("RoleName"), str) else request.get("RoleName")
    if not role_name:
        raise ValidationException("RoleName is required")

    if store.roles(role_name):
        raise ResourceInUseException(f"Resource role_name already exists")

    record = {
        "Path": path,
        "RoleName": role_name,
        "AssumeRolePolicyDocument": assume_role_policy_document,
        "Description": description,
        "MaxSessionDuration": max_session_duration,
        "PermissionsBoundary": permissions_boundary,
        "Tags": tags,
    }

    store.roles(role_name, record)

    return {
        "Role": record.get("Role", {}),
    }
```
