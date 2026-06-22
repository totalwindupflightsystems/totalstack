---
id: "@specs/aws/opensearchserverless/docs/pipeline-blueprint"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Working with blueprints"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Working with blueprints

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/pipeline-blueprint
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Working with blueprints
<a name="pipeline-blueprint"></a>

Rather than creating a pipeline definition from scratch, you can use *configuration blueprints*, which are preconfigured templates for common ingestion scenarios such as Trace Analytics or Apache logs. Configuration blueprints help you easily provision pipelines without having to author a configuration from scratch. 

## Console
<a name="pipeline-blueprint-console"></a>

**To use a pipeline blueprint**

1. Sign in to the OpenSearch Ingestion console at [https://console.aws.amazon.com/aos/osis/home](https://console.aws.amazon.com/aos/osis/home#osis/ingestion-pipelines). You'll be on the Pipelines page.

1. Choose **Create pipeline**.

1. Select a blueprint from the list of use cases, then choose **Select blueprint**. The pipeline configuration populates with a sub-pipeline for the use case you selected. 

   The pipeline blueprint isn't valid as-is. You need to specify additional settings depending on the selected source.

## CLI
<a name="pipeline-blueprint-cli"></a>

To get a list of all available blueprints using the AWS CLI, send a [list-pipeline-blueprints](https://docs.aws.amazon.com/cli/latest/reference/osis/list-pipeline-blueprints.html) request.

```
aws osis list-pipeline-blueprints{{ }}
```

The request returns a list of all available blueprints.

To get more detailed information about a specific blueprint, use the [get-pipeline-blueprint](https://docs.aws.amazon.com/cli/latest/reference/osis/get-pipeline-blueprint.html) command:

```
aws osis get-pipeline-blueprint --blueprint-name {{AWS-ApacheLogPipeline}}
```

This request returns the contents of the Apache log pipeline blueprint:

```
{
   "Blueprint":{
      "PipelineConfigurationBody":"###\n  # Limitations: https://docs.aws.amazon.com/opensearch-service/latest/ingestion/ingestion.html#ingestion-limitations\n###\n###\n  # apache-log-pipeline:\n    # This pipeline receives logs via http (e.g. FluentBit), extracts important values from the logs by matching\n    # the value in the 'log' key against the grok common Apache log pattern. The grokked logs are then sent\n    # to OpenSearch to an index named 'logs'\n###\n\nversion: \"2\"\napache-log-pipeline:\n  source:\n    http:\n      # Provide the path for ingestion. ${pipelineName} will be replaced with pipeline name configured for this pipeline.\n      # In this case it would be \"/apache-log-pipeline/logs\". This will be the FluentBit output URI value.\n      path: \"/${pipelineName}/logs\"\n  processor:\n    - grok:\n        match:\n          log: [ \"%{COMMONAPACHELOG_DATATYPED}\" ]\n  sink:\n    - opensearch:\n        # Provide an AWS OpenSearch Service domain endpoint\n        # hosts: [ \"https://search-mydomain-1a2a3a4a5a6a7a8a9a0a9a8a7a.us-east-1.es.amazonaws.com\" ]\n        aws:\n          # Provide the region of the domain.\n          # region: \"us-east-1\"\n          # Enable the 'serverless' flag if the sink is an Amazon OpenSearch Serverless collection\n          # serverless: true\n        index: \"logs\"\n        # Enable the S3 DLQ to capture any failed requests in an S3 bucket\n        # dlq:\n          # s3:\n            # Provide an S3 bucket\n            # bucket: \"your-dlq-bucket-name\"\n            # Provide a key path prefix for the failed requests\n            # key_path_prefix: \"${pipelineName}/logs/dlq\"\n            # Provide the region of the bucket.\n            # region: \"us-east-1\"\n            # Provide a Role ARN with access to the bucket. This role should have a trust relationship with osis-pipelines.amazonaws.com\n"
      "BlueprintName":"AWS-ApacheLogPipeline"
   }
}
```

## OpenSearch Ingestion API
<a name="pipeline-blueprint-api"></a>

To get information about pipeline blueprints using the OpenSearch Ingestion API, use the [ListPipelineBlueprints](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_ListPipelineBlueprints.html) and [GetPipelineBlueprint](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_GetPipelineBlueprint.html) operations.