---
id: "@specs/aws/ec2/accept_reserved_instances_exchange_quote"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_AcceptReservedInstancesExchangeQuote"
---

# AcceptReservedInstancesExchangeQuote

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/accept_reserved_instances_exchange_quote
> **spec:implements:** @kind:operation AcceptReservedInstancesExchangeQuote
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_AcceptReservedInstancesExchangeQuote.spec.md

Accepts the Convertible Reserved Instance exchange quote described in the GetReservedInstancesExchangeQuote call.

## Input Shape: AcceptReservedInstancesExchangeQuoteRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| ReservedInstanceIds | Any  # complex shape | ✓ | The IDs of the Convertible Reserved Instances to exchange for another Convertible Reserved Instance of the same or highe |
| TargetConfigurations | Any  # complex shape |  | The configuration of the target Convertible Reserved Instance to exchange for your current Convertible Reserved Instance |

## Output Shape: AcceptReservedInstancesExchangeQuoteResult

- **ExchangeId** (str): The ID of the successful exchange.

## Implementation

```speclang
def accept_reserved_instances_exchange_quote(store, request: dict) -> dict:
    """Accepts the Convertible Reserved Instance exchange quote described in the GetReservedInstancesExchangeQuote call."""
    reserved_instance_ids = request.get("ReservedInstanceIds", "").strip() if isinstance(request.get("ReservedInstanceIds"), str) else request.get("ReservedInstanceIds")
    if not reserved_instance_ids:
        raise ValidationException("ReservedInstanceIds is required")

    resource = store.accept_reserved_instances_exchange_quotes(reserved_instance_ids)
    if not resource:
        raise ResourceNotFoundException(f"Resource reserved_instance_ids not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run
    if "TargetConfigurations" in request:
        resource["TargetConfigurations"] = target_configurations

    store.accept_reserved_instances_exchange_quotes(reserved_instance_ids, resource)
    return resource
```
