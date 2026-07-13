---
id: "@specs/aws/cloudformation/create_change_set"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_CreateChangeSet"
---

# CreateChangeSet

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/create_change_set
> **spec:implements:** @kind:operation CreateChangeSet
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_CreateChangeSet.spec.md

Creates a list of changes that will be applied to a stack so that you can review the changes before executing them. You can create a change set for a stack that doesn't exist or an existing stack. If you create a change set for a stack that doesn't exist, the change set shows all of the resources that CloudFormation will create. If you create a change set for an existing stack, CloudFormation compares the stack's information with the information that you submit in the change set and lists the differences. Use change sets to understand which resources CloudFormation will create or change, and how it will change resources in an existing stack, before you create or update a stack. To create a change set for a stack that doesn't exist, for the ChangeSetType parameter, specify CREATE . To create a change set for an existing stack, specify UPDATE for the ChangeSetType parameter. To create a change set for an import operation, specify IMPORT for the ChangeSetType parameter. After the CreateChangeSet call successfully completes, CloudFormation starts creating the change set. To check the status of the change set or to review it, use the DescribeChangeSet action. When you are satisfied with the changes the change set will make, execute the change set by using the ExecuteChangeSet action. CloudFormation doesn't make changes until you execute the change set. To create a change set for the entire stack hierarchy, set IncludeNestedStacks to True .

## Input Shape: CreateChangeSetInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Capabilities | Any  # complex shape |  | In some cases, you must explicitly acknowledge that your stack template contains certain capabilities in order for Cloud |
| ChangeSetName | Any  # complex shape | ✓ | The name of the change set. The name must be unique among all change sets that are associated with the specified stack.  |
| ChangeSetType | Any  # complex shape |  | The type of change set operation. To create a change set for a new stack, specify CREATE . To create a change set for an |
| ClientToken | Any  # complex shape |  | A unique identifier for this CreateChangeSet request. Specify this token if you plan to retry requests so that CloudForm |
| DeploymentMode | Any  # complex shape |  | Determines how CloudFormation handles configuration drift during deployment. REVERT_DRIFT – Creates a drift-aware change |
| Description | Any  # complex shape |  | A description to help you identify this change set. |
| ImportExistingResources | Any  # complex shape |  | Indicates if the change set auto-imports resources that already exist. For more information, see Import Amazon Web Servi |
| IncludeNestedStacks | Any  # complex shape |  | Creates a change set for the all nested stacks specified in the template. The default behavior of this action is set to  |
| NotificationARNs | Any  # complex shape |  | The Amazon Resource Names (ARNs) of Amazon SNS topics that CloudFormation associates with the stack. To remove all assoc |
| OnStackFailure | Any  # complex shape |  | Determines what action will be taken if stack creation fails. If this parameter is specified, the DisableRollback parame |
| Parameters | Any  # complex shape |  | A list of Parameter structures that specify input parameters for the change set. For more information, see the Parameter |
| ResourceTypes | Any  # complex shape |  | Specifies which resource types you can work with, such as AWS::EC2::Instance or Custom::MyCustomInstance . If the list o |
| ResourcesToImport | Any  # complex shape |  | The resources to import into your stack. |
| RoleARN | Any  # complex shape |  | The Amazon Resource Name (ARN) of an IAM role that CloudFormation assumes when executing the change set. CloudFormation  |
| RollbackConfiguration | Any  # complex shape |  | The rollback triggers for CloudFormation to monitor during stack creation and updating operations, and for the specified |
| StackName | Any  # complex shape | ✓ | The name or the unique ID of the stack for which you are creating a change set. CloudFormation generates the change set  |
| Tags | Any  # complex shape |  | Key-value pairs to associate with this stack. CloudFormation also propagates these tags to resources in the stack. You c |
| TemplateBody | Any  # complex shape |  | A structure that contains the body of the revised template, with a minimum length of 1 byte and a maximum length of 51,2 |
| TemplateURL | Any  # complex shape |  | The URL of the file that contains the revised template. The URL must point to a template (max size: 1 MB) that's located |
| UsePreviousTemplate | Any  # complex shape |  | Whether to reuse the template that's associated with the stack to create the change set. When using templates with the A |

## Output Shape: CreateChangeSetOutput

- **Id** (Any  # complex shape): The Amazon Resource Name (ARN) of the change set.
- **StackId** (Any  # complex shape): The unique ID of the stack.

## Errors
- **AlreadyExistsException**: The resource with the name requested already exists.
- **InsufficientCapabilitiesException**: The template contains resources with capabilities that weren't specified in the Capabilities parameter.
- **LimitExceededException**: The quota for the resource has already been reached. For information about resource and stack limitations, see CloudFormation quotas in the CloudFormation User Guide .

## Implementation

```speclang
def create_change_set(store, request: dict) -> dict:
    """Creates a list of changes that will be applied to a stack so that you can review the changes before executing them. You can create a change set for a stack that doesn't exist or an existing stack. If """
    change_set_name = request.get("ChangeSetName", "").strip() if isinstance(request.get("ChangeSetName"), str) else request.get("ChangeSetName")
    if not change_set_name:
        raise ValidationException("ChangeSetName is required")
    stack_name = request.get("StackName", "").strip() if isinstance(request.get("StackName"), str) else request.get("StackName")
    if not stack_name:
        raise ValidationException("StackName is required")

    if store.change_sets(change_set_name):
        raise ResourceInUseException(f"Resource change_set_name already exists")

    record = {
        "StackName": stack_name,
        "TemplateBody": template_body,
        "TemplateURL": template_url,
        "UsePreviousTemplate": use_previous_template,
        "Parameters": parameters,
        "Capabilities": capabilities,
        "ResourceTypes": resource_types,
        "RoleARN": role_arn,
        "RollbackConfiguration": rollback_configuration,
        "NotificationARNs": notification_ar_ns,
        "Tags": tags,
        "ChangeSetName": change_set_name,
        "ClientToken": client_token,
        "Description": description,
        "ChangeSetType": change_set_type,
        "ResourcesToImport": resources_to_import,
        "IncludeNestedStacks": include_nested_stacks,
        "OnStackFailure": on_stack_failure,
        "ImportExistingResources": import_existing_resources,
        "DeploymentMode": deployment_mode,
    }

    store.change_sets(change_set_name, record)

    return {
        "Id": record.get("Id", {}),
        "StackId": record.get("StackId", {}),
    }
```
