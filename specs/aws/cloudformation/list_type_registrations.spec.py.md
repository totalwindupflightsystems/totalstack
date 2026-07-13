---
id: "@specs/aws/cloudformation/list_type_registrations"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_ListTypeRegistrations"
---

# ListTypeRegistrations

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/list_type_registrations
> **spec:implements:** @kind:operation ListTypeRegistrations
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_ListTypeRegistrations.spec.md

Returns a list of registration tokens for the specified extension(s).

## Input Shape: ListTypeRegistrationsInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| MaxResults | Any  # complex shape |  | The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum |
| NextToken | Any  # complex shape |  | The token for the next set of items to return. (You received this token from a previous call.) |
| RegistrationStatusFilter | Any  # complex shape |  | The current status of the extension registration request. The default is IN_PROGRESS . |
| Type | Any  # complex shape |  | The kind of extension. Conditional: You must specify either TypeName and Type , or Arn . |
| TypeArn | Any  # complex shape |  | The Amazon Resource Name (ARN) of the extension. Conditional: You must specify either TypeName and Type , or Arn . |
| TypeName | Any  # complex shape |  | The name of the extension. Conditional: You must specify either TypeName and Type , or Arn . |

## Output Shape: ListTypeRegistrationsOutput

- **NextToken** (Any  # complex shape): If the request doesn't return all the remaining results, NextToken is set to a token. To retrieve the next set of result
- **RegistrationTokenList** (list[Any  # complex shape]): A list of extension registration tokens. Use DescribeTypeRegistration to return detailed information about a type regist

## Errors
- **CFNRegistryException**: An error occurred during a CloudFormation registry operation.

## Implementation

```speclang
def list_type_registrations(store, request: dict) -> dict:
    """Returns a list of registration tokens for the specified extension(s)."""

    items = store.list_type_registrationss()
    return {"RegistrationTokenList": list(items.values())}
```
