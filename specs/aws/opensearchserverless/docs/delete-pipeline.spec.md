---
id: "@specs/aws/opensearchserverless/docs/delete-pipeline"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Deleting pipelines"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Deleting pipelines

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/delete-pipeline
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Deleting Amazon OpenSearch Ingestion pipelines
<a name="delete-pipeline"></a>

You can delete an Amazon OpenSearch Ingestion pipeline using the AWS Management Console, the AWS CLI, or the OpenSearch Ingestion API. You can't delete a pipeline when has a status of `Creating` or `Updating`.

## Console
<a name="delete-pipeline-console"></a>

**To delete a pipeline**

1. Sign in to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/osis/home](https://console.aws.amazon.com/aos/osis/home#osis/ingestion-pipelines). You'll be on the Pipelines page.

1. Select the pipeline that you want to delete and choose **Actions**, **Delete**.

1. Confirm deletion and choose **Delete**.

## CLI
<a name="delete-pipeline-cli"></a>

To delete a pipeline using the AWS CLI, send a [delete-pipeline](https://docs.aws.amazon.com/cli/latest/reference/osis/delete-pipeline.html) request:

```
aws osis delete-pipeline --pipeline-name "{{my-pipeline}}"
```

## OpenSearch Ingestion API
<a name="delete-pipeline-api"></a>

To delete an OpenSearch Ingestion pipeline using the OpenSearch Ingestion API, call the [DeletePipeline](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_DeletePipeline.html) operation with the following parameter: 
+ `PipelineName` – the name of the pipeline.