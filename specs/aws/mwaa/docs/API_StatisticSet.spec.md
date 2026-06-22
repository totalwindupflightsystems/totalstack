---
id: "@specs/aws/mwaa/docs/API_StatisticSet"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StatisticSet"
status: active
depends_on:
  - "@specs/aws/mwaa/meta"
---

# StatisticSet

> **source:** AWS Documentation
> **spec:id:** @specs/aws/mwaa/docs/API_StatisticSet
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StatisticSet
<a name="API_StatisticSet"></a>

 *This data type has been deprecated.* 

 **Internal only**. Represents a set of statistics that describe a specific metric. To learn more about the metrics published to Amazon CloudWatch, see [Amazon MWAA performance metrics in Amazon CloudWatch](https://docs.aws.amazon.com/mwaa/latest/userguide/cw-metrics.html).

## Contents
<a name="API_StatisticSet_Contents"></a>

 ** Maximum **   <a name="mwaa-Type-StatisticSet-Maximum"></a>
 **Internal only**. The maximum value of the sample set.  
Type: Double  
Required: No

 ** Minimum **   <a name="mwaa-Type-StatisticSet-Minimum"></a>
 **Internal only**. The minimum value of the sample set.  
Type: Double  
Required: No

 ** SampleCount **   <a name="mwaa-Type-StatisticSet-SampleCount"></a>
 **Internal only**. The number of samples used for the statistic set.  
Type: Integer  
Required: No

 ** Sum **   <a name="mwaa-Type-StatisticSet-Sum"></a>
 **Internal only**. The sum of values for the sample set.  
Type: Double  
Required: No

## See Also
<a name="API_StatisticSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mwaa-2020-07-01/StatisticSet) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mwaa-2020-07-01/StatisticSet) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mwaa-2020-07-01/StatisticSet) 