---
id: "@specs/aws/iam/list_virtual_mfa_devices"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_ListVirtualMFADevices"
---

# ListVirtualMFADevices

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/list_virtual_mfa_devices
> **spec:implements:** @kind:operation ListVirtualMFADevices
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_ListVirtualMFADevices.spec.md

Lists the virtual MFA devices defined in the Amazon Web Services account by assignment status. If you do not specify an assignment status, the operation returns a list of all virtual MFA devices. Assignment status can be Assigned , Unassigned , or Any . IAM resource-listing operations return a subset of the available attributes for the resource. For example, this operation does not return tags, even though they are an attribute of the returned object. To view tag information for a virtual MFA device, see ListMFADeviceTags . You can paginate the results using the MaxItems and Marker parameters.

## Input Shape: ListVirtualMFADevicesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AssignmentStatus | Any  # complex shape |  | The status ( Unassigned or Assigned ) of the devices to list. If you do not specify an AssignmentStatus , the operation  |
| Marker | Any  # complex shape |  | Use this parameter only when paginating results and only after you receive a response indicating that the results are tr |
| MaxItems | Any  # complex shape |  | Use this only when paginating results to indicate the maximum number of items you want in the response. If additional it |

## Output Shape: ListVirtualMFADevicesResponse

- **IsTruncated** (Any  # complex shape): A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent 
- **Marker** (Any  # complex shape): When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequen
- **VirtualMFADevices** (Any  # complex shape): The list of virtual MFA devices in the current account that match the AssignmentStatus value that was passed in the requ

## Implementation

```speclang
def list_virtual_mfa_devices(store, request: dict) -> dict:
    """Lists the virtual MFA devices defined in the Amazon Web Services account by assignment status. If you do not specify an assignment status, the operation returns a list of all virtual MFA devices. Assi"""

    items = store.list_virtual_mfa_devicess()
    return {"VirtualMFADevices": list(items.values())}
```
