---
id: "@specs/aws/iam/list_access_keys"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_ListAccessKeys"
---

# ListAccessKeys

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/list_access_keys
> **spec:implements:** @kind:operation ListAccessKeys
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_ListAccessKeys.spec.md

Returns information about the access key IDs associated with the specified IAM user. If there is none, the operation returns an empty list. Although each user is limited to a small number of keys, you can still paginate the results using the MaxItems and Marker parameters. If the UserName is not specified, the user name is determined implicitly based on the Amazon Web Services access key ID used to sign the request. If a temporary access key is used, then UserName is required. If a long-term key is assigned to the user, then UserName is not required. This operation works for access keys under the Amazon Web Services account. If the Amazon Web Services account has no associated users, the root user returns it's own access key IDs by running this command. To ensure the security of your Amazon Web Services account, the secret access key is accessible only during key and user creation.

## Input Shape: ListAccessKeysRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Marker | Any  # complex shape |  | Use this parameter only when paginating results and only after you receive a response indicating that the results are tr |
| MaxItems | Any  # complex shape |  | Use this only when paginating results to indicate the maximum number of items you want in the response. If additional it |
| UserName | Any  # complex shape |  | The name of the user. This parameter allows (through its regex pattern ) a string of characters consisting of upper and  |

## Output Shape: ListAccessKeysResponse

- **AccessKeyMetadata** (Any  # complex shape): A list of objects containing metadata about the access keys.
- **IsTruncated** (Any  # complex shape): A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent 
- **Marker** (Any  # complex shape): When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequen

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def list_access_keys(store, request: dict) -> dict:
    """Returns information about the access key IDs associated with the specified IAM user. If there is none, the operation returns an empty list. Although each user is limited to a small number of keys, you"""

    items = store.list_access_keyss()
    return {"AccessKeyMetadata": list(items.values())}
```
