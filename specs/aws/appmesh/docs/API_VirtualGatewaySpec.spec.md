---
id: "@specs/aws/appmesh/docs/API_VirtualGatewaySpec"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS VirtualGatewaySpec"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# VirtualGatewaySpec

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_VirtualGatewaySpec
> **target_lang:** meta — documentation tier. ALL sections preserved.



# VirtualGatewaySpec
<a name="API_VirtualGatewaySpec"></a>

An object that represents the specification of a service mesh resource.

## Contents
<a name="API_VirtualGatewaySpec_Contents"></a>

 ** listeners **   <a name="appmesh-Type-VirtualGatewaySpec-listeners"></a>
The listeners that the mesh endpoint is expected to receive inbound traffic from. You can specify one listener.  
Type: Array of [VirtualGatewayListener](API_VirtualGatewayListener.md) objects  
Required: Yes

 ** backendDefaults **   <a name="appmesh-Type-VirtualGatewaySpec-backendDefaults"></a>
A reference to an object that represents the defaults for backends.  
Type: [VirtualGatewayBackendDefaults](API_VirtualGatewayBackendDefaults.md) object  
Required: No

 ** logging **   <a name="appmesh-Type-VirtualGatewaySpec-logging"></a>
An object that represents logging information.  
Type: [VirtualGatewayLogging](API_VirtualGatewayLogging.md) object  
Required: No

## See Also
<a name="API_VirtualGatewaySpec_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/VirtualGatewaySpec) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/VirtualGatewaySpec) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/VirtualGatewaySpec) 