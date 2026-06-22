---
id: "@specs/aws/opensearchserverless/docs/pipeline--stop"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Stopping a pipeline"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Stopping a pipeline

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/pipeline--stop
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Stopping an Amazon OpenSearch Ingestion pipeline
<a name="pipeline--stop"></a>

To use an OpenSearch Ingestion pipeline or perform administration, you always begin with an active pipeline, then stop the pipeline, and then start the pipeline again. While your pipeline is stopped, you're not charged for Ingestion OCU hours.

## Console
<a name="stop-pipeline-console"></a>

**To stop a pipeline**

1. Sign in to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/osis/home](https://console.aws.amazon.com/aos/osis/home#osis/ingestion-pipelines). You'll be on the Pipelines page.

1. Choose a pipeline. You can perform the stop operation from this page, or navigate to the details page for the pipeline that you want to stop.

1. For **Actions**, choose **Stop pipeline**.

   If a pipeline can't be stopped and started, the **Stop pipeline** action isn't available.

## AWS CLI
<a name="stop-pipeline-cli"></a>

To stop a pipeline using the AWS CLI, call the [stop-pipeline](https://docs.aws.amazon.com/cli/latest/reference/osis/stop-pipeline.html) command with the following parameters: 
+ `--pipeline-name` – the name of the pipeline. 

**Example**  

```
aws osis stop-pipeline --pipeline-name {{my-pipeline}}
```

## OpenSearch Ingestion API
<a name="stop-pipeline-api"></a>

To stop a pipeline using the OpenSearch Ingestion API, call the [StopPipeline](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_StopPipeline.html) operation with the following parameter: 
+ `PipelineName` – the name of the pipeline. 