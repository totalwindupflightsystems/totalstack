---
id: "@specs/aws/cloudformation/update_stack"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_UpdateStack"
---

# UpdateStack

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/update_stack
> **spec:implements:** @kind:operation UpdateStack
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_UpdateStack.spec.md

Updates a stack as specified in the template. After the call completes successfully, the stack update starts. You can check the status of the stack through the DescribeStacks action. To get a copy of the template for an existing stack, you can use the GetTemplate action. For more information about updating a stack and monitoring the progress of the update, see Managing Amazon Web Services resources as a single unit with CloudFormation stacks in the CloudFormation User Guide .

## Input Shape: UpdateStackInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Capabilities | Any  # complex shape |  | In some cases, you must explicitly acknowledge that your stack template contains certain capabilities in order for Cloud |
| ClientRequestToken | Any  # complex shape |  | A unique identifier for this UpdateStack request. Specify this token if you plan to retry requests so that CloudFormatio |
| DisableRollback | Any  # complex shape |  | Preserve the state of previously provisioned resources when an operation fails. Default: False |
| NotificationARNs | Any  # complex shape |  | Amazon Simple Notification Service topic Amazon Resource Names (ARNs) that CloudFormation associates with the stack. Spe |
| Parameters | Any  # complex shape |  | A list of Parameter structures that specify input parameters for the stack. For more information, see the Parameter data |
| ResourceTypes | Any  # complex shape |  | Specifies which resource types you can work with, such as AWS::EC2::Instance or Custom::MyCustomInstance . If the list o |
| RetainExceptOnCreate | Any  # complex shape |  | When set to true , newly created resources are deleted when the operation rolls back. This includes newly created resour |
| RoleARN | Any  # complex shape |  | The Amazon Resource Name (ARN) of an IAM role that CloudFormation assumes to update the stack. CloudFormation uses the r |
| RollbackConfiguration | Any  # complex shape |  | The rollback triggers for CloudFormation to monitor during stack creation and updating operations, and for the specified |
| StackName | Any  # complex shape | ✓ | The name or unique stack ID of the stack to update. |
| StackPolicyBody | Any  # complex shape |  | Structure that contains a new stack policy body. You can specify either the StackPolicyBody or the StackPolicyURL parame |
| StackPolicyDuringUpdateBody | Any  # complex shape |  | Structure that contains the temporary overriding stack policy body. You can specify either the StackPolicyDuringUpdateBo |
| StackPolicyDuringUpdateURL | Any  # complex shape |  | Location of a file that contains the temporary overriding stack policy. The URL must point to a policy (max size: 16KB)  |
| StackPolicyURL | Any  # complex shape |  | Location of a file that contains the updated stack policy. The URL must point to a policy (max size: 16KB) located in an |
| Tags | Any  # complex shape |  | Key-value pairs to associate with this stack. CloudFormation also propagates these tags to supported resources in the st |
| TemplateBody | Any  # complex shape |  | Structure that contains the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. Conditio |
| TemplateURL | Any  # complex shape |  | The URL of a file that contains the template body. The URL must point to a template that's located in an Amazon S3 bucke |
| UsePreviousTemplate | Any  # complex shape |  | Reuse the existing template that is associated with the stack that you are updating. When using templates with the AWS:: |

## Output Shape: UpdateStackOutput

- **OperationId** (Any  # complex shape): A unique identifier for this update operation that can be used to track the operation's progress and events.
- **StackId** (Any  # complex shape): Unique identifier of the stack.

## Errors
- **InsufficientCapabilitiesException**: The template contains resources with capabilities that weren't specified in the Capabilities parameter.
- **TokenAlreadyExistsException**: A client request token already exists.

## Implementation

```speclang
def update_stack(store, request: dict) -> dict:
    """Updates a stack as specified in the template. After the call completes successfully, the stack update starts. You can check the status of the stack through the DescribeStacks action. To get a copy of """
    stack_name = request.get("StackName", "").strip() if isinstance(request.get("StackName"), str) else request.get("StackName")
    if not stack_name:
        raise ValidationException("StackName is required")

    resource = store.stacks(stack_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource stack_name not found")

    # Update mutable fields
    if "TemplateBody" in request:
        resource["TemplateBody"] = template_body
    if "TemplateURL" in request:
        resource["TemplateURL"] = template_url
    if "UsePreviousTemplate" in request:
        resource["UsePreviousTemplate"] = use_previous_template
    if "StackPolicyDuringUpdateBody" in request:
        resource["StackPolicyDuringUpdateBody"] = stack_policy_during_update_body
    if "StackPolicyDuringUpdateURL" in request:
        resource["StackPolicyDuringUpdateURL"] = stack_policy_during_update_url
    if "Parameters" in request:
        resource["Parameters"] = parameters
    if "Capabilities" in request:
        resource["Capabilities"] = capabilities
    if "ResourceTypes" in request:
        resource["ResourceTypes"] = resource_types
    if "RoleARN" in request:
        resource["RoleARN"] = role_arn
    if "RollbackConfiguration" in request:
        resource["RollbackConfiguration"] = rollback_configuration
    if "StackPolicyBody" in request:
        resource["StackPolicyBody"] = stack_policy_body
    if "StackPolicyURL" in request:
        resource["StackPolicyURL"] = stack_policy_url
    if "NotificationARNs" in request:
        resource["NotificationARNs"] = notification_ar_ns
    if "Tags" in request:
        resource["Tags"] = tags
    if "DisableRollback" in request:
        resource["DisableRollback"] = disable_rollback
    if "ClientRequestToken" in request:
        resource["ClientRequestToken"] = client_request_token
    if "RetainExceptOnCreate" in request:
        resource["RetainExceptOnCreate"] = retain_except_on_create

    store.stacks(stack_name, resource)
    return resource
```
