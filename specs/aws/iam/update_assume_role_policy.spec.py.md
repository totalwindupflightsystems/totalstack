---
id: "@specs/aws/iam/update_assume_role_policy"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_UpdateAssumeRolePolicy"
---

# UpdateAssumeRolePolicy

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/update_assume_role_policy
> **spec:implements:** @kind:operation UpdateAssumeRolePolicy
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_UpdateAssumeRolePolicy.spec.md

Updates the policy that grants an IAM entity permission to assume a role. This is typically referred to as the "role trust policy". For more information about roles, see Using roles to delegate permissions and federate identities .

## Input Shape: UpdateAssumeRolePolicyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| PolicyDocument | Any  # complex shape | ✓ | The policy that grants an entity permission to assume the role. You must provide policies in JSON format in IAM. However |
| RoleName | Any  # complex shape | ✓ | The name of the role to update with the new policy. This parameter allows (through its regex pattern ) a string of chara |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **MalformedPolicyDocumentException**: The request was rejected because the policy document was malformed. The error message describes the specific error.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **UnmodifiableEntityException**: The request was rejected because service-linked roles are protected Amazon Web Services resources. Only the service that depends on the service-linked role can modify or delete the role on your behalf
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def update_assume_role_policy(store, request: dict) -> dict:
    """Updates the policy that grants an IAM entity permission to assume a role. This is typically referred to as the "role trust policy". For more information about roles, see Using roles to delegate permis"""
    policy_document = request.get("PolicyDocument", "").strip() if isinstance(request.get("PolicyDocument"), str) else request.get("PolicyDocument")
    if not policy_document:
        raise ValidationException("PolicyDocument is required")
    role_name = request.get("RoleName", "").strip() if isinstance(request.get("RoleName"), str) else request.get("RoleName")
    if not role_name:
        raise ValidationException("RoleName is required")

    resource = store.assume_role_policys(role_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource role_name not found")

    # Update mutable fields

    store.assume_role_policys(role_name, resource)
    return resource
```
