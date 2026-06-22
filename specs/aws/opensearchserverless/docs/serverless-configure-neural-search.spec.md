---
id: "@specs/aws/opensearchserverless/docs/serverless-configure-neural-search"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Configure Neural and Hybrid Search"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Configure Neural and Hybrid Search

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/serverless-configure-neural-search
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configure Neural Search and Hybrid Search on OpenSearch Serverless
<a name="serverless-configure-neural-search"></a>

## Neural Search
<a name="serverless-configure-neural-search-what-is"></a>

Amazon OpenSearch Serverless supports Neural Search functionality for semantic search operations on your data. Neural Search uses machine learning models to understand the semantic meaning and context of your queries, providing more relevant search results than traditional keyword-based searches. This section explains how to configure Neural Search in OpenSearch Serverless, including the required permissions, supported processors, and key differences from the standard OpenSearch implementation.

With Neural Search you can perform semantic search on your data, which considers semantic meaning to understand the intent of your search queries. This capability is powered by the following components:
+ Text embedding ingest pipeline processor
+ Neural query
+ Neural sparse query

## Hybrid Search
<a name="serverless-configure-hybrid-search"></a>

With hybrid search, you can improve search relevance by combining keyword and semantic search capabilities. To use hybrid search, create a search pipeline that processes your search results and combines document scores. For more information, see [Search pipelines](https://docs.opensearch.org/latest/search-plugins/search-pipelines/index/) on the *OpenSearch Documentation* website. Use the following components to implement hybrid search:
+ Normalization search pipeline processor

**Supported normalization techniques**
  + `min_max`
  + `l2`

**Supported combination techniques**
  + `arithmetic_mean`
  + `geometric_mean`
  + `harmonic_mean`

  For more information about normalization and combination techniques, see [Request body fields](https://docs.opensearch.org/latest/search-plugins/search-pipelines/normalization-processor/#request-body-fields) on the *OpenSearch Documentation* website.
+ Hybrid query

## Neural and hybrid queries
<a name="serverless-configure-neural-search-hybrid-queries"></a>

By default, OpenSearch calculates document scores using the keyword-based Okapi BM25 algorithm, which works well for search queries that contain keywords. Neural Search provides new query types for natural language queries and the ability to combine both semantic and keyword search.

**Example : `neural`**  

```
"neural": {
  "{{vector_field}}": {
    "query_text": "{{query_text}}",
    "query_image": "{{image_binary}}",
    "model_id": "{{model_id}}",
    "k": 100
  }
}
```

For more information, see [Neural query](https://docs.opensearch.org/latest/query-dsl/specialized/neural/) on the *OpenSearch Documentation* website.

**Example : `hybrid`**  

```
"hybrid": {
      "queries": [
        {{array of lexical, neural, or combined queries}}
      ]
    }
```

For more information, see [Hybrid query](https://docs.opensearch.org/latest/query-dsl/compound/hybrid/) on the *OpenSearch Documentation* website.

To configure semantic search components in Amazon OpenSearch Serverless, follow the steps in the [Neural Search tutorial](https://docs.opensearch.org/latest/tutorials/vector-search/neural-search-tutorial/) on the *OpenSearch Documentation* website. Keep in mind these important differences:
+ OpenSearch Serverless supports only remote models. You must configure connectors to remotely hosted models. You don't need to deploy or remove remote models. For more information, see [Getting started with semantic and hybrid search](https://docs.opensearch.org/latest/tutorials/vector-search/neural-search-tutorial/) on the *OpenSearch Documentation* website.
+ Expect up to 15 seconds of latency when you search against your vector index or search for recently created search and ingest pipelines.

## Configure permissions
<a name="serverless-configure-neural-search-permissions"></a>

Neural Search in OpenSearch Serverless requires the following permissions. For more information, see [Supported policy permissions](serverless-data-access.md#serverless-data-supported-permissions).

**Example : Neural search policy**    
****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "NeuralSearch",
            "Effect": "Allow",
            "Action": [
              "aoss:CreateIndex",
              "aoss:CreateCollection",
              "aoss:UpdateCollection",
              "aoss:DeleteIndex",
              "aoss:DeleteCollection"
            ],
            "Resource": "arn:aws:aoss:{{us-east-1}}:{{111122223333}}:collection/{{your-collection-name}}"
        }
    ]
}
```
+ **aoss:\*Index** – Creates a vector index where text embeddings are stored.
+ **aoss:\*CollectionItems** – Creates ingest and search pipelines.
+ **aoss:\*MLResource** – Creates and registers text embedding models.
+ **aoss:APIAccessAll** – Provides access to OpenSearch APIs for search and ingest operations.

The following describes the collection data access policies required for neural search. Replace the {{placeholder values}} with your specific information.

**Example : Data access policy**  

```
[
    {
        "Description": "Create index permission",
        "Rules": [
            {
                "ResourceType": "index",
                "Resource": ["index/{{collection_name}}/*"],
                "Permission": [
                  "aoss:CreateIndex", 
                  "aoss:DescribeIndex",
                  "aoss:UpdateIndex",
                  "aoss:DeleteIndex"
                ]
            }
        ],
        "Principal": [
            "arn:aws:iam::{{account_id}}:role/{{role_name}}"
        ]
    },
    {
        "Description": "Create pipeline permission",
        "Rules": [
            {
                "ResourceType": "collection",
                "Resource": ["collection/{{collection_name}}"],
                "Permission": [
                  "aoss:CreateCollectionItems",
                  "aoss:DescribeCollectionItems",
                  "aoss:UpdateCollectionItems",
                  "aoss:DeleteCollectionItems"
                ]
            }
        ],
        "Principal": [
            "arn:aws:iam::{{account_id}}:role/{{role_name}}"
        ]
    },
    {
        "Description": "Create model permission",
        "Rules": [
            {
                "ResourceType": "model",
                "Resource": ["model/{{collection_name}}/*"],
                "Permission": ["aoss:CreateMLResources"]
            }
        ],
        "Principal": [
            "arn:aws:iam::{{account_id}}:role/{{role_name}}"
        ]
    }
]
```

## Supported AWS Regions
<a name="serverless-neural-search-supported-regions"></a>

Neural search for OpenSearch Serverless is available in the following AWS Regions:
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