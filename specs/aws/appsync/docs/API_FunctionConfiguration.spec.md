---
id: "@specs/aws/appsync/docs/API_FunctionConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS FunctionConfiguration"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# FunctionConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_FunctionConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# FunctionConfiguration
<a name="API_FunctionConfiguration"></a>

A function is a reusable entity. You can use multiple functions to compose the resolver logic.

## Contents
<a name="API_FunctionConfiguration_Contents"></a>

 ** code **   <a name="appsync-Type-FunctionConfiguration-code"></a>
The `function` code that contains the request and response functions. When code is used, the `runtime` is required. The `runtime` value must be `APPSYNC_JS`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 32768.  
Required: No

 ** dataSourceName **   <a name="appsync-Type-FunctionConfiguration-dataSourceName"></a>
The name of the `DataSource`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 65536.  
Pattern: `[_A-Za-z][_0-9A-Za-z]*`   
Required: No

 ** description **   <a name="appsync-Type-FunctionConfiguration-description"></a>
The `Function` description.  
Type: String  
Required: No

 ** functionArn **   <a name="appsync-Type-FunctionConfiguration-functionArn"></a>
The Amazon Resource Name (ARN) of the `Function` object.  
Type: String  
Required: No

 ** functionId **   <a name="appsync-Type-FunctionConfiguration-functionId"></a>
A unique ID representing the `Function` object.  
Type: String  
Required: No

 ** functionVersion **   <a name="appsync-Type-FunctionConfiguration-functionVersion"></a>
The version of the request mapping template. Currently, only the 2018-05-29 version of the template is supported.  
Type: String  
Required: No

 ** maxBatchSize **   <a name="appsync-Type-FunctionConfiguration-maxBatchSize"></a>
The maximum batching size for a resolver.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 2000.  
Required: No

 ** name **   <a name="appsync-Type-FunctionConfiguration-name"></a>
The name of the `Function` object.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 65536.  
Pattern: `[_A-Za-z][_0-9A-Za-z]*`   
Required: No

 ** requestMappingTemplate **   <a name="appsync-Type-FunctionConfiguration-requestMappingTemplate"></a>
The `Function` request mapping template. Functions support only the 2018-05-29 version of the request mapping template.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 65536.  
Pattern: `^.*$`   
Required: No

 ** responseMappingTemplate **   <a name="appsync-Type-FunctionConfiguration-responseMappingTemplate"></a>
The `Function` response mapping template.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 65536.  
Pattern: `^.*$`   
Required: No

 ** runtime **   <a name="appsync-Type-FunctionConfiguration-runtime"></a>
Describes a runtime used by an AWS AppSync pipeline resolver or AWS AppSync function. Specifies the name and version of the runtime to use. Note that if a runtime is specified, code must also be specified.  
Type: [AppSyncRuntime](API_AppSyncRuntime.md) object  
Required: No

 ** syncConfig **   <a name="appsync-Type-FunctionConfiguration-syncConfig"></a>
Describes a Sync configuration for a resolver.  
Specifies which Conflict Detection strategy and Resolution strategy to use when the resolver is invoked.  
Type: [SyncConfig](API_SyncConfig.md) object  
Required: No

## See Also
<a name="API_FunctionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/FunctionConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/FunctionConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/FunctionConfiguration) 