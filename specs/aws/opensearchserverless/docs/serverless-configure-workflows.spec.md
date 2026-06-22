---
id: "@specs/aws/opensearchserverless/docs/serverless-configure-workflows"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Configure Workflows"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Configure Workflows

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/serverless-configure-workflows
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configure Workflows on Amazon OpenSearch Serverless
<a name="serverless-configure-workflows"></a>

## Workflows
<a name="serverless-configure-workflows-what-is"></a>

Workflows support builders in innovating AI applications on OpenSearch. The current process of using machine learning (ML) offerings in OpenSearch, such as Semantic Search, requires complex setup and pre-processing tasks, along with verbose user queries, both of which can be time-consuming and error-prone. Workflows are a simplification framework to chain multiple API calls for OpenSearch.

For setup and usage, see [Automating configurations](https://docs.opensearch.org/docs/latest/automating-configurations/index/) on the *OpenSearch* website. When you use Workflows in OpenSearch Serverless, consider these important differences:
+ OpenSearch Serverless uses only remote models in workflow steps. You don't need to deploy these models.
+ OpenSearch Serverless doesn't support the **Re-index** Workflow step.
+ When you search **Workflows** and **Workflow states** after other API calls, expect up to 15 seconds of latency for updates to appear.

OpenSearch Serverless Collections support Workflows when it's used as a data source in your OpenSearch UI application. For more information, see [Managing data source associations](application-data-sources-and-vpc.md).

## Configure permissions
<a name="serverless-configure-workflows-permissions"></a>

Before you create and provision a template, verify that you have the required permissions. If you need assistance, contact your account administrator. OpenSearch Serverless Workflows require the following permissions. You can scope permissions to a specific collection by defining the collection resource ARN in your IAM policy.

**Example : Workflows policy**    
****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "NeuralSearch",
      "Effect": "Allow",
      "Principal": {
        "AWS": [
          "arn:aws:iam::{{111122223333}}:role/{{Cognito_identitypoolname}}/Auth_Role"
        ]
      },
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
+ **aoss:\*CollectionItems** – Grants permission to create and manage templates, and provision [search and ingest pipelines](serverless-configure-neural-search.md).
+ **aoss:\*Index** – Grants permission to create and delete indices using OpenSearch API operations.
+ **aoss:\*MLResource** – Grants permission to provision workflow steps that use the [Configure Machine Learning](serverless-configure-machine-learning.md).