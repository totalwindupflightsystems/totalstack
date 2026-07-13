---
id: "@specs/aws/iam/list_signing_certificates"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_ListSigningCertificates"
---

# ListSigningCertificates

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/list_signing_certificates
> **spec:implements:** @kind:operation ListSigningCertificates
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_ListSigningCertificates.spec.md

Returns information about the signing certificates associated with the specified IAM user. If none exists, the operation returns an empty list. Although each user is limited to a small number of signing certificates, you can still paginate the results using the MaxItems and Marker parameters. If the UserName field is not specified, the user name is determined implicitly based on the Amazon Web Services access key ID used to sign the request for this operation. This operation works for access keys under the Amazon Web Services account. Consequently, you can use this operation to manage Amazon Web Services account root user credentials even if the Amazon Web Services account has no associated users.

## Input Shape: ListSigningCertificatesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Marker | Any  # complex shape |  | Use this parameter only when paginating results and only after you receive a response indicating that the results are tr |
| MaxItems | Any  # complex shape |  | Use this only when paginating results to indicate the maximum number of items you want in the response. If additional it |
| UserName | Any  # complex shape |  | The name of the IAM user whose signing certificates you want to examine. This parameter allows (through its regex patter |

## Output Shape: ListSigningCertificatesResponse

- **Certificates** (Any  # complex shape): A list of the user's signing certificate information.
- **IsTruncated** (Any  # complex shape): A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent 
- **Marker** (Any  # complex shape): When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequen

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def list_signing_certificates(store, request: dict) -> dict:
    """Returns information about the signing certificates associated with the specified IAM user. If none exists, the operation returns an empty list. Although each user is limited to a small number of signi"""

    items = store.list_signing_certificatess()
    return {"Certificates": list(items.values())}
```
