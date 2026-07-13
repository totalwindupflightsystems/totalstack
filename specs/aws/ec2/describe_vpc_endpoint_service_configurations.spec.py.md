---
id: "@specs/aws/ec2/describe_vpc_endpoint_service_configurations"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeVpcEndpointServiceConfigurations"
---

# DescribeVpcEndpointServiceConfigurations

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_vpc_endpoint_service_configurations
> **spec:implements:** @kind:operation DescribeVpcEndpointServiceConfigurations
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeVpcEndpointServiceConfigurations.spec.md

Describes the VPC endpoint service configurations in your account (your services).

## Input Shape: DescribeVpcEndpointServiceConfigurationsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters. service-name - The name of the service. service-id - The ID of the service. service-state - The state of th |
| MaxResults | int |  | The maximum number of results to return for the request in a single page. The remaining results of the initial request c |
| NextToken | str |  | The token to retrieve the next page of results. |
| ServiceIds | list[Any  # complex shape] |  | The IDs of the endpoint services. |

## Output Shape: DescribeVpcEndpointServiceConfigurationsResult

- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.
- **ServiceConfigurations** (Any  # complex shape): Information about the services.

## Implementation

```speclang
def describe_vpc_endpoint_service_configurations(store, request: dict) -> dict:
    """Describes the VPC endpoint service configurations in your account (your services)."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
