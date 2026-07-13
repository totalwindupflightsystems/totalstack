---
id: "@specs/aws/ec2/create_ipam_pool"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateIpamPool"
---

# CreateIpamPool

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_ipam_pool
> **spec:implements:** @kind:operation CreateIpamPool
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateIpamPool.spec.md

Create an IP address pool for Amazon VPC IP Address Manager (IPAM). In IPAM, a pool is a collection of contiguous IP addresses CIDRs. Pools enable you to organize your IP addresses according to your routing and security needs. For example, if you have separate routing and security needs for development and production applications, you can create a pool for each. For more information, see Create a top-level pool in the Amazon VPC IPAM User Guide .

## Input Shape: CreateIpamPoolRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AddressFamily | Any  # complex shape | ✓ | The IP protocol assigned to this IPAM pool. You must choose either IPv4 or IPv6 protocol for a pool. |
| AllocationDefaultNetmaskLength | Any  # complex shape |  | The default netmask length for allocations added to this pool. If, for example, the CIDR assigned to this pool is 10.0.0 |
| AllocationMaxNetmaskLength | Any  # complex shape |  | The maximum netmask length possible for CIDR allocations in this IPAM pool to be compliant. The maximum netmask length m |
| AllocationMinNetmaskLength | Any  # complex shape |  | The minimum netmask length required for CIDR allocations in this IPAM pool to be compliant. The minimum netmask length m |
| AllocationResourceTags | list[Any  # complex shape] |  | Tags that are required for resources that use CIDRs from this IPAM pool. Resources that do not have these tags will not  |
| AutoImport | bool |  | If selected, IPAM will continuously look for resources within the CIDR range of this pool and automatically import them  |
| AwsService | Any  # complex shape |  | Limits which service in Amazon Web Services that the pool can be used in. "ec2", for example, allows users to use space  |
| ClientToken | str |  | A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see |
| Description | str |  | A description for the IPAM pool. |
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| IpamScopeId | Any  # complex shape | ✓ | The ID of the scope in which you would like to create the IPAM pool. |
| Locale | str |  | The locale for the pool should be one of the following: An Amazon Web Services Region where you want this IPAM pool to b |
| PublicIpSource | Any  # complex shape |  | The IP address source for pools in the public scope. Only used for provisioning IP address CIDRs to pools in the public  |
| PubliclyAdvertisable | bool |  | Determines if the pool is publicly advertisable. The request can only contain PubliclyAdvertisable if AddressFamily is i |
| SourceIpamPoolId | Any  # complex shape |  | The ID of the source IPAM pool. Use this option to create a pool within an existing pool. Note that the CIDR you provisi |
| SourceResource | Any  # complex shape |  | The resource used to provision CIDRs to a resource planning pool. |
| TagSpecifications | list[Any  # complex shape] |  | The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the |

## Output Shape: CreateIpamPoolResult

- **IpamPool** (Any  # complex shape): Information about the IPAM pool created.

## Implementation

```speclang
def create_ipam_pool(store, request: dict) -> dict:
    """Create an IP address pool for Amazon VPC IP Address Manager (IPAM). In IPAM, a pool is a collection of contiguous IP addresses CIDRs. Pools enable you to organize your IP addresses according to your r"""
    address_family = request.get("AddressFamily", "").strip() if isinstance(request.get("AddressFamily"), str) else request.get("AddressFamily")
    if not address_family:
        raise ValidationException("AddressFamily is required")
    ipam_scope_id = request.get("IpamScopeId", "").strip() if isinstance(request.get("IpamScopeId"), str) else request.get("IpamScopeId")
    if not ipam_scope_id:
        raise ValidationException("IpamScopeId is required")

    if store.ipam_pools(ipam_scope_id):
        raise ResourceInUseException(f"Resource ipam_scope_id already exists")

    record = {
        "DryRun": dry_run,
        "IpamScopeId": ipam_scope_id,
        "Locale": locale,
        "SourceIpamPoolId": source_ipam_pool_id,
        "Description": description,
        "AddressFamily": address_family,
        "AutoImport": auto_import,
        "PubliclyAdvertisable": publicly_advertisable,
        "AllocationMinNetmaskLength": allocation_min_netmask_length,
        "AllocationMaxNetmaskLength": allocation_max_netmask_length,
        "AllocationDefaultNetmaskLength": allocation_default_netmask_length,
        "AllocationResourceTags": allocation_resource_tags,
        "TagSpecifications": tag_specifications,
        "ClientToken": client_token,
        "AwsService": aws_service,
        "PublicIpSource": public_ip_source,
        "SourceResource": source_resource,
    }

    store.ipam_pools(ipam_scope_id, record)

    return {
        "IpamPool": record.get("IpamPool", {}),
    }
```
