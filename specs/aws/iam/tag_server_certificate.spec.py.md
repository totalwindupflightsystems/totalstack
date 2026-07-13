---
id: "@specs/aws/iam/tag_server_certificate"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_TagServerCertificate"
---

# TagServerCertificate

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/tag_server_certificate
> **spec:implements:** @kind:operation TagServerCertificate
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_TagServerCertificate.spec.md

Adds one or more tags to an IAM server certificate. If a tag with the same key name already exists, then that tag is overwritten with the new value. For certificates in a Region supported by Certificate Manager (ACM), we recommend that you don't use IAM server certificates. Instead, use ACM to provision, manage, and deploy your server certificates. For more information about IAM server certificates, Working with server certificates in the IAM User Guide . A tag consists of a key name and an associated value. By assigning tags to your resources, you can do the following: Administrative grouping and discovery - Attach tags to resources to aid in organization and search. For example, you could search for all resources with the key name Project and the value MyImportantProject . Or search for all resources with the key name Cost Center and the value 41200 . Access control - Include tags in IAM user-based and resource-based policies. You can use tags to restrict access to only a server certificate that has a specified tag attached. For examples of policies that show how to use tags to control access, see Control access using IAM tags in the IAM User Guide . Cost allocation - Use tags to help track which individuals and teams are using which Amazon Web Services resources. If any one of the tags is invalid or if you exceed the allowed maximum number of tags, then the entire request fails and the resource is not created. For more information about tagging, see Tagging IAM resources in the IAM User Guide . Amazon Web Services always interprets the tag Value as a single string. If you need to store an array, you can store comma-separated values in the string. However, you must interpret the value in your code.

## Input Shape: TagServerCertificateRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ServerCertificateName | Any  # complex shape | ✓ | The name of the IAM server certificate to which you want to add tags. This parameter allows (through its regex pattern ) |
| Tags | Any  # complex shape | ✓ | The list of tags that you want to attach to the IAM server certificate. Each tag consists of a key name and an associate |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **ConcurrentModificationException**: The request was rejected because multiple requests to change this object were submitted simultaneously. Wait a few minutes and submit your request again.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def tag_server_certificate(store, request: dict) -> dict:
    """Adds one or more tags to an IAM server certificate. If a tag with the same key name already exists, then that tag is overwritten with the new value. For certificates in a Region supported by Certifica"""
    server_certificate_name = request.get("ServerCertificateName", "").strip() if isinstance(request.get("ServerCertificateName"), str) else request.get("ServerCertificateName")
    if not server_certificate_name:
        raise ValidationException("ServerCertificateName is required")
    tags = request.get("Tags", "").strip() if isinstance(request.get("Tags"), str) else request.get("Tags")
    if not tags:
        raise ValidationException("Tags is required")

    # Tag/untag resource
    resource_arn = request.get("ResourceARN", request.get("ResourceName", ""))
    store.tag_resource(resource_arn, request.get("Tags", []))
    return {}
```
