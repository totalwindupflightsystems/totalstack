---
id: "@specs/aws/appsync/docs/API_DataSourceIntrospectionModel"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DataSourceIntrospectionModel"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# DataSourceIntrospectionModel

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_DataSourceIntrospectionModel
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DataSourceIntrospectionModel
<a name="API_DataSourceIntrospectionModel"></a>

Contains the introspected data that was retrieved from the data source.

## Contents
<a name="API_DataSourceIntrospectionModel_Contents"></a>

 ** fields **   <a name="appsync-Type-DataSourceIntrospectionModel-fields"></a>
The `DataSourceIntrospectionModelField` object data.  
Type: Array of [DataSourceIntrospectionModelField](API_DataSourceIntrospectionModelField.md) objects  
Required: No

 ** indexes **   <a name="appsync-Type-DataSourceIntrospectionModel-indexes"></a>
The array of `DataSourceIntrospectionModelIndex` objects.  
Type: Array of [DataSourceIntrospectionModelIndex](API_DataSourceIntrospectionModelIndex.md) objects  
Required: No

 ** name **   <a name="appsync-Type-DataSourceIntrospectionModel-name"></a>
The name of the model. For example, this could be the name of a single table in a database.  
Type: String  
Required: No

 ** primaryKey **   <a name="appsync-Type-DataSourceIntrospectionModel-primaryKey"></a>
The primary key stored as a `DataSourceIntrospectionModelIndex` object.  
Type: [DataSourceIntrospectionModelIndex](API_DataSourceIntrospectionModelIndex.md) object  
Required: No

 ** sdl **   <a name="appsync-Type-DataSourceIntrospectionModel-sdl"></a>
Contains the output of the SDL that was generated from the introspected types. This is controlled by the `includeModelsSDL` parameter of the `GetDataSourceIntrospection` operation.  
Type: String  
Required: No

## See Also
<a name="API_DataSourceIntrospectionModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/DataSourceIntrospectionModel) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/DataSourceIntrospectionModel) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/DataSourceIntrospectionModel) 