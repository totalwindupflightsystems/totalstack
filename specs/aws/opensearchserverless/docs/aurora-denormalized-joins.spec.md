---
id: "@specs/aws/opensearchserverless/docs/aurora-denormalized-joins"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Joining data from multiple tables"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Joining data from multiple tables

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/aurora-denormalized-joins
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Joining data from multiple tables to ingest into one document
<a name="aurora-denormalized-joins"></a>

The `joins` configuration in the RDS source plugin enables automatic denormalization of normalized relational tables into single OpenSearch documents. When configured, the pipeline reads change data capture (CDC) events from multiple related tables and merges them into a parent document using Painless script-based upserts.

This topic explains how to configure table joins in Aurora and Amazon RDS ingestion pipelines, including join types, prerequisites, configuration syntax, version tracking, and troubleshooting common issues.

## Prerequisites
<a name="aurora-joins-prerequisites"></a>
+ Basic understanding of relational database concepts including primary keys, foreign keys, and table relationships.
+ Tables with foreign key relationships (parent-child).
+ All tables in `relations` must be listed in `tables.include`.
+ The parent table must have a primary key.
+ Child tables must have a column referencing the parent's primary key.
+ Child tables must have their own primary key (`child_primary_key`) for identifying individual records in upserts.

## Supported join patterns
<a name="aurora-joins-supported-patterns"></a>
+ Parent → Child (1:1)
+ Parent → Child (1:N)
+ Multiple children per parent

## Example configuration
<a name="aurora-joins-configuration"></a>

The following YAML configuration shows how to define parent-child table relationships for the Aurora source plugin. This example configures a parent table with two child tables using different join types:

```
version: "2"
aurora-joins-pipeline:
  source:
    rds:
      db_identifier: "my-aurora-cluster"
      engine: "aurora-mysql"
      database: "my_database"
      tables:
        include:
          - "parent_table"
          - "child_table_1"
          - "child_table_2"
      s3_bucket: "my-pipeline-bucket"
      s3_region: "us-east-1"
      s3_prefix: "rds-export"
      export:
        kms_key_id: "my-kms-key-id"
        iam_role_arn: "arn:aws:iam::123456789012:role/my-export-role"
      stream: true
      aws:
        sts_role_arn: "arn:aws:iam::123456789012:role/my-pipeline-role"
        region: "us-east-1"
      authentication:
        username: ${{aws_secrets:secret:username}}
        password: ${{aws_secrets:secret:password}}
      joins:
        version_field: "__versions"
        relations:
          - parent: "parent_table"
            child: "child_table_1"
            parent_key: "id"
            child_key: "parent_id"
            child_primary_key: "child_id"
            join_type: "one_to_many"
            max_child_records: 100
          - parent: "parent_table"
            child: "child_table_2"
            parent_key: "id"
            child_key: "parent_id"
            child_primary_key: "child_id"
            join_type: "one_to_one"
  sink:
    - opensearch:
        hosts: ["https://search-mydomain.us-east-1.es.amazonaws.com"]
        index: "my-joined-index"
        document_id: "${getMetadata(\"primary_key\")}"
        action: "${getMetadata(\"opensearch_action\")}"
        aws:
          sts_role_arn: "arn:aws:iam::123456789012:role/my-pipeline-role"
          region: "us-east-1"
extension:
  aws:
    secrets:
      secret:
        secret_id: "arn:aws:secretsmanager:us-east-1:123456789012:secret:my-db-secret"
        region: "us-east-1"
        sts_role_arn: "arn:aws:iam::123456789012:role/my-pipeline-role"
        refresh_interval: PT1H
```

## Join types
<a name="aurora-joins-types"></a>

one\_to\_one  
Child fields are flattened at the root level of the parent document. Use when each parent has exactly one related child record.  

```
Parent table: orders (order_id, customer_name, total)
Child table:  shipping (shipping_id, order_id, tracking_number, carrier)

Result document:
{
  "order_id": 1,
  "customer_name": "Alice",
  "total": 299.99,
  "shipping_id": "1",
  "tracking_number": "TRK-1",
  "carrier": "FedEx"
}
```

one\_to\_many  
Child records are stored as a nested array in the parent document. Use when each parent can have multiple related child records.  

```
Parent table: orders (order_id, customer_name, total)
Child table:  order_items (item_id, order_id, product_name, quantity, price)

Result document:
{
  "order_id": 1,
  "customer_name": "Alice",
  "total": 299.99,
  "order_items": [
    {"item_id": 10, "product_name": "Keyboard", "quantity": 1, "price": 149.99},
    {"item_id": 11, "product_name": "Mouse", "quantity": 1, "price": 29.99}
  ]
}
```

## Document structure
<a name="aurora-joins-document-structure"></a>

Document ID  
The OpenSearch document `_id` is set to the value of the parent table's primary key. All child records for the same parent are merged into this single document.

Version tracking  
The `version_field` (default: `__versions`) stores a map of per-table version counters:  

```
"__versions": {
  "orders": 12345678901,
  "order_items": 12345678902,
  "shipping": 12345678903
}
```
Each table's version is derived from the export timestamp or binlog timestamp. When an export or CDC event arrives, the Painless script checks if the incoming version is newer than the stored version for that specific table. If older, the event is skipped. This ensures:  
+ Idempotent processing—replayed events are safely ignored.
+ Independent versioning—an order update doesn't interfere with item updates.
+ Concurrent safety—multiple child inserts for the same parent are handled correctly.

Document \_version  
The OpenSearch `_version` field increments with each successful upsert. For a document with 1 parent \+ N items \+ 1 shipping record, `_version` = N \+ 2.

## Limitations
<a name="aurora-joins-limitations"></a>
+ Single-level joins only—parent → child. Multi-level (parent → child → grandchild) is not supported.
+ One parent table per pipeline. All child tables join to the same parent.
+ Child tables cannot belong to multiple parents in the same pipeline.
+ `max_child_records` limits the array size for `one_to_many` joins. Records beyond this limit are dropped.

**Field name conflicts**  
For `one_to_one` joins, child fields are flattened at the root level. If a child table has a column with the same name as a parent column, the child value overwrites the parent value. Use distinct column names across parent and `one_to_one` child tables.  
For `one_to_many` joins, child fields are nested inside an array named after the child table, so conflicts are not an issue.

## Troubleshooting
<a name="aurora-joins-troubleshooting"></a>

Documents missing child records  
+ Check `__versions` in the document. If a child table's version is missing, the child events haven't been processed yet.
+ Verify the pipeline is active and the `changeEventsProcessed` metric is non-zero.

Documents not appearing in OpenSearch  
+ Check if the parent record exists in the source table.
+ Verify the `tables.include` list contains all required tables.
+ Check pipeline logs for ingestion failures and configuration issues: `/aws/vendedlogs/{{pipeline-log-group}}`.