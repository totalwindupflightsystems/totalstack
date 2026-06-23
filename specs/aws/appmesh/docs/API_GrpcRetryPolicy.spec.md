---
id: "@specs/aws/appmesh/docs/API_GrpcRetryPolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GrpcRetryPolicy"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# GrpcRetryPolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_GrpcRetryPolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GrpcRetryPolicy
<a name="API_GrpcRetryPolicy"></a>

An object that represents a retry policy. Specify at least one value for at least one of the types of `RetryEvents`, a value for `maxRetries`, and a value for `perRetryTimeout`. Both `server-error` and `gateway-error` under `httpRetryEvents` include the Envoy `reset` policy. For more information on the `reset` policy, see the [Envoy documentation](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/router_filter#x-envoy-retry-on).

## Contents
<a name="API_GrpcRetryPolicy_Contents"></a>

 ** maxRetries **   <a name="appmesh-Type-GrpcRetryPolicy-maxRetries"></a>
The maximum number of retry attempts.  
Type: Long  
Valid Range: Minimum value of 0.  
Required: Yes

 ** perRetryTimeout **   <a name="appmesh-Type-GrpcRetryPolicy-perRetryTimeout"></a>
The timeout for each retry attempt.  
Type: [Duration](API_Duration.md) object  
Required: Yes

 ** grpcRetryEvents **   <a name="appmesh-Type-GrpcRetryPolicy-grpcRetryEvents"></a>
Specify at least one of the valid values.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 5 items.  
Valid Values: `cancelled | deadline-exceeded | internal | resource-exhausted | unavailable`   
Required: No

 ** httpRetryEvents **   <a name="appmesh-Type-GrpcRetryPolicy-httpRetryEvents"></a>
Specify at least one of the following values.  
+  **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510, and 511
+  **gateway-error** – HTTP status codes 502, 503, and 504
+  **client-error** – HTTP status code 409
+  **stream-error** – Retry on refused stream
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 25 items.  
Length Constraints: Minimum length of 1. Maximum length of 25.  
Required: No

 ** tcpRetryEvents **   <a name="appmesh-Type-GrpcRetryPolicy-tcpRetryEvents"></a>
Specify a valid value. The event occurs before any processing of a request has started and is encountered when the upstream is temporarily or permanently unavailable.  
Type: Array of strings  
Array Members: Fixed number of 1 item.  
Valid Values: `connection-error`   
Required: No

## See Also
<a name="API_GrpcRetryPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/GrpcRetryPolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/GrpcRetryPolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/GrpcRetryPolicy) 