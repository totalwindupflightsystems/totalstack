---
id: "@specs/aws/ec2/get_ipam_address_history"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetIpamAddressHistory"
---

# GetIpamAddressHistory

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_ipam_address_history
> **spec:implements:** @kind:operation GetIpamAddressHistory
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetIpamAddressHistory.spec.md

Retrieve historical information about a CIDR within an IPAM scope. For more information, see View the history of IP addresses in the Amazon VPC IPAM User Guide .

## Input Shape: GetIpamAddressHistoryRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Cidr | str | ✓ | The CIDR you want the history of. The CIDR can be an IPv4 or IPv6 IP address range. If you enter a /16 IPv4 CIDR, you wi |
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| EndTime | Any  # complex shape |  | The end of the time period for which you are looking for history. If you omit this option, it will default to the curren |
| IpamScopeId | Any  # complex shape | ✓ | The ID of the IPAM scope that the CIDR is in. |
| MaxResults | Any  # complex shape |  | The maximum number of historical results you would like returned per page. Defaults to 100. |
| NextToken | Any  # complex shape |  | The token for the next page of results. |
| StartTime | Any  # complex shape |  | The start of the time period for which you are looking for history. If you omit this option, it will default to the valu |
| VpcId | str |  | The ID of the VPC you want your history records filtered by. |

## Output Shape: GetIpamAddressHistoryResult

- **HistoryRecords** (Any  # complex shape): A historical record for a CIDR within an IPAM scope. If the CIDR is associated with an EC2 instance, you will see an obj
- **NextToken** (Any  # complex shape): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def get_ipam_address_history(store, request: dict) -> dict:
    """Retrieve historical information about a CIDR within an IPAM scope. For more information, see View the history of IP addresses in the Amazon VPC IPAM User Guide ."""
    cidr = request.get("Cidr", "").strip() if isinstance(request.get("Cidr"), str) else request.get("Cidr")
    if not cidr:
        raise ValidationException("Cidr is required")
    ipam_scope_id = request.get("IpamScopeId", "").strip() if isinstance(request.get("IpamScopeId"), str) else request.get("IpamScopeId")
    if not ipam_scope_id:
        raise ValidationException("IpamScopeId is required")

    if store.ipam_address_historys(cidr):
        raise ResourceInUseException(f"Resource cidr already exists")

    record = {
        "DryRun": dry_run,
        "Cidr": cidr,
        "IpamScopeId": ipam_scope_id,
        "VpcId": vpc_id,
        "StartTime": start_time,
        "EndTime": end_time,
        "MaxResults": max_results,
        "NextToken": next_token,
    }

    store.ipam_address_historys(cidr, record)

    return {
        "HistoryRecords": record.get("HistoryRecords", {}),
        "NextToken": record.get("NextToken", {}),
    }
```
