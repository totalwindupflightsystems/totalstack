---
id: "@specs/aws/cloudfront/docs/API_GetFunction"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetFunction"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# GetFunction

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_GetFunction
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetFunction
<a name="API_GetFunction"></a>

Gets the code of a CloudFront function. To get configuration information and metadata about a function, use `DescribeFunction`.

To get a function's code, you must provide the function's name and stage. To get these values, you can use `ListFunctions`.

## Request Syntax
<a name="API_GetFunction_RequestSyntax"></a>

```
GET /2020-05-31/function/{{Name}}?Stage={{Stage}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetFunction_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Name](#API_GetFunction_RequestSyntax) **   <a name="cloudfront-GetFunction-request-uri-Name"></a>
The name of the function whose code you are getting.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9-_]{1,64}`   
Required: Yes

 ** [Stage](#API_GetFunction_RequestSyntax) **   <a name="cloudfront-GetFunction-request-uri-Stage"></a>
The function's stage, either `DEVELOPMENT` or `LIVE`.  
Valid Values: `DEVELOPMENT | LIVE` 

## Request Body
<a name="API_GetFunction_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetFunction_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_GetFunction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_GetFunction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** NoSuchFunctionExists **   
The function does not exist.  
HTTP Status Code: 404

 ** UnsupportedOperation **   
This operation is not supported in this AWS Region.  
HTTP Status Code: 400

## See Also
<a name="API_GetFunction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetFunction) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/GetFunction) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetFunction) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetFunction) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetFunction) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetFunction) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetFunction) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetFunction) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetFunction) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetFunction) 