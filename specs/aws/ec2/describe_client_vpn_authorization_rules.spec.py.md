---
id: "@specs/aws/ec2/describe_client_vpn_authorization_rules"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeClientVpnAuthorizationRules"
---

# DescribeClientVpnAuthorizationRules

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_client_vpn_authorization_rules
> **spec:implements:** @kind:operation DescribeClientVpnAuthorizationRules
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeClientVpnAuthorizationRules.spec.md

Describes the authorization rules for a specified Client VPN endpoint.

## Input Shape: DescribeClientVpnAuthorizationRulesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientVpnEndpointId | Any  # complex shape | ✓ | The ID of the Client VPN endpoint. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. Filter names and values are case-sensitive. description - The description of the authorization rule |
| MaxResults | Any  # complex shape |  | The maximum number of results to return for the request in a single page. The remaining results can be seen by sending a |
| NextToken | Any  # complex shape |  | The token to retrieve the next page of results. |

## Output Shape: DescribeClientVpnAuthorizationRulesResult

- **AuthorizationRules** (Any  # complex shape): Information about the authorization rules.
- **NextToken** (Any  # complex shape): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_client_vpn_authorization_rules(store, request: dict) -> dict:
    """Describes the authorization rules for a specified Client VPN endpoint."""
    client_vpn_endpoint_id = request.get("ClientVpnEndpointId", "").strip() if isinstance(request.get("ClientVpnEndpointId"), str) else request.get("ClientVpnEndpointId")
    if not client_vpn_endpoint_id:
        raise ValidationException("ClientVpnEndpointId is required")

    resource = store.client_vpn_authorization_ruless(client_vpn_endpoint_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource client_vpn_endpoint_id not found")
    return {"ClientVpnEndpointId": client_vpn_endpoint_id, **resource}
```
