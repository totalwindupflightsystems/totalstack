---
id: "@specs/aws/amp/docs/API_LimitsPerLabelSet"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS LimitsPerLabelSet"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# LimitsPerLabelSet

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_LimitsPerLabelSet
> **target_lang:** meta — documentation tier. ALL sections preserved.



# LimitsPerLabelSet
<a name="API_LimitsPerLabelSet"></a>

This structure defines one label set used to enforce active time series limits for the workspace, and defines the limit for that label set.

A label set is a unique combination of label-value pairs. Use them to control time series limits and to monitor usage by specific label groups. Example label sets might be `team:finance` or `env:prod` 

## Contents
<a name="API_LimitsPerLabelSet_Contents"></a>

 ** labelSet **   <a name="prometheus-Type-LimitsPerLabelSet-labelSet"></a>
This defines one label set that will have an enforced active time series limit.   
Label values accept ASCII characters and must contain at least one character that isn't whitespace. ASCII control characters are not accepted. If the label name is metric name label `__name__`, then the *metric* part of the name must conform to the following pattern: `[a-zA-Z_:][a-zA-Z0-9_:]*`   
Type: String to string map  
Key Length Constraints: Minimum length of 1.  
Key Pattern: `[a-zA-Z_][a-zA-Z0-9_]*`   
Value Length Constraints: Minimum length of 1.  
Required: Yes

 ** limits **   <a name="prometheus-Type-LimitsPerLabelSet-limits"></a>
This structure contains the information about the limits that apply to time series that match this label set.  
Type: [LimitsPerLabelSetEntry](API_LimitsPerLabelSetEntry.md) object  
Required: Yes

## See Also
<a name="API_LimitsPerLabelSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/LimitsPerLabelSet) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/LimitsPerLabelSet) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/LimitsPerLabelSet) 