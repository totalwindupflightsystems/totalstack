---
id: "@specs/aws/opensearchserverless/docs/agentic-search"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Agentic search"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Agentic search

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/agentic-search
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Agentic search in Amazon OpenSearch Service
<a name="agentic-search"></a>

Starting with OpenSearch version 3.3, agentic search enables an AI-powered process that uses an autonomous agent to execute complex searches on your behalf.

Agentic search introduces an intelligent agent system that understands user intent, orchestrates the right tools, and generates optimized queries. It provides transparent summaries of its decisions through a natural language interface.

With OpenSearch Service, you can configure [AI connectors for AWS services](ml-amazon-connector.md) and [external services](ml-external-connector.md). Using the console, you can also create an ML model with a CloudFormation template that can be used for building your agent. For more information, see [Configuring Agentic Search with Bedrock Claude](cfn-template-agentic-search.md).

For complete documentation and step-by-step implementation, see [Agentic Search](https://docs.opensearch.org/latest/vector-search/ai-search/agentic-search/index/) in the OpenSearch documentation.