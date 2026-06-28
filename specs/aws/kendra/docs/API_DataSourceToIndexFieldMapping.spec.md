---
id: "@specs/aws/kendra/docs/API_DataSourceToIndexFieldMapping"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DataSourceToIndexFieldMapping"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# DataSourceToIndexFieldMapping

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_DataSourceToIndexFieldMapping
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DataSourceToIndexFieldMapping
<a name="API_DataSourceToIndexFieldMapping"></a>

Maps attributes or field names of the documents synced from the data source to Amazon Kendra index field names. You can set up field mappings for each data source when calling [CreateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateDataSource.html) or [UpdateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UpdateDataSource.html) API. To create custom fields, use the `UpdateIndex` API to first create an index field and then map to the data source field. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html).

## Contents
<a name="API_DataSourceToIndexFieldMapping_Contents"></a>

 ** DataSourceFieldName **   <a name="kendra-Type-DataSourceToIndexFieldMapping-DataSourceFieldName"></a>
The name of the field in the data source. You must first create the index field using the `UpdateIndex` API.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `^[a-zA-Z][a-zA-Z0-9_.]*$`   
Required: Yes

 ** IndexFieldName **   <a name="kendra-Type-DataSourceToIndexFieldMapping-IndexFieldName"></a>
The name of the index field to map to the data source field. The index field type must match the data source field type.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 30.  
Pattern: `^\P{C}*$`   
Required: Yes

 ** DateFieldFormat **   <a name="kendra-Type-DataSourceToIndexFieldMapping-DateFieldFormat"></a>
The format for date fields in the data source. If the field specified in `DataSourceFieldName` is a date field, you must specify the date format. If the field is not a date field, an exception is thrown.  
Type: String  
Length Constraints: Minimum length of 4. Maximum length of 40.  
Pattern: `^(?!\s).*(?<!\s)$`   
Required: No

## See Also
<a name="API_DataSourceToIndexFieldMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/DataSourceToIndexFieldMapping) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/DataSourceToIndexFieldMapping) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/DataSourceToIndexFieldMapping) 