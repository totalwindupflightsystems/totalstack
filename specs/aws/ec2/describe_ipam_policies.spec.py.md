---
id: "@specs/aws/ec2/describe_ipam_policies"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeIpamPolicies"
---

# DescribeIpamPolicies

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_ipam_policies
> **spec:implements:** @kind:operation DescribeIpamPolicies
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeIpamPolicies.spec.md

Describes one or more IPAM policies. An IPAM policy is a set of rules that define how public IPv4 addresses from IPAM pools are allocated to Amazon Web Services resources. Each rule maps an Amazon Web Services service to IPAM pools that the service will use to get IP addresses. A single policy can have multiple rules and be applied to multiple Amazon Web Services Regions. If the IPAM pool run out of addresses then the services fallback to Amazon-provided IP addresses. A policy can be applied to an individual Amazon Web Services account or an entity within Amazon Web Services Organizations.

## Input Shape: DescribeIpamPoliciesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| Filters | list[Any  # complex shape] |  | One or more filters for the IPAM policy description. |
| IpamPolicyIds | list[str] |  | The IDs of the IPAM policies to describe. |
| MaxResults | Any  # complex shape |  | The maximum number of results to return in a single call. |
| NextToken | Any  # complex shape |  | The token for the next page of results. |

## Output Shape: DescribeIpamPoliciesResult

- **IpamPolicies** (Any  # complex shape): Information about the IPAM policies. An IPAM policy is a set of rules that define how public IPv4 addresses from IPAM po
- **NextToken** (Any  # complex shape): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_ipam_policies(store, request: dict) -> dict:
    """Describes one or more IPAM policies. An IPAM policy is a set of rules that define how public IPv4 addresses from IPAM pools are allocated to Amazon Web Services resources. Each rule maps an Amazon Web"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
