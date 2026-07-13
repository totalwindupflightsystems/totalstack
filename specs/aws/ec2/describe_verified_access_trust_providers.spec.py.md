---
id: "@specs/aws/ec2/describe_verified_access_trust_providers"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeVerifiedAccessTrustProviders"
---

# DescribeVerifiedAccessTrustProviders

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_verified_access_trust_providers
> **spec:implements:** @kind:operation DescribeVerifiedAccessTrustProviders
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeVerifiedAccessTrustProviders.spec.md

Describes the specified Amazon Web Services Verified Access trust providers.

## Input Shape: DescribeVerifiedAccessTrustProvidersRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. Filter names and values are case-sensitive. |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | Any  # complex shape |  | The token for the next page of results. |
| VerifiedAccessTrustProviderIds | list[Any  # complex shape] |  | The IDs of the Verified Access trust providers. |

## Output Shape: DescribeVerifiedAccessTrustProvidersResult

- **NextToken** (Any  # complex shape): The token to use to retrieve the next page of results. This value is null when there are no more results to return.
- **VerifiedAccessTrustProviders** (list[Any  # complex shape]): Details about the Verified Access trust providers.

## Implementation

```speclang
def describe_verified_access_trust_providers(store, request: dict) -> dict:
    """Describes the specified Amazon Web Services Verified Access trust providers."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
