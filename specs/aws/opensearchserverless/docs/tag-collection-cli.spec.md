---
id: "@specs/aws/opensearchserverless/docs/tag-collection-cli"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Tagging collections (AWS CLI)"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Tagging collections (AWS CLI)

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/tag-collection-cli
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Tagging collections (AWS CLI)
<a name="tag-collection-cli"></a>

To tag a collection using the AWS CLI, send a [TagResource](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_TagResource.html) request: 

```
aws opensearchserverless tag-resource
  --resource-arn arn:aws:aoss:{{us-east-1}}:{{123456789012}}:collection/{{my-collection}} 
  --tags Key={{service}},Value={{aoss}} Key={{source}},Value={{logs}}
```

View the existing tags for a collection with the [ListTagsForResource](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_ListTagsForResource.html) command:

```
aws opensearchserverless list-tags-for-resource
  --resource-arn arn:aws:aoss:{{us-east-1}}:{{123456789012}}:collection/{{my-collection}}
```

Remove tags from a collection using the [UntagResource](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_UntagResource.html) command:

```
aws opensearchserverless untag-resource
  --resource-arn arn:aws:aoss:{{us-east-1}}:{{123456789012}}:collection/{{my-collection}}
  --tag-keys {{service}}
```