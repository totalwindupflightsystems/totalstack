---
id: "@specs/aws/ec2/describe_vpc_endpoint_services"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeVpcEndpointServices"
---

# DescribeVpcEndpointServices

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_vpc_endpoint_services
> **spec:implements:** @kind:operation DescribeVpcEndpointServices
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeVpcEndpointServices.spec.md

Describes available services to which you can create a VPC endpoint. When the service provider and the consumer have different accounts in multiple Availability Zones, and the consumer views the VPC endpoint service information, the response only includes the common Availability Zones. For example, when the service provider account uses us-east-1a and us-east-1c and the consumer uses us-east-1a and us-east-1b , the response includes the VPC endpoint services in the common Availability Zone, us-east-1a .

## Input Shape: DescribeVpcEndpointServicesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters. owner - The ID or alias of the Amazon Web Services account that owns the service. service-name - The name o |
| MaxResults | int |  | The maximum number of items to return for this request. The request returns a token that you can specify in a subsequent |
| NextToken | str |  | The token for the next set of items to return. (You received this token from a prior call.) |
| ServiceNames | list[str] |  | The service names. |
| ServiceRegions | list[str] |  | The service Regions. |

## Output Shape: DescribeVpcEndpointServicesResult

- **NextToken** (str): The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
- **ServiceDetails** (Any  # complex shape): Information about the service.
- **ServiceNames** (list[str]): The supported services.

## Implementation

```speclang
def describe_vpc_endpoint_services(store, request: dict) -> dict:
    """Describes available services to which you can create a VPC endpoint. When the service provider and the consumer have different accounts in multiple Availability Zones, and the consumer views the VPC e"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
