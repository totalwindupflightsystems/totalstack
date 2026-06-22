---
id: "@specs/aws/opensearchserverless/docs/auto-optimize-console"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Using auto-optimize in the console"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Using auto-optimize in the console

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/auto-optimize-console
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Using auto-optimize in the console
<a name="auto-optimize-console"></a>

You can use the Amazon OpenSearch Service console to create vector ingestion jobs, monitor their progress, view optimization recommendations, and build indexes based on those recommendations.

## Prerequisites
<a name="auto-optimize-console-prerequisites"></a>

Before you can use auto-optimize in the console, you must have the following:
+ An active AWS account with access to the OpenSearch console.
+ An existing OpenSearch Serverless collection of type *vector search* or a Managed OpenSearch domain.
+ IAM permissions for the following actions:
  + `opensearch:SubmitAutoOptimizeJob`
  + `opensearch:GetAutoOptimizeJob`
  + `opensearch:DeleteAutoOptimizeJob`
  + `opensearch:CancelAutoOptimizeJob`
  + `opensearch:ListAutoOptimizeJobs`
**Note**  
These are identity-based policies. AWS does not support resource-based policies for auto-optimize resources.
+ Configure your federated user session to have a minimum credential expiry of at least 1 hour. For very large datasets or high dimensions, consider increasing the expiration duration up to 3 hours.

## Creating a vector ingestion job
<a name="auto-optimize-console-create-job"></a>

A vector ingestion job analyzes your vector data and provides optimization recommendations for index configuration.

**To create a vector ingestion job**

1. Sign in to the Amazon OpenSearch Service console at [AWS Management Console](https://console.aws.amazon.com/aos/home).

1. In the navigation pane, choose **Auto-Optimize**.

1. Choose **Create vector ingestion job**.

1. Under **Job details**, enter a name for your vector ingestion job. This name helps you identify the job in the console.

1. Under **Data source**, configure the following:

   1. For **Amazon S3 URI**, enter the Amazon S3 URI of the folder containing your data files (Parquet or JSONL). The URI must point to the enclosing folder, not individual files. For example, if your file is at `s3://my-bucket/my-folder/file1.parquet` or `s3://my-bucket/my-folder/data.jsonl`, enter `s3://my-bucket/my-folder/`.
**Note**  
The folder must contain files of a single format. Do not mix Parquet and JSONL files in the same folder.

   1. For **Region**, select the AWS Region where your Amazon S3 bucket is located. The Region must match the bucket location.

1. Under **OpenSearch domain**, select an existing domain or collection, or choose **Create new** to create one.
**Note**  
You can specify either an OpenSearch Managed domain or an OpenSearch Serverless serverless collection.

1. Under **Data source permissions**, specify the IAM role that has permissions to access your Amazon S3 bucket and OpenSearch domain or collection. The role must have the necessary permissions based on your domain or collection configuration:
   + For OpenSearch domains with a domain access policy, grant the role access through that policy.
   + For OpenSearch domains with fine-grained access control, add the role as a backend role.
   + For OpenSearch Serverless collections, add the role to the data access policy.

1. Choose **Next**.

1. Under **Configure index**, specify the following:

   1. For **Field name**, enter the field name from your dataset that contains the vector data.

   1. For **Space type**, select the distance metric used to calculate the distance between vectors:
      + **l2** - Euclidean distance
      + **cosinesimil** - Cosine similarity
      + **innerproduct** - Inner product

   1. For **Dimension**, enter the number of floating point values in each vector.

1. Under **Performance requirements**, configure the following:

   1. For **Recall**, specify your desired search quality as a decimal value between 0 and 1. Higher recall values return more relevant results. For example:
      + 0.95 indicates that on average 19 of the 20 true nearest document vectors to a query vector are returned
      + 0.9 indicates 9 in 10
      + 0.8 indicates 8 in 10

   1. For **Search latency requirements**, select your latency tolerance. Modest requirements allow for more cost savings through compression methods that decrease memory requirements.

1. Choose **Next**.

1. Review your configuration and choose **Create**.

The job begins processing. You can monitor its progress in the **Vector Ingestion Jobs** table.

## Monitoring optimization jobs
<a name="auto-optimize-console-monitor"></a>

You can monitor the status of your vector ingestion jobs from the auto-optimize landing page.

**To monitor optimization jobs**

1. Sign in to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home).

1. In the navigation pane, choose **Auto-optimize**.

1. The **Vector Ingestion Jobs** table displays all jobs with their current status. Refresh the page to see updated status information.
**Note**  
There is no automatic refresh or notification mechanism. You must manually refresh the console to see when a job completes.

### Understanding job status states
<a name="auto-optimize-console-job-status"></a>

Auto-optimize jobs can have the following status values:

Pending  
The job is queued and waiting to start.

Running  
The auto-optimize job is actively analyzing your data and generating recommendations.

Completed  
The auto-optimize job has finished successfully. All analysis, evaluation, and recommendations are complete and available for viewing.

Failed  
The job encountered an error. View the error details in the job details page to determine the cause.

Active  
An index has been created in the attached cluster and data has been ingested.

Job duration depends primarily on dataset size and current service load. Typical jobs complete within 15 minutes to several hours.

## Viewing job details
<a name="auto-optimize-console-view-details"></a>

You can view detailed information about a specific optimization job, including its configuration and status.

**To view job details**

1. Sign in to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home).

1. In the navigation pane, choose **Auto-Optimize**.

1. In the **Vector Ingestion Jobs** table, choose the job name.

1. The job details page displays the following information:
   + Job name and status
   + Data source configuration (Amazon S3 URI and Region)
   + OpenSearch domain or collection
   + Index configuration (field name, space type, dimension)
   + Performance requirements (recall and latency)
   + Error messages (if the job failed)

## Viewing and understanding results
<a name="auto-optimize-console-view-results"></a>

After a job completes successfully, you can view the optimization recommendations.

**To view optimization results**

1. Sign in to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home).

1. In the navigation pane, choose **Auto-Optimize**.

1. In the **Vector Ingestion Jobs** table, choose a job with **Completed** status.

1. The results page displays the following sections:
   + **Results overview** - Shows the estimated search quality recall compared to your requirement and the index memory footprint compared to the top recommended configuration.
   + **Recommendations** - Lists up to three optimization recommendations, ordered with the top recommendation as the best match for your configuration. Each recommendation includes:
     + Index configuration parameters
     + Search configuration parameters
     + Expected performance metrics
     + Memory footprint estimates
**Note**  
While recommendations are ordered by best match, you can select any recommendation that better fits your specific use case. Auto-optimize attempts to find the closest matches to your chosen recall criteria.

## Building an index from recommendations
<a name="auto-optimize-console-build-index"></a>

After reviewing the optimization recommendations, you can either manually create an index using the recommended configuration or automatically build an index with the selected recommendation.

**To build an index automatically**

1. Sign in to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home).

1. In the navigation pane, choose **Auto-Optimize**.

1. In the **Vector Ingestion Jobs** table, choose a job with **Completed** status.

1. Review the recommendations and select the one you want to use.

1. Choose **Build index**.

1. The system automatically creates an index in your cluster using the selected recommendation and ingests the vector data from your dataset.

**To build an index manually**

1. Sign in to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home).

1. In the navigation pane, choose **Auto-Optimize**.

1. In the **Vector Ingestion Jobs** table, choose a job with **Completed** status.

1. Review the recommendations and note the index configuration and search configuration parameters for your chosen recommendation.

1. Use the OpenSearch API or console to manually create an index with the recommended parameters.