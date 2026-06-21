---
id: "@specs/aws/wafv2/docs/API_ListAvailableManagedRuleGroupVersions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListAvailableManagedRuleGroupVersions"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# ListAvailableManagedRuleGroupVersions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_ListAvailableManagedRuleGroupVersions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListAvailableManagedRuleGroupVersions
<a name="API_ListAvailableManagedRuleGroupVersions"></a>

Returns a list of the available versions for the specified managed rule group. 

## Request Syntax
<a name="API_ListAvailableManagedRuleGroupVersions_RequestSyntax"></a>

```
{
   "Limit": {{number}},
   "Name": "{{string}}",
   "NextMarker": "{{string}}",
   "Scope": "{{string}}",
   "VendorName": "{{string}}"
}
```

## Request Parameters
<a name="API_ListAvailableManagedRuleGroupVersions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Limit](#API_ListAvailableManagedRuleGroupVersions_RequestSyntax) **   <a name="WAF-ListAvailableManagedRuleGroupVersions-request-Limit"></a>
The maximum number of objects that you want AWS WAF to return for this request. If more objects are available, in the response, AWS WAF provides a `NextMarker` value that you can use in a subsequent call to get the next batch of objects.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [Name](#API_ListAvailableManagedRuleGroupVersions_RequestSyntax) **   <a name="WAF-ListAvailableManagedRuleGroupVersions-request-Name"></a>
The name of the managed rule group. You use this, along with the vendor name, to identify the rule group.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[\w\-]+$`   
Required: Yes

 ** [NextMarker](#API_ListAvailableManagedRuleGroupVersions_RequestSyntax) **   <a name="WAF-ListAvailableManagedRuleGroupVersions-request-NextMarker"></a>
When you request a list of objects with a `Limit` setting, if the number of objects that are still available for retrieval exceeds the limit, AWS WAF returns a `NextMarker` value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `.*\S.*`   
Required: No

 ** [Scope](#API_ListAvailableManagedRuleGroupVersions_RequestSyntax) **   <a name="WAF-ListAvailableManagedRuleGroupVersions-request-Scope"></a>
Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an AWS Amplify application, use `CLOUDFRONT`.  
To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:   
+ CLI - Specify the Region when you use the CloudFront scope: `--scope=CLOUDFRONT --region=us-east-1`. 
+ API and SDKs - For all calls, use the Region endpoint us-east-1. 
Type: String  
Valid Values: `CLOUDFRONT | REGIONAL`   
Required: Yes

 ** [VendorName](#API_ListAvailableManagedRuleGroupVersions_RequestSyntax) **   <a name="WAF-ListAvailableManagedRuleGroupVersions-request-VendorName"></a>
The name of the managed rule group vendor. You use this, along with the rule group name, to identify a rule group.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

## Response Syntax
<a name="API_ListAvailableManagedRuleGroupVersions_ResponseSyntax"></a>

```
{
   "CurrentDefaultVersion": "string",
   "NextMarker": "string",
   "Versions": [ 
      { 
         "LastUpdateTimestamp": number,
         "Name": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListAvailableManagedRuleGroupVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CurrentDefaultVersion](#API_ListAvailableManagedRuleGroupVersions_ResponseSyntax) **   <a name="WAF-ListAvailableManagedRuleGroupVersions-response-CurrentDefaultVersion"></a>
The name of the version that's currently set as the default.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `^[\w#:\.\-/]+$` 

 ** [NextMarker](#API_ListAvailableManagedRuleGroupVersions_ResponseSyntax) **   <a name="WAF-ListAvailableManagedRuleGroupVersions-response-NextMarker"></a>
When you request a list of objects with a `Limit` setting, if the number of objects that are still available for retrieval exceeds the limit, AWS WAF returns a `NextMarker` value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `.*\S.*` 

 ** [Versions](#API_ListAvailableManagedRuleGroupVersions_ResponseSyntax) **   <a name="WAF-ListAvailableManagedRuleGroupVersions-response-Versions"></a>
The versions that are currently available for the specified managed rule group. If you specified a `Limit` in your request, this might not be the full list.   
Type: Array of [ManagedRuleGroupVersion](API_ManagedRuleGroupVersion.md) objects

## Errors
<a name="API_ListAvailableManagedRuleGroupVersions_Errors"></a>

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

 ** WAFNonexistentItemException **   
 AWS WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate.   
HTTP Status Code: 400

## See Also
<a name="API_ListAvailableManagedRuleGroupVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wafv2-2019-07-29/ListAvailableManagedRuleGroupVersions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wafv2-2019-07-29/ListAvailableManagedRuleGroupVersions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/ListAvailableManagedRuleGroupVersions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wafv2-2019-07-29/ListAvailableManagedRuleGroupVersions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/ListAvailableManagedRuleGroupVersions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wafv2-2019-07-29/ListAvailableManagedRuleGroupVersions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wafv2-2019-07-29/ListAvailableManagedRuleGroupVersions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wafv2-2019-07-29/ListAvailableManagedRuleGroupVersions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/wafv2-2019-07-29/ListAvailableManagedRuleGroupVersions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/ListAvailableManagedRuleGroupVersions) 