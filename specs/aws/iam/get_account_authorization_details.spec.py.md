---
id: "@specs/aws/iam/get_account_authorization_details"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_GetAccountAuthorizationDetails"
---

# GetAccountAuthorizationDetails

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/get_account_authorization_details
> **spec:implements:** @kind:operation GetAccountAuthorizationDetails
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_GetAccountAuthorizationDetails.spec.md

Retrieves information about all IAM users, groups, roles, and policies in your Amazon Web Services account, including their relationships to one another. Use this operation to obtain a snapshot of the configuration of IAM permissions (users, groups, roles, and policies) in your account. Policies returned by this operation are URL-encoded compliant with RFC 3986 . You can use a URL decoding method to convert the policy back to plain JSON text. For example, if you use Java, you can use the decode method of the java.net.URLDecoder utility class in the Java SDK. Other languages and SDKs provide similar functionality, and some SDKs do this decoding automatically. You can optionally filter the results using the Filter parameter. You can paginate the results using the MaxItems and Marker parameters.

## Input Shape: GetAccountAuthorizationDetailsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Filter | Any  # complex shape |  | A list of entity types used to filter the results. Only the entities that match the types you specify are included in th |
| Marker | Any  # complex shape |  | Use this parameter only when paginating results and only after you receive a response indicating that the results are tr |
| MaxItems | Any  # complex shape |  | Use this only when paginating results to indicate the maximum number of items you want in the response. If additional it |

## Output Shape: GetAccountAuthorizationDetailsResponse

- **GroupDetailList** (Any  # complex shape): A list containing information about IAM groups.
- **IsTruncated** (Any  # complex shape): A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent 
- **Marker** (Any  # complex shape): When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequen
- **Policies** (Any  # complex shape): A list containing information about managed policies.
- **RoleDetailList** (Any  # complex shape): A list containing information about IAM roles.
- **UserDetailList** (Any  # complex shape): A list containing information about IAM users.

## Errors
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def get_account_authorization_details(store, request: dict) -> dict:
    """Retrieves information about all IAM users, groups, roles, and policies in your Amazon Web Services account, including their relationships to one another. Use this operation to obtain a snapshot of the"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
