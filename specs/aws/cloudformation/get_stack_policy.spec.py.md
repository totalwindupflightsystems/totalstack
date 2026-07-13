---
id: "@specs/aws/cloudformation/get_stack_policy"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_GetStackPolicy"
---

# GetStackPolicy

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/get_stack_policy
> **spec:implements:** @kind:operation GetStackPolicy
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_GetStackPolicy.spec.md

Returns the stack policy for a specified stack. If a stack doesn't have a policy, a null value is returned.

## Input Shape: GetStackPolicyInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| StackName | Any  # complex shape | ✓ | The name or unique stack ID that's associated with the stack whose policy you want to get. |

## Output Shape: GetStackPolicyOutput

- **StackPolicyBody** (Any  # complex shape): Structure that contains the stack policy body. For more information, see Prevent updates to stack resources in the Cloud

## Implementation

```speclang
def get_stack_policy(store, request: dict) -> dict:
    """Returns the stack policy for a specified stack. If a stack doesn't have a policy, a null value is returned."""
    stack_name = request.get("StackName", "").strip() if isinstance(request.get("StackName"), str) else request.get("StackName")
    if not stack_name:
        raise ValidationException("StackName is required")

    resource = store.stack_policys(stack_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource stack_name not found")
    return {"StackName": stack_name, **resource}
```
