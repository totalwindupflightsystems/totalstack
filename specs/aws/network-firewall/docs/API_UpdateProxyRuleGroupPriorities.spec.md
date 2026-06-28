---
id: "@specs/aws/network-firewall/docs/API_UpdateProxyRuleGroupPriorities"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateProxyRuleGroupPriorities"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# UpdateProxyRuleGroupPriorities

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_UpdateProxyRuleGroupPriorities
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateProxyRuleGroupPriorities
<a name="API_UpdateProxyRuleGroupPriorities"></a>

Updates proxy rule group priorities within a proxy configuration.

## Request Syntax
<a name="API_UpdateProxyRuleGroupPriorities_RequestSyntax"></a>

```
{
   "ProxyConfigurationArn": "{{string}}",
   "ProxyConfigurationName": "{{string}}",
   "RuleGroups": [ 
      { 
         "NewPosition": {{number}},
         "ProxyRuleGroupName": "{{string}}"
      }
   ],
   "UpdateToken": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateProxyRuleGroupPriorities_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ProxyConfigurationArn](#API_UpdateProxyRuleGroupPriorities_RequestSyntax) **   <a name="networkfirewall-UpdateProxyRuleGroupPriorities-request-ProxyConfigurationArn"></a>
The Amazon Resource Name (ARN) of a proxy configuration.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** [ProxyConfigurationName](#API_UpdateProxyRuleGroupPriorities_RequestSyntax) **   <a name="networkfirewall-UpdateProxyRuleGroupPriorities-request-ProxyConfigurationName"></a>
The descriptive name of the proxy configuration. You can't change the name of a proxy configuration after you create it.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

 ** [RuleGroups](#API_UpdateProxyRuleGroupPriorities_RequestSyntax) **   <a name="networkfirewall-UpdateProxyRuleGroupPriorities-request-RuleGroups"></a>
proxy rule group resources to update to new positions.   
Type: Array of [ProxyRuleGroupPriority](API_ProxyRuleGroupPriority.md) objects  
Required: Yes

 ** [UpdateToken](#API_UpdateProxyRuleGroupPriorities_RequestSyntax) **   <a name="networkfirewall-UpdateProxyRuleGroupPriorities-request-UpdateToken"></a>
A token used for optimistic locking. Network Firewall returns a token to your requests that access the proxy configuration. The token marks the state of the proxy configuration resource at the time of the request.   
To make changes to the proxy configuration, you provide the token in your request. Network Firewall uses the token to ensure that the proxy configuration hasn't changed since you last retrieved it. If it has changed, the operation fails with an `InvalidTokenException`. If this happens, retrieve the proxy configuration again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$`   
Required: Yes

## Response Syntax
<a name="API_UpdateProxyRuleGroupPriorities_ResponseSyntax"></a>

```
{
   "ProxyRuleGroups": [ 
      { 
         "Priority": number,
         "ProxyRuleGroupName": "string"
      }
   ],
   "UpdateToken": "string"
}
```

## Response Elements
<a name="API_UpdateProxyRuleGroupPriorities_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ProxyRuleGroups](#API_UpdateProxyRuleGroupPriorities_ResponseSyntax) **   <a name="networkfirewall-UpdateProxyRuleGroupPriorities-response-ProxyRuleGroups"></a>
The updated proxy rule group hierarchy that reflects the updates from the request.  
Type: Array of [ProxyRuleGroupPriorityResult](API_ProxyRuleGroupPriorityResult.md) objects

 ** [UpdateToken](#API_UpdateProxyRuleGroupPriorities_ResponseSyntax) **   <a name="networkfirewall-UpdateProxyRuleGroupPriorities-response-UpdateToken"></a>
A token used for optimistic locking. Network Firewall returns a token to your requests that access the proxy configuration. The token marks the state of the proxy configuration resource at the time of the request.   
To make changes to the proxy configuration, you provide the token in your request. Network Firewall uses the token to ensure that the proxy configuration hasn't changed since you last retrieved it. If it has changed, the operation fails with an `InvalidTokenException`. If this happens, retrieve the proxy configuration again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$` 

## Errors
<a name="API_UpdateProxyRuleGroupPriorities_Errors"></a>

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
<a name="API_UpdateProxyRuleGroupPriorities_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/UpdateProxyRuleGroupPriorities) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/UpdateProxyRuleGroupPriorities) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/UpdateProxyRuleGroupPriorities) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/UpdateProxyRuleGroupPriorities) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/UpdateProxyRuleGroupPriorities) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/UpdateProxyRuleGroupPriorities) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/UpdateProxyRuleGroupPriorities) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/UpdateProxyRuleGroupPriorities) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/UpdateProxyRuleGroupPriorities) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/UpdateProxyRuleGroupPriorities) 