---
id: "@specs/aws/network-firewall/docs/API_Proxy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Proxy"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# Proxy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_Proxy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Proxy
<a name="API_Proxy"></a>

Proxy attached to a NAT gateway. 

## Contents
<a name="API_Proxy_Contents"></a>

 ** CreateTime **   <a name="networkfirewall-Type-Proxy-CreateTime"></a>
Time the Proxy was created.   
Type: Timestamp  
Required: No

 ** DeleteTime **   <a name="networkfirewall-Type-Proxy-DeleteTime"></a>
Time the Proxy was deleted.   
Type: Timestamp  
Required: No

 ** FailureCode **   <a name="networkfirewall-Type-Proxy-FailureCode"></a>
Failure code for cases when the Proxy fails to attach or update.   
Type: String  
Required: No

 ** FailureMessage **   <a name="networkfirewall-Type-Proxy-FailureMessage"></a>
Failure message for cases when the Proxy fails to attach or update.   
Type: String  
Required: No

 ** ListenerProperties **   <a name="networkfirewall-Type-Proxy-ListenerProperties"></a>
Listener properties for HTTP and HTTPS traffic.   
Type: Array of [ListenerProperty](API_ListenerProperty.md) objects  
Required: No

 ** NatGatewayId **   <a name="networkfirewall-Type-Proxy-NatGatewayId"></a>
The NAT Gateway for the proxy.   
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

 ** ProxyArn **   <a name="networkfirewall-Type-Proxy-ProxyArn"></a>
The Amazon Resource Name (ARN) of a proxy.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** ProxyConfigurationArn **   <a name="networkfirewall-Type-Proxy-ProxyConfigurationArn"></a>
The Amazon Resource Name (ARN) of a proxy configuration.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** ProxyConfigurationName **   <a name="networkfirewall-Type-Proxy-ProxyConfigurationName"></a>
The descriptive name of the proxy configuration. You can't change the name of a proxy configuration after you create it.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

 ** ProxyModifyState **   <a name="networkfirewall-Type-Proxy-ProxyModifyState"></a>
Current modification status of the Proxy.   
Type: String  
Valid Values: `MODIFYING | COMPLETED | FAILED`   
Required: No

 ** ProxyName **   <a name="networkfirewall-Type-Proxy-ProxyName"></a>
The descriptive name of the proxy. You can't change the name of a proxy after you create it.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

 ** ProxyState **   <a name="networkfirewall-Type-Proxy-ProxyState"></a>
Current attachment/detachment status of the Proxy.   
Type: String  
Valid Values: `ATTACHING | ATTACHED | DETACHING | DETACHED | ATTACH_FAILED | DETACH_FAILED`   
Required: No

 ** Tags **   <a name="networkfirewall-Type-Proxy-Tags"></a>
The key:value pairs to associate with the resource.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.  
Required: No

 ** TlsInterceptProperties **   <a name="networkfirewall-Type-Proxy-TlsInterceptProperties"></a>
TLS decryption on traffic to filter on attributes in the HTTP header.   
Type: [TlsInterceptProperties](API_TlsInterceptProperties.md) object  
Required: No

 ** UpdateTime **   <a name="networkfirewall-Type-Proxy-UpdateTime"></a>
Time the Proxy was updated.   
Type: Timestamp  
Required: No

## See Also
<a name="API_Proxy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/Proxy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/Proxy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/Proxy) 