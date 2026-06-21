---
id: "@specs/aws/rds/plan"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
---

# RDS Plan — Amazon Relational Database Service

## Service Overview

RDS is AWS's managed relational database service supporting MySQL, PostgreSQL, MariaDB, Oracle, and SQL Server engines. TotalStack emulates the RDS management plane (create/describe/modify/delete instances, clusters, snapshots, parameter groups, subnet groups) plus the data plane proxy (running a local database engine for testing).

## Architecture

```
Client (boto3) → RDS API handler → RDSStore → local MySQL/PostgreSQL (optional)
```

## Core Entities

| Entity | Operations | Store |
|--------|-----------|-------|
| DBInstance | Create, Describe, Modify, Delete, Reboot | self._instances: dict |
| DBCluster | Create, Describe, Modify, Delete | self._clusters: dict |
| DBSnapshot | Create, Describe, Delete, Copy | self._snapshots: dict |
| DBParameterGroup | Create, Describe, Modify, Delete | self._param_groups: dict |
| DBSubnetGroup | Create, Describe, Delete | self._subnet_groups: dict |
| DBClusterParameterGroup | Create, Describe, Delete | self._cluster_param_groups: dict |

## Error Model

- DBInstanceNotFoundFault
- DBClusterNotFoundFault  
- DBSnapshotNotFoundFault
- DBParameterGroupNotFoundFault
- DBSubnetGroupNotFoundFault
- InvalidParameterException
- ResourceNotFoundException

## Operation Inventory

See individual handler specs in specs/aws/rds/handler-*.spec.py.md
