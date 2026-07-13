---
id: "@specs/aws/iam/delete_service_linked_role"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_DeleteServiceLinkedRole"
---

# DeleteServiceLinkedRole

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/delete_service_linked_role
> **spec:implements:** @kind:operation DeleteServiceLinkedRole
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_DeleteServiceLinkedRole.spec.md

Submits a service-linked role deletion request and returns a DeletionTaskId , which you can use to check the status of the deletion. Before you call this operation, confirm that the role has no active sessions and that any resources used by the role in the linked service are deleted. If you call this operation more than once for the same service-linked role and an earlier deletion task is not complete, then the DeletionTaskId of the earlier request is returned. If you submit a deletion request for a service-linked role whose linked service is still accessing a resource, then the deletion task fails. If it fails, the GetServiceLinkedRoleDeletionStatus operation returns the reason for the failure, usually including the resources that must be deleted. To delete the service-linked role, you must first remove those resources from the linked service and then submit the deletion request again. Resources are specific to the service that is linked to the role. For more information about removing resources from a service, see the Amazon Web Services documentation for your service. For more information about service-linked roles, see Roles terms and concepts: Amazon Web Services service-linked role in the IAM User Guide .

## Input Shape: DeleteServiceLinkedRoleRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| RoleName | Any  # complex shape | ✓ | The name of the service-linked role to be deleted. |

## Output Shape: DeleteServiceLinkedRoleResponse

- **DeletionTaskId** (Any  # complex shape): The deletion task identifier that you can use to check the status of the deletion. This identifier is returned in the fo

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def delete_service_linked_role(store, request: dict) -> dict:
    """Submits a service-linked role deletion request and returns a DeletionTaskId , which you can use to check the status of the deletion. Before you call this operation, confirm that the role has no active"""
    role_name = request.get("RoleName", "").strip() if isinstance(request.get("RoleName"), str) else request.get("RoleName")

    if not store.service_linked_roles(role_name):
        raise ResourceNotFoundException(f"Resource role_name not found")
    store.delete_service_linked_roles(role_name)
    return {}
```
