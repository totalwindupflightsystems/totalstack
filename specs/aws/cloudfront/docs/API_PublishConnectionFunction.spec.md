---
id: "@specs/aws/cloudfront/docs/API_PublishConnectionFunction"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PublishConnectionFunction"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# PublishConnectionFunction

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_PublishConnectionFunction
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PublishConnectionFunction
<a name="API_PublishConnectionFunction"></a>

Publishes a connection function.

## Request Syntax
<a name="API_PublishConnectionFunction_RequestSyntax"></a>

```
POST /2020-05-31/connection-function/{{Id}}/publish HTTP/1.1
If-Match: {{IfMatch}}
```

## URI Request Parameters
<a name="API_PublishConnectionFunction_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_PublishConnectionFunction_RequestSyntax) **   <a name="cloudfront-PublishConnectionFunction-request-uri-Id"></a>
The connection function ID.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Required: Yes

 ** [If-Match](#API_PublishConnectionFunction_RequestSyntax) **   <a name="cloudfront-PublishConnectionFunction-request-IfMatch"></a>
The current version (`ETag` value) of the connection function.  
Required: Yes

## Request Body
<a name="API_PublishConnectionFunction_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_PublishConnectionFunction_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ConnectionFunctionSummary>
   <ConnectionFunctionArn>string</ConnectionFunctionArn>
   <ConnectionFunctionConfig>
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
   </ConnectionFunctionConfig>
   <CreatedTime>timestamp</CreatedTime>
   <Id>string</Id>
   <LastModifiedTime>timestamp</LastModifiedTime>
   <Name>string</Name>
   <Stage>string</Stage>
   <Status>string</Status>
</ConnectionFunctionSummary>
```

## Response Elements
<a name="API_PublishConnectionFunction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ConnectionFunctionSummary](#API_PublishConnectionFunction_ResponseSyntax) **   <a name="cloudfront-PublishConnectionFunction-response-ConnectionFunctionSummary"></a>
Root level tag for the ConnectionFunctionSummary parameters.  
Required: Yes

 ** [ConnectionFunctionArn](#API_PublishConnectionFunction_ResponseSyntax) **   <a name="cloudfront-PublishConnectionFunction-response-ConnectionFunctionArn"></a>
The connection function Amazon Resource Name (ARN).  
Type: String

 ** [ConnectionFunctionConfig](#API_PublishConnectionFunction_ResponseSyntax) **   <a name="cloudfront-PublishConnectionFunction-response-ConnectionFunctionConfig"></a>
Contains configuration information about a CloudFront function.  
Type: [FunctionConfig](API_FunctionConfig.md) object

 ** [CreatedTime](#API_PublishConnectionFunction_ResponseSyntax) **   <a name="cloudfront-PublishConnectionFunction-response-CreatedTime"></a>
The connection function created time.  
Type: Timestamp

 ** [Id](#API_PublishConnectionFunction_ResponseSyntax) **   <a name="cloudfront-PublishConnectionFunction-response-Id"></a>
The connection function ID.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [LastModifiedTime](#API_PublishConnectionFunction_ResponseSyntax) **   <a name="cloudfront-PublishConnectionFunction-response-LastModifiedTime"></a>
The connection function last modified time.  
Type: Timestamp

 ** [Name](#API_PublishConnectionFunction_ResponseSyntax) **   <a name="cloudfront-PublishConnectionFunction-response-Name"></a>
The connection function name.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9-_]{1,64}` 

 ** [Stage](#API_PublishConnectionFunction_ResponseSyntax) **   <a name="cloudfront-PublishConnectionFunction-response-Stage"></a>
The connection function stage.  
Type: String  
Valid Values: `DEVELOPMENT | LIVE` 

 ** [Status](#API_PublishConnectionFunction_ResponseSyntax) **   <a name="cloudfront-PublishConnectionFunction-response-Status"></a>
The connection function status.  
Type: String

## Errors
<a name="API_PublishConnectionFunction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDenied **   
Access denied.  
HTTP Status Code: 403

 ** EntityAlreadyExists **   
The entity already exists. You must provide a unique entity.  
HTTP Status Code: 409

 ** EntityNotFound **   
The entity was not found.  
HTTP Status Code: 404

 ** InvalidArgument **   
An argument is invalid.  
HTTP Status Code: 400

 ** InvalidIfMatchVersion **   
The `If-Match` version is missing or not valid.  
HTTP Status Code: 400

 ** PreconditionFailed **   
The precondition in one or more of the request fields evaluated to `false`.  
HTTP Status Code: 412

 ** UnsupportedOperation **   
This operation is not supported in this AWS Region.  
HTTP Status Code: 400

## See Also
<a name="API_PublishConnectionFunction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/PublishConnectionFunction) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/PublishConnectionFunction) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/PublishConnectionFunction) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/PublishConnectionFunction) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/PublishConnectionFunction) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/PublishConnectionFunction) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/PublishConnectionFunction) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/PublishConnectionFunction) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/PublishConnectionFunction) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/PublishConnectionFunction) 