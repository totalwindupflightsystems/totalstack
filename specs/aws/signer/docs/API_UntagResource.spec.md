---
id: "@specs/aws/signer/docs/API_UntagResource"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UntagResource"
status: active
depends_on:
  - "@specs/aws/signer/meta"
---

# UntagResource

> **source:** AWS Documentation
> **spec:id:** @specs/aws/signer/docs/API_UntagResource
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UntagResource
<a name="API_UntagResource"></a>

Removes one or more tags from a signing profile. To remove the tags, specify a list of tag keys.

## Request Syntax
<a name="API_UntagResource_RequestSyntax"></a>

```
DELETE /tags/{{resourceArn}}?tagKeys={{tagKeys}} HTTP/1.1
```

## URI Request Parameters
<a name="API_UntagResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceArn](#API_UntagResource_RequestSyntax) **   <a name="signer-UntagResource-request-uri-resourceArn"></a>
The Amazon Resource Name (ARN) for the signing profile.  
Required: Yes

 ** [tagKeys](#API_UntagResource_RequestSyntax) **   <a name="signer-UntagResource-request-uri-tagKeys"></a>
A list of tag keys to be removed from the signing profile.  
Array Members: Minimum number of 1 item. Maximum number of 200 items.  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`   
Required: Yes

## Request Body
<a name="API_UntagResource_RequestBody"></a>

The request does not have a request body.

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

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
The request contains invalid parameters for the ARN or tags. This exception also occurs when you call a tagging API on a cancelled signing profile.  
HTTP Status Code: 400

 ** InternalServiceErrorException **   
An internal error occurred.  
HTTP Status Code: 500

 ** NotFoundException **   
The signing profile was not found.  
HTTP Status Code: 404

 ** TooManyRequestsException **   
The allowed number of job-signing requests has been exceeded.  
This error supersedes the error `ThrottlingException`.  
HTTP Status Code: 429

## See Also
<a name="API_UntagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/signer-2017-08-25/UntagResource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/signer-2017-08-25/UntagResource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signer-2017-08-25/UntagResource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/signer-2017-08-25/UntagResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signer-2017-08-25/UntagResource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/signer-2017-08-25/UntagResource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/signer-2017-08-25/UntagResource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/signer-2017-08-25/UntagResource) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/signer-2017-08-25/UntagResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signer-2017-08-25/UntagResource) 