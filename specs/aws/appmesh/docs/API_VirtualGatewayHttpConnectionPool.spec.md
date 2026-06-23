---
id: "@specs/aws/appmesh/docs/API_VirtualGatewayHttpConnectionPool"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS VirtualGatewayHttpConnectionPool"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# VirtualGatewayHttpConnectionPool

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_VirtualGatewayHttpConnectionPool
> **target_lang:** meta — documentation tier. ALL sections preserved.



# VirtualGatewayHttpConnectionPool
<a name="API_VirtualGatewayHttpConnectionPool"></a>

An object that represents a type of connection pool.

## Contents
<a name="API_VirtualGatewayHttpConnectionPool_Contents"></a>

 ** maxConnections **   <a name="appmesh-Type-VirtualGatewayHttpConnectionPool-maxConnections"></a>
Maximum number of outbound TCP connections Envoy can establish concurrently with all hosts in upstream cluster.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: Yes

 ** maxPendingRequests **   <a name="appmesh-Type-VirtualGatewayHttpConnectionPool-maxPendingRequests"></a>
Number of overflowing requests after `max_connections` Envoy will queue to upstream cluster.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

## See Also
<a name="API_VirtualGatewayHttpConnectionPool_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/VirtualGatewayHttpConnectionPool) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/VirtualGatewayHttpConnectionPool) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/VirtualGatewayHttpConnectionPool) 