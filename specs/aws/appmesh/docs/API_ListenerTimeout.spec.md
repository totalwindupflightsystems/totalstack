---
id: "@specs/aws/appmesh/docs/API_ListenerTimeout"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListenerTimeout"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# ListenerTimeout

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_ListenerTimeout
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListenerTimeout
<a name="API_ListenerTimeout"></a>

An object that represents timeouts for different protocols.

## Contents
<a name="API_ListenerTimeout_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** grpc **   <a name="appmesh-Type-ListenerTimeout-grpc"></a>
An object that represents types of timeouts.   
Type: [GrpcTimeout](API_GrpcTimeout.md) object  
Required: No

 ** http **   <a name="appmesh-Type-ListenerTimeout-http"></a>
An object that represents types of timeouts.   
Type: [HttpTimeout](API_HttpTimeout.md) object  
Required: No

 ** http2 **   <a name="appmesh-Type-ListenerTimeout-http2"></a>
An object that represents types of timeouts.   
Type: [HttpTimeout](API_HttpTimeout.md) object  
Required: No

 ** tcp **   <a name="appmesh-Type-ListenerTimeout-tcp"></a>
An object that represents types of timeouts.   
Type: [TcpTimeout](API_TcpTimeout.md) object  
Required: No

## See Also
<a name="API_ListenerTimeout_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/ListenerTimeout) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/ListenerTimeout) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/ListenerTimeout) 