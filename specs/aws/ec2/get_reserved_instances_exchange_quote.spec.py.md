---
id: "@specs/aws/ec2/get_reserved_instances_exchange_quote"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetReservedInstancesExchangeQuote"
---

# GetReservedInstancesExchangeQuote

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_reserved_instances_exchange_quote
> **spec:implements:** @kind:operation GetReservedInstancesExchangeQuote
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetReservedInstancesExchangeQuote.spec.md

Returns a quote and exchange information for exchanging one or more specified Convertible Reserved Instances for a new Convertible Reserved Instance. If the exchange cannot be performed, the reason is returned in the response. Use AcceptReservedInstancesExchangeQuote to perform the exchange.

## Input Shape: GetReservedInstancesExchangeQuoteRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| ReservedInstanceIds | Any  # complex shape | ✓ | The IDs of the Convertible Reserved Instances to exchange. |
| TargetConfigurations | Any  # complex shape |  | The configuration of the target Convertible Reserved Instance to exchange for your current Convertible Reserved Instance |

## Output Shape: GetReservedInstancesExchangeQuoteResult

- **CurrencyCode** (str): The currency of the transaction.
- **IsValidExchange** (bool): If true , the exchange is valid. If false , the exchange cannot be completed.
- **OutputReservedInstancesWillExpireAt** (Any  # complex shape): The new end date of the reservation term.
- **PaymentDue** (str): The total true upfront charge for the exchange.
- **ReservedInstanceValueRollup** (Any  # complex shape): The cost associated with the Reserved Instance.
- **ReservedInstanceValueSet** (Any  # complex shape): The configuration of your Convertible Reserved Instances.
- **TargetConfigurationValueRollup** (Any  # complex shape): The cost associated with the Reserved Instance.
- **TargetConfigurationValueSet** (Any  # complex shape): The values of the target Convertible Reserved Instances.
- **ValidationFailureReason** (str): Describes the reason why the exchange cannot be completed.

## Implementation

```speclang
def get_reserved_instances_exchange_quote(store, request: dict) -> dict:
    """Returns a quote and exchange information for exchanging one or more specified Convertible Reserved Instances for a new Convertible Reserved Instance. If the exchange cannot be performed, the reason is"""
    reserved_instance_ids = request.get("ReservedInstanceIds", "").strip() if isinstance(request.get("ReservedInstanceIds"), str) else request.get("ReservedInstanceIds")
    if not reserved_instance_ids:
        raise ValidationException("ReservedInstanceIds is required")

    resource = store.reserved_instances_exchange_quotes(reserved_instance_ids)
    if not resource:
        raise ResourceNotFoundException(f"Resource reserved_instance_ids not found")
    return {"ReservedInstanceIds": reserved_instance_ids, **resource}
```
