---
id: "@specs/aws/ec2/describe_verified_access_endpoints"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeVerifiedAccessEndpoints"
---

# DescribeVerifiedAccessEndpoints

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_verified_access_endpoints
> **spec:implements:** @kind:operation DescribeVerifiedAccessEndpoints
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeVerifiedAccessEndpoints.spec.md

Describes the specified Amazon Web Services Verified Access endpoints.

## Input Shape: DescribeVerifiedAccessEndpointsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. Filter names and values are case-sensitive. |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | Any  # complex shape |  | The token for the next page of results. |
| VerifiedAccessEndpointIds | list[Any  # complex shape] |  | The ID of the Verified Access endpoint. |
| VerifiedAccessGroupId | Any  # complex shape |  | The ID of the Verified Access group. |
| VerifiedAccessInstanceId | Any  # complex shape |  | The ID of the Verified Access instance. |

## Output Shape: DescribeVerifiedAccessEndpointsResult

- **NextToken** (Any  # complex shape): The token to use to retrieve the next page of results. This value is null when there are no more results to return.
- **VerifiedAccessEndpoints** (list[Any  # complex shape]): Details about the Verified Access endpoints.

## Implementation

```speclang
def describe_verified_access_endpoints(store, request: dict) -> dict:
    """Describes the specified Amazon Web Services Verified Access endpoints."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
