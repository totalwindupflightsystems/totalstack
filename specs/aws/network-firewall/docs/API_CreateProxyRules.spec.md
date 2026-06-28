---
id: "@specs/aws/network-firewall/docs/API_CreateProxyRules"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateProxyRules"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# CreateProxyRules

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_CreateProxyRules
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateProxyRules
<a name="API_CreateProxyRules"></a>

Creates AWS Network Firewall [ProxyRule](API_ProxyRule.md) resources. 

Attaches new proxy rule(s) to an existing proxy rule group. 

To retrieve information about individual proxy rules, use [DescribeProxyRuleGroup](API_DescribeProxyRuleGroup.md) and [DescribeProxyRule](API_DescribeProxyRule.md).

## Request Syntax
<a name="API_CreateProxyRules_RequestSyntax"></a>

```
{
   "ProxyRuleGroupArn": "{{string}}",
   "ProxyRuleGroupName": "{{string}}",
   "Rules": { 
      "PostRESPONSE": [ 
         { 
            "Action": "{{string}}",
            "Conditions": [ 
               { 
                  "ConditionKey": "{{string}}",
                  "ConditionOperator": "{{string}}",
                  "ConditionValues": [ "{{string}}" ]
               }
            ],
            "Description": "{{string}}",
            "InsertPosition": {{number}},
            "ProxyRuleName": "{{string}}"
         }
      ],
      "PreDNS": [ 
         { 
            "Action": "{{string}}",
            "Conditions": [ 
               { 
                  "ConditionKey": "{{string}}",
                  "ConditionOperator": "{{string}}",
                  "ConditionValues": [ "{{string}}" ]
               }
            ],
            "Description": "{{string}}",
            "InsertPosition": {{number}},
            "ProxyRuleName": "{{string}}"
         }
      ],
      "PreREQUEST": [ 
         { 
            "Action": "{{string}}",
            "Conditions": [ 
               { 
                  "ConditionKey": "{{string}}",
                  "ConditionOperator": "{{string}}",
                  "ConditionValues": [ "{{string}}" ]
               }
            ],
            "Description": "{{string}}",
            "InsertPosition": {{number}},
            "ProxyRuleName": "{{string}}"
         }
      ]
   }
}
```

## Request Parameters
<a name="API_CreateProxyRules_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ProxyRuleGroupArn](#API_CreateProxyRules_RequestSyntax) **   <a name="networkfirewall-CreateProxyRules-request-ProxyRuleGroupArn"></a>
The Amazon Resource Name (ARN) of a proxy rule group.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** [ProxyRuleGroupName](#API_CreateProxyRules_RequestSyntax) **   <a name="networkfirewall-CreateProxyRules-request-ProxyRuleGroupName"></a>
The descriptive name of the proxy rule group. You can't change the name of a proxy rule group after you create it.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

 ** [Rules](#API_CreateProxyRules_RequestSyntax) **   <a name="networkfirewall-CreateProxyRules-request-Rules"></a>
Individual rules that define match conditions and actions for application-layer traffic. Rules specify what to inspect (domains, headers, methods) and what action to take (allow, deny, alert).   
Type: [CreateProxyRulesByRequestPhase](API_CreateProxyRulesByRequestPhase.md) object  
Required: Yes

## Response Syntax
<a name="API_CreateProxyRules_ResponseSyntax"></a>

```
{
   "ProxyRuleGroup": { 
      "CreateTime": number,
      "DeleteTime": number,
      "Description": "string",
      "ProxyRuleGroupArn": "string",
      "ProxyRuleGroupName": "string",
      "Rules": { 
         "PostRESPONSE": [ 
            { 
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
            }
         ],
         "PreDNS": [ 
            { 
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
            }
         ],
         "PreREQUEST": [ 
            { 
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
            }
         ]
      },
      "Tags": [ 
         { 
            "Key": "string",
            "Value": "string"
         }
      ]
   },
   "UpdateToken": "string"
}
```

## Response Elements
<a name="API_CreateProxyRules_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ProxyRuleGroup](#API_CreateProxyRules_ResponseSyntax) **   <a name="networkfirewall-CreateProxyRules-response-ProxyRuleGroup"></a>
The properties that define the proxy rule group with the newly created proxy rule(s).   
Type: [ProxyRuleGroup](API_ProxyRuleGroup.md) object

 ** [UpdateToken](#API_CreateProxyRules_ResponseSyntax) **   <a name="networkfirewall-CreateProxyRules-response-UpdateToken"></a>
A token used for optimistic locking. Network Firewall returns a token to your requests that access the proxy rule. The token marks the state of the proxy rule resource at the time of the request.   
To make changes to the proxy rule, you provide the token in your request. Network Firewall uses the token to ensure that the proxy rule hasn't changed since you last retrieved it. If it has changed, the operation fails with an `InvalidTokenException`. If this happens, retrieve the proxy rule again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$` 

## Errors
<a name="API_CreateProxyRules_Errors"></a>

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

 ** ThrottlingException **   
Unable to process the request due to throttling limitations.  
HTTP Status Code: 400

## See Also
<a name="API_CreateProxyRules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/CreateProxyRules) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/CreateProxyRules) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/CreateProxyRules) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/CreateProxyRules) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/CreateProxyRules) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/CreateProxyRules) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/CreateProxyRules) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/CreateProxyRules) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/CreateProxyRules) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/CreateProxyRules) 