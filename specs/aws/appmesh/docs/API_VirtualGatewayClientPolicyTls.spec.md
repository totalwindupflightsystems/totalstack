---
id: "@specs/aws/appmesh/docs/API_VirtualGatewayClientPolicyTls"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS VirtualGatewayClientPolicyTls"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# VirtualGatewayClientPolicyTls

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_VirtualGatewayClientPolicyTls
> **target_lang:** meta — documentation tier. ALL sections preserved.



# VirtualGatewayClientPolicyTls
<a name="API_VirtualGatewayClientPolicyTls"></a>

An object that represents a Transport Layer Security (TLS) client policy.

## Contents
<a name="API_VirtualGatewayClientPolicyTls_Contents"></a>

 ** validation **   <a name="appmesh-Type-VirtualGatewayClientPolicyTls-validation"></a>
A reference to an object that represents a Transport Layer Security (TLS) validation context.  
Type: [VirtualGatewayTlsValidationContext](API_VirtualGatewayTlsValidationContext.md) object  
Required: Yes

 ** certificate **   <a name="appmesh-Type-VirtualGatewayClientPolicyTls-certificate"></a>
A reference to an object that represents a virtual gateway's client's Transport Layer Security (TLS) certificate.  
Type: [VirtualGatewayClientTlsCertificate](API_VirtualGatewayClientTlsCertificate.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** enforce **   <a name="appmesh-Type-VirtualGatewayClientPolicyTls-enforce"></a>
Whether the policy is enforced. The default is `True`, if a value isn't specified.  
Type: Boolean  
Required: No

 ** ports **   <a name="appmesh-Type-VirtualGatewayClientPolicyTls-ports"></a>
One or more ports that the policy is enforced for.  
Type: Array of integers  
Valid Range: Minimum value of 1. Maximum value of 65535.  
Required: No

## See Also
<a name="API_VirtualGatewayClientPolicyTls_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/VirtualGatewayClientPolicyTls) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/VirtualGatewayClientPolicyTls) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/VirtualGatewayClientPolicyTls) 