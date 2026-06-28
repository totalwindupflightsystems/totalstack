---
id: "@specs/aws/network-firewall/docs/API_DeleteFirewallPolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteFirewallPolicy"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# DeleteFirewallPolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_DeleteFirewallPolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteFirewallPolicy
<a name="API_DeleteFirewallPolicy"></a>

Deletes the specified [FirewallPolicy](API_FirewallPolicy.md). 

## Request Syntax
<a name="API_DeleteFirewallPolicy_RequestSyntax"></a>

```
{
   "FirewallPolicyArn": "{{string}}",
   "FirewallPolicyName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteFirewallPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [FirewallPolicyArn](#API_DeleteFirewallPolicy_RequestSyntax) **   <a name="networkfirewall-DeleteFirewallPolicy-request-FirewallPolicyArn"></a>
The Amazon Resource Name (ARN) of the firewall policy.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** [FirewallPolicyName](#API_DeleteFirewallPolicy_RequestSyntax) **   <a name="networkfirewall-DeleteFirewallPolicy-request-FirewallPolicyName"></a>
The descriptive name of the firewall policy. You can't change the name of a firewall policy after you create it.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

## Response Syntax
<a name="API_DeleteFirewallPolicy_ResponseSyntax"></a>

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
   }
}
```

## Response Elements
<a name="API_DeleteFirewallPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FirewallPolicyResponse](#API_DeleteFirewallPolicy_ResponseSyntax) **   <a name="networkfirewall-DeleteFirewallPolicy-response-FirewallPolicyResponse"></a>
The object containing the definition of the [FirewallPolicyResponse](API_FirewallPolicyResponse.md) that you asked to delete.   
Type: [FirewallPolicyResponse](API_FirewallPolicyResponse.md) object

## Errors
<a name="API_DeleteFirewallPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **   
Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request.   
HTTP Status Code: 500

 ** InvalidOperationException **   
The operation failed because it's not valid. For example, you might have tried to delete a rule group or firewall policy that's in use.  
HTTP Status Code: 400

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

 ** UnsupportedOperationException **   
The operation you requested isn't supported by Network Firewall.   
HTTP Status Code: 400

## See Also
<a name="API_DeleteFirewallPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/DeleteFirewallPolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/DeleteFirewallPolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/DeleteFirewallPolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/DeleteFirewallPolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/DeleteFirewallPolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/DeleteFirewallPolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/DeleteFirewallPolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/DeleteFirewallPolicy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/DeleteFirewallPolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/DeleteFirewallPolicy) 