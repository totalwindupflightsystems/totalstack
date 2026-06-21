---
id: "@specs/aws/athena/plan"
version: 1.0.0
target_lang: plan
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/athena"
---

# AWS Athena — Implementation Plan

## Operations Inventory (70 total, 25 core implemented)

### DataCatalogs (5 ops)
| Operation | HTTP | Core? |
|-----------|------|-------|
| CreateDataCatalog | POST / | ✓ |
| GetDataCatalog | POST / | ✓ |
| ListDataCatalogs | POST / | ✓ |
| UpdateDataCatalog | POST / | ✓ |
| DeleteDataCatalog | POST / | ✓ |

### WorkGroups (5 ops)
| Operation | HTTP | Core? |
|-----------|------|-------|
| CreateWorkGroup | POST / | ✓ |
| GetWorkGroup | POST / | ✓ |
| ListWorkGroups | POST / | ✓ |
| UpdateWorkGroup | POST / | ✓ |
| DeleteWorkGroup | POST / | ✓ |

### NamedQueries (6 ops)
| Operation | HTTP | Core? |
|-----------|------|-------|
| CreateNamedQuery | POST / | ✓ |
| GetNamedQuery | POST / | ✓ |
| ListNamedQueries | POST / | ✓ |
| UpdateNamedQuery | POST / | ✓ |
| DeleteNamedQuery | POST / | ✓ |
| BatchGetNamedQuery | POST / | ✓ |

### QueryExecutions (5 ops)
| Operation | HTTP | Core? |
|-----------|------|-------|
| StartQueryExecution | POST / | ✓ |
| GetQueryExecution | POST / | ✓ |
| StopQueryExecution | POST / | ✓ |
| GetQueryResults | POST / | ✓ |
| ListQueryExecutions | POST / | ✓ |
| BatchGetQueryExecution | POST / | ✓ |
| GetQueryRuntimeStatistics | POST / | — skip |

### PreparedStatements (5 ops)
| Operation | HTTP | Core? |
|-----------|------|-------|
| CreatePreparedStatement | POST / | ✓ |
| GetPreparedStatement | POST / | ✓ |
| ListPreparedStatements | POST / | ✓ |
| UpdatePreparedStatement | POST / | ✓ |
| DeletePreparedStatement | POST / | ✓ |
| BatchGetPreparedStatement | POST / | — skip |

### Databases & Tables (4 ops)
| Operation | HTTP | Core? |
|-----------|------|-------|
| GetDatabase | POST / | ✓ |
| ListDatabases | POST / | ✓ |
| GetTableMetadata | POST / | ✓ |
| ListTableMetadata | POST / | ✓ |

### Tags (3 ops)
| Operation | HTTP | Core? |
|-----------|------|-------|
| TagResource | POST / | ✓ |
| UntagResource | POST / | ✓ |
| ListTagsForResource | POST / | ✓ |

### Skipped (notebooks, capacity, sessions, calculations = 37 ops)
CancelCapacityReservation, CreateCapacityReservation, CreateNotebook, CreatePresignedNotebookUrl,
DeleteNotebook, ExportNotebook, GetCalculationExecution, GetCalculationExecutionCode,
GetCalculationExecutionStatus, GetCapacityAssignmentConfiguration, GetCapacityReservation,
GetNotebookMetadata, GetResourceDashboard, GetSession, GetSessionEndpoint, GetSessionStatus,
ImportNotebook, ListApplicationDPUSizes, ListCalculationExecutions, ListCapacityReservations,
ListEngineVersions, ListExecutors, ListNotebookMetadata, ListNotebookSessions, ListSessions,
PutCapacityAssignmentConfiguration, StartCalculationExecution, StartSession,
StopCalculationExecution, TerminateSession, UpdateCapacityReservation, UpdateNotebook,
UpdateNotebookMetadata

## Store Design

```python
class AthenaStore:
    """Dict-backed store for all Athena resources."""
    def __init__(self):
        self.data_catalogs = {}
        self.work_groups = {}
        self.named_queries = {}
        self.prepared_statements = {}  # keyed by (workgroup, statement_name)
        self.query_executions = {}
        self.databases = {}  # keyed by (catalog, db_name)
        self.table_metadata = {}  # keyed by (catalog, db, table_name)
        self.tags = {}  # keyed by resource ARN
```

## Error Model

| Error Code | HTTP | Meaning |
|-----------|------|---------|
| InvalidRequestException | 400 | Bad request, missing fields, duplicate names |
| ResourceNotFoundException | 404 | Named resource not found |
| InternalServerException | 500 | Server error |

## Implementation Approach

1. **Store-first**: Build AthenaStore with all resource collections
2. **Handler-per-operation**: Each .spec.py.md defines one handler function
3. **Validation**: Required field checks, name format validation
4. **ARN generation**: Construct ARNs for resources that AWS identifies by ARN
5. **WorkGroup scoping**: PreparedStatements keyed by (workgroup, name)

## Verification

Integration tests will verify:
- Create → Get → List → Update → Delete lifecycle for each resource type
- Error path: missing required fields, duplicate names, nonexistent resources
- WorkGroup scoping: PreparedStatements isolated per workgroup
- Tag operations: Tag/Untag/ListTags on all resource types
