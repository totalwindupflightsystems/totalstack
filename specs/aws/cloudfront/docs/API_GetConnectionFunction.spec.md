---
id: "@specs/aws/cloudfront/docs/API_GetConnectionFunction"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetConnectionFunction"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# GetConnectionFunction

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_GetConnectionFunction
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetConnectionFunction
<a name="API_GetConnectionFunction"></a>

Gets a connection function.

## Request Syntax
<a name="API_GetConnectionFunction_RequestSyntax"></a>

```
GET /2020-05-31/connection-function/{{Identifier}}?Stage={{Stage}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetConnectionFunction_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_GetConnectionFunction_RequestSyntax) **   <a name="cloudfront-GetConnectionFunction-request-uri-Identifier"></a>
The connection function's identifier.  
Required: Yes

 ** [Stage](#API_GetConnectionFunction_RequestSyntax) **   <a name="cloudfront-GetConnectionFunction-request-uri-Stage"></a>
The connection function's stage.  
Valid Values: `DEVELOPMENT | LIVE` 

## Request Body
<a name="API_GetConnectionFunction_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetConnectionFunction_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_GetConnectionFunction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_GetConnectionFunction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDenied **   
Access denied.  
HTTP Status Code: 403

 ** EntityNotFound **   
The entity was not found.  
HTTP Status Code: 404

 ** UnsupportedOperation **   
This operation is not supported in this AWS Region.  
HTTP Status Code: 400

## See Also
<a name="API_GetConnectionFunction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetConnectionFunction) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/GetConnectionFunction) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetConnectionFunction) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetConnectionFunction) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetConnectionFunction) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetConnectionFunction) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetConnectionFunction) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetConnectionFunction) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetConnectionFunction) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetConnectionFunction) 