---
id: "@specs/aws/appmesh/docs/API_VirtualNodeSpec"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS VirtualNodeSpec"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# VirtualNodeSpec

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_VirtualNodeSpec
> **target_lang:** meta — documentation tier. ALL sections preserved.



# VirtualNodeSpec
<a name="API_VirtualNodeSpec"></a>

An object that represents the specification of a virtual node.

## Contents
<a name="API_VirtualNodeSpec_Contents"></a>

 ** backendDefaults **   <a name="appmesh-Type-VirtualNodeSpec-backendDefaults"></a>
A reference to an object that represents the defaults for backends.  
Type: [BackendDefaults](API_BackendDefaults.md) object  
Required: No

 ** backends **   <a name="appmesh-Type-VirtualNodeSpec-backends"></a>
The backends that the virtual node is expected to send outbound traffic to.  
App Mesh doesn't validate the existence of those virtual services specified in backends. This is to prevent a cyclic dependency between virtual nodes and virtual services creation. Make sure the virtual service name is correct. The virtual service can be created afterwards if it doesn't already exist. 
Type: Array of [Backend](API_Backend.md) objects  
Required: No

 ** listeners **   <a name="appmesh-Type-VirtualNodeSpec-listeners"></a>
The listener that the virtual node is expected to receive inbound traffic from. You can specify one listener.  
Type: Array of [Listener](API_Listener.md) objects  
Required: No

 ** logging **   <a name="appmesh-Type-VirtualNodeSpec-logging"></a>
The inbound and outbound access logging information for the virtual node.  
Type: [Logging](API_Logging.md) object  
Required: No

 ** serviceDiscovery **   <a name="appmesh-Type-VirtualNodeSpec-serviceDiscovery"></a>
The service discovery information for the virtual node. If your virtual node does not expect ingress traffic, you can omit this parameter. If you specify a `listener`, then you must specify service discovery information.  
Type: [ServiceDiscovery](API_ServiceDiscovery.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

## See Also
<a name="API_VirtualNodeSpec_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/VirtualNodeSpec) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/VirtualNodeSpec) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/VirtualNodeSpec) 