---
id: "@specs/aws/wafv2/docs/API_UpdateRegexPatternSet"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateRegexPatternSet"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# UpdateRegexPatternSet

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_UpdateRegexPatternSet
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateRegexPatternSet
<a name="API_UpdateRegexPatternSet"></a>

Updates the specified [RegexPatternSet](API_RegexPatternSet.md).

**Note**  
This operation completely replaces the mutable specifications that you already have for the regex pattern set with the ones that you provide to this call.   
To modify a regex pattern set, do the following:   
Retrieve it by calling [GetRegexPatternSet](API_GetRegexPatternSet.md) 
Update its settings as needed
Provide the complete regex pattern set specification to this call

 **Temporary inconsistencies during updates** 

When you create or change a web ACL or other AWS WAF resources, the changes take a small amount of time to propagate to all areas where the resources are stored. The propagation time can be from a few seconds to a number of minutes. 

The following are examples of the temporary inconsistencies that you might notice during change propagation: 
+ After you create a web ACL, if you try to associate it with a resource, you might get an exception indicating that the web ACL is unavailable. 
+ After you add a rule group to a web ACL, the new rule group rules might be in effect in one area where the web ACL is used and not in another.
+ After you change a rule action setting, you might see the old action in some places and the new action in others. 
+ After you add an IP address to an IP set that is in use in a blocking rule, the new address might be blocked in one area while still allowed in another.

## Request Syntax
<a name="API_UpdateRegexPatternSet_RequestSyntax"></a>

```
{
   "Description": "{{string}}",
   "Id": "{{string}}",
   "LockToken": "{{string}}",
   "Name": "{{string}}",
   "RegularExpressionList": [ 
      { 
         "RegexString": "{{string}}"
      }
   ],
   "Scope": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateRegexPatternSet_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateRegexPatternSet_RequestSyntax) **   <a name="WAF-UpdateRegexPatternSet-request-Description"></a>
A description of the set that helps with identification.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^[\w+=:#@/\-,\.][\w+=:#@/\-,\.\s]+[\w+=:#@/\-,\.]$`   
Required: No

 ** [Id](#API_UpdateRegexPatternSet_RequestSyntax) **   <a name="WAF-UpdateRegexPatternSet-request-Id"></a>
A unique identifier for the set. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 36.  
Pattern: `^[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$`   
Required: Yes

 ** [LockToken](#API_UpdateRegexPatternSet_RequestSyntax) **   <a name="WAF-UpdateRegexPatternSet-request-LockToken"></a>
A token used for optimistic locking. AWS WAF returns a token to your `get` and `list` requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like `update` and `delete`. AWS WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a `WAFOptimisticLockException`. If this happens, perform another `get`, and use the new token returned by that operation.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 36.  
Pattern: `^[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$`   
Required: Yes

 ** [Name](#API_UpdateRegexPatternSet_RequestSyntax) **   <a name="WAF-UpdateRegexPatternSet-request-Name"></a>
The name of the set. You cannot change the name after you create the set.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[\w\-]+$`   
Required: Yes

 ** [RegularExpressionList](#API_UpdateRegexPatternSet_RequestSyntax) **   <a name="WAF-UpdateRegexPatternSet-request-RegularExpressionList"></a>
  
Type: Array of [Regex](API_Regex.md) objects  
Required: Yes

 ** [Scope](#API_UpdateRegexPatternSet_RequestSyntax) **   <a name="WAF-UpdateRegexPatternSet-request-Scope"></a>
Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an AWS Amplify application, use `CLOUDFRONT`.  
To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:   
+ CLI - Specify the Region when you use the CloudFront scope: `--scope=CLOUDFRONT --region=us-east-1`. 
+ API and SDKs - For all calls, use the Region endpoint us-east-1. 
Type: String  
Valid Values: `CLOUDFRONT | REGIONAL`   
Required: Yes

## Response Syntax
<a name="API_UpdateRegexPatternSet_ResponseSyntax"></a>

```
{
   "NextLockToken": "string"
}
```

## Response Elements
<a name="API_UpdateRegexPatternSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextLockToken](#API_UpdateRegexPatternSet_ResponseSyntax) **   <a name="WAF-UpdateRegexPatternSet-response-NextLockToken"></a>
A token used for optimistic locking. AWS WAF returns this token to your `update` requests. You use `NextLockToken` in the same manner as you use `LockToken`.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 36.  
Pattern: `^[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$` 

## Errors
<a name="API_UpdateRegexPatternSet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** WAFDuplicateItemException **   
 AWS WAF couldn’t perform the operation because the resource that you tried to save is a duplicate of an existing one.  
HTTP Status Code: 400

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

 ** WAFLimitsExceededException **   
 AWS WAF couldn’t perform the operation because you exceeded your resource limit. For example, the maximum number of `WebACL` objects that you can create for an AWS account. For more information, see [AWS WAF quotas](https://docs.aws.amazon.com/waf/latest/developerguide/limits.html) in the * AWS WAF Developer Guide*.    
 ** SourceType **   
Source type for the exception. 
HTTP Status Code: 400

 ** WAFNonexistentItemException **   
 AWS WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate.   
HTTP Status Code: 400

 ** WAFOptimisticLockException **   
 AWS WAF couldn’t save your changes because you tried to update or delete a resource that has changed since you last retrieved it. Get the resource again, make any changes you need to make to the new copy, and retry your operation.   
HTTP Status Code: 400

## See Also
<a name="API_UpdateRegexPatternSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wafv2-2019-07-29/UpdateRegexPatternSet) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wafv2-2019-07-29/UpdateRegexPatternSet) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/UpdateRegexPatternSet) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wafv2-2019-07-29/UpdateRegexPatternSet) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/UpdateRegexPatternSet) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wafv2-2019-07-29/UpdateRegexPatternSet) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wafv2-2019-07-29/UpdateRegexPatternSet) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wafv2-2019-07-29/UpdateRegexPatternSet) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/wafv2-2019-07-29/UpdateRegexPatternSet) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/UpdateRegexPatternSet) 