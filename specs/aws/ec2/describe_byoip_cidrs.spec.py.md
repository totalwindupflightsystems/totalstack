---
id: "@specs/aws/ec2/describe_byoip_cidrs"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeByoipCidrs"
---

# DescribeByoipCidrs

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_byoip_cidrs
> **spec:implements:** @kind:operation DescribeByoipCidrs
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeByoipCidrs.spec.md

Describes the IP address ranges that were provisioned for use with Amazon Web Services resources through through bring your own IP addresses (BYOIP).

## Input Shape: DescribeByoipCidrsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| MaxResults | Any  # complex shape | ✓ | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | Any  # complex shape |  | The token for the next page of results. |

## Output Shape: DescribeByoipCidrsResult

- **ByoipCidrs** (Any  # complex shape): Information about your address ranges.
- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_byoip_cidrs(store, request: dict) -> dict:
    """Describes the IP address ranges that were provisioned for use with Amazon Web Services resources through through bring your own IP addresses (BYOIP)."""
    max_results = request.get("MaxResults", "").strip() if isinstance(request.get("MaxResults"), str) else request.get("MaxResults")
    if not max_results:
        raise ValidationException("MaxResults is required")

    resource = store.byoip_cidrss(max_results)
    if not resource:
        raise ResourceNotFoundException(f"Resource max_results not found")
    return {"MaxResults": max_results, **resource}
```
