---
id: "@specs/aws/appsync/docs/API_DataSourceIntrospectionResult"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DataSourceIntrospectionResult"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# DataSourceIntrospectionResult

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_DataSourceIntrospectionResult
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DataSourceIntrospectionResult
<a name="API_DataSourceIntrospectionResult"></a>

Represents the output of a `DataSourceIntrospectionResult`. This is the populated result of a `GetDataSourceIntrospection` operation.

## Contents
<a name="API_DataSourceIntrospectionResult_Contents"></a>

 ** models **   <a name="appsync-Type-DataSourceIntrospectionResult-models"></a>
The array of `DataSourceIntrospectionModel` objects.  
Type: Array of [DataSourceIntrospectionModel](API_DataSourceIntrospectionModel.md) objects  
Required: No

 ** nextToken **   <a name="appsync-Type-DataSourceIntrospectionResult-nextToken"></a>
Determines the number of types to be returned in a single response before paginating. This value is typically taken from `nextToken` value from the previous response.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 65536.  
Pattern: `[\S]+`   
Required: No

## See Also
<a name="API_DataSourceIntrospectionResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/DataSourceIntrospectionResult) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/DataSourceIntrospectionResult) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/DataSourceIntrospectionResult) 