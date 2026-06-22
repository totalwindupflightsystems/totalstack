---
id: "@specs/aws/opensearchserverless/docs/serverless-machine-learning-unsupported-features"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Unsupported APIs and features"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Unsupported APIs and features

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/serverless-machine-learning-unsupported-features
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Unsupported Machine Learning APIs and features
<a name="serverless-machine-learning-unsupported-features"></a>

## Unsupported APIs
<a name="serverless-unsupported-ml-api"></a>

The following Machine Learning (ML) APIs are not supported on Amazon OpenSearch Serverless:
+ Local Model functionality
+ Model Train API
+ Model Predict algorithm API
+ Model Batch Predict API
+ Agents API
+ MCP Server APIs
+ Memory APIs
+ Controller APIs
+ Execute Algorithm API
+ ML Profile AP
+ ML stats API

For more information about ML APIs, see [ML APIs](https://docs.opensearch.org/latest/ml-commons-plugin/api/index/) on the *OpenSearch Documentation* website.

## Unsupported features
<a name="serverless-unsupported-ml-features"></a>

The following ML features are not supported on Amazon OpenSearch Serverless:
+ Agents and tools
+ Local models
+ The ML Inference processor within Search and Ingest Pipelines
  + ML Inference Ingest Processor
  + ML Inference Search Response Processor
  + ML Inference Search Request Processor

For more information about these features, see the following documentation on the *OpenSearch Documentation* website:
+ [Machine learning](https://docs.opensearch.org/latest/ml-commons-plugin)
+ [ML inference processor](https://docs.opensearch.org/latest/ingest-pipelines/processors/ml-inference/)
+ [Search pipelines](https://docs.opensearch.org/latest/search-plugins/search-pipelines/index/)