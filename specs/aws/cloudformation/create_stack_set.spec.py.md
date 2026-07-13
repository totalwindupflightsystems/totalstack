---
id: "@specs/aws/cloudformation/create_stack_set"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_CreateStackSet"
---

# CreateStackSet

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/create_stack_set
> **spec:implements:** @kind:operation CreateStackSet
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_CreateStackSet.spec.md

Creates a StackSet.

## Input Shape: CreateStackSetInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AdministrationRoleARN | Any  # complex shape |  | The Amazon Resource Name (ARN) of the IAM role to use to create this StackSet. Specify an IAM role only if you are using |
| AutoDeployment | Any  # complex shape |  | Describes whether StackSets automatically deploys to Organizations accounts that are added to the target organization or |
| CallAs | Any  # complex shape |  | Specifies whether you are acting as an account administrator in the organization's management account or as a delegated  |
| Capabilities | Any  # complex shape |  | In some cases, you must explicitly acknowledge that your StackSet template contains certain capabilities in order for Cl |
| ClientRequestToken | Any  # complex shape |  | A unique identifier for this CreateStackSet request. Specify this token if you plan to retry requests so that CloudForma |
| Description | Any  # complex shape |  | A description of the StackSet. You can use the description to identify the StackSet's purpose or other important informa |
| ExecutionRoleName | Any  # complex shape |  | The name of the IAM execution role to use to create the StackSet. If you do not specify an execution role, CloudFormatio |
| ManagedExecution | Any  # complex shape |  | Describes whether CloudFormation performs non-conflicting operations concurrently and queues conflicting operations. |
| Parameters | Any  # complex shape |  | The input parameters for the StackSet template. |
| PermissionModel | Any  # complex shape |  | Describes how the IAM roles required for StackSet operations are created. By default, SELF-MANAGED is specified. With se |
| StackId | Any  # complex shape |  | The stack ID you are importing into a new StackSet. Specify the Amazon Resource Name (ARN) of the stack. |
| StackSetName | Any  # complex shape | ✓ | The name to associate with the StackSet. The name must be unique in the Region where you create your StackSet. A stack n |
| Tags | Any  # complex shape |  | The key-value pairs to associate with this StackSet and the stacks created from it. CloudFormation also propagates these |
| TemplateBody | Any  # complex shape |  | The structure that contains the template body, with a minimum length of 1 byte and a maximum length of 51,200 bytes. Con |
| TemplateURL | Any  # complex shape |  | The URL of a file that contains the template body. The URL must point to a template (maximum size: 1 MB) that's located  |

## Output Shape: CreateStackSetOutput

- **StackSetId** (Any  # complex shape): The ID of the StackSet that you're creating.

## Errors
- **NameAlreadyExistsException**: The specified name is already in use.
- **CreatedButModifiedException**: The specified resource exists, but has been changed.
- **LimitExceededException**: The quota for the resource has already been reached. For information about resource and stack limitations, see CloudFormation quotas in the CloudFormation User Guide .

## Implementation

```speclang
def create_stack_set(store, request: dict) -> dict:
    """Creates a StackSet."""
    stack_set_name = request.get("StackSetName", "").strip() if isinstance(request.get("StackSetName"), str) else request.get("StackSetName")
    if not stack_set_name:
        raise ValidationException("StackSetName is required")

    if store.stack_sets(stack_set_name):
        raise ResourceInUseException(f"Resource stack_set_name already exists")

    record = {
        "StackSetName": stack_set_name,
        "Description": description,
        "TemplateBody": template_body,
        "TemplateURL": template_url,
        "StackId": stack_id,
        "Parameters": parameters,
        "Capabilities": capabilities,
        "Tags": tags,
        "AdministrationRoleARN": administration_role_arn,
        "ExecutionRoleName": execution_role_name,
        "PermissionModel": permission_model,
        "AutoDeployment": auto_deployment,
        "CallAs": call_as,
        "ClientRequestToken": client_request_token,
        "ManagedExecution": managed_execution,
    }

    store.stack_sets(stack_set_name, record)

    return {
        "StackSetId": record.get("StackSetId", {}),
    }
```
