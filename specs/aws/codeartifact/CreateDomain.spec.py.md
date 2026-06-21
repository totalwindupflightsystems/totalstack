---
id: "@specs/aws/codeartifact/create_domain"
target_lang: py
version: 1.0.0
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/codeartifact/plan"
---

# CreateDomain

Creates a domain. CodeArtifact domains make it easier to manage multiple repositories across an organization.

## Input Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `domain` | DomainName | Yes | Name of the domain to create (2-50 chars, alphanumeric+hyphen) |
| `encryptionKey` | Arn | No | KMS key ARN for encryption (default: AWS-managed key) |
| `tags` | TagList | No | Tags to associate with the domain |

## Errors
- `AccessDeniedException`
- `ConflictException`
- `InternalServerException`
- `ServiceQuotaExceededException`
- `ThrottlingException`
- `ValidationException`

## Output Members
- `domain` (DomainDescription): arn, name, owner, status, createdTime, encryptionKey, repositoryCount, assetSizeBytes, s3BucketArn

## Implementation

```speclang
@dataclass
@kind: operation
def execute_create_domain(store, request):
    """Creates a domain. CodeArtifact domains make it easier to manage multiple repositories across an organization."""
    domain_name = request.get("domain", "")
    if not domain_name:
        raise ValidationException("domain is required")

    _validate_domain_name(domain_name)

    if domain_name in store.domains:
        raise ConflictException(f"Domain {domain_name} already exists")

    owner = "123456789012"
    domain = DomainRecord(
        name=domain_name,
        owner=owner,
        encryption_key=request.get("encryptionKey"),
    )

    store.domains[domain_name] = domain
    store.domain_policies[domain_name] = ""

    result = {
        "domain": {
            "name": domain.name,
            "owner": domain.owner,
            "arn": domain.arn,
            "status": domain.status,
            "createdTime": domain.created_time,
            "encryptionKey": domain.encryption_key,
            "repositoryCount": domain.repository_count,
            "assetSizeBytes": domain.asset_size_bytes,
            "s3BucketArn": domain.s3_bucket_arn,
        }
    }

    if request.get("tags"):
        arn = domain.arn
        for tag in request["tags"]:
            store.tags[arn][tag["key"]] = tag["value"]

    return result
```
