---
id: "@specs/aws/iam/create_service_linked_role"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_CreateServiceLinkedRole"
---

# CreateServiceLinkedRole

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/create_service_linked_role
> **spec:implements:** @kind:operation CreateServiceLinkedRole
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_CreateServiceLinkedRole.spec.md

Creates an IAM role that is linked to a specific Amazon Web Services service. The service controls the attached policies and when the role can be deleted. This helps ensure that the service is not broken by an unexpectedly changed or deleted role, which could put your Amazon Web Services resources into an unknown state. Allowing the service to control the role helps improve service stability and proper cleanup when a service and its role are no longer needed. For more information, see Using service-linked roles in the IAM User Guide . To attach a policy to this service-linked role, you must make the request using the Amazon Web Services service that depends on this role.

## Input Shape: CreateServiceLinkedRoleRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AWSServiceName | Any  # complex shape | ✓ | The service principal for the Amazon Web Services service to which this role is attached. You use a string similar to a  |
| CustomSuffix | Any  # complex shape |  | A string that you provide, which is combined with the service-provided prefix to form the complete role name. If you mak |
| Description | Any  # complex shape |  | The description of the role. |

## Output Shape: CreateServiceLinkedRoleResponse

- **Role** (Any  # complex shape): A Role object that contains details about the newly created role.

## Errors
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def create_service_linked_role(store, request: dict) -> dict:
    """Creates an IAM role that is linked to a specific Amazon Web Services service. The service controls the attached policies and when the role can be deleted. This helps ensure that the service is not bro"""
    aws_service_name = request.get("AWSServiceName", "").strip() if isinstance(request.get("AWSServiceName"), str) else request.get("AWSServiceName")
    if not aws_service_name:
        raise ValidationException("AWSServiceName is required")

    if store.service_linked_roles(aws_service_name):
        raise ResourceInUseException(f"Resource aws_service_name already exists")

    record = {
        "AWSServiceName": aws_service_name,
        "Description": description,
        "CustomSuffix": custom_suffix,
    }

    store.service_linked_roles(aws_service_name, record)

    return {
        "Role": record.get("Role", {}),
    }
```
