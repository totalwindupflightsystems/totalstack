---
id: "@specs/aws/cloudfront/docs/API_UpdateFunction"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateFunction"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# UpdateFunction

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_UpdateFunction
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateFunction
<a name="API_UpdateFunction"></a>

Updates a CloudFront function.

You can update a function's code or the comment that describes the function. You cannot update a function's name.

To update a function, you provide the function's name and version (`ETag` value) along with the updated function code. To get the name and version, you can use `ListFunctions` and `DescribeFunction`.

## Request Syntax
<a name="API_UpdateFunction_RequestSyntax"></a>

```
PUT /2020-05-31/function/{{Name}} HTTP/1.1
If-Match: {{IfMatch}}
<?xml version="1.0" encoding="UTF-8"?>
<UpdateFunctionRequest xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
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
</UpdateFunctionRequest>
```

## URI Request Parameters
<a name="API_UpdateFunction_RequestParameters"></a>

The request uses the following URI parameters.

 ** [If-Match](#API_UpdateFunction_RequestSyntax) **   <a name="cloudfront-UpdateFunction-request-IfMatch"></a>
The current version (`ETag` value) of the function that you are updating, which you can get using `DescribeFunction`.  
Required: Yes

 ** [Name](#API_UpdateFunction_RequestSyntax) **   <a name="cloudfront-UpdateFunction-request-uri-Name"></a>
The name of the function that you are updating.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9-_]{1,64}`   
Required: Yes

## Request Body
<a name="API_UpdateFunction_RequestBody"></a>

The request accepts the following data in XML format.

 ** [UpdateFunctionRequest](#API_UpdateFunction_RequestSyntax) **   <a name="cloudfront-UpdateFunction-request-UpdateFunctionRequest"></a>
Root level tag for the UpdateFunctionRequest parameters.  
Required: Yes

 ** [FunctionCode](#API_UpdateFunction_RequestSyntax) **   <a name="cloudfront-UpdateFunction-request-FunctionCode"></a>
The function code. For more information about writing a CloudFront function, see [Writing function code for CloudFront Functions](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/writing-function-code.html) in the *Amazon CloudFront Developer Guide*.  
Type: Base64-encoded binary data object  
Length Constraints: Minimum length of 1. Maximum length of 40960.  
Required: Yes

 ** [FunctionConfig](#API_UpdateFunction_RequestSyntax) **   <a name="cloudfront-UpdateFunction-request-FunctionConfig"></a>
Configuration information about the function.  
Type: [FunctionConfig](API_FunctionConfig.md) object  
Required: Yes

## Response Syntax
<a name="API_UpdateFunction_ResponseSyntax"></a>

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
<a name="API_UpdateFunction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [FunctionSummary](#API_UpdateFunction_ResponseSyntax) **   <a name="cloudfront-UpdateFunction-response-FunctionSummary"></a>
Root level tag for the FunctionSummary parameters.  
Required: Yes

 ** [FunctionConfig](#API_UpdateFunction_ResponseSyntax) **   <a name="cloudfront-UpdateFunction-response-FunctionConfig"></a>
Contains configuration information about a CloudFront function.  
Type: [FunctionConfig](API_FunctionConfig.md) object

 ** [FunctionMetadata](#API_UpdateFunction_ResponseSyntax) **   <a name="cloudfront-UpdateFunction-response-FunctionMetadata"></a>
Contains metadata about a CloudFront function.  
Type: [FunctionMetadata](API_FunctionMetadata.md) object

 ** [Name](#API_UpdateFunction_ResponseSyntax) **   <a name="cloudfront-UpdateFunction-response-Name"></a>
The name of the CloudFront function.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9-_]{1,64}` 

 ** [Status](#API_UpdateFunction_ResponseSyntax) **   <a name="cloudfront-UpdateFunction-response-Status"></a>
The status of the CloudFront function.  
Type: String

## Errors
<a name="API_UpdateFunction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** FunctionSizeLimitExceeded **   
The function is too large. For more information, see [Quotas](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html) (formerly known as limits) in the *Amazon CloudFront Developer Guide*.  
HTTP Status Code: 413

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
<a name="API_UpdateFunction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/UpdateFunction) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/UpdateFunction) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/UpdateFunction) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/UpdateFunction) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/UpdateFunction) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/UpdateFunction) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/UpdateFunction) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/UpdateFunction) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/UpdateFunction) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/UpdateFunction) 