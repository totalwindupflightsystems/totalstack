---
id: "@specs/aws/cloudformation/get_hook_result"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_GetHookResult"
---

# GetHookResult

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/get_hook_result
> **spec:implements:** @kind:operation GetHookResult
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_GetHookResult.spec.md

Retrieves detailed information and remediation guidance for a Hook invocation result. If the Hook uses a KMS key to encrypt annotations, callers of the GetHookResult operation must have kms:Decrypt permissions. For more information, see KMS key policy and permissions for encrypting CloudFormation Hooks results at rest in the CloudFormation Hooks User Guide .

## Input Shape: GetHookResultInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| HookResultId | Any  # complex shape |  | The unique identifier (ID) of the Hook invocation result that you want details about. You can get the ID from the ListHo |

## Output Shape: GetHookResultOutput

- **Annotations** (list[Any  # complex shape]): A list of objects with additional information and guidance that can help you resolve a failed Hook invocation.
- **FailureMode** (Any  # complex shape): The failure mode of the invocation.
- **HookResultId** (Any  # complex shape): The unique identifier of the Hook result.
- **HookStatusReason** (Any  # complex shape): A message that provides additional details about the Hook invocation status.
- **InvocationPoint** (Any  # complex shape): The specific point in the provisioning process where the Hook is invoked.
- **InvokedAt** (str  # ISO8601): The timestamp when the Hook was invoked.
- **OriginalTypeName** (Any  # complex shape): The original public type name of the Hook when an alias is used. For example, if you activate AWS::Hooks::GuardHook with
- **Status** (Any  # complex shape): The status of the Hook invocation. The following statuses are possible: HOOK_IN_PROGRESS : The Hook is currently running
- **Target** (Any  # complex shape): Information about the target of the Hook invocation.
- **TypeArn** (Any  # complex shape): The Amazon Resource Name (ARN) of the Hook.
- **TypeConfigurationVersionId** (Any  # complex shape): The version identifier of the Hook configuration data that was used during invocation.
- **TypeName** (Any  # complex shape): The name of the Hook that was invoked.
- **TypeVersionId** (Any  # complex shape): The version identifier of the Hook that was invoked.

## Errors
- **HookResultNotFoundException**: The specified target doesn't have any requested Hook invocations.

## Implementation

```speclang
def get_hook_result(store, request: dict) -> dict:
    """Retrieves detailed information and remediation guidance for a Hook invocation result. If the Hook uses a KMS key to encrypt annotations, callers of the GetHookResult operation must have kms:Decrypt pe"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
