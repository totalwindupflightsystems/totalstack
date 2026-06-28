---
id: "@specs/aws/kendra/docs/API_SalesforceKnowledgeArticleConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SalesforceKnowledgeArticleConfiguration"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# SalesforceKnowledgeArticleConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_SalesforceKnowledgeArticleConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SalesforceKnowledgeArticleConfiguration
<a name="API_SalesforceKnowledgeArticleConfiguration"></a>

Provides the configuration information for the knowledge article types that Amazon Kendra indexes. Amazon Kendra indexes standard knowledge articles and the standard fields of knowledge articles, or the custom fields of custom knowledge articles, but not both 

## Contents
<a name="API_SalesforceKnowledgeArticleConfiguration_Contents"></a>

 ** IncludedStates **   <a name="kendra-Type-SalesforceKnowledgeArticleConfiguration-IncludedStates"></a>
Specifies the document states that should be included when Amazon Kendra indexes knowledge articles. You must specify at least one state.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 3 items.  
Valid Values: `DRAFT | PUBLISHED | ARCHIVED`   
Required: Yes

 ** CustomKnowledgeArticleTypeConfigurations **   <a name="kendra-Type-SalesforceKnowledgeArticleConfiguration-CustomKnowledgeArticleTypeConfigurations"></a>
Configuration information for custom Salesforce knowledge articles.  
Type: Array of [SalesforceCustomKnowledgeArticleTypeConfiguration](API_SalesforceCustomKnowledgeArticleTypeConfiguration.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Required: No

 ** StandardKnowledgeArticleTypeConfiguration **   <a name="kendra-Type-SalesforceKnowledgeArticleConfiguration-StandardKnowledgeArticleTypeConfiguration"></a>
Configuration information for standard Salesforce knowledge articles.  
Type: [SalesforceStandardKnowledgeArticleTypeConfiguration](API_SalesforceStandardKnowledgeArticleTypeConfiguration.md) object  
Required: No

## See Also
<a name="API_SalesforceKnowledgeArticleConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/SalesforceKnowledgeArticleConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/SalesforceKnowledgeArticleConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/SalesforceKnowledgeArticleConfiguration) 