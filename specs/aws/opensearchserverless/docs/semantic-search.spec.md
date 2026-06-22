---
id: "@specs/aws/opensearchserverless/docs/semantic-search"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Semantic search"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Semantic search

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/semantic-search
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Semantic search in Amazon OpenSearch Service
<a name="semantic-search"></a>

Starting with version 2.19, you can use automatic semantic enrichment to implement semantic search with minimal configuration effort. This feature automatically generates sparse encoding for your text fields, eliminating the need for manual ingestion pipeline setup. For details, see [Automatic Semantic Enrichment](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/opensearch-semantic-enrichment.html) in the OpenSearch documentation.

Starting with OpenSearch version 2.9, you can use semantic search to help you understand search queries and improve search relevance. You can use semantic search in one of two ways – with [neural search](https://opensearch.org/docs/latest/search-plugins/neural-search/) and with [k-Nearest Neighbor (k-NN)](https://opensearch.org/docs/latest/search-plugins/knn/index/) search.

With OpenSearch Service, you can set up [AI connectors for AWS services](ml-amazon-connector.md) and [external services](ml-external-connector.md). Using the console, you can also create an ML model with a CloudFormation template. For more information, see [Using CloudFormation to set up remote inference for semantic search](cfn-template.md).

For full documentation of semantic search, including a step-by-step guide to use semantic search, see [Semantic search](https://opensearch.org/docs/latest/search-plugins/semantic-search/) in the open source OpenSearch documentation.