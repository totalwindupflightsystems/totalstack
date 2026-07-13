---
id: "@specs/aws/ec2/describe_ipam_byoasn"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeIpamByoasn"
---

# DescribeIpamByoasn

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_ipam_byoasn
> **spec:implements:** @kind:operation DescribeIpamByoasn
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeIpamByoasn.spec.md

Describes your Autonomous System Numbers (ASNs), their provisioning statuses, and the BYOIP CIDRs with which they are associated. For more information, see Tutorial: Bring your ASN to IPAM in the Amazon VPC IPAM guide .

## Input Shape: DescribeIpamByoasnRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | Any  # complex shape |  | The token for the next page of results. |

## Output Shape: DescribeIpamByoasnResult

- **Byoasns** (Any  # complex shape): ASN and BYOIP CIDR associations.
- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_ipam_byoasn(store, request: dict) -> dict:
    """Describes your Autonomous System Numbers (ASNs), their provisioning statuses, and the BYOIP CIDRs with which they are associated. For more information, see Tutorial: Bring your ASN to IPAM in the Amaz"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
