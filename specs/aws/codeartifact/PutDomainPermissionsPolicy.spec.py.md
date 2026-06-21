---
id: "@specs/aws/codeartifact/domain_policy_put"
target_lang: py
version: 1.0.0
owned-by: codegen
status: active
depends_on: ["@specs/aws/codeartifact/plan"]
---

# PutDomainPermissionsPolicy

Sets a resource policy on a domain.

## Input Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `domain` | DomainName | Yes | Domain name |
| `domainOwner` | AccountId | No | Domain owner account |
| `policyDocument` | PolicyDocument | Yes | IAM policy JSON string |
| `policyRevision` | PolicyRevision | No | Revision for optimistic locking |

## Implementation

```speclang
@dataclass
@kind: operation
def execute_put_domain_permissions_policy(store, request):
    """Sets a resource policy on a domain."""
    domain_name = request.get("domain", "")
    policy_doc = request.get("policyDocument", "")
    if not domain_name:
        raise ValidationException("domain is required")
    if not policy_doc:
        raise ValidationException("policyDocument is required")
    domain = store._get_domain(domain_name)
    store.domain_policies[domain_name] = policy_doc
    return {"policy": {"resourceArn": domain.arn, "document": policy_doc, "revision": str(uuid.uuid4().hex[:8])}}
```
