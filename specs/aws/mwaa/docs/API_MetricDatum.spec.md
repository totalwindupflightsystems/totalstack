---
id: "@specs/aws/mwaa/docs/API_MetricDatum"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS MetricDatum"
status: active
depends_on:
  - "@specs/aws/mwaa/meta"
---

# MetricDatum

> **source:** AWS Documentation
> **spec:id:** @specs/aws/mwaa/docs/API_MetricDatum
> **target_lang:** meta — documentation tier. ALL sections preserved.



# MetricDatum
<a name="API_MetricDatum"></a>

 *This data type has been deprecated.* 

 **Internal only**. Collects Apache Airflow metrics. To learn more about the metrics published to Amazon CloudWatch, see [Amazon MWAA performance metrics in Amazon CloudWatch](https://docs.aws.amazon.com/mwaa/latest/userguide/cw-metrics.html).

## Contents
<a name="API_MetricDatum_Contents"></a>

 ** MetricName **   <a name="mwaa-Type-MetricDatum-MetricName"></a>
 **Internal only**. The name of the metric.  
Type: String  
Required: Yes

 ** Timestamp **   <a name="mwaa-Type-MetricDatum-Timestamp"></a>
 **Internal only**. The time the metric data was received, expressed as an ISO 8601 datetime string.  
Type: Timestamp  
Required: Yes

 ** Dimensions **   <a name="mwaa-Type-MetricDatum-Dimensions"></a>
 *This member has been deprecated.*   
 **Internal only**. The dimensions associated with the metric.  
Type: Array of [Dimension](API_Dimension.md) objects  
Required: No

 ** StatisticValues **   <a name="mwaa-Type-MetricDatum-StatisticValues"></a>
 *This member has been deprecated.*   
 **Internal only**. The statistical values for the metric.  
Type: [StatisticSet](API_StatisticSet.md) object  
Required: No

 ** Unit **   <a name="mwaa-Type-MetricDatum-Unit"></a>
 **Internal only**. The unit used to store the metric.  
Type: String  
Valid Values: `Seconds | Microseconds | Milliseconds | Bytes | Kilobytes | Megabytes | Gigabytes | Terabytes | Bits | Kilobits | Megabits | Gigabits | Terabits | Percent | Count | Bytes/Second | Kilobytes/Second | Megabytes/Second | Gigabytes/Second | Terabytes/Second | Bits/Second | Kilobits/Second | Megabits/Second | Gigabits/Second | Terabits/Second | Count/Second | None`   
Required: No

 ** Value **   <a name="mwaa-Type-MetricDatum-Value"></a>
 **Internal only**. The value for the metric.  
Type: Double  
Required: No

## See Also
<a name="API_MetricDatum_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mwaa-2020-07-01/MetricDatum) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mwaa-2020-07-01/MetricDatum) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mwaa-2020-07-01/MetricDatum) 