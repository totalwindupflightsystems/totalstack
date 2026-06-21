---
id: "@specs/aws/cloudfront/docs/API_DeleteFunction"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteFunction"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# DeleteFunction

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_DeleteFunction
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteFunction
<a name="API_DeleteFunction"></a>

Deletes a CloudFront function.

You cannot delete a function if it's associated with a cache behavior. First, update your distributions to remove the function association from all cache behaviors, then delete the function.

To delete a function, you must provide the function's name and version (`ETag` value). To get these values, you can use `ListFunctions` and `DescribeFunction`.

## Request Syntax
<a name="API_DeleteFunction_RequestSyntax"></a>

```
DELETE /2020-05-31/function/{{Name}} HTTP/1.1
If-Match: {{IfMatch}}
```

## URI Request Parameters
<a name="API_DeleteFunction_RequestParameters"></a>

The request uses the following URI parameters.

 ** [If-Match](#API_DeleteFunction_RequestSyntax) **   <a name="cloudfront-DeleteFunction-request-IfMatch"></a>
The current version (`ETag` value) of the function that you are deleting, which you can get using `DescribeFunction`.  
Required: Yes

 ** [Name](#API_DeleteFunction_RequestSyntax) **   <a name="cloudfront-DeleteFunction-request-uri-Name"></a>
The name of the function that you are deleting.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9-_]{1,64}`   
Required: Yes

## Request Body
<a name="API_DeleteFunction_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteFunction_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteFunction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteFunction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** FunctionInUse **   
Cannot delete the function because it's attached to one or more cache behaviors.  
HTTP Status Code: 409

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
<a name="API_DeleteFunction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/DeleteFunction) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/DeleteFunction) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/DeleteFunction) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/DeleteFunction) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/DeleteFunction) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/DeleteFunction) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/DeleteFunction) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/DeleteFunction) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/DeleteFunction) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/DeleteFunction) 