---
id: "@specs/aws/quicksight/meta"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
status: active
depends_on: []
---

# QuickSight — Business Intelligence Service

Amazon QuickSight is a scalable, serverless, embeddable, machine learning-powered business
intelligence (BI) service built for the cloud.

## Architecture

```
┌─────────────────────────────────────────────────────┐
│                    QuickSight                        │
├─────────────────────────────────────────────────────┤
│  DataSet    DataSource    Dashboard    Analysis      │
│  (SPICE)    (Athena/S3)   (Visuals)   (Exploration)  │
├─────────────────────────────────────────────────────┤
│  Tags (resource-level), Namespace (multi-tenancy)    │
└─────────────────────────────────────────────────────┘
```

## Entity Inventory

| Entity | Created By | Key Fields | Status |
|--------|-----------|------------|--------|
| DataSet | CreateDataSet | DataSetId, Name, PhysicalTableMap, ImportMode | ✅ built |
| DataSource | CreateDataSource | DataSourceId, Name, Type | ✅ built |
| Dashboard | CreateDashboard | DashboardId, Name | ✅ built |
| Analysis | CreateAnalysis | AnalysisId, Name | ✅ built |

## Test Coverage

| Entity | Integration | E2E |
|--------|------------|-----|
| DataSet | 7 tests (create×2, describe×2, update, delete, list) | 4 tests (skip) |
| DataSource | 7 tests | included in E2E suite |
| Dashboard | 7 tests | included in E2E suite |
| Analysis | 7 tests | included in E2E suite |
| Tags | 5 tests (tag, untag, list, missing-arn×2) | included in E2E suite |
| **Total** | **33 integration tests** | **4 E2E tests** |

## Deferred (future pass)

- 205 additional operations (Template, Theme, Folder, Group, User, Namespace, etc.)
- Ingestion management
- Asset bundle import/export
- Embedding URL generation
- Q topic management
- SPICE capacity configuration
- Account customization/subscription
