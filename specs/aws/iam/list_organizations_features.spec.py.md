---
id: "@specs/aws/iam/list_organizations_features"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_ListOrganizationsFeatures"
---

# ListOrganizationsFeatures

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/list_organizations_features
> **spec:implements:** @kind:operation ListOrganizationsFeatures
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_ListOrganizationsFeatures.spec.md

Lists the centralized root access features enabled for your organization. For more information, see Centrally manage root access for member accounts .

## Input Shape: ListOrganizationsFeaturesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|

## Output Shape: ListOrganizationsFeaturesResponse

- **EnabledFeatures** (Any  # complex shape): Specifies the features that are currently available in your organization.
- **OrganizationId** (Any  # complex shape): The unique identifier (ID) of an organization.

## Errors
- **ServiceAccessNotEnabledException**: The request was rejected because trusted access is not enabled for IAM in Organizations. For details, see IAM and Organizations in the Organizations User Guide .
- **AccountNotManagementOrDelegatedAdministratorException**: The request was rejected because the account making the request is not the management account or delegated administrator account for centralized root access .
- **OrganizationNotFoundException**: The request was rejected because no organization is associated with your account.
- **OrganizationNotInAllFeaturesModeException**: The request was rejected because your organization does not have All features enabled. For more information, see Available feature sets in the Organizations User Guide .

## Implementation

```speclang
def list_organizations_features(store, request: dict) -> dict:
    """Lists the centralized root access features enabled for your organization. For more information, see Centrally manage root access for member accounts ."""

    items = store.list_organizations_featuress()
    return {"EnabledFeatures": list(items.values())}
```
