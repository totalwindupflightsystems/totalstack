---
id: "@specs/aws/appmesh/docs/API_VirtualNodeConnectionPool"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS VirtualNodeConnectionPool"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# VirtualNodeConnectionPool

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_VirtualNodeConnectionPool
> **target_lang:** meta — documentation tier. ALL sections preserved.



# VirtualNodeConnectionPool
<a name="API_VirtualNodeConnectionPool"></a>

An object that represents the type of virtual node connection pool.

Only one protocol is used at a time and should be the same protocol as the one chosen under port mapping.

If not present the default value for `maxPendingRequests` is `2147483647`.



## Contents
<a name="API_VirtualNodeConnectionPool_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** grpc **   <a name="appmesh-Type-VirtualNodeConnectionPool-grpc"></a>
An object that represents a type of connection pool.  
Type: [VirtualNodeGrpcConnectionPool](API_VirtualNodeGrpcConnectionPool.md) object  
Required: No

 ** http **   <a name="appmesh-Type-VirtualNodeConnectionPool-http"></a>
An object that represents a type of connection pool.  
Type: [VirtualNodeHttpConnectionPool](API_VirtualNodeHttpConnectionPool.md) object  
Required: No

 ** http2 **   <a name="appmesh-Type-VirtualNodeConnectionPool-http2"></a>
An object that represents a type of connection pool.  
Type: [VirtualNodeHttp2ConnectionPool](API_VirtualNodeHttp2ConnectionPool.md) object  
Required: No

 ** tcp **   <a name="appmesh-Type-VirtualNodeConnectionPool-tcp"></a>
An object that represents a type of connection pool.  
Type: [VirtualNodeTcpConnectionPool](API_VirtualNodeTcpConnectionPool.md) object  
Required: No

## See Also
<a name="API_VirtualNodeConnectionPool_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/VirtualNodeConnectionPool) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/VirtualNodeConnectionPool) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/VirtualNodeConnectionPool) 