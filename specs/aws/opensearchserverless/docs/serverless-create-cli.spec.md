---
id: "@specs/aws/opensearchserverless/docs/serverless-create-cli"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Create a collection (CLI)"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Create a collection (CLI)

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/serverless-create-cli
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Create a collection (CLI)
<a name="serverless-create-cli"></a>

Use the procedures in this section to create an OpenSearch Serverless collection using the AWS CLI. 

**Topics**
+ [Before you begin](#serverless-create-cli-before-you-begin)
+ [Creating a collection](#serverless-create-cli-creating)
+ [Creating a collection with an automatic semantic enrichment index](#serverless-create-cli-automatic-semantic-enrichment)

## Before you begin
<a name="serverless-create-cli-before-you-begin"></a>

Before you create a collection using the AWS CLI, use the following procedure to create required policies for the collection.

**Note**  
In each of the following procedures, when you specify a name for a collection, the name must meet the following criteria:  
Is unique to your account and AWS Region
Contains only lowercase letters a-z, the numbers 0–9, and the hyphen (-)
Contains between 3 and 32 characters

**To create required policies for a collection**

1. Open the AWS CLI and run the following command to create an [encryption policy](serverless-encryption.md) with a resource pattern that matches the intended name of the collection. 

   ```
   &aws opensearchserverless create-security-policy \
     --name {{policy name}} \
     --type encryption --policy "{\"Rules\":[{\"ResourceType\":\"collection\",\"Resource\":[\"collection\/{{collection name}}\"]}],\"AWSOwnedKey\":true}"
   ```

   For example, if you plan to name your collection *logs-application*, you might create an encryption policy like this:

   ```
   &aws opensearchserverless create-security-policy \
     --name logs-policy \
     --type encryption --policy "{\"Rules\":[{\"ResourceType\":\"collection\",\"Resource\":[\"collection\/logs-application\"]}],\"AWSOwnedKey\":true}"
   ```

   If you plan to use the policy for additional collections, you can make the rule more broad, such as `collection/logs*` or `collection/*`.

1. Run the following command to configure network settings for the collection using a [network policy](serverless-network.md). You can create network policies after you create a collection, but as a best practice, do it beforehand.

   ```
   &aws opensearchserverless create-security-policy \
     --name {{policy name}} \
     --type network --policy "[{\"Description\":\"{{description}}\",\"Rules\":[{\"ResourceType\":\"dashboard\",\"Resource\":[\"collection\/{{collection name}}\"]},{\"ResourceType\":\"collection\",\"Resource\":[\"collection\/{{collection name}}\"]}],\"AllowFromPublic\":true}]"
   ```

   Using the previous *logs-application* example, you might create the following network policy:

   ```
   &aws opensearchserverless create-security-policy \
     --name logs-policy \
     --type network --policy "[{\"Description\":\"Public access for logs collection\",\"Rules\":[{\"ResourceType\":\"dashboard\",\"Resource\":[\"collection\/logs-application\"]},{\"ResourceType\":\"collection\",\"Resource\":[\"collection\/logs-application\"]}],\"AllowFromPublic\":true}]"
   ```

## Creating a collection
<a name="serverless-create-cli-creating"></a>

The following procedure uses the [CreateCollection](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CreateCollection.html) API action to create a collection of type `SEARCH` or `TIMESERIES`. If you don't specify a collection type in the request, it defaults to `TIMESERIES`. For more information about these types, see [Choosing a collection type](serverless-overview.md#serverless-usecase). To create a *vector search* collection, see [Working with vector search collections](serverless-vector-search.md). 

If your collection is encrypted with an AWS owned key, the `kmsKeyArn` is `auto` rather than an ARN.

**Important**  
After you create a collection, you can't access it unless it matches a data access policy. For more information, see [Data access control for Amazon OpenSearch Serverless](serverless-data-access.md).

**To create a collection**

1. Verify that you created required policies described in [Before you begin](#serverless-create-cli-before-you-begin).

1. Run the following command. For `type` specify either `SEARCH` or `TIMESERIES`.

   ```
   &aws opensearchserverless create-collection --name "{{collection name}}" --type {{collection type}} --description "{{description}}"
   ```

Collection creation typically takes several minutes. Use the [BatchGetCollection](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_BatchGetCollection.html) operation to check the collection status.

## Creating a collection with an automatic semantic enrichment index
<a name="serverless-create-cli-automatic-semantic-enrichment"></a>

Use the following procedure to create a new OpenSearch Serverless collection with an index that is configured for [automatic semantic enrichment](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-semantic-enrichment.html). The procedure uses the OpenSearch Serverless [CreateIndex](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CreateIndex.html) API action.

**To create a new collection with an index configured for automatic semantic enrichment**

Run the following command to create the collection and an index.

```
&aws opensearchserverless create-index \
--region {{Region ID}} \
--id {{collection name}} --index-name {{index name}} \
--index-schema \
'{{mapping in json}}'
```

Here's an example.

```
&aws opensearchserverless create-index \
--region us-east-1 \
--id conversation_history --index-name conversation_history_index \
--index-schema \ 
'{
    "mappings": {
        "properties": {
            "age": {
                "type": "integer"
            },
            "name": {
                "type": "keyword"
            },
            "user_description": {
                "type": "text"
            },
            "conversation_history": {
                "type": "text",
                "semantic_enrichment": {
                    "status": "ENABLED",
                    // Specifies the sparse tokenizer for processing multi-lingual text
                    "language_option": "MULTI-LINGUAL", 
                    // If embedding_field is provided, the semantic embedding field will be set to the given name rather than original field name + "_embedding"
                    "embedding_field": "conversation_history_user_defined" 
                }
            },
            "book_title": {
                "type": "text",
                "semantic_enrichment": {
                    // No embedding_field is provided, so the semantic embedding field is set to "book_title_embedding"
                    "status": "ENABLED",
                    "language_option": "ENGLISH"
                }
            },
            "abstract": {
                "type": "text",
                "semantic_enrichment": {
                    // If no language_option is provided, it will be set to English.
                    // No embedding_field is provided, so the semantic embedding field is set to "abstract_embedding"
                    "status": "ENABLED" 
                }
            }
        }
    }
}'
```