---
id: "@specs/aws/neptune/meta"
version: 1.0.0
target_lang: meta
owned-by: specwriter
status: active
depends_on:
  - "@specs/aws/neptune/plan"
---

# Amazon Neptune — Meta Specification

## Why
Amazon Neptune is a fully managed graph database service that supports both Property Graph (Gremlin/openCypher) and RDF/SPARQL query models. As one of AWS's specialized database services, it uses the RDS-family API surface (Query protocol, `rds` endpoint prefix) for cluster and instance management.

## Service Overview
Neptune provides:
- **DB Clusters**: The primary graph database resource containing one or more instances
- **DB Instances**: Compute nodes within a cluster (writer + read replicas)
- **Parameter Groups**: Cluster-level and instance-level configuration
- **Snapshots**: Backups for point-in-time recovery
- **Subnet Groups**: VPC network configuration
- **Custom Endpoints**: Reader endpoint routing
- **Global Clusters**: Multi-region disaster recovery
- **Event Subscriptions**: SNS notification for operational events

## API Surface
- **70 total operations** in botocore service-2.json
- **Protocol**: Query (RDS-family)
- **Endpoint prefix**: rds
- **Core entities**: 9 distinct resource types

## Implementation Status
- **28 core CRUD handlers** implemented (Phase 1)
- **42 remaining operations** deferred (tagging variants, event management, global cluster operations, copy/restore, describe-variants)
- **Integration tests**: 38/38 passing against real NeptuneStore
- **E2E tests**: 3 written, skipped pending provider wiring

## Design Philosophy
- Real in-memory store (NeptuneStore) with case-insensitive lookups
- Per-entity exception classes matching AWS error codes
- Handlers follow the standard pattern: validate → store operation → response
- Store methods raise typed exceptions; handlers translate AWS request shapes
