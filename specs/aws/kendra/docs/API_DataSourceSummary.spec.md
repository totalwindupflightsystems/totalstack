---
id: "@specs/aws/kendra/docs/API_DataSourceSummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DataSourceSummary"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# DataSourceSummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_DataSourceSummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DataSourceSummary
<a name="API_DataSourceSummary"></a>

Summary information for a Amazon Kendra data source.

## Contents
<a name="API_DataSourceSummary_Contents"></a>

 ** CreatedAt **   <a name="kendra-Type-DataSourceSummary-CreatedAt"></a>
The Unix timestamp when the data source connector was created.  
Type: Timestamp  
Required: No

 ** Id **   <a name="kendra-Type-DataSourceSummary-Id"></a>
The identifier for the data source.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`   
Required: No

 ** LanguageCode **   <a name="kendra-Type-DataSourceSummary-LanguageCode"></a>
The code for a language. This shows a supported language for all documents in the data source. English is supported by default. For more information on supported languages, including their codes, see [Adding documents in languages other than English](https://docs.aws.amazon.com/kendra/latest/dg/in-adding-languages.html).  
Type: String  
Length Constraints: Minimum length of 2. Maximum length of 10.  
Pattern: `[a-zA-Z-]*`   
Required: No

 ** Name **   <a name="kendra-Type-DataSourceSummary-Name"></a>
The name of the data source.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1000.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`   
Required: No

 ** Status **   <a name="kendra-Type-DataSourceSummary-Status"></a>
The status of the data source. When the status is `ACTIVE` the data source is ready to use.  
Type: String  
Valid Values: `CREATING | DELETING | FAILED | UPDATING | ACTIVE`   
Required: No

 ** Type **   <a name="kendra-Type-DataSourceSummary-Type"></a>
The type of the data source.  
Type: String  
Valid Values: `S3 | SHAREPOINT | DATABASE | SALESFORCE | ONEDRIVE | SERVICENOW | CUSTOM | CONFLUENCE | GOOGLEDRIVE | WEBCRAWLER | WORKDOCS | FSX | SLACK | BOX | QUIP | JIRA | GITHUB | ALFRESCO | TEMPLATE`   
Required: No

 ** UpdatedAt **   <a name="kendra-Type-DataSourceSummary-UpdatedAt"></a>
The Unix timestamp when the data source connector was last updated.  
Type: Timestamp  
Required: No

## See Also
<a name="API_DataSourceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/DataSourceSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/DataSourceSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/DataSourceSummary) 