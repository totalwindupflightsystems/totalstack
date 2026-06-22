---
id: "@specs/aws/opensearchserverless/docs/opensearch-semantic-enrichment"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Automatic semantic enrichment"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Automatic semantic enrichment

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/opensearch-semantic-enrichment
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Automatic semantic enrichment for Amazon OpenSearch Service
<a name="opensearch-semantic-enrichment"></a>

## Introduction
<a name="semantic-enrichment-intro"></a>

Amazon OpenSearch Service uses word-to-word matching (lexical search) to find results, similar to other traditional search engines. This approach works well for specific queries like product codes or model numbers, but struggles with abstract searches where understanding user intent becomes crucial. For example, when you search for "shoes for the beach," lexical search matches individual words "shoes," "beach," "for," and "the" in catalog items, potentially missing relevant products like "water-resistant sandals" or "surf footwear" that don't contain the exact search terms.

Automatic Semantic Enrichment solves this limitation by considering both keyword matches and the contextual meaning behind searches. This feature understands search intent and improves search relevance by up to 20%. Enable this feature for text fields in your index to enhance search results.

**Note**  
Automatic semantic enrichment is available for OpenSearch Service domains running version 2.19 or later. Additionally, domains with OpenSearch version 2.19 also need to be on the latest service software version update. Currently, feature is available for public domains, and VPC domains are not supported.

## Model details and performance benchmark
<a name="semantic-enrichment-model-detail"></a>

 While this feature handles the technical complexities behind the scenes without exposing the underlying model, we provide transparency through a brief model description and benchmark results to help you make informed decisions about feature adoption in your critical workloads.

 Automatic semantic enrichment uses a service-managed, pre-trained sparse model that works effectively without requiring custom fine-tuning. The model analyzes the fields you specify, expanding them into sparse vectors based on learned associations from diverse training data. The expanded terms and their significance weights are stored in native Lucene index format for efficient retrieval. We’ve optimized this process using [document-only mode,](https://docs.opensearch.org/docs/latest/vector-search/ai-search/neural-sparse-with-pipelines/#step-1a-choose-the-search-mode) where encoding happens only during data ingestion. Search queries are merely tokenized rather than processed through the sparse model, making the solution both cost-effective and performant. 

 Our performance validation during feature development used the [MS MARCO](https://huggingface.co/datasets/BeIR/msmarco) passage retrieval dataset, featuring passages averaging 334 characters. For relevance scoring, we measured average Normalized Discounted Cumulative Gain (NDCG) for the first 10 search results (ndcg@10) on the [BEIR](https://github.com/beir-cellar/beir) benchmark for English content and average ndcg@10 on MIRACL for multilingual content. We assessed latency through client-side, 90th-percentile (p90) measurements and search response p90 [took values.](https://github.com/beir-cellar/beir) These benchmarks provide baseline performance indicators for both search relevance and response times. Here are the key benchmark numbers - 
+ English language - Relevance improvement of 20% over lexical search. It also lowered P90 search latency by 7.7% over lexical search (BM25 is 26 ms, and automatic semantic enrichment is 24 ms).
+ Multi-lingual - Relevance improvement of 105% over lexical search, whereas P90 search latency increased by 38.4% over lexical search (BM25 is 26 ms, and automatic semantic enrichment is 36 ms).

Given the unique nature of each workload, we encourage you to evaluate this feature in your development environment using your own benchmarking criteria before making implementation decisions.

## Languages Supported
<a name="semantic-enrichment-languages"></a>

The feature supports English. In addition, the model also supports Arabic, Bengali, Chinese, Finnish, French, Hindi, Indonesian, Japanese, Korean, Persian, Russian, Spanish, Swahili, and Telugu.

## Set up an automatic semantic enrichment index for domains
<a name="semantic-enrichment-index-setup"></a>

Setting up an index with automatic semantic enrichment enabled for your text fields is easy, and you can manage it through the console, APIs, and CloudFormation templates during new index creation. To enable it for an existing index, you need to recreate the index with automatic semantic enrichment enabled for text fields.

Console experience - The AWS console allows you to easily create an index with automatic semantic enrichment fields. Once you select a domain, you will find the create index button at the top of the console. Once you click the create index button, you will find options to define automatic semantic enrichment fields. In one index, you can have combinations of automatic semantic enrichment for English and multilingual, as well as lexical fields.

![Create index page showing index name field, semantic enrichment fields, and search fields.](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/ase-console-exp.png)


API experience - To create an automatic semantic enrichment index using the AWS Command Line Interface (AWS CLI), use the create-index command: 

```
aws opensearch create-index \
--domain-name [domain_name] \
--index-name [index_name] \
--index-schema [index_body] \
```

 In the following example index-schema, the *title\_semantic *field has a field type set to *text* and has parameter *semantic\_enrichment *set to status *ENABLED*. Setting the *semantic\_enrichment* parameter enables automatic semantic enrichment on the *title\_semantic* field. You can use the *language\_options* field to specify either *english* or *MULTI-LINGUAL*. 

```
    aws opensearch create-index \
    --id XXXXXXXXX \
    --index-name 'product-catalog' \
    --index-schema '{
    "mappings": {
        "properties": {
            "product_id": {
                "type": "keyword"
            },
            "title_semantic": {
                "type": "text",
                "semantic_enrichment": {
                    "status": "ENABLED",
                    "language_options": "english"
                }
            },
            "title_non_semantic": {
                "type": "text"
            }
        }
    }
}'
```

To describe the created index, use the following command:

```
aws opensearch get-index \
--domain-name [domain_name] \
--index-name [index_name] \
```

## Update an existing index
<a name="semantic-enrichment-update-index"></a>

You can update an existing index to add new semantic enrichment fields, enable or disable semantic enrichment on existing fields, or add non-semantic text fields. Use the `update-index` command and provide only the fields you want to change in the `index-schema`. Fields not included in the request are left unchanged.

**Note**  
Index `settings` cannot be updated. If you include a `settings` block in the request, the operation returns a validation error. To change index settings, you must delete and recreate the index.

To update an index using the AWS CLI, use the `update-index` command:

```
aws opensearch update-index \
--domain-name [domain_name] \
--index-name [index_name] \
--index-schema [index_body]
```

### Add a new semantic enrichment field
<a name="semantic-enrichment-update-add-field"></a>

You can add a new `text` field with semantic enrichment enabled to an existing index. The service automatically sets up the required ML model, ingest pipeline, and search pipeline. New documents indexed after the update are enriched automatically.

**Important**  
Existing documents are not backfilled. To populate the semantic enrichment field on existing documents, you must re-ingest them after the update. Until re-ingested, existing documents will not benefit from semantic search on the new field.

```
aws opensearch update-index \
--domain-name my-domain \
--index-name product-catalog \
--index-schema '{
    "mappings": {
        "properties": {
            "description": {
                "type": "text",
                "semantic_enrichment": {
                    "status": "ENABLED",
                    "language_options": "english"
                }
            }
        }
    }
}'
```

### Disable semantic enrichment on a field
<a name="semantic-enrichment-update-disable-field"></a>

To disable semantic enrichment on a field that currently has it enabled, set `status` to `DISABLED`. The field is removed from the ingest and search pipelines. The underlying text field and its embedding field remain in the index but are no longer enriched.

```
aws opensearch update-index \
--domain-name my-domain \
--index-name product-catalog \
--index-schema '{
    "mappings": {
        "properties": {
            "title_semantic": {
                "type": "text",
                "semantic_enrichment": {
                    "status": "DISABLED"
                }
            }
        }
    }
}'
```

### Update limitations
<a name="semantic-enrichment-update-limitations"></a>

The following operations are not supported by `update-index` and require you to delete and recreate the index:
+ **Changing `language_options`** on a field that currently has semantic enrichment enabled. Disable the field first, then re-enable it with the new language option.
+ **Updating nested fields.** Semantic enrichment is only supported on top-level `text` fields.
+ **Updating index `settings`.**

**Note**  
If the index has a custom ingest or search pipeline that was not created by automatic semantic enrichment, the update operation is blocked. Remove the custom pipeline before adding semantic enrichment fields.

## Data ingestion and search
<a name="semantic-enrichment-data-ingest"></a>

Once you've created an index with automatic semantic enrichment enabled, the feature works automatically during data ingestion process, no additional configuration required.

Data ingestion: When you add documents to your index, the system automatically:
+ Analyzes the text fields you designated for semantic enrichment
+ Generates semantic encodings using OpenSearch Service managed sparse model
+ Stores these enriched representations alongside your original data

This process uses OpenSearch's built-in ML connectors and ingest pipelines, which are created and managed automatically behind the scenes.

Search: The semantic enrichment data is already indexed, so queries run efficiently without invoking the ML model again. This means you get improved search relevance with no additional search latency overhead.

## Configuring permissions for automatic semantic enrichment
<a name="opensearch-semantic-enrichment-permissions"></a>

Before creating an index with automatic semantic enrichment, you need to configure the required permissions. This section explains the permissions needed for different index operations and how to set them up for both AWS Identity and Access Management (IAM) and fine-grained access control scenarios.

### IAM permissions
<a name="opensearch-semantic-enrichment-iam-permissions"></a>

The following IAM permissions are required for automatic semantic enrichment operations. These permissions vary depending on the specific index operation you want to perform.

#### CreateIndex API permissions
<a name="opensearch-semantic-enrichment-create-index-permissions"></a>

To create an index with automatic semantic enrichment, you need the following IAM permissions:
+ `es:CreateIndex` – Create an index with semantic enrichment capabilities.
+ `es:ESHttpHead` – Perform HEAD requests to check index existence.
+ `es:ESHttpPut` – Perform PUT requests for index creation.
+ `es:ESHttpPost` – Perform POST requests for index operations.

#### UpdateIndex API permissions
<a name="opensearch-semantic-enrichment-update-index-permissions"></a>

To update an existing index with automatic semantic enrichment, you need the following IAM permissions:
+ `es:UpdateIndex` – Update index settings and mappings.
+ `es:ESHttpPut` – Perform PUT requests for index updates.
+ `es:ESHttpGet` – Perform GET requests to retrieve index information.
+ `es:ESHttpPost` – Perform POST requests for index operations.

#### GetIndex API permissions
<a name="opensearch-semantic-enrichment-get-index-permissions"></a>

To retrieve information about an index with automatic semantic enrichment, you need the following IAM permissions:
+ `es:GetIndex` – Retrieve index information and settings.
+ `es:ESHttpGet` – Perform GET requests to retrieve index data.

#### DeleteIndex API permissions
<a name="opensearch-semantic-enrichment-delete-index-permissions"></a>

To delete an index with automatic semantic enrichment, you need the following IAM permissions:
+ `es:DeleteIndex` – Delete an index and its semantic enrichment components.
+ `es:ESHttpDelete` – Perform DELETE requests for index removal.

### Sample IAM policy
<a name="opensearch-semantic-enrichment-sample-policy"></a>

The following sample identity-based access policy provides the permissions necessary for a user to manage indexes with automatic semantic enrichment:

```
{
    "Version": "2012-10-17", 		 	 	 
    "Statement": [
        {
            "Sid": "AllowSemanticEnrichmentIndexOperations",
            "Effect": "Allow",
            "Action": [
                "es:CreateIndex",
                "es:UpdateIndex",
                "es:GetIndex",
                "es:DeleteIndex",
                "es:ESHttpHead",
                "es:ESHttpGet",
                "es:ESHttpPut",
                "es:ESHttpPost",
                "es:ESHttpDelete"
            ],
            "Resource": "arn:aws:es:{{aws-region}}:{{111122223333}}:domain/{{domain-name}}"
        }
    ]
}
```

Replace {{aws-region}}, {{111122223333}}, and {{domain-name}} with your specific values. You can further restrict access by specifying particular index patterns in the resource ARN.

### Fine-grained access control permissions
<a name="opensearch-semantic-enrichment-fgac-permissions"></a>

If your Amazon OpenSearch Service domain has fine-grained access control enabled, you need additional permissions beyond the IAM permissions. The following permissions are required for each index operation.

#### CreateIndex API permissions
<a name="opensearch-semantic-enrichment-fgac-create-permissions"></a>

When fine-grained access control is enabled, the following additional permissions are required for creating an index with automatic semantic enrichment:
+ `indices:admin/create` – Create index operations.
+ `indices:admin/mapping/put` – Create and update index mappings.
+ `cluster:admin/opensearch/ml/create_connector` – Create machine learning connectors for semantic processing.
+ `cluster:admin/opensearch/ml/register_model` – Register machine learning models for semantic enrichment.
+ `cluster:admin/ingest/pipeline/put` – Create ingest pipelines for data processing.
+ `cluster:admin/search/pipeline/put` – Create search pipelines for query processing.

#### UpdateIndex API permissions
<a name="opensearch-semantic-enrichment-fgac-update-permissions"></a>

When fine-grained access control is enabled, the following additional permissions are required for updating an index with automatic semantic enrichment:
+ `indices:admin/get` – Retrieve index information.
+ `indices:admin/settings/update` – Update index settings.
+ `indices:admin/mapping/put` – Update index mappings.
+ `cluster:admin/opensearch/ml/create_connector` – Create machine learning connectors.
+ `cluster:admin/opensearch/ml/register_model` – Register machine learning models.
+ `cluster:admin/ingest/pipeline/put` – Create ingest pipelines.
+ `cluster:admin/search/pipeline/put` – Create search pipelines.
+ `cluster:admin/ingest/pipeline/get` – Retrieve ingest pipeline information.
+ `cluster:admin/search/pipeline/get` – Retrieve search pipeline information.

#### GetIndex API permissions
<a name="opensearch-semantic-enrichment-fgac-get-permissions"></a>

When fine-grained access control is enabled, the following additional permissions are required for retrieving information about an index with automatic semantic enrichment:
+ `indices:admin/get` – Retrieve index information.
+ `cluster:admin/ingest/pipeline/get` – Retrieve ingest pipeline information.
+ `cluster:admin/search/pipeline/get` – Retrieve search pipeline information.

#### DeleteIndex API permissions
<a name="opensearch-semantic-enrichment-fgac-delete-permissions"></a>

When fine-grained access control is enabled, the following additional permission is required for deleting an index with automatic semantic enrichment:
+ `indices:admin/delete` – Delete index operations.

## Query Rewrites
<a name="query-rewrite"></a>

Automatic semantic enrichment automatically converts your existing “match” queries to semantic search queries without requiring query modifications. If a match query is part of a compound query, the system traverses your query structure, finds match queries, and replaces them with neural sparse queries. Currently, the feature only supports replacing “match” queries, whether it’s a standalone query or part of a compound query. “multi\_match” is not supported. In addition, the feature supports all compound queries to replace their nested match queries. Compound queries include: bool, boosting, constant\_score, dis\_max, function\_score, and hybrid. 

## Limitations of automatic semantic enrichment
<a name="ase-limitation"></a>

Automatic semantic search is most effective when applied to small-to-medium sized fields containing natural language content, such as movie titles, product descriptions, reviews, and summaries. Although semantic search enhances relevance for most use cases, it might not be optimal for certain scenarios. Consider following limitations when deciding whether to implement automatic semantic enrichment for your specific use case. 
+ Very long documents – The current sparse model processes only the first 8,192 tokens of each document for English. For multilingual documents, it’s 512 tokens. For lengthy articles, consider implementing document chunking to ensure complete content processing.
+ Log analysis workloads – Semantic enrichment significantly increases index size, which might be unnecessary for log analysis where exact matching typically suffices. The additional semantic context rarely improves log search effectiveness enough to justify the increased storage requirements. 
+ Automatic semantic enrichment is not compatible with the Derived Source feature. 
+ Throttling – Indexing inference requests are currently capped at 200 TPS for OpenSearch Service domains. This is a soft limit; reach out to AWS Support for higher limits.

## Pricing
<a name="ase-pricing"></a>

Amazon OpenSearch Service bills automatic semantic enrichment based on OpenSearch Compute Units (OCUs) consumed during sparse vector generation at indexing time. You're charged only for actual usage during indexing for the text fields where you enabled automatic semantic enrichment. One Semantic Search OCU can process 11.1 million tokens for English content. To process 2.4 billion tokens, you'd need about 216 Semantic Search OCU-hours (2.4 billion / 11.10 million). With a price of $0.24 per Semantic Search OCU-hour, the cost for processing 10 GB of data for automatic semantic search would be $51 (216 OCU-hours x $0.24/OCU-hour). There are no additional Semantic Search OCU charges during search operations or for data storage.

You can monitor this consumption using the Amazon CloudWatch metric `SemanticSearchOCU`. For specific details about model token limits, volume throughput per OCU, and an example of a sample calculation, visit [OpenSearch Service Pricing](https://aws.amazon.com/opensearch-service/pricing/).

## Supported AWS Regions
<a name="semantic-enrichment-supported-regions"></a>

Automatic semantic enrichment is available in the following AWS Regions:
+ US East (N. Virginia)
+ US East (Ohio)
+ US West (Oregon)
+ Asia Pacific (Mumbai)
+ Asia Pacific (Singapore)
+ Asia Pacific (Sydney)
+ Asia Pacific (Tokyo)
+ Europe (Frankfurt)
+ Europe (Ireland)
+ Europe (Stockholm)
+ Europe (Spain)