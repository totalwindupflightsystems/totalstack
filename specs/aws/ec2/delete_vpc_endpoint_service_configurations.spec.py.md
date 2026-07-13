---
id: "@specs/aws/ec2/delete_vpc_endpoint_service_configurations"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteVpcEndpointServiceConfigurations"
---

# DeleteVpcEndpointServiceConfigurations

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_vpc_endpoint_service_configurations
> **spec:implements:** @kind:operation DeleteVpcEndpointServiceConfigurations
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteVpcEndpointServiceConfigurations.spec.md

Deletes the specified VPC endpoint service configurations. Before you can delete an endpoint service configuration, you must reject any Available or PendingAcceptance interface endpoint connections that are attached to the service.

## Input Shape: DeleteVpcEndpointServiceConfigurationsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| ServiceIds | list[Any  # complex shape] | ✓ | The IDs of the services. |

## Output Shape: DeleteVpcEndpointServiceConfigurationsResult

- **Unsuccessful** (Any  # complex shape): Information about the service configurations that were not deleted, if applicable.

## Implementation

```speclang
def delete_vpc_endpoint_service_configurations(store, request: dict) -> dict:
    """Deletes the specified VPC endpoint service configurations. Before you can delete an endpoint service configuration, you must reject any Available or PendingAcceptance interface endpoint connections th"""
    service_ids = request.get("ServiceIds", "").strip() if isinstance(request.get("ServiceIds"), str) else request.get("ServiceIds")

    if not store.vpc_endpoint_service_configurationss(service_ids):
        raise ResourceNotFoundException(f"Resource service_ids not found")
    store.delete_vpc_endpoint_service_configurationss(service_ids)
    return {}
```
