---
id: "@specs/aws/amp/docs/API_RandomCutForestConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RandomCutForestConfiguration"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# RandomCutForestConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_RandomCutForestConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RandomCutForestConfiguration
<a name="API_RandomCutForestConfiguration"></a>

Configuration for the Random Cut Forest algorithm used for anomaly detection in time-series data.

## Contents
<a name="API_RandomCutForestConfiguration_Contents"></a>

 ** query **   <a name="prometheus-Type-RandomCutForestConfiguration-query"></a>
The Prometheus query used to retrieve the time-series data for anomaly detection.  
Random Cut Forest queries must be wrapped by a supported PromQL aggregation operator. For more information, see [Aggregation operators](https://prometheus.io/docs/prometheus/latest/querying/operators/#aggregation-operators) on the *Prometheus docs* website.  
 **Supported PromQL aggregation operators**: `avg`, `count`, `group`, `max`, `min`, `quantile`, `stddev`, `stdvar`, and `sum`.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 8192.  
Required: Yes

 ** ignoreNearExpectedFromAbove **   <a name="prometheus-Type-RandomCutForestConfiguration-ignoreNearExpectedFromAbove"></a>
Configuration for ignoring values that are near expected values from above during anomaly detection.  
Type: [IgnoreNearExpected](API_IgnoreNearExpected.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** ignoreNearExpectedFromBelow **   <a name="prometheus-Type-RandomCutForestConfiguration-ignoreNearExpectedFromBelow"></a>
Configuration for ignoring values that are near expected values from below during anomaly detection.  
Type: [IgnoreNearExpected](API_IgnoreNearExpected.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** sampleSize **   <a name="prometheus-Type-RandomCutForestConfiguration-sampleSize"></a>
The number of data points sampled from the input stream for the Random Cut Forest algorithm. The default number is 256 consecutive data points.  
Type: Integer  
Valid Range: Minimum value of 256. Maximum value of 1024.  
Required: No

 ** shingleSize **   <a name="prometheus-Type-RandomCutForestConfiguration-shingleSize"></a>
The number of consecutive data points used to create a shingle for the Random Cut Forest algorithm. The default number is 8 consecutive data points.  
Type: Integer  
Valid Range: Minimum value of 2. Maximum value of 1024.  
Required: No

## See Also
<a name="API_RandomCutForestConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/RandomCutForestConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/RandomCutForestConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/RandomCutForestConfiguration) 