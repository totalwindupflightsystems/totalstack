---
id: "@specs/aws/appmesh/docs/API_HttpTimeout"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS HttpTimeout"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# HttpTimeout

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_HttpTimeout
> **target_lang:** meta — documentation tier. ALL sections preserved.



# HttpTimeout
<a name="API_HttpTimeout"></a>

An object that represents types of timeouts. 

## Contents
<a name="API_HttpTimeout_Contents"></a>

 ** idle **   <a name="appmesh-Type-HttpTimeout-idle"></a>
An object that represents an idle timeout. An idle timeout bounds the amount of time that a connection may be idle. The default value is none.  
Type: [Duration](API_Duration.md) object  
Required: No

 ** perRequest **   <a name="appmesh-Type-HttpTimeout-perRequest"></a>
An object that represents a per request timeout. The default value is 15 seconds. If you set a higher timeout, then make sure that the higher value is set for each App Mesh resource in a conversation. For example, if a virtual node backend uses a virtual router provider to route to another virtual node, then the timeout should be greater than 15 seconds for the source and destination virtual node and the route.  
Type: [Duration](API_Duration.md) object  
Required: No

## See Also
<a name="API_HttpTimeout_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/HttpTimeout) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/HttpTimeout) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/HttpTimeout) 