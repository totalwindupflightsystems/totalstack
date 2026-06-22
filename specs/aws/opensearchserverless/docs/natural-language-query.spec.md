---
id: "@specs/aws/opensearchserverless/docs/natural-language-query"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Natural language query generation"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Natural language query generation

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/natural-language-query
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Natural language query generation in Amazon OpenSearch Service
<a name="natural-language-query"></a>

The natural language query generation feature in Amazon OpenSearch Service allows you to query your operational and security log data through natural language. OpenSearch is an ideal option to explore log data because it is a highly scalable and performant log analytics and search engine, and now you can use natural language to explore these logs. This feature allows you to identify issues without relying on OpenSearch Piped Processing Language (PPL) or having to look up data definitions when you build your queries. You can use the natural language query generation feature on OpenSearch Service domains with version 2.13 and later. You must have fine-grained access control enabled. 

This feature was built with the [OpenSearch Assistant Toolkit](https://opensearch.org/docs/latest/ml-commons-plugin/opensearch-assistant/). If you want to create similar features that connect to your large language models, you can use the toolkit to configure your own agents and tools.

## Prerequisites
<a name="Prerequisites"></a>

Before you can use the natural language query generation feature, your domain must have the following:
+ Version 2.13 or later.
+ Service software R20240520-P4 or higher.
+ Fine-grained access control enabled. For more information, see [Enabling fine-grained access control](fgac.md#fgac-enabling).

## Getting started
<a name="natural-language-query-getting-started"></a>

Natural language query generation is enabled by default on all domains created with version 2.13 or later that have fine-grained access control enabled.

For other domains, enable it by selecting **Enable Natural Language Query Generation and Amazon Q Developer features**.

After you enable it, navigate to the **Logs** page in OpenSearch Dashboards. Choose **Event Explorer** and ask a question with the query assistant.

## Configure permissions
<a name="natural-language-query-permissions"></a>

If you enable natural language query generation on a preexisting OpenSearch Service domain, the **query\_assistant\_access** role might not be defined on the domain. Non-admin users must be mapped to this role in order to manage warm indexes on domains using fine-grained access control. To manually create the **query\_assistant\_access** role, perform the following steps:

1. In OpenSearch Dashboards, go to **Security** and choose **Roles**.

1. Choose **Create role** and configure the following cluster permissions: 
   + `cluster:admin/opensearch/ml/config/get`
   + `cluster:admin/opensearch/ml/execute`
   + `cluster:admin/opensearch/ml/predict`
   + `cluster:admin/opensearch/ppl`

1. Name the role **query\_assistant\_access**.

1. Choose **Create role**. The **query\_assistant\_access** role is now available.
**Note**  
You must also have the `indices:admin/mappings/get` and `read` index permissions for the indices that you want to use natural language questions with.

## Configuration automation
<a name="natural-language-query-automation"></a>

Flow Framework is an OpenSearch plugin that provides a way to [automate OpenSearch configurations](https://opensearch.org/docs/latest/automating-configurations/index/) for use cases such as query generation and conversational chat. Because the plugin tracks the resources that enable the natural language query generation feature, the flow framework index stores a template for each domain that uses query assist.

Flow Framework allows you to either select from a set of [predefined templates](https://opensearch.org/docs/latest/automating-configurations/workflow-templates/), or create your own automations for machine learning connectors, tools, agents, and other components that prepare OpenSearch as a backend for generative models. 