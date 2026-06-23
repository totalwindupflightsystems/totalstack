---
id: "@specs/aws/appmesh/docs/API_UntagResource"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UntagResource"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# UntagResource

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_UntagResource
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UntagResource
<a name="API_UntagResource"></a>

Deletes specified tags from a resource.

## Request Syntax
<a name="API_UntagResource_RequestSyntax"></a>

```
PUT /v20190125/untag?resourceArn={{resourceArn}} HTTP/1.1
Content-type: application/json

{
   "tagKeys": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_UntagResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceArn](#API_UntagResource_RequestSyntax) **   <a name="appmesh-UntagResource-request-uri-resourceArn"></a>
The Amazon Resource Name (ARN) of the resource to delete tags from.  
Required: Yes

## Request Body
<a name="API_UntagResource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [tagKeys](#API_UntagResource_RequestSyntax) **   <a name="appmesh-UntagResource-request-tagKeys"></a>
The keys of the tags to be removed.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 50 items.  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Required: Yes

## Response Syntax
<a name="API_UntagResource_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UntagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UntagResource_Errors"></a>

 ** BadRequestException **   
The request syntax was malformed. Check your request syntax and try again.  
HTTP Status Code: 400

 ** ForbiddenException **   
You don't have permissions to perform this action.  
HTTP Status Code: 403

 ** InternalServerErrorException **   
The request processing has failed because of an unknown error, exception, or failure.  
HTTP Status Code: 500

 ** NotFoundException **   
The specified resource doesn't exist. Check your request syntax and try again.  
HTTP Status Code: 404

 ** ServiceUnavailableException **   
The request has failed due to a temporary failure of the service.  
HTTP Status Code: 503

 ** TooManyRequestsException **   
The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.  
HTTP Status Code: 429

## See Also
<a name="API_UntagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appmesh-2019-01-25/UntagResource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appmesh-2019-01-25/UntagResource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/UntagResource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appmesh-2019-01-25/UntagResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/UntagResource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appmesh-2019-01-25/UntagResource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appmesh-2019-01-25/UntagResource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appmesh-2019-01-25/UntagResource) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appmesh-2019-01-25/UntagResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/UntagResource) 