---
id: "@specs/aws/ec2/describe_ipam_external_resource_verification_tokens"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeIpamExternalResourceVerificationTokens"
---

# DescribeIpamExternalResourceVerificationTokens

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_ipam_external_resource_verification_tokens
> **spec:implements:** @kind:operation DescribeIpamExternalResourceVerificationTokens
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeIpamExternalResourceVerificationTokens.spec.md

Describe verification tokens. A verification token is an Amazon Web Services-generated random value that you can use to prove ownership of an external resource. For example, you can use a verification token to validate that you control a public IP address range when you bring an IP address range to Amazon Web Services (BYOIP).

## Input Shape: DescribeIpamExternalResourceVerificationTokensRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| Filters | list[Any  # complex shape] |  | One or more filters for the request. For more information about filtering, see Filtering CLI output . Available filters: |
| IpamExternalResourceVerificationTokenIds | list[str] |  | Verification token IDs. |
| MaxResults | Any  # complex shape |  | The maximum number of tokens to return in one page of results. |
| NextToken | Any  # complex shape |  | The token for the next page of results. |

## Output Shape: DescribeIpamExternalResourceVerificationTokensResult

- **IpamExternalResourceVerificationTokens** (Any  # complex shape): Verification tokens.
- **NextToken** (Any  # complex shape): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_ipam_external_resource_verification_tokens(store, request: dict) -> dict:
    """Describe verification tokens. A verification token is an Amazon Web Services-generated random value that you can use to prove ownership of an external resource. For example, you can use a verification"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
