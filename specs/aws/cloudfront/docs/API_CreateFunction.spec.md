---
id: "@specs/aws/cloudfront/docs/API_CreateFunction"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateFunction"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# CreateFunction

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_CreateFunction
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateFunction
<a name="API_CreateFunction"></a>

Creates a CloudFront function.

To create a function, you provide the function code and some configuration information about the function. The response contains an Amazon Resource Name (ARN) that uniquely identifies the function.

When you create a function, it's in the `DEVELOPMENT` stage. In this stage, you can test the function with `TestFunction`, and update it with `UpdateFunction`.

When you're ready to use your function with a CloudFront distribution, use `PublishFunction` to copy the function from the `DEVELOPMENT` stage to `LIVE`. When it's live, you can attach the function to a distribution's cache behavior, using the function's ARN.

## Request Syntax
<a name="API_CreateFunction_RequestSyntax"></a>

```
POST /2020-05-31/function HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<CreateFunctionRequest xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <FunctionCode>{{blob}}</FunctionCode>
   <FunctionConfig>
      <Comment>{{string}}</Comment>
      <KeyValueStoreAssociations>
         <Items>
            <KeyValueStoreAssociation>
               <KeyValueStoreARN>{{string}}</KeyValueStoreARN>
            </KeyValueStoreAssociation>
         </Items>
         <Quantity>{{integer}}</Quantity>
      </KeyValueStoreAssociations>
      <Runtime>{{string}}</Runtime>
   </FunctionConfig>
   <Name>{{string}}</Name>
   <Tags>
      <Items>
         <Tag>
            <Key>{{string}}</Key>
            <Value>{{string}}</Value>
         </Tag>
      </Items>
   </Tags>
</CreateFunctionRequest>
```

## URI Request Parameters
<a name="API_CreateFunction_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateFunction_RequestBody"></a>

The request accepts the following data in XML format.

 ** [CreateFunctionRequest](#API_CreateFunction_RequestSyntax) **   <a name="cloudfront-CreateFunction-request-CreateFunctionRequest"></a>
Root level tag for the CreateFunctionRequest parameters.  
Required: Yes

 ** [FunctionCode](#API_CreateFunction_RequestSyntax) **   <a name="cloudfront-CreateFunction-request-FunctionCode"></a>
The function code. For more information about writing a CloudFront function, see [Writing function code for CloudFront Functions](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/writing-function-code.html) in the *Amazon CloudFront Developer Guide*.  
Type: Base64-encoded binary data object  
Length Constraints: Minimum length of 1. Maximum length of 40960.  
Required: Yes

 ** [FunctionConfig](#API_CreateFunction_RequestSyntax) **   <a name="cloudfront-CreateFunction-request-FunctionConfig"></a>
Configuration information about the function, including an optional comment and the function's runtime.  
Type: [FunctionConfig](API_FunctionConfig.md) object  
Required: Yes

 ** [Name](#API_CreateFunction_RequestSyntax) **   <a name="cloudfront-CreateFunction-request-Name"></a>
A name to identify the function.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9-_]{1,64}`   
Required: Yes

 ** [Tags](#API_CreateFunction_RequestSyntax) **   <a name="cloudfront-CreateFunction-request-Tags"></a>
A complex type that contains zero or more `Tag` elements.  
Type: [Tags](API_Tags.md) object  
Required: No

## Response Syntax
<a name="API_CreateFunction_ResponseSyntax"></a>

```
HTTP/1.1 201
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
<a name="API_CreateFunction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in XML format by the service.

 ** [FunctionSummary](#API_CreateFunction_ResponseSyntax) **   <a name="cloudfront-CreateFunction-response-FunctionSummary"></a>
Root level tag for the FunctionSummary parameters.  
Required: Yes

 ** [FunctionConfig](#API_CreateFunction_ResponseSyntax) **   <a name="cloudfront-CreateFunction-response-FunctionConfig"></a>
Contains configuration information about a CloudFront function.  
Type: [FunctionConfig](API_FunctionConfig.md) object

 ** [FunctionMetadata](#API_CreateFunction_ResponseSyntax) **   <a name="cloudfront-CreateFunction-response-FunctionMetadata"></a>
Contains metadata about a CloudFront function.  
Type: [FunctionMetadata](API_FunctionMetadata.md) object

 ** [Name](#API_CreateFunction_ResponseSyntax) **   <a name="cloudfront-CreateFunction-response-Name"></a>
The name of the CloudFront function.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9-_]{1,64}` 

 ** [Status](#API_CreateFunction_ResponseSyntax) **   <a name="cloudfront-CreateFunction-response-Status"></a>
The status of the CloudFront function.  
Type: String

## Errors
<a name="API_CreateFunction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** FunctionAlreadyExists **   
A function with the same name already exists in this AWS account. To create a function, you must provide a unique name. To update an existing function, use `UpdateFunction`.  
HTTP Status Code: 409

 ** FunctionSizeLimitExceeded **   
The function is too large. For more information, see [Quotas](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html) (formerly known as limits) in the *Amazon CloudFront Developer Guide*.  
HTTP Status Code: 413

 ** InvalidArgument **   
An argument is invalid.  
HTTP Status Code: 400

 ** InvalidTagging **   
The tagging specified is not valid.  
HTTP Status Code: 400

 ** TaggingConflict **   
The request to create a CloudFront function with tags could not be completed due to a tagging conflict. This can occur when orphaned tag entries exist from a previous failed function creation or deletion. To resolve this, retry the request without tags (including stack-level tags if using CloudFormation), use a different function name, or try again later.  
HTTP Status Code: 409

 ** TooManyFunctions **   
You have reached the maximum number of CloudFront functions for this AWS account. For more information, see [Quotas](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html) (formerly known as limits) in the *Amazon CloudFront Developer Guide*.  
HTTP Status Code: 400

 ** UnsupportedOperation **   
This operation is not supported in this AWS Region.  
HTTP Status Code: 400

## See Also
<a name="API_CreateFunction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/CreateFunction) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/CreateFunction) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CreateFunction) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/CreateFunction) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CreateFunction) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/CreateFunction) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/CreateFunction) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/CreateFunction) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/CreateFunction) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CreateFunction) 