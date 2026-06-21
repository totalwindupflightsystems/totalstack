---
id: "@specs/aws/wafv2/docs/API_DeleteFirewallManagerRuleGroups"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteFirewallManagerRuleGroups"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# DeleteFirewallManagerRuleGroups

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_DeleteFirewallManagerRuleGroups
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteFirewallManagerRuleGroups
<a name="API_DeleteFirewallManagerRuleGroups"></a>

Deletes all rule groups that are managed by AWS Firewall Manager from the specified [WebACL](API_WebACL.md). 

You can only use this if `ManagedByFirewallManager` and `RetrofittedByFirewallManager` are both false in the web ACL. 

## Request Syntax
<a name="API_DeleteFirewallManagerRuleGroups_RequestSyntax"></a>

```
{
   "WebACLArn": "{{string}}",
   "WebACLLockToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteFirewallManagerRuleGroups_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [WebACLArn](#API_DeleteFirewallManagerRuleGroups_RequestSyntax) **   <a name="WAF-DeleteFirewallManagerRuleGroups-request-WebACLArn"></a>
The Amazon Resource Name (ARN) of the web ACL.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `.*\S.*`   
Required: Yes

 ** [WebACLLockToken](#API_DeleteFirewallManagerRuleGroups_RequestSyntax) **   <a name="WAF-DeleteFirewallManagerRuleGroups-request-WebACLLockToken"></a>
A token used for optimistic locking. AWS WAF returns a token to your `get` and `list` requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like `update` and `delete`. AWS WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a `WAFOptimisticLockException`. If this happens, perform another `get`, and use the new token returned by that operation.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 36.  
Pattern: `^[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$`   
Required: Yes

## Response Syntax
<a name="API_DeleteFirewallManagerRuleGroups_ResponseSyntax"></a>

```
{
   "NextWebACLLockToken": "string"
}
```

## Response Elements
<a name="API_DeleteFirewallManagerRuleGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextWebACLLockToken](#API_DeleteFirewallManagerRuleGroups_ResponseSyntax) **   <a name="WAF-DeleteFirewallManagerRuleGroups-response-NextWebACLLockToken"></a>
A token used for optimistic locking. AWS WAF returns a token to your `get` and `list` requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like `update` and `delete`. AWS WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a `WAFOptimisticLockException`. If this happens, perform another `get`, and use the new token returned by that operation.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 36.  
Pattern: `^[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$` 

## Errors
<a name="API_DeleteFirewallManagerRuleGroups_Errors"></a>

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

 ** WAFOptimisticLockException **   
 AWS WAF couldn’t save your changes because you tried to update or delete a resource that has changed since you last retrieved it. Get the resource again, make any changes you need to make to the new copy, and retry your operation.   
HTTP Status Code: 400

## See Also
<a name="API_DeleteFirewallManagerRuleGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wafv2-2019-07-29/DeleteFirewallManagerRuleGroups) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wafv2-2019-07-29/DeleteFirewallManagerRuleGroups) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/DeleteFirewallManagerRuleGroups) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wafv2-2019-07-29/DeleteFirewallManagerRuleGroups) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/DeleteFirewallManagerRuleGroups) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wafv2-2019-07-29/DeleteFirewallManagerRuleGroups) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wafv2-2019-07-29/DeleteFirewallManagerRuleGroups) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wafv2-2019-07-29/DeleteFirewallManagerRuleGroups) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/wafv2-2019-07-29/DeleteFirewallManagerRuleGroups) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/DeleteFirewallManagerRuleGroups) 