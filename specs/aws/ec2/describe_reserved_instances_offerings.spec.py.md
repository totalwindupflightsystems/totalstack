---
id: "@specs/aws/ec2/describe_reserved_instances_offerings"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeReservedInstancesOfferings"
---

# DescribeReservedInstancesOfferings

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_reserved_instances_offerings
> **spec:implements:** @kind:operation DescribeReservedInstancesOfferings
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeReservedInstancesOfferings.spec.md

Describes Reserved Instance offerings that are available for purchase. With Reserved Instances, you purchase the right to launch instances for a period of time. During that time period, you do not receive insufficient capacity errors, and you pay a lower usage rate than the rate charged for On-Demand instances for the actual time used. If you have listed your own Reserved Instances for sale in the Reserved Instance Marketplace, they will be excluded from these results. This is to ensure that you do not purchase your own Reserved Instances. For more information, see Sell in the Reserved Instance Marketplace in the Amazon EC2 User Guide . The order of the elements in the response, including those within nested structures, might vary. Applications should not assume the elements appear in a particular order.

## Input Shape: DescribeReservedInstancesOfferingsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AvailabilityZone | str |  | The Availability Zone in which the Reserved Instance can be used. Either AvailabilityZone or AvailabilityZoneId can be s |
| AvailabilityZoneId | Any  # complex shape |  | The ID of the Availability Zone. Either AvailabilityZone or AvailabilityZoneId can be specified, but not both. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. availability-zone - The Availability Zone where the Reserved Instance can be used. availability-zon |
| IncludeMarketplace | bool |  | Include Reserved Instance Marketplace offerings in the response. |
| InstanceTenancy | Any  # complex shape |  | The tenancy of the instances covered by the reservation. A Reserved Instance with a tenancy of dedicated is applied to i |
| InstanceType | Any  # complex shape |  | The instance type that the reservation will cover (for example, m1.small ). For more information, see Amazon EC2 instanc |
| MaxDuration | int |  | The maximum duration (in seconds) to filter when searching for offerings. Default: 94608000 (3 years) |
| MaxInstanceCount | int |  | The maximum number of instances to filter when searching for offerings. Default: 20 |
| MaxResults | int |  | The maximum number of results to return for the request in a single page. The remaining results of the initial request c |
| MinDuration | int |  | The minimum duration (in seconds) to filter when searching for offerings. Default: 2592000 (1 month) |
| NextToken | str |  | The token to retrieve the next page of results. |
| OfferingClass | Any  # complex shape |  | The offering class of the Reserved Instance. Can be standard or convertible . |
| OfferingType | Any  # complex shape |  | The Reserved Instance offering type. If you are using tools that predate the 2011-11-01 API version, you only have acces |
| ProductDescription | Any  # complex shape |  | The Reserved Instance product platform description. Instances that include (Amazon VPC) in the description are for use w |
| ReservedInstancesOfferingIds | list[Any  # complex shape] |  | One or more Reserved Instances offering IDs. |

## Output Shape: DescribeReservedInstancesOfferingsResult

- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.
- **ReservedInstancesOfferings** (list[Any  # complex shape]): A list of Reserved Instances offerings.

## Implementation

```speclang
def describe_reserved_instances_offerings(store, request: dict) -> dict:
    """Describes Reserved Instance offerings that are available for purchase. With Reserved Instances, you purchase the right to launch instances for a period of time. During that time period, you do not rec"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
