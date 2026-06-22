---
id: "@specs/aws/opensearchserverless/docs/view-vector-ingestion-jobs"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS View vector ingestion jobs and import history"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# View vector ingestion jobs and import history

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/view-vector-ingestion-jobs
> **target_lang:** meta — documentation tier. ALL sections preserved.



# View vector ingestion jobs and import history
<a name="view-vector-ingestion-jobs"></a>

Vector ingestion jobs create a pipeline for vectorizing data sets, automating vector index tuning and accelerating large-scale index builds.

**To view vector ingestion jobs**

1. In the **Vector ingestion jobs** section, view the summary information:
   + **Jobs** - Total number of ingestion jobs
   + Choose **Create vector database** to create a new ingestion job

1. In the **Amazon S3 vectors imports** section, view the import summary:
   + **Total imports** - Number of completed imports
   + Choose **Import Amazon S3 vectors** to start a new import

1. In the **Vector ingestion jobs** table, monitor active jobs with the following information:
   + **Name** - The job name
   + **Status** - Current job status (e.g., Active)
   + **Data source** - Source location (e.g., s3://location)
   + **Destination** - Target destination
   + **Last updated** - Most recent update timestamp

1. Use the search box to **Find vector ingestion job** to locate specific jobs.

1. To manage jobs, choose from the following actions:
   + Choose **Delete** to remove selected jobs
   + Choose **Create vector database** to create additional jobs

1. In the **Amazon S3 vectors import history** section, track import events:

   1. Use the **Date range** filter to specify a time period for import history.

   1. Use the **Status** dropdown to filter by import status (e.g., Any status).

   1. Use the search box to **Find imports by Amazon S3 vector index na...** to locate specific imports.

   1. View import details including:
      + **Import initiated on (UTC\+5:30)** - When the import started
      + **Import status** - Current status (In progress, Complete, Failed, Partially complete)
      + **Amazon S3 vector index ARN** - Source index identifier
      + **OpenSearch Service vector collection** - Destination collection

1. Choose **Import Amazon S3 vector** to start a new import process.