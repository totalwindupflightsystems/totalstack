---
id: "@specs/aws/cloudformation/set_stack_policy"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_SetStackPolicy"
---

# SetStackPolicy

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/set_stack_policy
> **spec:implements:** @kind:operation SetStackPolicy
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_SetStackPolicy.spec.md

Sets a stack policy for a specified stack.

## Input Shape: SetStackPolicyInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| StackName | Any  # complex shape | ✓ | The name or unique stack ID that you want to associate a policy with. |
| StackPolicyBody | Any  # complex shape |  | Structure that contains the stack policy body. For more information, see Prevent updates to stack resources in the Cloud |
| StackPolicyURL | Any  # complex shape |  | Location of a file that contains the stack policy. The URL must point to a policy (maximum size: 16 KB) located in an Am |

## Implementation

```speclang
def set_stack_policy(store, request: dict) -> dict:
    """Sets a stack policy for a specified stack."""
    stack_name = request.get("StackName", "").strip() if isinstance(request.get("StackName"), str) else request.get("StackName")
    if not stack_name:
        raise ValidationException("StackName is required")

    resource = store.set_stack_policys(stack_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource stack_name not found")

    # Update mutable fields
    if "StackPolicyBody" in request:
        resource["StackPolicyBody"] = stack_policy_body
    if "StackPolicyURL" in request:
        resource["StackPolicyURL"] = stack_policy_url

    store.set_stack_policys(stack_name, resource)
    return resource
```
