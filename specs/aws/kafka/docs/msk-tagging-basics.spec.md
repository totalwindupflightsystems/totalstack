---
id: "@specs/aws/kafka/docs/msk-tagging-basics"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Tag basics for clusters"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Tag basics for clusters

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-tagging-basics
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Tag basics for Amazon MSK clusters
<a name="msk-tagging-basics"></a>

You can use the Amazon MSK API to complete the following tasks:
+ Add tags to an Amazon MSK resource.
+ List the tags for an Amazon MSK resource.
+ Remove tags from an Amazon MSK resource.

You can use tags to categorize your Amazon MSK resources. For example, you can categorize your Amazon MSK clusters by purpose, owner, or environment. Because you define the key and value for each tag, you can create a custom set of categories to meet your specific needs. For example, you might define a set of tags that help you track clusters by owner and associated application. 

The following are several examples of tags:
+ `Project: {{Project name}}`
+ `Owner: {{Name}}`
+ `Purpose: Load testing` 
+ `Environment: Production` 