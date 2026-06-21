---
id: "@specs/aws/wafv2/docs/API_ListAPIKeys"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListAPIKeys"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# ListAPIKeys

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_ListAPIKeys
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListAPIKeys
<a name="API_ListAPIKeys"></a>

Retrieves a list of the API keys that you've defined for the specified scope. 

API keys are required for the integration of the CAPTCHA API in your JavaScript client applications. The API lets you customize the placement and characteristics of the CAPTCHA puzzle for your end users. For more information about the CAPTCHA JavaScript integration, see [AWS WAF client application integration](https://docs.aws.amazon.com/waf/latest/developerguide/waf-application-integration.html) in the * AWS WAF Developer Guide*.

## Request Syntax
<a name="API_ListAPIKeys_RequestSyntax"></a>

```
{
   "Limit": {{number}},
   "NextMarker": "{{string}}",
   "Scope": "{{string}}"
}
```

## Request Parameters
<a name="API_ListAPIKeys_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Limit](#API_ListAPIKeys_RequestSyntax) **   <a name="WAF-ListAPIKeys-request-Limit"></a>
The maximum number of objects that you want AWS WAF to return for this request. If more objects are available, in the response, AWS WAF provides a `NextMarker` value that you can use in a subsequent call to get the next batch of objects.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [NextMarker](#API_ListAPIKeys_RequestSyntax) **   <a name="WAF-ListAPIKeys-request-NextMarker"></a>
When you request a list of objects with a `Limit` setting, if the number of objects that are still available for retrieval exceeds the limit, AWS WAF returns a `NextMarker` value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `.*\S.*`   
Required: No

 ** [Scope](#API_ListAPIKeys_RequestSyntax) **   <a name="WAF-ListAPIKeys-request-Scope"></a>
Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an AWS Amplify application, use `CLOUDFRONT`.  
To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:   
+ CLI - Specify the Region when you use the CloudFront scope: `--scope=CLOUDFRONT --region=us-east-1`. 
+ API and SDKs - For all calls, use the Region endpoint us-east-1. 
Type: String  
Valid Values: `CLOUDFRONT | REGIONAL`   
Required: Yes

## Response Syntax
<a name="API_ListAPIKeys_ResponseSyntax"></a>

```
{
   "APIKeySummaries": [ 
      { 
         "APIKey": "string",
         "CreationTimestamp": number,
         "TokenDomains": [ "string" ],
         "Version": number
      }
   ],
   "ApplicationIntegrationURL": "string",
   "NextMarker": "string"
}
```

## Response Elements
<a name="API_ListAPIKeys_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [APIKeySummaries](#API_ListAPIKeys_ResponseSyntax) **   <a name="WAF-ListAPIKeys-response-APIKeySummaries"></a>
The array of key summaries. If you specified a `Limit` in your request, this might not be the full list.   
Type: Array of [APIKeySummary](API_APIKeySummary.md) objects

 ** [ApplicationIntegrationURL](#API_ListAPIKeys_ResponseSyntax) **   <a name="WAF-ListAPIKeys-response-ApplicationIntegrationURL"></a>
The CAPTCHA application integration URL, for use in your JavaScript implementation.   
Type: String

 ** [NextMarker](#API_ListAPIKeys_ResponseSyntax) **   <a name="WAF-ListAPIKeys-response-NextMarker"></a>
When you request a list of objects with a `Limit` setting, if the number of objects that are still available for retrieval exceeds the limit, AWS WAF returns a `NextMarker` value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `.*\S.*` 

## Errors
<a name="API_ListAPIKeys_Errors"></a>

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

## See Also
<a name="API_ListAPIKeys_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wafv2-2019-07-29/ListAPIKeys) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wafv2-2019-07-29/ListAPIKeys) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/ListAPIKeys) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wafv2-2019-07-29/ListAPIKeys) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/ListAPIKeys) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wafv2-2019-07-29/ListAPIKeys) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wafv2-2019-07-29/ListAPIKeys) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wafv2-2019-07-29/ListAPIKeys) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/wafv2-2019-07-29/ListAPIKeys) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/ListAPIKeys) 