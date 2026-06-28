---
id: "@specs/aws/kendra/docs/API_SalesforceStandardObjectConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SalesforceStandardObjectConfiguration"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# SalesforceStandardObjectConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_SalesforceStandardObjectConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SalesforceStandardObjectConfiguration
<a name="API_SalesforceStandardObjectConfiguration"></a>

Provides the configuration information for indexing a single standard object.

## Contents
<a name="API_SalesforceStandardObjectConfiguration_Contents"></a>

 ** DocumentDataFieldName **   <a name="kendra-Type-SalesforceStandardObjectConfiguration-DocumentDataFieldName"></a>
The name of the field in the standard object table that contains the document contents.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `^[a-zA-Z][a-zA-Z0-9_.]*$`   
Required: Yes

 ** Name **   <a name="kendra-Type-SalesforceStandardObjectConfiguration-Name"></a>
The name of the standard object.  
Type: String  
Valid Values: `ACCOUNT | CAMPAIGN | CASE | CONTACT | CONTRACT | DOCUMENT | GROUP | IDEA | LEAD | OPPORTUNITY | PARTNER | PRICEBOOK | PRODUCT | PROFILE | SOLUTION | TASK | USER`   
Required: Yes

 ** DocumentTitleFieldName **   <a name="kendra-Type-SalesforceStandardObjectConfiguration-DocumentTitleFieldName"></a>
The name of the field in the standard object table that contains the document title.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `^[a-zA-Z][a-zA-Z0-9_.]*$`   
Required: No

 ** FieldMappings **   <a name="kendra-Type-SalesforceStandardObjectConfiguration-FieldMappings"></a>
Maps attributes or field names of the standard object to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to Salesforce fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html). The Salesforce data source field names must exist in your Salesforce custom metadata.  
Type: Array of [DataSourceToIndexFieldMapping](API_DataSourceToIndexFieldMapping.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 100 items.  
Required: No

## See Also
<a name="API_SalesforceStandardObjectConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/SalesforceStandardObjectConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/SalesforceStandardObjectConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/SalesforceStandardObjectConfiguration) 