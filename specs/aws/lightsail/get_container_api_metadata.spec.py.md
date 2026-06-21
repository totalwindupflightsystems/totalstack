---
id: "@specs/aws/lightsail/get_container_api_metadata"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_GetContainerAPIMetadata"
---

# GetContainerAPIMetadata

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/get_container_api_metadata
> **spec:implements:** @kind:operation GetContainerAPIMetadata
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_GetContainerAPIMetadata.spec.md

Returns information about Amazon Lightsail containers, such as the current version of the Lightsail Control (lightsailctl) plugin.

## Input Shape: GetContainerAPIMetadataRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|

## Output Shape: GetContainerAPIMetadataResult

- **metadata** (list[Any  # complex shape]): Metadata about Lightsail containers, such as the current version of the Lightsail Control (lightsailctl) plugin.

## Errors
- **ServiceException**: A general service exception.
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.
- **RegionSetupInProgressException**: Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.

## Implementation

```speclang
def get_container_api_metadata(store, request: dict) -> dict:
    """Returns information about Amazon Lightsail containers, such as the current version of the Lightsail Control (lightsailctl) plugin."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
