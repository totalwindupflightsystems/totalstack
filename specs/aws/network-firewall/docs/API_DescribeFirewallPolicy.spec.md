---
id: "@specs/aws/network-firewall/docs/API_DescribeFirewallPolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeFirewallPolicy"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# DescribeFirewallPolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_DescribeFirewallPolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeFirewallPolicy
<a name="API_DescribeFirewallPolicy"></a>

Returns the data objects for the specified firewall policy. 

## Request Syntax
<a name="API_DescribeFirewallPolicy_RequestSyntax"></a>

```
{
   "FirewallPolicyArn": "{{string}}",
   "FirewallPolicyName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeFirewallPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [FirewallPolicyArn](#API_DescribeFirewallPolicy_RequestSyntax) **   <a name="networkfirewall-DescribeFirewallPolicy-request-FirewallPolicyArn"></a>
The Amazon Resource Name (ARN) of the firewall policy.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** [FirewallPolicyName](#API_DescribeFirewallPolicy_RequestSyntax) **   <a name="networkfirewall-DescribeFirewallPolicy-request-FirewallPolicyName"></a>
The descriptive name of the firewall policy. You can't change the name of a firewall policy after you create it.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

## Response Syntax
<a name="API_DescribeFirewallPolicy_ResponseSyntax"></a>

```
{
   "FirewallPolicy": { 
      "EnableTLSSessionHolding": boolean,
      "PolicyVariables": { 
         "RuleVariables": { 
            "string" : { 
               "Definition": [ "string" ]
            }
         }
      },
      "StatefulDefaultActions": [ "string" ],
      "StatefulEngineOptions": { 
         "FlowTimeouts": { 
            "TcpIdleTimeoutSeconds": number
         },
         "RuleOrder": "string",
         "StreamExceptionPolicy": "string"
      },
      "StatefulRuleGroupReferences": [ 
         { 
            "DeepThreatInspection": boolean,
            "Override": { 
               "Action": "string"
            },
            "Priority": number,
            "ResourceArn": "string"
         }
      ],
      "StatelessCustomActions": [ 
         { 
            "ActionDefinition": { 
               "PublishMetricAction": { 
                  "Dimensions": [ 
                     { 
                        "Value": "string"
                     }
                  ]
               }
            },
            "ActionName": "string"
         }
      ],
      "StatelessDefaultActions": [ "string" ],
      "StatelessFragmentDefaultActions": [ "string" ],
      "StatelessRuleGroupReferences": [ 
         { 
            "Priority": number,
            "ResourceArn": "string"
         }
      ],
      "TLSInspectionConfigurationArn": "string"
   },
   "FirewallPolicyResponse": { 
      "ConsumedStatefulDomainCapacity": number,
      "ConsumedStatefulRuleCapacity": number,
      "ConsumedStatelessRuleCapacity": number,
      "Description": "string",
      "EncryptionConfiguration": { 
         "KeyId": "string",
         "Type": "string"
      },
      "FirewallPolicyArn": "string",
      "FirewallPolicyId": "string",
      "FirewallPolicyName": "string",
      "FirewallPolicyStatus": "string",
      "LastModifiedTime": number,
      "NumberOfAssociations": number,
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
<a name="API_DescribeFirewallPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FirewallPolicy](#API_DescribeFirewallPolicy_ResponseSyntax) **   <a name="networkfirewall-DescribeFirewallPolicy-response-FirewallPolicy"></a>
The policy for the specified firewall policy.   
Type: [FirewallPolicy](API_FirewallPolicy.md) object

 ** [FirewallPolicyResponse](#API_DescribeFirewallPolicy_ResponseSyntax) **   <a name="networkfirewall-DescribeFirewallPolicy-response-FirewallPolicyResponse"></a>
The high-level properties of a firewall policy. This, along with the [FirewallPolicy](API_FirewallPolicy.md), define the policy. You can retrieve all objects for a firewall policy by calling [DescribeFirewallPolicy](#API_DescribeFirewallPolicy).   
Type: [FirewallPolicyResponse](API_FirewallPolicyResponse.md) object

 ** [UpdateToken](#API_DescribeFirewallPolicy_ResponseSyntax) **   <a name="networkfirewall-DescribeFirewallPolicy-response-UpdateToken"></a>
A token used for optimistic locking. Network Firewall returns a token to your requests that access the firewall policy. The token marks the state of the policy resource at the time of the request.   
To make changes to the policy, you provide the token in your request. Network Firewall uses the token to ensure that the policy hasn't changed since you last retrieved it. If it has changed, the operation fails with an `InvalidTokenException`. If this happens, retrieve the firewall policy again to get a current copy of it with current token. Reapply your changes as needed, then try the operation again using the new token.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$` 

## Errors
<a name="API_DescribeFirewallPolicy_Errors"></a>

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
<a name="API_DescribeFirewallPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/DescribeFirewallPolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/DescribeFirewallPolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/DescribeFirewallPolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/DescribeFirewallPolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/DescribeFirewallPolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/DescribeFirewallPolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/DescribeFirewallPolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/DescribeFirewallPolicy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/DescribeFirewallPolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/DescribeFirewallPolicy) 