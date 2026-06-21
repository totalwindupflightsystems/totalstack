---
id: "@specs/aws/codeartifact/describe_domain"
target_lang: py
version: 1.0.0
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/codeartifact/plan"
---

# DescribeDomain

Returns a DomainDescription object that contains information about the requested domain.

## Input Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `domain` | DomainName | Yes | Name of the domain to describe |
| `domainOwner` | AccountId | No | 12-digit account number of the domain owner |

## Errors
- `AccessDeniedException`
- `InternalServerException`
- `ResourceNotFoundException`
- `ThrottlingException`
- `ValidationException`

## Implementation

```speclang
@dataclass
@kind: operation
def execute_describe_domain(store, request):
    """Returns a DomainDescription object that contains information about the requested domain."""
    domain_name = request.get("domain", "")
    if not domain_name:
        raise ValidationException("domain is required")

    domain = store._get_domain(domain_name)

    return {
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
```
