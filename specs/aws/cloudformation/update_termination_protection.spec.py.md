---
id: "@specs/aws/cloudformation/update_termination_protection"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_UpdateTerminationProtection"
---

# UpdateTerminationProtection

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/update_termination_protection
> **spec:implements:** @kind:operation UpdateTerminationProtection
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_UpdateTerminationProtection.spec.md

Updates termination protection for the specified stack. If a user attempts to delete a stack with termination protection enabled, the operation fails and the stack remains unchanged. For more information, see Protect a CloudFormation stack from being deleted in the CloudFormation User Guide . For nested stacks , termination protection is set on the root stack and can't be changed directly on the nested stack.

## Input Shape: UpdateTerminationProtectionInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| EnableTerminationProtection | Any  # complex shape | ✓ | Whether to enable termination protection on the specified stack. |
| StackName | Any  # complex shape | ✓ | The name or unique ID of the stack for which you want to set termination protection. |

## Output Shape: UpdateTerminationProtectionOutput

- **StackId** (Any  # complex shape): The unique ID of the stack.

## Implementation

```speclang
def update_termination_protection(store, request: dict) -> dict:
    """Updates termination protection for the specified stack. If a user attempts to delete a stack with termination protection enabled, the operation fails and the stack remains unchanged. For more informat"""
    enable_termination_protection = request.get("EnableTerminationProtection", "").strip() if isinstance(request.get("EnableTerminationProtection"), str) else request.get("EnableTerminationProtection")
    if not enable_termination_protection:
        raise ValidationException("EnableTerminationProtection is required")
    stack_name = request.get("StackName", "").strip() if isinstance(request.get("StackName"), str) else request.get("StackName")
    if not stack_name:
        raise ValidationException("StackName is required")

    resource = store.termination_protections(stack_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource stack_name not found")

    # Update mutable fields

    store.termination_protections(stack_name, resource)
    return resource
```
