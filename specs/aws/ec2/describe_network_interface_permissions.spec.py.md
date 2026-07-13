---
id: "@specs/aws/ec2/describe_network_interface_permissions"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeNetworkInterfacePermissions"
---

# DescribeNetworkInterfacePermissions

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_network_interface_permissions
> **spec:implements:** @kind:operation DescribeNetworkInterfacePermissions
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeNetworkInterfacePermissions.spec.md

Describes the permissions for your network interfaces.

## Input Shape: DescribeNetworkInterfacePermissionsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Filters | list[Any  # complex shape] |  | One or more filters. network-interface-permission.network-interface-permission-id - The ID of the permission. network-in |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NetworkInterfacePermissionIds | list[Any  # complex shape] |  | The network interface permission IDs. |
| NextToken | str |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |

## Output Shape: DescribeNetworkInterfacePermissionsResult

- **NetworkInterfacePermissions** (list[Any  # complex shape]): The network interface permissions.
- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t

## Implementation

```speclang
def describe_network_interface_permissions(store, request: dict) -> dict:
    """Describes the permissions for your network interfaces."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
