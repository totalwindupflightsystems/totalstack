---
id: "@specs/aws/ec2/describe_account_attributes"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeAccountAttributes"
---

# DescribeAccountAttributes

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_account_attributes
> **spec:implements:** @kind:operation DescribeAccountAttributes
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeAccountAttributes.spec.md

Describes attributes of your Amazon Web Services account. The following are the supported account attributes: default-vpc : The ID of the default VPC for your account, or none . max-instances : This attribute is no longer supported. The returned value does not reflect your actual vCPU limit for running On-Demand Instances. For more information, see On-Demand Instance Limits in the Amazon Elastic Compute Cloud User Guide . max-elastic-ips : The maximum number of Elastic IP addresses that you can allocate. supported-platforms : This attribute is deprecated. vpc-max-elastic-ips : The maximum number of Elastic IP addresses that you can allocate. vpc-max-security-groups-per-interface : The maximum number of security groups that you can assign to a network interface. The order of the elements in the response, including those within nested structures, might vary. Applications should not assume the elements appear in a particular order.

## Input Shape: DescribeAccountAttributesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AttributeNames | list[Any  # complex shape] |  | The account attribute names. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: DescribeAccountAttributesResult

- **AccountAttributes** (list[Any  # complex shape]): Information about the account attributes.

## Implementation

```speclang
def describe_account_attributes(store, request: dict) -> dict:
    """Describes attributes of your Amazon Web Services account. The following are the supported account attributes: default-vpc : The ID of the default VPC for your account, or none . max-instances : This a"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
