---
id: "@specs/aws/glue"
version: 1.0.0
target_lang: meta
status: active
description: AWS Glue service emulation for TotalStack
---

# AWS Glue — Service Specification

## Why Glue

AWS Glue is a serverless data integration service: ETL jobs, Data Catalog (metadata repository), crawlers (schema discovery), and triggers. It's one of the most complex AWS services (265 operations) and is **completely missing** from LocalStack v4.14.0 — no provider, no store, no moto fallback.

## Architecture

Glue has 6 major subsystems:

| Subsystem | Entities | Core Operations |
|-----------|----------|----------------|
| **Data Catalog** | Database, Table, Partition | CreateDatabase, GetDatabase, CreateTable, GetTable |
| **Crawlers** | Crawler, Classifier | CreateCrawler, StartCrawler, GetCrawler |
| **Jobs** | Job, JobRun | CreateJob, StartJobRun, GetJobRun |
| **Triggers** | Trigger | CreateTrigger, StartTrigger |
| **Workflows** | Workflow, Blueprint | CreateWorkflow, StartWorkflow |
| **Connections** | Connection | CreateConnection, GetConnection |

## Design Decisions

1. **In-memory store** with dict-backed collections — same pattern as all TotalStack services
2. **Core CRUD first** — 15-20 operations covering main entities, not all 265
3. **AWS doc-driven** — every handler references the AWS API Reference markdown via `@ref:`
4. **Traceable** — `spec:trace:` annotations link code back to AWS specification sections

> **@ref:** specs/aws/SERVICE-CLASSIFICATION.md — master service strategy
