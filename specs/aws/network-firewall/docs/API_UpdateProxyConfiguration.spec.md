---
id: "@specs/aws/network-firewall/docs/API_UpdateProxyConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateProxyConfiguration"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# UpdateProxyConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_UpdateProxyConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateProxyConfiguration
<a name="API_UpdateProxyConfiguration"></a>

Updates the properties of the specified proxy configuration.

## Request Syntax
<a name="API_UpdateProxyConfiguration_RequestSyntax"></a>

```
{
   "DefaultRulePhaseActions": { 
      "PostRESPONSE": "{{string}}",
      "PreDNS": "{{string}}",
      "PreREQUEST": "{{string}}"
   },
   "ProxyConfigurationArn": "{{string}}",
   "ProxyConfigurationName": "{{string}}",
   "UpdateToken": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateProxyConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DefaultRulePhaseActions](#API_UpdateProxyConfiguration_RequestSyntax) **   <a name="networkfirewall-UpdateProxyConfiguration-request-DefaultRulePhaseActions"></a>
Evaluation points in the traffic flow where rules are applied. There are three phases in a traffic where the rule match is applied.   
Type: [ProxyConfigDefaultRulePhaseActionsRequest](API_ProxyConfigDefaultRulePhaseActionsRequest.md) object  
Required: Yes

 ** [ProxyConfigurationArn](#API_UpdateProxyConfiguration_RequestSyntax) **   <a name="networkfirewall-UpdateProxyConfiguration-request-ProxyConfigurationArn"></a>
The Amazon Resource Name (ARN) of a proxy configuration.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** [ProxyConfigurationName](#API_UpdateProxyConfiguration_RequestSyntax) **   <a name="networkfirewall-UpdateProxyConfiguration-request-ProxyConfigurationName"></a>
The descriptive name of the proxy configuration. You can't change the name of a proxy configuration after you create it.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

 ** [UpdateToken](#API_UpdateProxyConfiguration_RequestSyntax) **   <a name="networkfirewall-UpdateProxyConfiguration-request-UpdateToken"></a>
A token used for optimistic locking. Network Firewall returns a token to your requests that access the proxy configuration. The token marks the state of the proxy configuration resource at the time of the request.   
To make changes to the proxy configuration, you provide the token in your request. Network Firewall uses the token to ensure that the proxy configuration hasn't changed since you last retrieved it. If it has changed, the operation fails with an `InvalidTokenException`. If this happens, retrieve the proxy configuration again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$`   
Required: Yes

## Response Syntax
<a name="API_UpdateProxyConfiguration_ResponseSyntax"></a>

```
{
   "ProxyConfiguration": { 
      "CreateTime": number,
      "DefaultRulePhaseActions": { 
         "PostRESPONSE": "string",
         "PreDNS": "string",
         "PreREQUEST": "string"
      },
      "DeleteTime": number,
      "Description": "string",
      "ProxyConfigurationArn": "string",
      "ProxyConfigurationName": "string",
      "RuleGroups": [ 
         { 
            "Priority": number,
            "ProxyRuleGroupArn": "string",
            "ProxyRuleGroupName": "string",
            "Type": "string"
         }
      ],
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
<a name="API_UpdateProxyConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ProxyConfiguration](#API_UpdateProxyConfiguration_ResponseSyntax) **   <a name="networkfirewall-UpdateProxyConfiguration-response-ProxyConfiguration"></a>
The updated proxy configuration resource that reflects the updates from the request.  
Type: [ProxyConfiguration](API_ProxyConfiguration.md) object

 ** [UpdateToken](#API_UpdateProxyConfiguration_ResponseSyntax) **   <a name="networkfirewall-UpdateProxyConfiguration-response-UpdateToken"></a>
A token used for optimistic locking. Network Firewall returns a token to your requests that access the proxy configuration. The token marks the state of the proxy configuration resource at the time of the request.   
To make changes to the proxy configuration, you provide the token in your request. Network Firewall uses the token to ensure that the proxy configuration hasn't changed since you last retrieved it. If it has changed, the operation fails with an `InvalidTokenException`. If this happens, retrieve the proxy configuration again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$` 

## Errors
<a name="API_UpdateProxyConfiguration_Errors"></a>

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
<a name="API_UpdateProxyConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/UpdateProxyConfiguration) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/UpdateProxyConfiguration) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/UpdateProxyConfiguration) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/UpdateProxyConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/UpdateProxyConfiguration) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/UpdateProxyConfiguration) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/UpdateProxyConfiguration) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/UpdateProxyConfiguration) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/UpdateProxyConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/UpdateProxyConfiguration) 