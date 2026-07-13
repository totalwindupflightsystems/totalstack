---
id: "@specs/aws/lambda/add_permission"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_AddPermission"
---

# AddPermission

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/add_permission
> **spec:implements:** @kind:operation AddPermission
> **AWS Protocol:** rest-json
> **HTTP:** POST /2015-03-31/functions/{FunctionName}/policy
> **@ref:** specs/aws/lambda/docs/API_AddPermission.spec.md

Grants a principal permission to use a function. You can apply the policy at the function level, or specify a qualifier to restrict access to a single version or alias. If you use a qualifier, the invoker must use the full Amazon Resource Name (ARN) of that version or alias to invoke the function. Note: Lambda does not support adding policies to version $LATEST. To grant permission to another account, specify the account ID as the Principal . To grant permission to an organization defined in Organizations, specify the organization ID as the PrincipalOrgID . For Amazon Web Services services, the principal is a domain-style identifier that the service defines, such as s3.amazonaws.com or sns.amazonaws.com . For Amazon Web Services services, you can also specify the ARN of the associated resource as the SourceArn . If you grant permission to a service principal without specifying the source, other accounts could potentially configure resources in their account to invoke your Lambda function. This operation adds a statement to a resource-based permissions policy for the function. For more information about function policies, see Using resource-based policies for Lambda .

## Input Shape: AddPermissionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Action | Any  # complex shape | ✓ | The action that the principal can use on the function. For example, lambda:InvokeFunction or lambda:GetFunction . |
| EventSourceToken | Any  # complex shape |  | For Alexa Smart Home functions, a token that the invoker must supply. |
| FunctionName | Any  # complex shape | ✓ | The name or ARN of the Lambda function, version, or alias. Name formats Function name – my-function (name-only), my-func |
| FunctionUrlAuthType | Any  # complex shape |  | The type of authentication that your function URL uses. Set to AWS_IAM if you want to restrict access to authenticated u |
| InvokedViaFunctionUrl | Any  # complex shape |  | Indicates whether the permission applies when the function is invoked through a function URL. |
| Principal | Any  # complex shape | ✓ | The Amazon Web Services service, Amazon Web Services account, IAM user, or IAM role that invokes the function. If you sp |
| PrincipalOrgID | Any  # complex shape |  | The identifier for your organization in Organizations. Use this to grant permissions to all the Amazon Web Services acco |
| Qualifier | Any  # complex shape |  | Specify a version or alias to add permissions to a published version of the function. |
| RevisionId | str |  | Update the policy only if the revision ID matches the ID that's specified. Use this option to avoid modifying a policy t |
| SourceAccount | Any  # complex shape |  | For Amazon Web Services service, the ID of the Amazon Web Services account that owns the resource. Use this together wit |
| SourceArn | Any  # complex shape |  | For Amazon Web Services services, the ARN of the Amazon Web Services resource that invokes the function. For example, an |
| StatementId | Any  # complex shape | ✓ | A statement identifier that differentiates the statement from others in the same policy. |

## Output Shape: AddPermissionResponse

- **Statement** (str): The permission statement that's added to the function policy.

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ResourceConflictException**: The resource already exists, or another operation is in progress.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **PolicyLengthExceededException**: The permissions policy for the resource is too large. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.
- **PreconditionFailedException**: The RevisionId provided does not match the latest RevisionId for the Lambda function or alias. For AddPermission and RemovePermission API operations: Call GetPolicy to retrieve the latest RevisionId f

## Implementation

```speclang
def add_permission(store, request: dict) -> dict:
    """Grants a principal permission to use a function. You can apply the policy at the function level, or specify a qualifier to restrict access to a single version or alias. If you use a qualifier, the inv"""
    action = request.get("Action", "").strip() if isinstance(request.get("Action"), str) else request.get("Action")
    if not action:
        raise ValidationException("Action is required")
    function_name = request.get("FunctionName", "").strip() if isinstance(request.get("FunctionName"), str) else request.get("FunctionName")
    if not function_name:
        raise ValidationException("FunctionName is required")
    principal = request.get("Principal", "").strip() if isinstance(request.get("Principal"), str) else request.get("Principal")
    if not principal:
        raise ValidationException("Principal is required")
    statement_id = request.get("StatementId", "").strip() if isinstance(request.get("StatementId"), str) else request.get("StatementId")
    if not statement_id:
        raise ValidationException("StatementId is required")

    if store.permissions(function_name):
        raise ResourceInUseException(f"Resource function_name already exists")

    record = {
        "FunctionName": function_name,
        "StatementId": statement_id,
        "Action": action,
        "Principal": principal,
        "SourceArn": source_arn,
        "SourceAccount": source_account,
        "EventSourceToken": event_source_token,
        "Qualifier": qualifier,
        "RevisionId": revision_id,
        "PrincipalOrgID": principal_org_id,
        "FunctionUrlAuthType": function_url_auth_type,
        "InvokedViaFunctionUrl": invoked_via_function_url,
    }

    store.permissions(function_name, record)

    return {
        "Statement": record.get("Statement", {}),
    }
```
