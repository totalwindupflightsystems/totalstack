---
id: "@specs/aws/cloudformation/create_stack"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_CreateStack"
---

# CreateStack

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/create_stack
> **spec:implements:** @kind:operation CreateStack
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_CreateStack.spec.md

Creates a stack as specified in the template. After the call completes successfully, the stack creation starts. You can check the status of the stack through the DescribeStacks operation. For more information about creating a stack and monitoring stack progress, see Managing Amazon Web Services resources as a single unit with CloudFormation stacks in the CloudFormation User Guide .

## Input Shape: CreateStackInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Capabilities | Any  # complex shape |  | In some cases, you must explicitly acknowledge that your stack template contains certain capabilities in order for Cloud |
| ClientRequestToken | Any  # complex shape |  | A unique identifier for this CreateStack request. Specify this token if you plan to retry requests so that CloudFormatio |
| DisableRollback | Any  # complex shape |  | Set to true to disable rollback of the stack if stack creation failed. You can specify either DisableRollback or OnFailu |
| EnableTerminationProtection | Any  # complex shape |  | Whether to enable termination protection on the specified stack. If a user attempts to delete a stack with termination p |
| NotificationARNs | Any  # complex shape |  | The Amazon SNS topic ARNs to publish stack related events. You can find your Amazon SNS topic ARNs using the Amazon SNS  |
| OnFailure | Any  # complex shape |  | Determines what action will be taken if stack creation fails. This must be one of: DO_NOTHING , ROLLBACK , or DELETE . Y |
| Parameters | Any  # complex shape |  | A list of Parameter structures that specify input parameters for the stack. For more information, see the Parameter data |
| ResourceTypes | Any  # complex shape |  | Specifies which resource types you can work with, such as AWS::EC2::Instance or Custom::MyCustomInstance . If the list o |
| RetainExceptOnCreate | Any  # complex shape |  | When set to true , newly created resources are deleted when the operation rolls back. This includes newly created resour |
| RoleARN | Any  # complex shape |  | The Amazon Resource Name (ARN) of an IAM role that CloudFormation assumes to create the stack. CloudFormation uses the r |
| RollbackConfiguration | Any  # complex shape |  | The rollback triggers for CloudFormation to monitor during stack creation and updating operations, and for the specified |
| StackName | Any  # complex shape | ✓ | The name that's associated with the stack. The name must be unique in the Region in which you are creating the stack. A  |
| StackPolicyBody | Any  # complex shape |  | Structure that contains the stack policy body. For more information, see Prevent updates to stack resources in the Cloud |
| StackPolicyURL | Any  # complex shape |  | Location of a file that contains the stack policy. The URL must point to a policy (maximum size: 16 KB) located in an S3 |
| Tags | Any  # complex shape |  | Key-value pairs to associate with this stack. CloudFormation also propagates these tags to the resources created in the  |
| TemplateBody | Any  # complex shape |  | Structure that contains the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. Conditio |
| TemplateURL | Any  # complex shape |  | The URL of a file that contains the template body. The URL must point to a template (max size: 1 MB) that's located in a |
| TimeoutInMinutes | Any  # complex shape |  | The amount of time that can pass before the stack status becomes CREATE_FAILED ; if DisableRollback is not set or is set |

## Output Shape: CreateStackOutput

- **OperationId** (Any  # complex shape): A unique identifier for this stack operation that can be used to track the operation's progress and events.
- **StackId** (Any  # complex shape): Unique identifier of the stack.

## Errors
- **LimitExceededException**: The quota for the resource has already been reached. For information about resource and stack limitations, see CloudFormation quotas in the CloudFormation User Guide .
- **AlreadyExistsException**: The resource with the name requested already exists.
- **TokenAlreadyExistsException**: A client request token already exists.
- **InsufficientCapabilitiesException**: The template contains resources with capabilities that weren't specified in the Capabilities parameter.

## Implementation

```speclang
def create_stack(store, request: dict) -> dict:
    """Creates a stack as specified in the template. After the call completes successfully, the stack creation starts. You can check the status of the stack through the DescribeStacks operation. For more inf"""
    stack_name = request.get("StackName", "").strip() if isinstance(request.get("StackName"), str) else request.get("StackName")
    if not stack_name:
        raise ValidationException("StackName is required")

    if store.stacks(stack_name):
        raise ResourceInUseException(f"Resource stack_name already exists")

    record = {
        "StackName": stack_name,
        "TemplateBody": template_body,
        "TemplateURL": template_url,
        "Parameters": parameters,
        "DisableRollback": disable_rollback,
        "RollbackConfiguration": rollback_configuration,
        "TimeoutInMinutes": timeout_in_minutes,
        "NotificationARNs": notification_ar_ns,
        "Capabilities": capabilities,
        "ResourceTypes": resource_types,
        "RoleARN": role_arn,
        "OnFailure": on_failure,
        "StackPolicyBody": stack_policy_body,
        "StackPolicyURL": stack_policy_url,
        "Tags": tags,
        "ClientRequestToken": client_request_token,
        "EnableTerminationProtection": enable_termination_protection,
        "RetainExceptOnCreate": retain_except_on_create,
    }

    store.stacks(stack_name, record)

    return {
        "StackId": record.get("StackId", {}),
        "OperationId": record.get("OperationId", {}),
    }
```
