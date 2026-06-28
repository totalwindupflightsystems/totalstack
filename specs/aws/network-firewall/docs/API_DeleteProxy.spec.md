---
id: "@specs/aws/network-firewall/docs/API_DeleteProxy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteProxy"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# DeleteProxy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_DeleteProxy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteProxy
<a name="API_DeleteProxy"></a>

Deletes the specified [Proxy](API_Proxy.md). 

Detaches a Proxy configuration from a NAT Gateway. 

## Request Syntax
<a name="API_DeleteProxy_RequestSyntax"></a>

```
{
   "NatGatewayId": "{{string}}",
   "ProxyArn": "{{string}}",
   "ProxyName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteProxy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [NatGatewayId](#API_DeleteProxy_RequestSyntax) **   <a name="networkfirewall-DeleteProxy-request-NatGatewayId"></a>
The NAT Gateway the proxy is attached to.   
Type: String  
Length Constraints: Minimum length of 1.  
Required: Yes

 ** [ProxyArn](#API_DeleteProxy_RequestSyntax) **   <a name="networkfirewall-DeleteProxy-request-ProxyArn"></a>
The Amazon Resource Name (ARN) of a proxy.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** [ProxyName](#API_DeleteProxy_RequestSyntax) **   <a name="networkfirewall-DeleteProxy-request-ProxyName"></a>
The descriptive name of the proxy. You can't change the name of a proxy after you create it.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

## Response Syntax
<a name="API_DeleteProxy_ResponseSyntax"></a>

```
{
   "NatGatewayId": "string",
   "ProxyArn": "string",
   "ProxyName": "string"
}
```

## Response Elements
<a name="API_DeleteProxy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NatGatewayId](#API_DeleteProxy_ResponseSyntax) **   <a name="networkfirewall-DeleteProxy-response-NatGatewayId"></a>
The NAT Gateway the Proxy was attached to.   
Type: String  
Length Constraints: Minimum length of 1.

 ** [ProxyArn](#API_DeleteProxy_ResponseSyntax) **   <a name="networkfirewall-DeleteProxy-response-ProxyArn"></a>
The Amazon Resource Name (ARN) of a proxy.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*` 

 ** [ProxyName](#API_DeleteProxy_ResponseSyntax) **   <a name="networkfirewall-DeleteProxy-response-ProxyName"></a>
The descriptive name of the proxy. You can't change the name of a proxy after you create it.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$` 

## Errors
<a name="API_DeleteProxy_Errors"></a>

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

 ** UnsupportedOperationException **   
The operation you requested isn't supported by Network Firewall.   
HTTP Status Code: 400

## See Also
<a name="API_DeleteProxy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/DeleteProxy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/DeleteProxy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/DeleteProxy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/DeleteProxy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/DeleteProxy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/DeleteProxy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/DeleteProxy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/DeleteProxy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/DeleteProxy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/DeleteProxy) 