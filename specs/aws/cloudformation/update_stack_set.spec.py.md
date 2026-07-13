---
id: "@specs/aws/cloudformation/update_stack_set"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_UpdateStackSet"
---

# UpdateStackSet

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/update_stack_set
> **spec:implements:** @kind:operation UpdateStackSet
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_UpdateStackSet.spec.md

Updates the StackSet and associated stack instances in the specified accounts and Amazon Web Services Regions. Even if the StackSet operation created by updating the StackSet fails (completely or partially, below or above a specified failure tolerance), the StackSet is updated with your changes. Subsequent CreateStackInstances calls on the specified StackSet use the updated StackSet. The maximum number of organizational unit (OUs) supported by a UpdateStackSet operation is 50. If you need more than 50, consider the following options: Batch processing: If you don't want to expose your OU hierarchy, split up the operations into multiple calls with less than 50 OUs each. Parent OU strategy: If you don't mind exposing the OU hierarchy, target a parent OU that contains all desired child OUs.

## Input Shape: UpdateStackSetInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Accounts | list[Any  # complex shape] |  | [Self-managed permissions] The accounts in which to update associated stack instances. If you specify accounts, you must |
| AdministrationRoleARN | Any  # complex shape |  | [Self-managed permissions] The Amazon Resource Name (ARN) of the IAM role to use to update this StackSet. Specify an IAM |
| AutoDeployment | Any  # complex shape |  | [Service-managed permissions] Describes whether StackSets automatically deploys to Organizations accounts that are added |
| CallAs | Any  # complex shape |  | [Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's managem |
| Capabilities | Any  # complex shape |  | In some cases, you must explicitly acknowledge that your stack template contains certain capabilities in order for Cloud |
| DeploymentTargets | Any  # complex shape |  | [Service-managed permissions] The Organizations accounts in which to update associated stack instances. To update all th |
| Description | Any  # complex shape |  | A brief description of updates that you are making. |
| ExecutionRoleName | Any  # complex shape |  | [Self-managed permissions] The name of the IAM execution role to use to update the stack set. If you do not specify an e |
| ManagedExecution | Any  # complex shape |  | Describes whether CloudFormation performs non-conflicting operations concurrently and queues conflicting operations. |
| OperationId | Any  # complex shape |  | The unique ID for this StackSet operation. The operation ID also functions as an idempotency token, to ensure that Cloud |
| OperationPreferences | Any  # complex shape |  | Preferences for how CloudFormation performs this StackSet operation. |
| Parameters | Any  # complex shape |  | A list of input parameters for the StackSet template. |
| PermissionModel | Any  # complex shape |  | Describes how the IAM roles required for StackSet operations are created. You cannot modify PermissionModel if there are |
| Regions | list[Any  # complex shape] |  | The Amazon Web Services Regions in which to update associated stack instances. If you specify Regions, you must also spe |
| StackSetName | Any  # complex shape | ✓ | The name or unique ID of the StackSet that you want to update. |
| Tags | Any  # complex shape |  | The key-value pairs to associate with this StackSet and the stacks created from it. CloudFormation also propagates these |
| TemplateBody | Any  # complex shape |  | The structure that contains the template body, with a minimum length of 1 byte and a maximum length of 51,200 bytes. Con |
| TemplateURL | Any  # complex shape |  | The URL of a file that contains the template body. The URL must point to a template (maximum size: 1 MB) that is located |
| UsePreviousTemplate | Any  # complex shape |  | Use the existing template that's associated with the StackSet that you're updating. Conditional: You must specify only o |

## Output Shape: UpdateStackSetOutput

- **OperationId** (Any  # complex shape): The unique ID for this StackSet operation.

## Errors
- **StackSetNotFoundException**: The specified StackSet doesn't exist.
- **OperationInProgressException**: Another operation is currently in progress for this StackSet. Only one operation can be performed for a stack set at a given time.
- **OperationIdAlreadyExistsException**: The specified operation ID already exists.
- **StaleRequestException**: Another operation has been performed on this StackSet since the specified operation was performed.
- **InvalidOperationException**: The specified operation isn't valid.
- **StackInstanceNotFoundException**: The specified stack instance doesn't exist.

## Implementation

```speclang
def update_stack_set(store, request: dict) -> dict:
    """Updates the StackSet and associated stack instances in the specified accounts and Amazon Web Services Regions. Even if the StackSet operation created by updating the StackSet fails (completely or part"""
    stack_set_name = request.get("StackSetName", "").strip() if isinstance(request.get("StackSetName"), str) else request.get("StackSetName")
    if not stack_set_name:
        raise ValidationException("StackSetName is required")

    resource = store.stack_sets(stack_set_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource stack_set_name not found")

    # Update mutable fields
    if "Description" in request:
        resource["Description"] = description
    if "TemplateBody" in request:
        resource["TemplateBody"] = template_body
    if "TemplateURL" in request:
        resource["TemplateURL"] = template_url
    if "UsePreviousTemplate" in request:
        resource["UsePreviousTemplate"] = use_previous_template
    if "Parameters" in request:
        resource["Parameters"] = parameters
    if "Capabilities" in request:
        resource["Capabilities"] = capabilities
    if "Tags" in request:
        resource["Tags"] = tags
    if "OperationPreferences" in request:
        resource["OperationPreferences"] = operation_preferences
    if "AdministrationRoleARN" in request:
        resource["AdministrationRoleARN"] = administration_role_arn
    if "ExecutionRoleName" in request:
        resource["ExecutionRoleName"] = execution_role_name
    if "DeploymentTargets" in request:
        resource["DeploymentTargets"] = deployment_targets
    if "PermissionModel" in request:
        resource["PermissionModel"] = permission_model
    if "AutoDeployment" in request:
        resource["AutoDeployment"] = auto_deployment
    if "OperationId" in request:
        resource["OperationId"] = operation_id
    if "Accounts" in request:
        resource["Accounts"] = accounts
    if "Regions" in request:
        resource["Regions"] = regions
    if "CallAs" in request:
        resource["CallAs"] = call_as
    if "ManagedExecution" in request:
        resource["ManagedExecution"] = managed_execution

    store.stack_sets(stack_set_name, resource)
    return resource
```
