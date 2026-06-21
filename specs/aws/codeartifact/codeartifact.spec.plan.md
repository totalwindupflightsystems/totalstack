---
id: "@specs/aws/codeartifact/plan"
target_lang: plan
version: 1.0.0
owned-by: specwriter
status: active
depends_on:
  - "@specs/aws/codeartifact/meta"
---

# CodeArtifact Service — Implementation Plan

## Operation Inventory

### Domain Operations (7)
| Operation | Method | Path | Description |
|-----------|--------|------|-------------|
| CreateDomain | POST | /v1/domain | Creates a domain |
| DescribeDomain | GET | /v1/domain | Returns domain info |
| DeleteDomain | DELETE | /v1/domain | Deletes a domain |
| ListDomains | POST | /v1/domains | Lists all domains |
| GetDomainPermissionsPolicy | GET | /v1/domain/permissions-policy | Gets domain policy |
| PutDomainPermissionsPolicy | PUT | /v1/domain/permissions-policy | Sets domain policy |
| DeleteDomainPermissionsPolicy | DELETE | /v1/domain/permissions-policy | Deletes domain policy |

### Repository Operations (7)
| Operation | Method | Path | Description |
|-----------|--------|------|-------------|
| CreateRepository | POST | /v1/repository | Creates a repository |
| DescribeRepository | GET | /v1/repository | Returns repository info |
| UpdateRepository | PUT | /v1/repository | Updates repository config |
| DeleteRepository | DELETE | /v1/repository | Deletes a repository |
| ListRepositories | POST | /v1/repositories | Lists repositories |
| ListRepositoriesInDomain | POST | /v1/repositories/in-domain | Lists repos in a domain |
| GetRepositoryEndpoint | GET | /v1/repository/endpoint | Gets repo endpoint URL |
| GetRepositoryPermissionsPolicy | GET | /v1/repository/permissions-policy | Gets repo policy |
| PutRepositoryPermissionsPolicy | PUT | /v1/repository/permissions-policy | Sets repo policy |
| DeleteRepositoryPermissionsPolicy | DELETE | /v1/repository/permissions-policy | Deletes repo policy |

### Package Operations (5)
| Operation | Method | Path | Description |
|-----------|--------|------|-------------|
| ListPackages | POST | /v1/packages | Lists packages in a repository |
| ListPackageVersions | POST | /v1/package/versions | Lists versions of a package |
| DescribePackageVersion | GET | /v1/package/version | Gets version details |
| GetPackageVersionReadme | GET | /v1/package/version/readme | Gets README for version |

### Authorization (1)
| Operation | Method | Path | Description |
|-----------|--------|------|-------------|
| GetAuthorizationToken | POST | /v1/authorization-token | Gets auth token |

### Tagging (3)
| Operation | Method | Path | Description |
|-----------|--------|------|-------------|
| TagResource | POST | /v1/tag | Tags a resource |
| UntagResource | POST | /v1/untag | Removes tags |
| ListTagsForResource | POST | /v1/tags | Lists tags |

**Total: 23 operations implemented**

## Error Model

All operations can raise:
- `AccessDeniedException` — insufficient permissions
- `ConflictException` — resource conflict (name taken, state conflict)
- `InternalServerException` — unexpected errors
- `ResourceNotFoundException` — referenced resource missing
- `ServiceQuotaExceededException` — quota exceeded
- `ThrottlingException` — rate limit
- `ValidationException` — invalid input

## Store Design

```
CodeArtifactStore
├── domains: dict[name → DomainRecord]
├── domain_policies: dict[name → policy_doc]
├── repositories: dict[(domain, repo) → RepositoryRecord]
├── repo_policies: dict[(domain, repo) → policy_doc]
├── repo_endpoints: dict[(domain, repo) → {format: url}]
├── packages: defaultdict[(domain, repo) → {pkg: info}]
├── package_versions: defaultdict[(domain,repo,pkg,fmt) → {ver: PackageVersionRecord}]
├── package_groups: dict[name → PackageGroupRecord]
└── tags: defaultdict[arn → {key: value}]
```

## Pagination

List operations support `maxResults` (default 100, max 1000) and `nextToken` for pagination. Return format:
```python
{"items": [...], "nextToken": next_token_or_None}
```

## Protocol

JSON over HTTP/HTTPS (rest-json protocol). Service endpoint: `codeartifact.us-east-1.amazonaws.com`
