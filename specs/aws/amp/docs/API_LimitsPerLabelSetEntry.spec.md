---
id: "@specs/aws/amp/docs/API_LimitsPerLabelSetEntry"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS LimitsPerLabelSetEntry"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# LimitsPerLabelSetEntry

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_LimitsPerLabelSetEntry
> **target_lang:** meta — documentation tier. ALL sections preserved.



# LimitsPerLabelSetEntry
<a name="API_LimitsPerLabelSetEntry"></a>

This structure contains the information about the limits that apply to time series that match one label set.

## Contents
<a name="API_LimitsPerLabelSetEntry_Contents"></a>

 ** maxSeries **   <a name="prometheus-Type-LimitsPerLabelSetEntry-maxSeries"></a>
The maximum number of active series that can be ingested that match this label set.   
Setting this to 0 causes no label set limit to be enforced, but it does cause Amazon Managed Service for Prometheus to vend label set metrics to CloudWatch  
Type: Long  
Valid Range: Minimum value of 0.  
Required: No

## See Also
<a name="API_LimitsPerLabelSetEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/LimitsPerLabelSetEntry) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/LimitsPerLabelSetEntry) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/LimitsPerLabelSetEntry) 