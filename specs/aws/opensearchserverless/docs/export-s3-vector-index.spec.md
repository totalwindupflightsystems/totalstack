---
id: "@specs/aws/opensearchserverless/docs/export-s3-vector-index"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Export Amazon S3 vector index to OpenSearch Service vector engine"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Export Amazon S3 vector index to OpenSearch Service vector engine

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/export-s3-vector-index
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Export Amazon S3 vector index to OpenSearch Service vector engine
<a name="export-s3-vector-index"></a>

A point-in-time export for your selected Amazon S3 vector index to OpenSearch Service. The OpenSearch Service vector engine provides a simple and scalable vector store with advanced search functionality.

**To export Amazon S3 vector index to OpenSearch Service vector engine**

1. In the **Source** section, verify the Amazon S3 vector index details:
   + **Amazon S3 vector index** - The name of your source index
   + **Amazon S3 vector index ARN** - The Amazon Resource Name of your index

1. In the **Service access** section, configure OpenSearch Service authorization:

   1. For **Choose a method to authorize OpenSearch Service**, select one of the following:
      + **Create and use a new service role**
      + **Use an existing service role**

   1. For **Service role name**, enter a name for the service role.
**Note**  
Service role name must be 1 to 64 characters. Valid characters are a-z, A-Z, 0-9, and periods (.).

   1. Choose **View permission details** to review the required permissions.

1. Expand **Additional settings - optional** to configure advanced options if needed.

1. In the **Export details** section, configure the following options:
   + **Automate OpenSearch Service vector collection creation** - OpenSearch Service collections are used to store vector data. Serverless compute capacity is measured in OpenSearch Service Compute Units (OCUs), by default the Max OCU capacity is 50.
   + **Automate IAM role creation for service access** - This role is used by OpenSearch Service to read the Amazon S3 vector index and write to the OpenSearch Service collection.
   + **Automate OpenSearch Service ingestion pipeline creation** - OpenSearch Service ingestion pipelines are used to ingest data. An Amazon S3 bucket is created as a best practice to capture and store failed events in an Amazon S3 bucket Dead Letter Queue (DLQ), enabling easy access for troubleshooting and analysis.

1. Choose **Export** to start the export process, or choose **Cancel** to exit without exporting.