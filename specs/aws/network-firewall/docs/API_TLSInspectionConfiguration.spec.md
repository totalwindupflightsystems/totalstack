---
id: "@specs/aws/network-firewall/docs/API_TLSInspectionConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS TLSInspectionConfiguration"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# TLSInspectionConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_TLSInspectionConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# TLSInspectionConfiguration
<a name="API_TLSInspectionConfiguration"></a>

The object that defines a TLS inspection configuration. This, along with [TLSInspectionConfigurationResponse](API_TLSInspectionConfigurationResponse.md), define the TLS inspection configuration. You can retrieve all objects for a TLS inspection configuration by calling [DescribeTLSInspectionConfiguration](API_DescribeTLSInspectionConfiguration.md). 

 AWS Network Firewall uses a TLS inspection configuration to decrypt traffic. Network Firewall re-encrypts the traffic before sending it to its destination.

To use a TLS inspection configuration, you add it to a new Network Firewall firewall policy, then you apply the firewall policy to a firewall. Network Firewall acts as a proxy service to decrypt and inspect the traffic traveling through your firewalls. You can reference a TLS inspection configuration from more than one firewall policy, and you can use a firewall policy in more than one firewall. For more information about using TLS inspection configurations, see [Inspecting SSL/TLS traffic with TLS inspection configurations](https://docs.aws.amazon.com/network-firewall/latest/developerguide/tls-inspection.html) in the * AWS Network Firewall Developer Guide*.

## Contents
<a name="API_TLSInspectionConfiguration_Contents"></a>

 ** ServerCertificateConfigurations **   <a name="networkfirewall-Type-TLSInspectionConfiguration-ServerCertificateConfigurations"></a>
Lists the server certificate configurations that are associated with the TLS configuration.  
Type: Array of [ServerCertificateConfiguration](API_ServerCertificateConfiguration.md) objects  
Required: No

## See Also
<a name="API_TLSInspectionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/TLSInspectionConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/TLSInspectionConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/TLSInspectionConfiguration) 