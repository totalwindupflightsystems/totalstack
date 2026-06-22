---
id: "@specs/aws/emr/docs/API_CloudWatchAlarmDefinition"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CloudWatchAlarmDefinition"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# CloudWatchAlarmDefinition

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_CloudWatchAlarmDefinition
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CloudWatchAlarmDefinition
<a name="API_CloudWatchAlarmDefinition"></a>

The definition of a CloudWatch metric alarm, which determines when an automatic scaling activity is triggered. When the defined alarm conditions are satisfied, scaling activity begins.

## Contents
<a name="API_CloudWatchAlarmDefinition_Contents"></a>

 ** ComparisonOperator **   <a name="EMR-Type-CloudWatchAlarmDefinition-ComparisonOperator"></a>
Determines how the metric specified by `MetricName` is compared to the value specified by `Threshold`.  
Type: String  
Valid Values: `GREATER_THAN_OR_EQUAL | GREATER_THAN | LESS_THAN | LESS_THAN_OR_EQUAL`   
Required: Yes

 ** MetricName **   <a name="EMR-Type-CloudWatchAlarmDefinition-MetricName"></a>
The name of the CloudWatch metric that is watched to determine an alarm condition.  
Type: String  
Required: Yes

 ** Period **   <a name="EMR-Type-CloudWatchAlarmDefinition-Period"></a>
The period, in seconds, over which the statistic is applied. CloudWatch metrics for Amazon EMR are emitted every five minutes (300 seconds), so if you specify a CloudWatch metric, specify `300`.  
Type: Integer  
Required: Yes

 ** Threshold **   <a name="EMR-Type-CloudWatchAlarmDefinition-Threshold"></a>
The value against which the specified statistic is compared.  
Type: Double  
Valid Range: Minimum value of 0.0.  
Required: Yes

 ** Dimensions **   <a name="EMR-Type-CloudWatchAlarmDefinition-Dimensions"></a>
A CloudWatch metric dimension.  
Type: Array of [MetricDimension](API_MetricDimension.md) objects  
Required: No

 ** EvaluationPeriods **   <a name="EMR-Type-CloudWatchAlarmDefinition-EvaluationPeriods"></a>
The number of periods, in five-minute increments, during which the alarm condition must exist before the alarm triggers automatic scaling activity. The default value is `1`.  
Type: Integer  
Required: No

 ** Namespace **   <a name="EMR-Type-CloudWatchAlarmDefinition-Namespace"></a>
The namespace for the CloudWatch metric. The default is `AWS/ElasticMapReduce`.  
Type: String  
Required: No

 ** Statistic **   <a name="EMR-Type-CloudWatchAlarmDefinition-Statistic"></a>
The statistic to apply to the metric associated with the alarm. The default is `AVERAGE`.  
Type: String  
Valid Values: `SAMPLE_COUNT | AVERAGE | SUM | MINIMUM | MAXIMUM`   
Required: No

 ** Unit **   <a name="EMR-Type-CloudWatchAlarmDefinition-Unit"></a>
The unit of measure associated with the CloudWatch metric being watched. The value specified for `Unit` must correspond to the units specified in the CloudWatch metric.  
Type: String  
Valid Values: `NONE | SECONDS | MICRO_SECONDS | MILLI_SECONDS | BYTES | KILO_BYTES | MEGA_BYTES | GIGA_BYTES | TERA_BYTES | BITS | KILO_BITS | MEGA_BITS | GIGA_BITS | TERA_BITS | PERCENT | COUNT | BYTES_PER_SECOND | KILO_BYTES_PER_SECOND | MEGA_BYTES_PER_SECOND | GIGA_BYTES_PER_SECOND | TERA_BYTES_PER_SECOND | BITS_PER_SECOND | KILO_BITS_PER_SECOND | MEGA_BITS_PER_SECOND | GIGA_BITS_PER_SECOND | TERA_BITS_PER_SECOND | COUNT_PER_SECOND`   
Required: No

## See Also
<a name="API_CloudWatchAlarmDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/CloudWatchAlarmDefinition) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/CloudWatchAlarmDefinition) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/CloudWatchAlarmDefinition) 