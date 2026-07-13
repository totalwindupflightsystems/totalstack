---
id: "@specs/aws/ec2/describe_elastic_gpus"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeElasticGpus"
---

# DescribeElasticGpus

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_elastic_gpus
> **spec:implements:** @kind:operation DescribeElasticGpus
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeElasticGpus.spec.md

Amazon Elastic Graphics reached end of life on January 8, 2024. Describes the Elastic Graphics accelerator associated with your instances.

## Input Shape: DescribeElasticGpusRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| ElasticGpuIds | Any  # complex shape |  | The Elastic Graphics accelerator IDs. |
| Filters | list[Any  # complex shape] |  | The filters. availability-zone - The Availability Zone in which the Elastic Graphics accelerator resides. elastic-gpu-he |
| MaxResults | Any  # complex shape |  | The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the  |
| NextToken | str |  | The token to request the next page of results. |

## Output Shape: DescribeElasticGpusResult

- **ElasticGpuSet** (Any  # complex shape): Information about the Elastic Graphics accelerators.
- **MaxResults** (int): The total number of items to return. If the total number of items available is more than the value specified in max-item
- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_elastic_gpus(store, request: dict) -> dict:
    """Amazon Elastic Graphics reached end of life on January 8, 2024. Describes the Elastic Graphics accelerator associated with your instances."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
