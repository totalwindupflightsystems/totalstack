---
id: "@specs/aws/ec2/describe_network_acls"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeNetworkAcls"
---

# DescribeNetworkAcls

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_network_acls
> **spec:implements:** @kind:operation DescribeNetworkAcls
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeNetworkAcls.spec.md

Describes your network ACLs. The default is to describe all your network ACLs. Alternatively, you can specify specific network ACL IDs or filter the results to include only the network ACLs that match specific criteria. For more information, see Network ACLs in the Amazon VPC User Guide .

## Input Shape: DescribeNetworkAclsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters. association.association-id - The ID of an association ID for the ACL. association.network-acl-id - The ID o |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NetworkAclIds | list[Any  # complex shape] |  | The IDs of the network ACLs. |
| NextToken | str |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |

## Output Shape: DescribeNetworkAclsResult

- **NetworkAcls** (list[Any  # complex shape]): Information about the network ACLs.
- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t

## Implementation

```speclang
def describe_network_acls(store, request: dict) -> dict:
    """Describes your network ACLs. The default is to describe all your network ACLs. Alternatively, you can specify specific network ACL IDs or filter the results to include only the network ACLs that match"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
