---
id: "@specs/aws/ec2/describe_vpc_endpoint_service_permissions"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeVpcEndpointServicePermissions"
---

# DescribeVpcEndpointServicePermissions

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_vpc_endpoint_service_permissions
> **spec:implements:** @kind:operation DescribeVpcEndpointServicePermissions
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeVpcEndpointServicePermissions.spec.md

Describes the principals (service consumers) that are permitted to discover your VPC endpoint service. Principal ARNs with path components aren't supported.

## Input Shape: DescribeVpcEndpointServicePermissionsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters. principal - The ARN of the principal. principal-type - The principal type ( All | Service | OrganizationUni |
| MaxResults | int |  | The maximum number of results to return for the request in a single page. The remaining results of the initial request c |
| NextToken | str |  | The token to retrieve the next page of results. |
| ServiceId | Any  # complex shape | ✓ | The ID of the service. |

## Output Shape: DescribeVpcEndpointServicePermissionsResult

- **AllowedPrincipals** (Any  # complex shape): Information about the allowed principals.
- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_vpc_endpoint_service_permissions(store, request: dict) -> dict:
    """Describes the principals (service consumers) that are permitted to discover your VPC endpoint service. Principal ARNs with path components aren't supported."""
    service_id = request.get("ServiceId", "").strip() if isinstance(request.get("ServiceId"), str) else request.get("ServiceId")
    if not service_id:
        raise ValidationException("ServiceId is required")

    resource = store.vpc_endpoint_service_permissionss(service_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource service_id not found")
    return {"ServiceId": service_id, **resource}
```
