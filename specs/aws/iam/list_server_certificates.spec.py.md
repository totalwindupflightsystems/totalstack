---
id: "@specs/aws/iam/list_server_certificates"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_ListServerCertificates"
---

# ListServerCertificates

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/list_server_certificates
> **spec:implements:** @kind:operation ListServerCertificates
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_ListServerCertificates.spec.md

Lists the server certificates stored in IAM that have the specified path prefix. If none exist, the operation returns an empty list. You can paginate the results using the MaxItems and Marker parameters. For more information about working with server certificates, see Working with server certificates in the IAM User Guide . This topic also includes a list of Amazon Web Services services that can use the server certificates that you manage with IAM. IAM resource-listing operations return a subset of the available attributes for the resource. For example, this operation does not return tags, even though they are an attribute of the returned object. To view all of the information for a servercertificate, see GetServerCertificate .

## Input Shape: ListServerCertificatesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Marker | Any  # complex shape |  | Use this parameter only when paginating results and only after you receive a response indicating that the results are tr |
| MaxItems | Any  # complex shape |  | Use this only when paginating results to indicate the maximum number of items you want in the response. If additional it |
| PathPrefix | Any  # complex shape |  | The path prefix for filtering the results. For example: /company/servercerts would get all server certificates for which |

## Output Shape: ListServerCertificatesResponse

- **IsTruncated** (Any  # complex shape): A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent 
- **Marker** (Any  # complex shape): When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequen
- **ServerCertificateMetadataList** (Any  # complex shape): A list of server certificates.

## Errors
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def list_server_certificates(store, request: dict) -> dict:
    """Lists the server certificates stored in IAM that have the specified path prefix. If none exist, the operation returns an empty list. You can paginate the results using the MaxItems and Marker paramete"""

    items = store.list_server_certificatess()
    return {"ServerCertificateMetadataList": list(items.values())}
```
