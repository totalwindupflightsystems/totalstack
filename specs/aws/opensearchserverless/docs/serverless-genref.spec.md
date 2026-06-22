---
id: "@specs/aws/opensearchserverless/docs/serverless-genref"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Supported operations and plugins"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Supported operations and plugins

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/serverless-genref
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Supported operations and plugins in Amazon OpenSearch Serverless
<a name="serverless-genref"></a>

Amazon OpenSearch Serverless supports a variety of OpenSearch plugins, as well as a subset of the indexing, search, and metadata [API operations](https://opensearch.org/docs/latest/opensearch/rest-api/index/) available in OpenSearch. You can include the permissions in the left column of the table within [data access policies](serverless-data-access.md) in order to limit access to certain operations.

**Topics**
+ [Supported OpenSearch API operations and permissions](#serverless-operations)
+ [Supported OpenSearch plugins](#serverless-plugins)

## Supported OpenSearch API operations and permissions
<a name="serverless-operations"></a>

The following table lists the API operations that OpenSearch Serverless supports, along with their corresponding data access policy permissions:


| Data access policy permission | OpenSearch API operations | Description and caveats | 
| --- | --- | --- | 
| `aoss:CreateIndex` | PUT <index> | Create indexes. For more information, see [Create index](https://opensearch.org/docs/latest/api-reference/index-apis/create-index/). This permission also applies to creating indexes with the sample data on OpenSearch Dashboards.  | 
| `aoss:DescribeIndex` |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-genref.html)  | Describe indexes. For more information, see the following resources:[See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-genref.html) | 
| `aoss:WriteDocument` |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-genref.html)  | Write and update documents. For more information, see the following resources:[See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-genref.html) Some operations are only allowed for collections of type `SEARCH`. For more information, see [Choosing a collection type](serverless-overview.md#serverless-usecase).  | 
| `aoss:ReadDocument` |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-genref.html)  | Read documents. For more information, see the following resources:[See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-genref.html) | 
| `aoss:DeleteIndex` | DELETE <target> | Delete indexes. For more information, see [Delete index](https://opensearch.org/docs/latest/api-reference/index-apis/delete-index/). | 
| `aoss:UpdateIndex` |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-genref.html)  | Update index settings. For more information, see the following resources:[See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-genref.html) | 
| `aoss:CreateCollectionItems` |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-genref.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-genref.html) | 
| `aoss:DescribeCollectionItems` |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-genref.html)  | Describes how to work with aliases, index and framework templates, and pipelines. For more information, see the following resources:[See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-genref.html) | 
| `aoss:UpdateCollectionItems` |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-genref.html)  | Update aliases, index templates, and framework templates. For more information, see the following resources: [See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-genref.html)\* The API to de-provision templates. The ML Commons Client and OpenSearch Serverless services manage dependent policies. | 
| `aoss:DeleteCollectionItems` |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-genref.html)  | Delete aliases, index and framework templates, and pipelines. For more information, see the following resources:[See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-genref.html) | 
| `aoss:DescribeMLResource` |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-genref.html)  | Describes GET and search APIs to retrieve information about models, and connectors.  | 
| `aoss:CreateMLResource` |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-genref.html)  | Provides permission to create ML resources. | 
| `aoss:UpdateMLResource` |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-genref.html)  | Provides permission to update existing ML resources. | 
| `aoss:DeleteMLResource` |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-genref.html)  | Provides permission to delete ML resources. | 
| `aoss:ExecuteMLResource` |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-genref.html)  | Provides permission to run models. | 
| `aoss:CreateAgent` |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-genref.html)  | Provides permission to create agents. | 
| `aoss:DescribeAgent` |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-genref.html)  | Provides permission to retrieve agent information. | 
| `aoss:UpdateAgent` |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-genref.html)  | Provides permission to update existing agents. | 
| `aoss:DeleteAgent` |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-genref.html)  | Provides permission to delete agents. | 
| `aoss:InvokeAgent` |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-genref.html)  | Provides permission to invoke (execute) agents. | 
| `aoss:SearchAgents` |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-genref.html)  | Provides permission to search for agents. | 

## Supported OpenSearch plugins
<a name="serverless-plugins"></a>

OpenSearch Serverless collections come prepackaged with the following plugins from the OpenSearch community. Serverless automatically deploys and manages plugins for you.

**Analysis plugins**
+  [ICU Analysis](https://github.com/opensearch-project/OpenSearch/tree/main/plugins/analysis-icu) 
+  [Japanese (kuromoji) Analysis](https://github.com/opensearch-project/OpenSearch/tree/main/plugins/analysis-kuromoji)
+  [Korean (Nori) Analysis](https://github.com/opensearch-project/OpenSearch/tree/main/plugins/analysis-nori) 
+  [Phonetic Analysis](https://github.com/opensearch-project/OpenSearch/tree/main/plugins/analysis-phonetic) 
+  [Smart Chinese Analysis](https://github.com/opensearch-project/OpenSearch/tree/main/plugins/analysis-smartcn) 
+  [Stempel Polish Analysis](https://github.com/opensearch-project/OpenSearch/tree/main/plugins/analysis-stempel)
+  [Ukrainian Analysis](https://github.com/opensearch-project/OpenSearch/tree/main/plugins/analysis-ukrainian)

**Mapper plugins**
+  [Mapper Size](https://github.com/opensearch-project/OpenSearch/tree/main/plugins/mapper-size) 
+  [Mapper Murmur3](https://github.com/opensearch-project/OpenSearch/tree/main/plugins/mapper-murmur3) 
+  [Mapper Annotated Text](https://github.com/opensearch-project/OpenSearch/tree/main/plugins/mapper-annotated-text)

**Scripting plugins**
+  [Painless](https://opensearch.org/docs/latest/search-plugins/search-pipelines/index/) (inline scripts in search queries and aggregations only; stored scripts and the `/_scripts` endpoint are not supported in OpenSearch Serverless)
+  [Expression](https://opensearch.org/docs/latest/data-prepper/pipelines/expression-syntax/) 
+  [Mustache](https://mustache.github.io/mustache.5.html)

In addition, OpenSearch Serverless includes all plugins that ship as modules. 