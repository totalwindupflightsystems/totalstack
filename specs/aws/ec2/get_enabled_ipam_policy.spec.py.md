---
id: "@specs/aws/ec2/get_enabled_ipam_policy"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetEnabledIpamPolicy"
---

# GetEnabledIpamPolicy

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_enabled_ipam_policy
> **spec:implements:** @kind:operation GetEnabledIpamPolicy
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetEnabledIpamPolicy.spec.md

Gets the enabled IPAM policy. An IPAM policy is a set of rules that define how public IPv4 addresses from IPAM pools are allocated to Amazon Web Services resources. Each rule maps an Amazon Web Services service to IPAM pools that the service will use to get IP addresses. A single policy can have multiple rules and be applied to multiple Amazon Web Services Regions. If the IPAM pool run out of addresses then the services fallback to Amazon-provided IP addresses. A policy can be applied to an individual Amazon Web Services account or an entity within Amazon Web Services Organizations.

## Input Shape: GetEnabledIpamPolicyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |

## Output Shape: GetEnabledIpamPolicyResult

- **IpamPolicyEnabled** (bool): Indicates whether the IPAM policy is enabled.
- **IpamPolicyId** (Any  # complex shape): The ID of the enabled IPAM policy.
- **ManagedBy** (Any  # complex shape): The entity that manages the IPAM policy.

## Implementation

```speclang
def get_enabled_ipam_policy(store, request: dict) -> dict:
    """Gets the enabled IPAM policy. An IPAM policy is a set of rules that define how public IPv4 addresses from IPAM pools are allocated to Amazon Web Services resources. Each rule maps an Amazon Web Servic"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
