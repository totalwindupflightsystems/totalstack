---
id: "@specs/aws/ec2/create_verified_access_instance"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateVerifiedAccessInstance"
---

# CreateVerifiedAccessInstance

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_verified_access_instance
> **spec:implements:** @kind:operation CreateVerifiedAccessInstance
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateVerifiedAccessInstance.spec.md

An Amazon Web Services Verified Access instance is a regional entity that evaluates application requests and grants access only when your security requirements are met.

## Input Shape: CreateVerifiedAccessInstanceRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CidrEndpointsCustomSubDomain | str |  | The custom subdomain. |
| ClientToken | str |  | A unique, case-sensitive token that you provide to ensure idempotency of your modification request. For more information |
| Description | str |  | A description for the Verified Access instance. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| FIPSEnabled | bool |  | Enable or disable support for Federal Information Processing Standards (FIPS) on the instance. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to assign to the Verified Access instance. |

## Output Shape: CreateVerifiedAccessInstanceResult

- **VerifiedAccessInstance** (Any  # complex shape): Details about the Verified Access instance.

## Implementation

```speclang
def create_verified_access_instance(store, request: dict) -> dict:
    """An Amazon Web Services Verified Access instance is a regional entity that evaluates application requests and grants access only when your security requirements are met."""


    record = {
        "Description": description,
        "TagSpecifications": tag_specifications,
        "ClientToken": client_token,
        "DryRun": dry_run,
        "FIPSEnabled": fips_enabled,
        "CidrEndpointsCustomSubDomain": cidr_endpoints_custom_sub_domain,
    }

    store.verified_access_instances(record)

    return {
        "VerifiedAccessInstance": record.get("VerifiedAccessInstance", {}),
    }
```
