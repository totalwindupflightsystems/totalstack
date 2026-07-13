---
id: "@specs/aws/iam/delete_role"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_DeleteRole"
---

# DeleteRole

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/delete_role
> **spec:implements:** @kind:operation DeleteRole
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_DeleteRole.spec.md

Deletes the specified role. Unlike the Amazon Web Services Management Console, when you delete a role programmatically, you must delete the items attached to the role manually, or the deletion fails. For more information, see Deleting an IAM role . Before attempting to delete a role, remove the following attached items: Inline policies ( DeleteRolePolicy ) Attached managed policies ( DetachRolePolicy ) Instance profile ( RemoveRoleFromInstanceProfile ) Optional – Delete instance profile after detaching from role for resource clean up ( DeleteInstanceProfile ) Make sure that you do not have any Amazon EC2 instances running with the role you are about to delete. Deleting a role or instance profile that is associated with a running instance will break any applications running on the instance.

## Input Shape: DeleteRoleRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| RoleName | Any  # complex shape | ✓ | The name of the role to delete. This parameter allows (through its regex pattern ) a string of characters consisting of  |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **DeleteConflictException**: The request was rejected because it attempted to delete a resource that has attached subordinate entities. The error message describes these entities.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **UnmodifiableEntityException**: The request was rejected because service-linked roles are protected Amazon Web Services resources. Only the service that depends on the service-linked role can modify or delete the role on your behalf
- **ConcurrentModificationException**: The request was rejected because multiple requests to change this object were submitted simultaneously. Wait a few minutes and submit your request again.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def delete_role(store, request: dict) -> dict:
    """Deletes the specified role. Unlike the Amazon Web Services Management Console, when you delete a role programmatically, you must delete the items attached to the role manually, or the deletion fails. """
    role_name = request.get("RoleName", "").strip() if isinstance(request.get("RoleName"), str) else request.get("RoleName")

    if not store.roles(role_name):
        raise ResourceNotFoundException(f"Resource role_name not found")
    store.delete_roles(role_name)
    return {}
```
