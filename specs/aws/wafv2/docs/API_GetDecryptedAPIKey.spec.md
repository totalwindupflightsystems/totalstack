---
id: "@specs/aws/wafv2/docs/API_GetDecryptedAPIKey"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetDecryptedAPIKey"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# GetDecryptedAPIKey

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_GetDecryptedAPIKey
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetDecryptedAPIKey
<a name="API_GetDecryptedAPIKey"></a>

Returns your API key in decrypted form. Use this to check the token domains that you have defined for the key. 

API keys are required for the integration of the CAPTCHA API in your JavaScript client applications. The API lets you customize the placement and characteristics of the CAPTCHA puzzle for your end users. For more information about the CAPTCHA JavaScript integration, see [AWS WAF client application integration](https://docs.aws.amazon.com/waf/latest/developerguide/waf-application-integration.html) in the * AWS WAF Developer Guide*.

## Request Syntax
<a name="API_GetDecryptedAPIKey_RequestSyntax"></a>

```
{
   "APIKey": "{{string}}",
   "Scope": "{{string}}"
}
```

## Request Parameters
<a name="API_GetDecryptedAPIKey_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [APIKey](#API_GetDecryptedAPIKey_RequestSyntax) **   <a name="WAF-GetDecryptedAPIKey-request-APIKey"></a>
The encrypted API key.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `.*\S.*`   
Required: Yes

 ** [Scope](#API_GetDecryptedAPIKey_RequestSyntax) **   <a name="WAF-GetDecryptedAPIKey-request-Scope"></a>
Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an AWS Amplify application, use `CLOUDFRONT`.  
To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:   
+ CLI - Specify the Region when you use the CloudFront scope: `--scope=CLOUDFRONT --region=us-east-1`. 
+ API and SDKs - For all calls, use the Region endpoint us-east-1. 
Type: String  
Valid Values: `CLOUDFRONT | REGIONAL`   
Required: Yes

## Response Syntax
<a name="API_GetDecryptedAPIKey_ResponseSyntax"></a>

```
{
   "CreationTimestamp": number,
   "TokenDomains": [ "string" ]
}
```

## Response Elements
<a name="API_GetDecryptedAPIKey_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreationTimestamp](#API_GetDecryptedAPIKey_ResponseSyntax) **   <a name="WAF-GetDecryptedAPIKey-response-CreationTimestamp"></a>
The date and time that the key was created.   
Type: Timestamp

 ** [TokenDomains](#API_GetDecryptedAPIKey_ResponseSyntax) **   <a name="WAF-GetDecryptedAPIKey-response-TokenDomains"></a>
The token domains that are defined in this API key.   
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 253.  
Pattern: `^[\w\.\-/]+$` 

## Errors
<a name="API_GetDecryptedAPIKey_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** WAFInternalErrorException **   
Your request is valid, but AWS WAF couldn’t perform the operation because of a system problem. Retry your request.   
HTTP Status Code: 500

 ** WAFInvalidOperationException **   
The operation isn't valid.   
HTTP Status Code: 400

 ** WAFInvalidParameterException **   
The operation failed because AWS WAF didn't recognize a parameter in the request. For example:   
+ You specified a parameter name or value that isn't valid.
+ Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. 
+ You tried to update a `WebACL` with a `DefaultAction` that isn't among the types available at [DefaultAction](API_DefaultAction.md).
+ Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.  
 ** Field **   
The settings where the invalid parameter was found.   
 ** Parameter **   
The invalid parameter that resulted in the exception.   
 ** Reason **   
Additional information about the exception.
HTTP Status Code: 400

 ** WAFInvalidResourceException **   
 AWS WAF couldn’t perform the operation because the resource that you requested isn’t valid. Check the resource, and try again.  
HTTP Status Code: 400

 ** WAFNonexistentItemException **   
 AWS WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate.   
HTTP Status Code: 400

## See Also
<a name="API_GetDecryptedAPIKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wafv2-2019-07-29/GetDecryptedAPIKey) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wafv2-2019-07-29/GetDecryptedAPIKey) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/GetDecryptedAPIKey) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wafv2-2019-07-29/GetDecryptedAPIKey) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/GetDecryptedAPIKey) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wafv2-2019-07-29/GetDecryptedAPIKey) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wafv2-2019-07-29/GetDecryptedAPIKey) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wafv2-2019-07-29/GetDecryptedAPIKey) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/wafv2-2019-07-29/GetDecryptedAPIKey) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/GetDecryptedAPIKey) 