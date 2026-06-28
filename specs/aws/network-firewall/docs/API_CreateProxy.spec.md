---
id: "@specs/aws/network-firewall/docs/API_CreateProxy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateProxy"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# CreateProxy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_CreateProxy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateProxy
<a name="API_CreateProxy"></a>

Creates an AWS Network Firewall [Proxy](API_Proxy.md) 

Attaches a Proxy configuration to a NAT Gateway. 

To manage a proxy's tags, use the standard AWS resource tagging operations, [ListTagsForResource](API_ListTagsForResource.md), [TagResource](API_TagResource.md), and [UntagResource](API_UntagResource.md).

To retrieve information about proxies, use [ListProxies](API_ListProxies.md) and [DescribeProxy](API_DescribeProxy.md).

## Request Syntax
<a name="API_CreateProxy_RequestSyntax"></a>

```
{
   "ListenerProperties": [ 
      { 
         "Port": {{number}},
         "Type": "{{string}}"
      }
   ],
   "NatGatewayId": "{{string}}",
   "ProxyConfigurationArn": "{{string}}",
   "ProxyConfigurationName": "{{string}}",
   "ProxyName": "{{string}}",
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "TlsInterceptProperties": { 
      "PcaArn": "{{string}}",
      "TlsInterceptMode": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateProxy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ListenerProperties](#API_CreateProxy_RequestSyntax) **   <a name="networkfirewall-CreateProxy-request-ListenerProperties"></a>
Listener properties for HTTP and HTTPS traffic.  
Type: Array of [ListenerPropertyRequest](API_ListenerPropertyRequest.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 2 items.  
Required: No

 ** [NatGatewayId](#API_CreateProxy_RequestSyntax) **   <a name="networkfirewall-CreateProxy-request-NatGatewayId"></a>
A unique identifier for the NAT gateway to use with proxy resources.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: Yes

 ** [ProxyConfigurationArn](#API_CreateProxy_RequestSyntax) **   <a name="networkfirewall-CreateProxy-request-ProxyConfigurationArn"></a>
The Amazon Resource Name (ARN) of a proxy configuration.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** [ProxyConfigurationName](#API_CreateProxy_RequestSyntax) **   <a name="networkfirewall-CreateProxy-request-ProxyConfigurationName"></a>
The descriptive name of the proxy configuration. You can't change the name of a proxy configuration after you create it.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

 ** [ProxyName](#API_CreateProxy_RequestSyntax) **   <a name="networkfirewall-CreateProxy-request-ProxyName"></a>
The descriptive name of the proxy. You can't change the name of a proxy after you create it.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: Yes

 ** [Tags](#API_CreateProxy_RequestSyntax) **   <a name="networkfirewall-CreateProxy-request-Tags"></a>
The key:value pairs to associate with the resource.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.  
Required: No

 ** [TlsInterceptProperties](#API_CreateProxy_RequestSyntax) **   <a name="networkfirewall-CreateProxy-request-TlsInterceptProperties"></a>
TLS decryption on traffic to filter on attributes in the HTTP header.   
Type: [TlsInterceptPropertiesRequest](API_TlsInterceptPropertiesRequest.md) object  
Required: Yes

## Response Syntax
<a name="API_CreateProxy_ResponseSyntax"></a>

```
{
   "Proxy": { 
      "CreateTime": number,
      "DeleteTime": number,
      "FailureCode": "string",
      "FailureMessage": "string",
      "ListenerProperties": [ 
         { 
            "Port": number,
            "Type": "string"
         }
      ],
      "NatGatewayId": "string",
      "ProxyArn": "string",
      "ProxyConfigurationArn": "string",
      "ProxyConfigurationName": "string",
      "ProxyModifyState": "string",
      "ProxyName": "string",
      "ProxyState": "string",
      "Tags": [ 
         { 
            "Key": "string",
            "Value": "string"
         }
      ],
      "TlsInterceptProperties": { 
         "PcaArn": "string",
         "TlsInterceptMode": "string"
      },
      "UpdateTime": number
   },
   "UpdateToken": "string"
}
```

## Response Elements
<a name="API_CreateProxy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Proxy](#API_CreateProxy_ResponseSyntax) **   <a name="networkfirewall-CreateProxy-response-Proxy"></a>
Proxy attached to a NAT gateway.   
Type: [Proxy](API_Proxy.md) object

 ** [UpdateToken](#API_CreateProxy_ResponseSyntax) **   <a name="networkfirewall-CreateProxy-response-UpdateToken"></a>
A token used for optimistic locking. Network Firewall returns a token to your requests that access the proxy. The token marks the state of the proxy resource at the time of the request.   
To make changes to the proxy, you provide the token in your request. Network Firewall uses the token to ensure that the proxy hasn't changed since you last retrieved it. If it has changed, the operation fails with an `InvalidTokenException`. If this happens, retrieve the proxy again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$` 

## Errors
<a name="API_CreateProxy_Errors"></a>

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

 ** LimitExceededException **   
Unable to perform the operation because doing so would violate a limit setting.   
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
<a name="API_CreateProxy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/CreateProxy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/CreateProxy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/CreateProxy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/CreateProxy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/CreateProxy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/CreateProxy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/CreateProxy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/CreateProxy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/CreateProxy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/CreateProxy) 