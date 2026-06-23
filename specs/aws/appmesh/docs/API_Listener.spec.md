---
id: "@specs/aws/appmesh/docs/API_Listener"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Listener"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# Listener

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_Listener
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Listener
<a name="API_Listener"></a>

An object that represents a listener for a virtual node.

## Contents
<a name="API_Listener_Contents"></a>

 ** portMapping **   <a name="appmesh-Type-Listener-portMapping"></a>
The port mapping information for the listener.  
Type: [PortMapping](API_PortMapping.md) object  
Required: Yes

 ** connectionPool **   <a name="appmesh-Type-Listener-connectionPool"></a>
The connection pool information for the listener.  
Type: [VirtualNodeConnectionPool](API_VirtualNodeConnectionPool.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** healthCheck **   <a name="appmesh-Type-Listener-healthCheck"></a>
The health check information for the listener.  
Type: [HealthCheckPolicy](API_HealthCheckPolicy.md) object  
Required: No

 ** outlierDetection **   <a name="appmesh-Type-Listener-outlierDetection"></a>
The outlier detection information for the listener.  
Type: [OutlierDetection](API_OutlierDetection.md) object  
Required: No

 ** timeout **   <a name="appmesh-Type-Listener-timeout"></a>
An object that represents timeouts for different protocols.  
Type: [ListenerTimeout](API_ListenerTimeout.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** tls **   <a name="appmesh-Type-Listener-tls"></a>
A reference to an object that represents the Transport Layer Security (TLS) properties for a listener.  
Type: [ListenerTls](API_ListenerTls.md) object  
Required: No

## See Also
<a name="API_Listener_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/Listener) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/Listener) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/Listener) 