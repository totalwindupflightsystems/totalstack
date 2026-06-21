---
id: "@specs/aws/codeartifact/delete_domain"
target_lang: py
version: 1.0.0
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/codeartifact/plan"
---

# DeleteDomain

Deletes a domain. You cannot delete a domain that contains repositories.

## Input Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `domain` | DomainName | Yes | Name of the domain to delete |
| `domainOwner` | AccountId | No | 12-digit account number of the domain owner |

## Errors
- `AccessDeniedException`
- `ConflictException`
- `InternalServerException`
- `ResourceNotFoundException`
- `ThrottlingException`
- `ValidationException`

## Implementation

```speclang
@dataclass
@kind: operation
def execute_delete_domain(store, request):
    """Deletes a domain. You cannot delete a domain that contains repositories."""
    domain_name = request.get("domain", "")
    if not domain_name:
        raise ValidationException("domain is required")

    domain = store._get_domain(domain_name)

    if domain.repository_count > 0:
        raise ConflictException(
            f"Domain {domain_name} contains {domain.repository_count} repositories. Delete them first."
        )

    del store.domains[domain_name]
    store.domain_policies.pop(domain_name, None)
    store.tags.pop(domain.arn, None)

    return {"domain": {"name": domain_name, "arn": domain.arn, "status": "Deleted"}}
```
