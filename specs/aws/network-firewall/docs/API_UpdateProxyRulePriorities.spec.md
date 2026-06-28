---
id: "@specs/aws/network-firewall/docs/API_UpdateProxyRulePriorities"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateProxyRulePriorities"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# UpdateProxyRulePriorities

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_UpdateProxyRulePriorities
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateProxyRulePriorities
<a name="API_UpdateProxyRulePriorities"></a>

Updates proxy rule priorities within a proxy rule group.

## Request Syntax
<a name="API_UpdateProxyRulePriorities_RequestSyntax"></a>

```
{
   "ProxyRuleGroupArn": "{{string}}",
   "ProxyRuleGroupName": "{{string}}",
   "RuleGroupRequestPhase": "{{string}}",
   "Rules": [ 
      { 
         "NewPosition": {{number}},
         "ProxyRuleName": "{{string}}"
      }
   ],
   "UpdateToken": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateProxyRulePriorities_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ProxyRuleGroupArn](#API_UpdateProxyRulePriorities_RequestSyntax) **   <a name="networkfirewall-UpdateProxyRulePriorities-request-ProxyRuleGroupArn"></a>
The Amazon Resource Name (ARN) of a proxy rule group.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** [ProxyRuleGroupName](#API_UpdateProxyRulePriorities_RequestSyntax) **   <a name="networkfirewall-UpdateProxyRulePriorities-request-ProxyRuleGroupName"></a>
The descriptive name of the proxy rule group. You can't change the name of a proxy rule group after you create it.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

 ** [RuleGroupRequestPhase](#API_UpdateProxyRulePriorities_RequestSyntax) **   <a name="networkfirewall-UpdateProxyRulePriorities-request-RuleGroupRequestPhase"></a>
Evaluation points in the traffic flow where rules are applied. There are three phases in a traffic where the rule match is applied.   
Type: String  
Valid Values: `PRE_DNS | PRE_REQ | POST_RES`   
Required: Yes

 ** [Rules](#API_UpdateProxyRulePriorities_RequestSyntax) **   <a name="networkfirewall-UpdateProxyRulePriorities-request-Rules"></a>
proxy rule resources to update to new positions.   
Type: Array of [ProxyRulePriority](API_ProxyRulePriority.md) objects  
Required: Yes

 ** [UpdateToken](#API_UpdateProxyRulePriorities_RequestSyntax) **   <a name="networkfirewall-UpdateProxyRulePriorities-request-UpdateToken"></a>
A token used for optimistic locking. Network Firewall returns a token to your requests that access the proxy rule group. The token marks the state of the proxy rule group resource at the time of the request.   
To make changes to the proxy rule group, you provide the token in your request. Network Firewall uses the token to ensure that the proxy rule group hasn't changed since you last retrieved it. If it has changed, the operation fails with an `InvalidTokenException`. If this happens, retrieve the proxy rule group again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$`   
Required: Yes

## Response Syntax
<a name="API_UpdateProxyRulePriorities_ResponseSyntax"></a>

```
{
   "ProxyRuleGroupArn": "string",
   "ProxyRuleGroupName": "string",
   "RuleGroupRequestPhase": "string",
   "Rules": [ 
      { 
         "NewPosition": number,
         "ProxyRuleName": "string"
      }
   ],
   "UpdateToken": "string"
}
```

## Response Elements
<a name="API_UpdateProxyRulePriorities_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ProxyRuleGroupArn](#API_UpdateProxyRulePriorities_ResponseSyntax) **   <a name="networkfirewall-UpdateProxyRulePriorities-response-ProxyRuleGroupArn"></a>
The Amazon Resource Name (ARN) of a proxy rule group.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*` 

 ** [ProxyRuleGroupName](#API_UpdateProxyRulePriorities_ResponseSyntax) **   <a name="networkfirewall-UpdateProxyRulePriorities-response-ProxyRuleGroupName"></a>
The descriptive name of the proxy rule group. You can't change the name of a proxy rule group after you create it.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$` 

 ** [RuleGroupRequestPhase](#API_UpdateProxyRulePriorities_ResponseSyntax) **   <a name="networkfirewall-UpdateProxyRulePriorities-response-RuleGroupRequestPhase"></a>
Evaluation points in the traffic flow where rules are applied. There are three phases in a traffic where the rule match is applied.   
Type: String  
Valid Values: `PRE_DNS | PRE_REQ | POST_RES` 

 ** [Rules](#API_UpdateProxyRulePriorities_ResponseSyntax) **   <a name="networkfirewall-UpdateProxyRulePriorities-response-Rules"></a>
The updated proxy rule hierarchy that reflects the updates from the request.  
Type: Array of [ProxyRulePriority](API_ProxyRulePriority.md) objects

 ** [UpdateToken](#API_UpdateProxyRulePriorities_ResponseSyntax) **   <a name="networkfirewall-UpdateProxyRulePriorities-response-UpdateToken"></a>
A token used for optimistic locking. Network Firewall returns a token to your requests that access the proxy rule group. The token marks the state of the proxy rule group resource at the time of the request.   
To make changes to the proxy rule group, you provide the token in your request. Network Firewall uses the token to ensure that the proxy rule group hasn't changed since you last retrieved it. If it has changed, the operation fails with an `InvalidTokenException`. If this happens, retrieve the proxy rule group again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$` 

## Errors
<a name="API_UpdateProxyRulePriorities_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **   
Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request.   
HTTP Status Code: 500

 ** InvalidRequestException **   
The operation failed because of a problem with your request. Examples include:   
+ You specified an unsupported parameter name or value.
+ You tried to update a property with a value that isn't among the available types.
+ Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.
HTTP Status Code: 400

 ** ResourceNotFoundException **   
Unable to locate a resource using the parameters that you provided.  
HTTP Status Code: 400

 ** ThrottlingException **   
Unable to process the request due to throttling limitations.  
HTTP Status Code: 400

## See Also
<a name="API_UpdateProxyRulePriorities_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/UpdateProxyRulePriorities) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/UpdateProxyRulePriorities) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/UpdateProxyRulePriorities) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/UpdateProxyRulePriorities) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/UpdateProxyRulePriorities) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/UpdateProxyRulePriorities) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/UpdateProxyRulePriorities) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/UpdateProxyRulePriorities) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/UpdateProxyRulePriorities) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/UpdateProxyRulePriorities) 