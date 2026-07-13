---
id: "@specs/aws/iam/get_service_linked_role_deletion_status"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_GetServiceLinkedRoleDeletionStatus"
---

# GetServiceLinkedRoleDeletionStatus

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/get_service_linked_role_deletion_status
> **spec:implements:** @kind:operation GetServiceLinkedRoleDeletionStatus
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_GetServiceLinkedRoleDeletionStatus.spec.md

Retrieves the status of your service-linked role deletion. After you use DeleteServiceLinkedRole to submit a service-linked role for deletion, you can use the DeletionTaskId parameter in GetServiceLinkedRoleDeletionStatus to check the status of the deletion. If the deletion fails, this operation returns the reason that it failed, if that information is returned by the service.

## Input Shape: GetServiceLinkedRoleDeletionStatusRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DeletionTaskId | Any  # complex shape | ✓ | The deletion task identifier. This identifier is returned by the DeleteServiceLinkedRole operation in the format task/aw |

## Output Shape: GetServiceLinkedRoleDeletionStatusResponse

- **Reason** (Any  # complex shape): An object that contains details about the reason the deletion failed.
- **Status** (Any  # complex shape): The status of the deletion.

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def get_service_linked_role_deletion_status(store, request: dict) -> dict:
    """Retrieves the status of your service-linked role deletion. After you use DeleteServiceLinkedRole to submit a service-linked role for deletion, you can use the DeletionTaskId parameter in GetServiceLin"""
    deletion_task_id = request.get("DeletionTaskId", "").strip() if isinstance(request.get("DeletionTaskId"), str) else request.get("DeletionTaskId")
    if not deletion_task_id:
        raise ValidationException("DeletionTaskId is required")

    resource = store.service_linked_role_deletion_statuss(deletion_task_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource deletion_task_id not found")
    return {"DeletionTaskId": deletion_task_id, **resource}
```
