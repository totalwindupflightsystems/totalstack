---
id: "@specs/aws/network-firewall/docs/API_UpdateFirewallPolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateFirewallPolicy"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# UpdateFirewallPolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_UpdateFirewallPolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateFirewallPolicy
<a name="API_UpdateFirewallPolicy"></a>

Updates the properties of the specified firewall policy.

## Request Syntax
<a name="API_UpdateFirewallPolicy_RequestSyntax"></a>

```
{
   "Description": "{{string}}",
   "DryRun": {{boolean}},
   "EncryptionConfiguration": { 
      "KeyId": "{{string}}",
      "Type": "{{string}}"
   },
   "FirewallPolicy": { 
      "EnableTLSSessionHolding": {{boolean}},
      "PolicyVariables": { 
         "RuleVariables": { 
            "{{string}}" : { 
               "Definition": [ "{{string}}" ]
            }
         }
      },
      "StatefulDefaultActions": [ "{{string}}" ],
      "StatefulEngineOptions": { 
         "FlowTimeouts": { 
            "TcpIdleTimeoutSeconds": {{number}}
         },
         "RuleOrder": "{{string}}",
         "StreamExceptionPolicy": "{{string}}"
      },
      "StatefulRuleGroupReferences": [ 
         { 
            "DeepThreatInspection": {{boolean}},
            "Override": { 
               "Action": "{{string}}"
            },
            "Priority": {{number}},
            "ResourceArn": "{{string}}"
         }
      ],
      "StatelessCustomActions": [ 
         { 
            "ActionDefinition": { 
               "PublishMetricAction": { 
                  "Dimensions": [ 
                     { 
                        "Value": "{{string}}"
                     }
                  ]
               }
            },
            "ActionName": "{{string}}"
         }
      ],
      "StatelessDefaultActions": [ "{{string}}" ],
      "StatelessFragmentDefaultActions": [ "{{string}}" ],
      "StatelessRuleGroupReferences": [ 
         { 
            "Priority": {{number}},
            "ResourceArn": "{{string}}"
         }
      ],
      "TLSInspectionConfigurationArn": "{{string}}"
   },
   "FirewallPolicyArn": "{{string}}",
   "FirewallPolicyName": "{{string}}",
   "UpdateToken": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateFirewallPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateFirewallPolicy_RequestSyntax) **   <a name="networkfirewall-UpdateFirewallPolicy-request-Description"></a>
A description of the firewall policy.  
Type: String  
Length Constraints: Maximum length of 512.  
Pattern: `^.*$`   
Required: No

 ** [DryRun](#API_UpdateFirewallPolicy_RequestSyntax) **   <a name="networkfirewall-UpdateFirewallPolicy-request-DryRun"></a>
Indicates whether you want Network Firewall to just check the validity of the request, rather than run the request.   
If set to `TRUE`, Network Firewall checks whether the request can run successfully, but doesn't actually make the requested changes. The call returns the value that the request would return if you ran it with dry run set to `FALSE`, but doesn't make additions or changes to your resources. This option allows you to make sure that you have the required permissions to run the request and that your request parameters are valid.   
If set to `FALSE`, Network Firewall makes the requested changes to your resources.   
Type: Boolean  
Required: No

 ** [EncryptionConfiguration](#API_UpdateFirewallPolicy_RequestSyntax) **   <a name="networkfirewall-UpdateFirewallPolicy-request-EncryptionConfiguration"></a>
A complex type that contains settings for encryption of your firewall policy resources.  
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object  
Required: No

 ** [FirewallPolicy](#API_UpdateFirewallPolicy_RequestSyntax) **   <a name="networkfirewall-UpdateFirewallPolicy-request-FirewallPolicy"></a>
The updated firewall policy to use for the firewall. You can't add or remove a [TLSInspectionConfiguration](API_TLSInspectionConfiguration.md) after you create a firewall policy. However, you can replace an existing TLS inspection configuration with another `TLSInspectionConfiguration`.  
Type: [FirewallPolicy](API_FirewallPolicy.md) object  
Required: Yes

 ** [FirewallPolicyArn](#API_UpdateFirewallPolicy_RequestSyntax) **   <a name="networkfirewall-UpdateFirewallPolicy-request-FirewallPolicyArn"></a>
The Amazon Resource Name (ARN) of the firewall policy.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** [FirewallPolicyName](#API_UpdateFirewallPolicy_RequestSyntax) **   <a name="networkfirewall-UpdateFirewallPolicy-request-FirewallPolicyName"></a>
The descriptive name of the firewall policy. You can't change the name of a firewall policy after you create it.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

 ** [UpdateToken](#API_UpdateFirewallPolicy_RequestSyntax) **   <a name="networkfirewall-UpdateFirewallPolicy-request-UpdateToken"></a>
A token used for optimistic locking. Network Firewall returns a token to your requests that access the firewall policy. The token marks the state of the policy resource at the time of the request.   
To make changes to the policy, you provide the token in your request. Network Firewall uses the token to ensure that the policy hasn't changed since you last retrieved it. If it has changed, the operation fails with an `InvalidTokenException`. If this happens, retrieve the firewall policy again to get a current copy of it with current token. Reapply your changes as needed, then try the operation again using the new token.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$`   
Required: Yes

## Response Syntax
<a name="API_UpdateFirewallPolicy_ResponseSyntax"></a>

```
{
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
<a name="API_UpdateFirewallPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FirewallPolicyResponse](#API_UpdateFirewallPolicy_ResponseSyntax) **   <a name="networkfirewall-UpdateFirewallPolicy-response-FirewallPolicyResponse"></a>
The high-level properties of a firewall policy. This, along with the [FirewallPolicy](API_FirewallPolicy.md), define the policy. You can retrieve all objects for a firewall policy by calling [DescribeFirewallPolicy](API_DescribeFirewallPolicy.md).   
Type: [FirewallPolicyResponse](API_FirewallPolicyResponse.md) object

 ** [UpdateToken](#API_UpdateFirewallPolicy_ResponseSyntax) **   <a name="networkfirewall-UpdateFirewallPolicy-response-UpdateToken"></a>
A token used for optimistic locking. Network Firewall returns a token to your requests that access the firewall policy. The token marks the state of the policy resource at the time of the request.   
To make changes to the policy, you provide the token in your request. Network Firewall uses the token to ensure that the policy hasn't changed since you last retrieved it. If it has changed, the operation fails with an `InvalidTokenException`. If this happens, retrieve the firewall policy again to get a current copy of it with current token. Reapply your changes as needed, then try the operation again using the new token.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$` 

## Errors
<a name="API_UpdateFirewallPolicy_Errors"></a>

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

 ** InvalidTokenException **   
The token you provided is stale or isn't valid for the operation.   
HTTP Status Code: 400

 ** ResourceNotFoundException **   
Unable to locate a resource using the parameters that you provided.  
HTTP Status Code: 400

 ** ThrottlingException **   
Unable to process the request due to throttling limitations.  
HTTP Status Code: 400

## See Also
<a name="API_UpdateFirewallPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/UpdateFirewallPolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/UpdateFirewallPolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/UpdateFirewallPolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/UpdateFirewallPolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/UpdateFirewallPolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/UpdateFirewallPolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/UpdateFirewallPolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/UpdateFirewallPolicy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/UpdateFirewallPolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/UpdateFirewallPolicy) 