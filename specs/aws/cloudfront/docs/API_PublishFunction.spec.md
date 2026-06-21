---
id: "@specs/aws/cloudfront/docs/API_PublishFunction"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PublishFunction"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# PublishFunction

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_PublishFunction
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PublishFunction
<a name="API_PublishFunction"></a>

Publishes a CloudFront function by copying the function code from the `DEVELOPMENT` stage to `LIVE`. This automatically updates all cache behaviors that are using this function to use the newly published copy in the `LIVE` stage.

When a function is published to the `LIVE` stage, you can attach the function to a distribution's cache behavior, using the function's Amazon Resource Name (ARN).

To publish a function, you must provide the function's name and version (`ETag` value). To get these values, you can use `ListFunctions` and `DescribeFunction`.

## Request Syntax
<a name="API_PublishFunction_RequestSyntax"></a>

```
POST /2020-05-31/function/{{Name}}/publish HTTP/1.1
If-Match: {{IfMatch}}
```

## URI Request Parameters
<a name="API_PublishFunction_RequestParameters"></a>

The request uses the following URI parameters.

 ** [If-Match](#API_PublishFunction_RequestSyntax) **   <a name="cloudfront-PublishFunction-request-IfMatch"></a>
The current version (`ETag` value) of the function that you are publishing, which you can get using `DescribeFunction`.  
Required: Yes

 ** [Name](#API_PublishFunction_RequestSyntax) **   <a name="cloudfront-PublishFunction-request-uri-Name"></a>
The name of the function that you are publishing.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9-_]{1,64}`   
Required: Yes

## Request Body
<a name="API_PublishFunction_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_PublishFunction_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<FunctionSummary>
   <FunctionConfig>
      <Comment>string</Comment>
      <KeyValueStoreAssociations>
         <Items>
            <KeyValueStoreAssociation>
               <KeyValueStoreARN>string</KeyValueStoreARN>
            </KeyValueStoreAssociation>
         </Items>
         <Quantity>integer</Quantity>
      </KeyValueStoreAssociations>
      <Runtime>string</Runtime>
   </FunctionConfig>
   <FunctionMetadata>
      <CreatedTime>timestamp</CreatedTime>
      <FunctionARN>string</FunctionARN>
      <LastModifiedTime>timestamp</LastModifiedTime>
      <Stage>string</Stage>
   </FunctionMetadata>
   <Name>string</Name>
   <Status>string</Status>
</FunctionSummary>
```

## Response Elements
<a name="API_PublishFunction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [FunctionSummary](#API_PublishFunction_ResponseSyntax) **   <a name="cloudfront-PublishFunction-response-FunctionSummary"></a>
Root level tag for the FunctionSummary parameters.  
Required: Yes

 ** [FunctionConfig](#API_PublishFunction_ResponseSyntax) **   <a name="cloudfront-PublishFunction-response-FunctionConfig"></a>
Contains configuration information about a CloudFront function.  
Type: [FunctionConfig](API_FunctionConfig.md) object

 ** [FunctionMetadata](#API_PublishFunction_ResponseSyntax) **   <a name="cloudfront-PublishFunction-response-FunctionMetadata"></a>
Contains metadata about a CloudFront function.  
Type: [FunctionMetadata](API_FunctionMetadata.md) object

 ** [Name](#API_PublishFunction_ResponseSyntax) **   <a name="cloudfront-PublishFunction-response-Name"></a>
The name of the CloudFront function.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9-_]{1,64}` 

 ** [Status](#API_PublishFunction_ResponseSyntax) **   <a name="cloudfront-PublishFunction-response-Status"></a>
The status of the CloudFront function.  
Type: String

## Errors
<a name="API_PublishFunction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidArgument **   
An argument is invalid.  
HTTP Status Code: 400

 ** InvalidIfMatchVersion **   
The `If-Match` version is missing or not valid.  
HTTP Status Code: 400

 ** NoSuchFunctionExists **   
The function does not exist.  
HTTP Status Code: 404

 ** PreconditionFailed **   
The precondition in one or more of the request fields evaluated to `false`.  
HTTP Status Code: 412

 ** UnsupportedOperation **   
This operation is not supported in this AWS Region.  
HTTP Status Code: 400

## See Also
<a name="API_PublishFunction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/PublishFunction) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/PublishFunction) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/PublishFunction) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/PublishFunction) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/PublishFunction) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/PublishFunction) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/PublishFunction) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/PublishFunction) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/PublishFunction) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/PublishFunction) 