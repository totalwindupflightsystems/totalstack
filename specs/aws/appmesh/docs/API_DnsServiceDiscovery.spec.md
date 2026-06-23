---
id: "@specs/aws/appmesh/docs/API_DnsServiceDiscovery"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DnsServiceDiscovery"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# DnsServiceDiscovery

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_DnsServiceDiscovery
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DnsServiceDiscovery
<a name="API_DnsServiceDiscovery"></a>

An object that represents the DNS service discovery information for your virtual node.

## Contents
<a name="API_DnsServiceDiscovery_Contents"></a>

 ** hostname **   <a name="appmesh-Type-DnsServiceDiscovery-hostname"></a>
Specifies the DNS service discovery hostname for the virtual node.   
Type: String  
Required: Yes

 ** ipPreference **   <a name="appmesh-Type-DnsServiceDiscovery-ipPreference"></a>
The preferred IP version that this virtual node uses. Setting the IP preference on the virtual node only overrides the IP preference set for the mesh on this specific node.  
Type: String  
Valid Values: `IPv6_PREFERRED | IPv4_PREFERRED | IPv4_ONLY | IPv6_ONLY`   
Required: No

 ** responseType **   <a name="appmesh-Type-DnsServiceDiscovery-responseType"></a>
Specifies the DNS response type for the virtual node.  
Type: String  
Valid Values: `LOADBALANCER | ENDPOINTS`   
Required: No

## See Also
<a name="API_DnsServiceDiscovery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/DnsServiceDiscovery) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/DnsServiceDiscovery) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/DnsServiceDiscovery) 