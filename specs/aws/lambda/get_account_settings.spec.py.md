---
id: "@specs/aws/lambda/get_account_settings"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_GetAccountSettings"
---

# GetAccountSettings

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/get_account_settings
> **spec:implements:** @kind:operation GetAccountSettings
> **AWS Protocol:** rest-json
> **HTTP:** GET /2016-08-19/account-settings
> **@ref:** specs/aws/lambda/docs/API_GetAccountSettings.spec.md

Retrieves details about your account's limits and usage in an Amazon Web Services Region.

## Input Shape: GetAccountSettingsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|

## Output Shape: GetAccountSettingsResponse

- **AccountLimit** (Any  # complex shape): Limits that are related to concurrency and code storage.
- **AccountUsage** (Any  # complex shape): The number of functions and amount of storage in use.

## Errors
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .

## Implementation

```speclang
def get_account_settings(store, request: dict) -> dict:
    """Retrieves details about your account's limits and usage in an Amazon Web Services Region."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
