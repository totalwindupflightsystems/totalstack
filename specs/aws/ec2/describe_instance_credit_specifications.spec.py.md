---
id: "@specs/aws/ec2/describe_instance_credit_specifications"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeInstanceCreditSpecifications"
---

# DescribeInstanceCreditSpecifications

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_instance_credit_specifications
> **spec:implements:** @kind:operation DescribeInstanceCreditSpecifications
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeInstanceCreditSpecifications.spec.md

Describes the credit option for CPU usage of the specified burstable performance instances. The credit options are standard and unlimited . If you do not specify an instance ID, Amazon EC2 returns burstable performance instances with the unlimited credit option, as well as instances that were previously configured as T2, T3, and T3a with the unlimited credit option. For example, if you resize a T2 instance, while it is configured as unlimited , to an M4 instance, Amazon EC2 returns the M4 instance. If you specify one or more instance IDs, Amazon EC2 returns the credit option ( standard or unlimited ) of those instances. If you specify an instance ID that is not valid, such as an instance that is not a burstable performance instance, an error is returned. Recently terminated instances might appear in the returned results. This interval is usually less than one hour. If an Availability Zone is experiencing a service disruption and you specify instance IDs in the affected zone, or do not specify any instance IDs at all, the call fails. If you specify only instance IDs in an unaffected zone, the call works normally. For more information, see Burstable performance instances in the Amazon EC2 User Guide .

## Input Shape: DescribeInstanceCreditSpecificationsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the operation, without actually making the request, and provides an |
| Filters | list[Any  # complex shape] |  | The filters. instance-id - The ID of the instance. |
| InstanceIds | list[Any  # complex shape] |  | The instance IDs. Default: Describes all your instances. Constraints: Maximum 1000 explicitly specified instance IDs. |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |

## Output Shape: DescribeInstanceCreditSpecificationsResult

- **InstanceCreditSpecifications** (list[Any  # complex shape]): Information about the credit option for CPU usage of an instance.
- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t

## Implementation

```speclang
def describe_instance_credit_specifications(store, request: dict) -> dict:
    """Describes the credit option for CPU usage of the specified burstable performance instances. The credit options are standard and unlimited . If you do not specify an instance ID, Amazon EC2 returns bur"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
