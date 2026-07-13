---
id: "@specs/aws/cloudformation/create_stack_refactor"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_CreateStackRefactor"
---

# CreateStackRefactor

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/create_stack_refactor
> **spec:implements:** @kind:operation CreateStackRefactor
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_CreateStackRefactor.spec.md

Creates a refactor across multiple stacks, with the list of stacks and resources that are affected.

## Input Shape: CreateStackRefactorInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Description | Any  # complex shape |  | A description to help you identify the stack refactor. |
| EnableStackCreation | Any  # complex shape |  | Determines if a new stack is created with the refactor. |
| ResourceMappings | Any  # complex shape |  | The mappings for the stack resource Source and stack resource Destination . |
| StackDefinitions | Any  # complex shape | ✓ | The stacks being refactored. |

## Output Shape: CreateStackRefactorOutput

- **StackRefactorId** (Any  # complex shape): The ID associated with the stack refactor created from the CreateStackRefactor action.

## Implementation

```speclang
def create_stack_refactor(store, request: dict) -> dict:
    """Creates a refactor across multiple stacks, with the list of stacks and resources that are affected."""
    stack_definitions = request.get("StackDefinitions", "").strip() if isinstance(request.get("StackDefinitions"), str) else request.get("StackDefinitions")
    if not stack_definitions:
        raise ValidationException("StackDefinitions is required")

    if store.stack_refactors(stack_definitions):
        raise ResourceInUseException(f"Resource stack_definitions already exists")

    record = {
        "Description": description,
        "EnableStackCreation": enable_stack_creation,
        "ResourceMappings": resource_mappings,
        "StackDefinitions": stack_definitions,
    }

    store.stack_refactors(stack_definitions, record)

    return {
        "StackRefactorId": record.get("StackRefactorId", {}),
    }
```
