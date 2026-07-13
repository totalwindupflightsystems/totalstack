---
id: "@specs/aws/iam/list_server_certificate_tags"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_ListServerCertificateTags"
---

# ListServerCertificateTags

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/list_server_certificate_tags
> **spec:implements:** @kind:operation ListServerCertificateTags
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_ListServerCertificateTags.spec.md

Lists the tags that are attached to the specified IAM server certificate. The returned list of tags is sorted by tag key. For more information about tagging, see Tagging IAM resources in the IAM User Guide . For certificates in a Region supported by Certificate Manager (ACM), we recommend that you don't use IAM server certificates. Instead, use ACM to provision, manage, and deploy your server certificates. For more information about IAM server certificates, Working with server certificates in the IAM User Guide .

## Input Shape: ListServerCertificateTagsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Marker | Any  # complex shape |  | Use this parameter only when paginating results and only after you receive a response indicating that the results are tr |
| MaxItems | Any  # complex shape |  | Use this only when paginating results to indicate the maximum number of items you want in the response. If additional it |
| ServerCertificateName | Any  # complex shape | ✓ | The name of the IAM server certificate whose tags you want to see. This parameter allows (through its regex pattern ) a  |

## Output Shape: ListServerCertificateTagsResponse

- **IsTruncated** (Any  # complex shape): A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent 
- **Marker** (Any  # complex shape): When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequen
- **Tags** (Any  # complex shape): The list of tags that are currently attached to the IAM server certificate. Each tag consists of a key name and an assoc

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def list_server_certificate_tags(store, request: dict) -> dict:
    """Lists the tags that are attached to the specified IAM server certificate. The returned list of tags is sorted by tag key. For more information about tagging, see Tagging IAM resources in the IAM User """
    server_certificate_name = request.get("ServerCertificateName", "").strip() if isinstance(request.get("ServerCertificateName"), str) else request.get("ServerCertificateName")
    if not server_certificate_name:
        raise ValidationException("ServerCertificateName is required")

    items = store.list_server_certificate_tagss()
    return {"Tags": list(items.values())}
```
