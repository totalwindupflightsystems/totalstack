---
id: "@specs/aws/iam/list_service_specific_credentials"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_ListServiceSpecificCredentials"
---

# ListServiceSpecificCredentials

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/list_service_specific_credentials
> **spec:implements:** @kind:operation ListServiceSpecificCredentials
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_ListServiceSpecificCredentials.spec.md

Returns information about the service-specific credentials associated with the specified IAM user. If none exists, the operation returns an empty list. The service-specific credentials returned by this operation are used only for authenticating the IAM user to a specific service. For more information about using service-specific credentials to authenticate to an Amazon Web Services service, see Set up service-specific credentials in the CodeCommit User Guide.

## Input Shape: ListServiceSpecificCredentialsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AllUsers | Any  # complex shape |  | A flag indicating whether to list service specific credentials for all users. This parameter cannot be specified togethe |
| Marker | Any  # complex shape |  | Use this parameter only when paginating results and only after you receive a response indicating that the results are tr |
| MaxItems | Any  # complex shape |  | Use this only when paginating results to indicate the maximum number of items you want in the response. If additional it |
| ServiceName | Any  # complex shape |  | Filters the returned results to only those for the specified Amazon Web Services service. If not specified, then Amazon  |
| UserName | Any  # complex shape |  | The name of the user whose service-specific credentials you want information about. If this value is not specified, then |

## Output Shape: ListServiceSpecificCredentialsResponse

- **IsTruncated** (Any  # complex shape): A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent 
- **Marker** (Any  # complex shape): When IsTruncated is true, this element is present and contains the value to use for the Marker parameter in a subsequent
- **ServiceSpecificCredentials** (Any  # complex shape): A list of structures that each contain details about a service-specific credential.

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ServiceNotSupportedException**: The specified service does not support service-specific credentials.

## Implementation

```speclang
def list_service_specific_credentials(store, request: dict) -> dict:
    """Returns information about the service-specific credentials associated with the specified IAM user. If none exists, the operation returns an empty list. The service-specific credentials returned by thi"""

    items = store.list_service_specific_credentialss()
    return {"ServiceSpecificCredentials": list(items.values())}
```
