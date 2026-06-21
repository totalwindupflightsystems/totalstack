---
id: "@specs/aws/athena"
version: 1.0.0
target_lang: meta
owned-by: hermes
status: active
---

# AWS Athena Service — Meta Spec

## Why Athena

Amazon Athena is a serverless interactive query service that makes it easy to analyze
data in Amazon S3 using standard SQL. Key capabilities:

- **Serverless SQL**: Run SQL queries on S3 data without managing infrastructure
- **Workgroups**: Isolate queries, enforce cost controls, and manage per-user limits
- **Named Queries**: Save and reuse SQL queries across sessions
- **Data Catalogs**: Connect to external metadata stores (Glue, Hive, federated)
- **Prepared Statements**: Parameterized SQL for efficient repeated execution
- **Federated Queries**: Query data across multiple sources through connectors

## Service Architecture

```
┌──────────────┐     ┌───────────────┐     ┌──────────────┐
│  Console/CLI  │────▶│  Athena API   │────▶│  Query Engine │
│  (users)      │     │  (JSON/REST)  │     │  (Presto/Trino)│
└──────────────┘     └───────┬───────┘     └──────┬───────┘
                             │                     │
                    ┌────────▼───────┐     ┌───────▼───────┐
                    │  WorkGroup     │     │  S3 Buckets   │
                    │  (isolation)   │     │  (data lake)   │
                    └────────────────┘     └───────────────┘
```

## Resource Model

| Resource | Key | Operations |
|----------|-----|-----------|
| DataCatalog | Name | Create, Get, List, Update, Delete |
| WorkGroup | Name | Create, Get, List, Update, Delete |
| NamedQuery | NamedQueryId | Create, Get, List, Update, Delete, BatchGet |
| PreparedStatement | StatementName (scoped to WorkGroup) | Create, Get, List, Update, Delete, BatchGet |
| QueryExecution | QueryExecutionId | Start, Get, Stop, List, BatchGet, GetQueryResults |
| Database | (catalog + name) | Get, List |
| Table | (catalog + database + name) | GetTableMetadata, ListTableMetadata |
| Tags | (resource ARN) | TagResource, UntagResource, ListTagsForResource |

## Protocol

Athena uses the AWS JSON protocol. All operations are HTTP POST to `/`.

## Design Decisions

1. **Greenfield store**: Athena has no existing store in LocalStack v4.14.0. We build a custom `AthenaStore` with dict-backed storage for all resource types.
2. **WorkGroup scoping**: NamedQueries and PreparedStatements are scoped to WorkGroups. The store tracks this relationship.
3. **Query results**: QueryExecution results are stored as JSON in the store (no real S3 backend needed for emulation).
4. **DataCatalog metadata**: Catalogs reference Glue databases/tables via metadata descriptors.

## Success Criteria

- All CRUD operations for DataCatalogs, WorkGroups, NamedQueries complete
- QueryExecution lifecycle: Start → Running → Succeeded/Failed → Results retrievable
- PreparedStatement CRUD with workgroup scoping
- Tag management on all resources
- Integration tests against AthenaStore pass
