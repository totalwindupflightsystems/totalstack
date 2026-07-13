---
id: "@specs/aws/iam/list_mfa_devices"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_ListMFADevices"
---

# ListMFADevices

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/list_mfa_devices
> **spec:implements:** @kind:operation ListMFADevices
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_ListMFADevices.spec.md

Lists the MFA devices for an IAM user. If the request includes a IAM user name, then this operation lists all the MFA devices associated with the specified user. If you do not specify a user name, IAM determines the user name implicitly based on the Amazon Web Services access key ID signing the request for this operation. You can paginate the results using the MaxItems and Marker parameters.

## Input Shape: ListMFADevicesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Marker | Any  # complex shape |  | Use this parameter only when paginating results and only after you receive a response indicating that the results are tr |
| MaxItems | Any  # complex shape |  | Use this only when paginating results to indicate the maximum number of items you want in the response. If additional it |
| UserName | Any  # complex shape |  | The name of the user whose MFA devices you want to list. This parameter allows (through its regex pattern ) a string of  |

## Output Shape: ListMFADevicesResponse

- **IsTruncated** (Any  # complex shape): A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent 
- **MFADevices** (Any  # complex shape): A list of MFA devices.
- **Marker** (Any  # complex shape): When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequen

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def list_mfa_devices(store, request: dict) -> dict:
    """Lists the MFA devices for an IAM user. If the request includes a IAM user name, then this operation lists all the MFA devices associated with the specified user. If you do not specify a user name, IAM"""

    items = store.list_mfa_devicess()
    return {"MFADevices": list(items.values())}
```
