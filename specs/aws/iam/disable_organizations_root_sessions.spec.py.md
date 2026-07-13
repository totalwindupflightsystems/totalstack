---
id: "@specs/aws/iam/disable_organizations_root_sessions"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_DisableOrganizationsRootSessions"
---

# DisableOrganizationsRootSessions

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/disable_organizations_root_sessions
> **spec:implements:** @kind:operation DisableOrganizationsRootSessions
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_DisableOrganizationsRootSessions.spec.md

Disables root user sessions for privileged tasks across member accounts in your organization. When you disable this feature, the management account and the delegated administrator for IAM can no longer perform privileged tasks on member accounts in your organization.

## Input Shape: DisableOrganizationsRootSessionsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|

## Output Shape: DisableOrganizationsRootSessionsResponse

- **EnabledFeatures** (Any  # complex shape): The features you have enabled for centralized root access of member accounts in your organization.
- **OrganizationId** (Any  # complex shape): The unique identifier (ID) of an organization.

## Errors
- **ServiceAccessNotEnabledException**: The request was rejected because trusted access is not enabled for IAM in Organizations. For details, see IAM and Organizations in the Organizations User Guide .
- **AccountNotManagementOrDelegatedAdministratorException**: The request was rejected because the account making the request is not the management account or delegated administrator account for centralized root access .
- **OrganizationNotFoundException**: The request was rejected because no organization is associated with your account.
- **OrganizationNotInAllFeaturesModeException**: The request was rejected because your organization does not have All features enabled. For more information, see Available feature sets in the Organizations User Guide .

## Implementation

```speclang
def disable_organizations_root_sessions(store, request: dict) -> dict:
    """Disables root user sessions for privileged tasks across member accounts in your organization. When you disable this feature, the management account and the delegated administrator for IAM can no longe"""

```
