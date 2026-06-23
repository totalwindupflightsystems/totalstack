---
id: "@specs/aws/appmesh/docs/API_OutlierDetection"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS OutlierDetection"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# OutlierDetection

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_OutlierDetection
> **target_lang:** meta — documentation tier. ALL sections preserved.



# OutlierDetection
<a name="API_OutlierDetection"></a>

An object that represents the outlier detection for a virtual node's listener.

## Contents
<a name="API_OutlierDetection_Contents"></a>

 ** baseEjectionDuration **   <a name="appmesh-Type-OutlierDetection-baseEjectionDuration"></a>
The base amount of time for which a host is ejected.  
Type: [Duration](API_Duration.md) object  
Required: Yes

 ** interval **   <a name="appmesh-Type-OutlierDetection-interval"></a>
The time interval between ejection sweep analysis.  
Type: [Duration](API_Duration.md) object  
Required: Yes

 ** maxEjectionPercent **   <a name="appmesh-Type-OutlierDetection-maxEjectionPercent"></a>
Maximum percentage of hosts in load balancing pool for upstream service that can be ejected. Will eject at least one host regardless of the value.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 100.  
Required: Yes

 ** maxServerErrors **   <a name="appmesh-Type-OutlierDetection-maxServerErrors"></a>
Number of consecutive `5xx` errors required for ejection.   
Type: Long  
Valid Range: Minimum value of 1.  
Required: Yes

## See Also
<a name="API_OutlierDetection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/OutlierDetection) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/OutlierDetection) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/OutlierDetection) 