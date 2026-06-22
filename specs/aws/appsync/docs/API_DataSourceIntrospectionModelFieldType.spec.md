---
id: "@specs/aws/appsync/docs/API_DataSourceIntrospectionModelFieldType"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DataSourceIntrospectionModelFieldType"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# DataSourceIntrospectionModelFieldType

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_DataSourceIntrospectionModelFieldType
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DataSourceIntrospectionModelFieldType
<a name="API_DataSourceIntrospectionModelFieldType"></a>

Represents the type data for each field retrieved from the introspection.

## Contents
<a name="API_DataSourceIntrospectionModelFieldType_Contents"></a>

 ** kind **   <a name="appsync-Type-DataSourceIntrospectionModelFieldType-kind"></a>
Specifies the classification of data. For example, this could be set to values like `Scalar` or `NonNull` to indicate a fundamental property of the field.  
Valid values include:  
+  `Scalar`: Indicates the value is a primitive type (scalar).
+  `NonNull`: Indicates the field cannot be `null`.
+  `List`: Indicates the field contains a list.
Type: String  
Required: No

 ** name **   <a name="appsync-Type-DataSourceIntrospectionModelFieldType-name"></a>
The name of the data type that represents the field. For example, `String` is a valid `name` value.  
Type: String  
Required: No

 ** type **   <a name="appsync-Type-DataSourceIntrospectionModelFieldType-type"></a>
The `DataSourceIntrospectionModelFieldType` object data. The `type` is only present if `DataSourceIntrospectionModelFieldType.kind` is set to `NonNull` or `List`.   
The `type` typically contains its own `kind` and `name` fields to represent the actual type data. For instance, `type` could contain a `kind` value of `Scalar` with a `name` value of `String`. The values `Scalar` and `String` will be collectively stored in the `values` field.  
Type: [DataSourceIntrospectionModelFieldType](#API_DataSourceIntrospectionModelFieldType) object  
Required: No

 ** values **   <a name="appsync-Type-DataSourceIntrospectionModelFieldType-values"></a>
The values of the `type` field. This field represents the AppSync data type equivalent of the introspected field.  
Type: Array of strings  
Required: No

## See Also
<a name="API_DataSourceIntrospectionModelFieldType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/DataSourceIntrospectionModelFieldType) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/DataSourceIntrospectionModelFieldType) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/DataSourceIntrospectionModelFieldType) 