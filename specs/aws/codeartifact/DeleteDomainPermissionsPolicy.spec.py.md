---
id: "@specs/aws/codeartifact/domain_policy_delete"
target_lang: py
version: 1.0.0
owned-by: codegen
status: active
depends_on: ["@specs/aws/codeartifact/plan"]
---

# DeleteDomainPermissionsPolicy

Deletes the resource policy set on a domain.

## Input Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `domain` | DomainName | Yes | Domain name |
| `domainOwner` | AccountId | No | Domain owner account |
| `policyRevision` | PolicyRevision | No | Revision for optimistic locking |

## Implementation

```speclang
@dataclass
@kind: operation
def execute_delete_domain_permissions_policy(store, request):
    """Deletes the resource policy set on a domain."""
    domain_name = request.get("domain", "")
    if not domain_name:
        raise ValidationException("domain is required")
    domain = store._get_domain(domain_name)
    store.domain_policies[domain_name] = ""
    return {"policy": {"resourceArn": domain.arn, "document": "", "revision": str(uuid.uuid4().hex[:8])}}
```
