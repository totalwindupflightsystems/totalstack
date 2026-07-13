---
id: "@specs/aws/ec2/describe_principal_id_format"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribePrincipalIdFormat"
---

# DescribePrincipalIdFormat

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_principal_id_format
> **spec:implements:** @kind:operation DescribePrincipalIdFormat
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribePrincipalIdFormat.spec.md

Describes the ID format settings for the root user and all IAM roles and IAM users that have explicitly specified a longer ID (17-character ID) preference. By default, all IAM roles and IAM users default to the same ID settings as the root user, unless they explicitly override the settings. This request is useful for identifying those IAM users and IAM roles that have overridden the default ID settings. The following resource types support longer IDs: bundle | conversion-task | customer-gateway | dhcp-options | elastic-ip-allocation | elastic-ip-association | export-task | flow-log | image | import-task | instance | internet-gateway | network-acl | network-acl-association | network-interface | network-interface-attachment | prefix-list | reservation | route-table | route-table-association | security-group | snapshot | subnet | subnet-cidr-block-association | volume | vpc | vpc-cidr-block-association | vpc-endpoint | vpc-peering-connection | vpn-connection | vpn-gateway .

## Input Shape: DescribePrincipalIdFormatRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| MaxResults | Any  # complex shape |  | The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the  |
| NextToken | str |  | The token to request the next page of results. |
| Resources | list[str] |  | The type of resource: bundle | conversion-task | customer-gateway | dhcp-options | elastic-ip-allocation | elastic-ip-as |

## Output Shape: DescribePrincipalIdFormatResult

- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.
- **Principals** (list[Any  # complex shape]): Information about the ID format settings for the ARN.

## Implementation

```speclang
def describe_principal_id_format(store, request: dict) -> dict:
    """Describes the ID format settings for the root user and all IAM roles and IAM users that have explicitly specified a longer ID (17-character ID) preference. By default, all IAM roles and IAM users defa"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
