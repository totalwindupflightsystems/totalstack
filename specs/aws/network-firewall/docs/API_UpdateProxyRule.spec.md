---
id: "@specs/aws/network-firewall/docs/API_UpdateProxyRule"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateProxyRule"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# UpdateProxyRule

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_UpdateProxyRule
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateProxyRule
<a name="API_UpdateProxyRule"></a>

Updates the properties of the specified proxy rule.

## Request Syntax
<a name="API_UpdateProxyRule_RequestSyntax"></a>

```
{
   "Action": "{{string}}",
   "AddConditions": [ 
      { 
         "ConditionKey": "{{string}}",
         "ConditionOperator": "{{string}}",
         "ConditionValues": [ "{{string}}" ]
      }
   ],
   "Description": "{{string}}",
   "ProxyRuleGroupArn": "{{string}}",
   "ProxyRuleGroupName": "{{string}}",
   "ProxyRuleName": "{{string}}",
   "RemoveConditions": [ 
      { 
         "ConditionKey": "{{string}}",
         "ConditionOperator": "{{string}}",
         "ConditionValues": [ "{{string}}" ]
      }
   ],
   "UpdateToken": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateProxyRule_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Action](#API_UpdateProxyRule_RequestSyntax) **   <a name="networkfirewall-UpdateProxyRule-request-Action"></a>
Depending on the match action, the proxy either stops the evaluation (if the action is terminal - allow or deny), or continues it (if the action is alert) until it matches a rule with a terminal action.   
Type: String  
Valid Values: `ALLOW | DENY | ALERT`   
Required: No

 ** [AddConditions](#API_UpdateProxyRule_RequestSyntax) **   <a name="networkfirewall-UpdateProxyRule-request-AddConditions"></a>
Proxy rule conditions to add. Match criteria that specify what traffic attributes to examine. Conditions include operators (StringEquals, StringLike) and values to match against.   
Type: Array of [ProxyRuleCondition](API_ProxyRuleCondition.md) objects  
Required: No

 ** [Description](#API_UpdateProxyRule_RequestSyntax) **   <a name="networkfirewall-UpdateProxyRule-request-Description"></a>
A description of the proxy rule.   
Type: String  
Length Constraints: Maximum length of 512.  
Pattern: `^.*$`   
Required: No

 ** [ProxyRuleGroupArn](#API_UpdateProxyRule_RequestSyntax) **   <a name="networkfirewall-UpdateProxyRule-request-ProxyRuleGroupArn"></a>
The Amazon Resource Name (ARN) of a proxy rule group.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** [ProxyRuleGroupName](#API_UpdateProxyRule_RequestSyntax) **   <a name="networkfirewall-UpdateProxyRule-request-ProxyRuleGroupName"></a>
The descriptive name of the proxy rule group. You can't change the name of a proxy rule group after you create it.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

 ** [ProxyRuleName](#API_UpdateProxyRule_RequestSyntax) **   <a name="networkfirewall-UpdateProxyRule-request-ProxyRuleName"></a>
The descriptive name of the proxy rule. You can't change the name of a proxy rule after you create it.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: Yes

 ** [RemoveConditions](#API_UpdateProxyRule_RequestSyntax) **   <a name="networkfirewall-UpdateProxyRule-request-RemoveConditions"></a>
Proxy rule conditions to remove. Match criteria that specify what traffic attributes to examine. Conditions include operators (StringEquals, StringLike) and values to match against.   
Type: Array of [ProxyRuleCondition](API_ProxyRuleCondition.md) objects  
Required: No

 ** [UpdateToken](#API_UpdateProxyRule_RequestSyntax) **   <a name="networkfirewall-UpdateProxyRule-request-UpdateToken"></a>
A token used for optimistic locking. Network Firewall returns a token to your requests that access the proxy rule. The token marks the state of the proxy rule resource at the time of the request.   
To make changes to the proxy rule, you provide the token in your request. Network Firewall uses the token to ensure that the proxy rule hasn't changed since you last retrieved it. If it has changed, the operation fails with an `InvalidTokenException`. If this happens, retrieve the proxy rule again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$`   
Required: Yes

## Response Syntax
<a name="API_UpdateProxyRule_ResponseSyntax"></a>

```
{
   "ProxyRule": { 
      "Action": "string",
      "Conditions": [ 
         { 
            "ConditionKey": "string",
            "ConditionOperator": "string",
            "ConditionValues": [ "string" ]
         }
      ],
      "Description": "string",
      "ProxyRuleName": "string"
   },
   "RemovedConditions": [ 
      { 
         "ConditionKey": "string",
         "ConditionOperator": "string",
         "ConditionValues": [ "string" ]
      }
   ],
   "UpdateToken": "string"
}
```

## Response Elements
<a name="API_UpdateProxyRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ProxyRule](#API_UpdateProxyRule_ResponseSyntax) **   <a name="networkfirewall-UpdateProxyRule-response-ProxyRule"></a>
The updated proxy rule resource that reflects the updates from the request.  
Type: [ProxyRule](API_ProxyRule.md) object

 ** [RemovedConditions](#API_UpdateProxyRule_ResponseSyntax) **   <a name="networkfirewall-UpdateProxyRule-response-RemovedConditions"></a>
Proxy rule conditions removed from the rule.   
Type: Array of [ProxyRuleCondition](API_ProxyRuleCondition.md) objects

 ** [UpdateToken](#API_UpdateProxyRule_ResponseSyntax) **   <a name="networkfirewall-UpdateProxyRule-response-UpdateToken"></a>
A token used for optimistic locking. Network Firewall returns a token to your requests that access the proxy rule. The token marks the state of the proxy rule resource at the time of the request.   
To make changes to the proxy rule, you provide the token in your request. Network Firewall uses the token to ensure that the proxy rule hasn't changed since you last retrieved it. If it has changed, the operation fails with an `InvalidTokenException`. If this happens, retrieve the proxy rule again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$` 

## Errors
<a name="API_UpdateProxyRule_Errors"></a>

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
<a name="API_UpdateProxyRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/UpdateProxyRule) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/UpdateProxyRule) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/UpdateProxyRule) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/UpdateProxyRule) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/UpdateProxyRule) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/UpdateProxyRule) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/UpdateProxyRule) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/UpdateProxyRule) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/UpdateProxyRule) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/UpdateProxyRule) 