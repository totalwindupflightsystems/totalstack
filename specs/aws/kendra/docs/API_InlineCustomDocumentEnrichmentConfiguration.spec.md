---
id: "@specs/aws/kendra/docs/API_InlineCustomDocumentEnrichmentConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS InlineCustomDocumentEnrichmentConfiguration"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# InlineCustomDocumentEnrichmentConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_InlineCustomDocumentEnrichmentConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# InlineCustomDocumentEnrichmentConfiguration
<a name="API_InlineCustomDocumentEnrichmentConfiguration"></a>

Provides the configuration information for applying basic logic to alter document metadata and content when ingesting documents into Amazon Kendra. To apply advanced logic, to go beyond what you can do with basic logic, see [HookConfiguration](https://docs.aws.amazon.com/kendra/latest/dg/API_HookConfiguration.html).

For more information, see [Customizing document metadata during the ingestion process](https://docs.aws.amazon.com/kendra/latest/dg/custom-document-enrichment.html).

## Contents
<a name="API_InlineCustomDocumentEnrichmentConfiguration_Contents"></a>

 ** Condition **   <a name="kendra-Type-InlineCustomDocumentEnrichmentConfiguration-Condition"></a>
Configuration of the condition used for the target document attribute or metadata field when ingesting documents into Amazon Kendra.  
Type: [DocumentAttributeCondition](API_DocumentAttributeCondition.md) object  
Required: No

 ** DocumentContentDeletion **   <a name="kendra-Type-InlineCustomDocumentEnrichmentConfiguration-DocumentContentDeletion"></a>
 `TRUE` to delete content if the condition used for the target attribute is met.  
Type: Boolean  
Required: No

 ** Target **   <a name="kendra-Type-InlineCustomDocumentEnrichmentConfiguration-Target"></a>
Configuration of the target document attribute or metadata field when ingesting documents into Amazon Kendra. You can also include a value.  
Type: [DocumentAttributeTarget](API_DocumentAttributeTarget.md) object  
Required: No

## See Also
<a name="API_InlineCustomDocumentEnrichmentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/InlineCustomDocumentEnrichmentConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/InlineCustomDocumentEnrichmentConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/InlineCustomDocumentEnrichmentConfiguration) 