---
id: "@specs/aws/glue/plan"
version: 1.0.0
target_lang: plan
status: active
depends_on:
  - "@specs/aws/glue"
---

# Glue Implementation Plan

## Phase 1: Core CRUD (this session)

15 operations covering 5 entities:

| Entity | Create | Read | List | Update | Delete |
|--------|--------|------|------|--------|--------|
| Database | CreateDatabase | GetDatabase | GetDatabases | UpdateDatabase | DeleteDatabase |
| Table | CreateTable | GetTable | GetTables | UpdateTable | DeleteTable |
| Job | CreateJob | GetJob | GetJobs | — | DeleteJob |
| Crawler | CreateCrawler | GetCrawler | GetCrawlers | — | DeleteCrawler |
| Trigger | CreateTrigger | GetTrigger | GetTriggers | — | DeleteTrigger |

## Store Design

Single `GlueStore` class with `_databases`, `_tables`, `_jobs`, `_crawlers`, `_triggers` dicts.
Each entity gets a `@dataclass` Record class with AWS fields.

## Error Model

- `EntityNotFoundException` — resource not found
- `AlreadyExistsException` — duplicate creation
- `InvalidInputException` — bad parameters
- `ConcurrentModificationException` — stale version

## Spec Structure

Each handler spec follows the TotalStack pattern:
- YAML frontmatter with `depends_on` + `target_lang: py`
- `@ref:` directive to AWS API Reference markdown doc
- ` ```speclang` code block with handler implementation
- `spec:trace:` annotations

## Integration Test Plan

One test class per entity. Happy path + error path per operation.
Total expected: ~25 tests (15 happy path + 10 error path).
