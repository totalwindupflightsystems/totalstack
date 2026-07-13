---
id: "@specs/aws/iam/enable_organizations_root_sessions"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_EnableOrganizationsRootSessions"
---

# EnableOrganizationsRootSessions

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/enable_organizations_root_sessions
> **spec:implements:** @kind:operation EnableOrganizationsRootSessions
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_EnableOrganizationsRootSessions.spec.md

Allows the management account or delegated administrator to perform privileged tasks on member accounts in your organization. For more information, see Centrally manage root access for member accounts in the Identity and Access Management User Guide . Before you enable this feature, you must have an account configured with the following settings: You must manage your Amazon Web Services accounts in Organizations . Enable trusted access for Identity and Access Management in Organizations. For details, see IAM and Organizations in the Organizations User Guide .

## Input Shape: EnableOrganizationsRootSessionsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|

## Output Shape: EnableOrganizationsRootSessionsResponse

- **EnabledFeatures** (Any  # complex shape): The features you have enabled for centralized root access.
- **OrganizationId** (Any  # complex shape): The unique identifier (ID) of an organization.

## Errors
- **ServiceAccessNotEnabledException**: The request was rejected because trusted access is not enabled for IAM in Organizations. For details, see IAM and Organizations in the Organizations User Guide .
- **AccountNotManagementOrDelegatedAdministratorException**: The request was rejected because the account making the request is not the management account or delegated administrator account for centralized root access .
- **OrganizationNotFoundException**: The request was rejected because no organization is associated with your account.
- **OrganizationNotInAllFeaturesModeException**: The request was rejected because your organization does not have All features enabled. For more information, see Available feature sets in the Organizations User Guide .
- **CallerIsNotManagementAccountException**: The request was rejected because the account making the request is not the management account for the organization.

## Implementation

```speclang
def enable_organizations_root_sessions(store, request: dict) -> dict:
    """Allows the management account or delegated administrator to perform privileged tasks on member accounts in your organization. For more information, see Centrally manage root access for member accounts"""

```
