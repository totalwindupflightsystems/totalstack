---
id: "@specs/aws/amp/docs/API_AnomalyDetectorMissingDataAction"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AnomalyDetectorMissingDataAction"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# AnomalyDetectorMissingDataAction

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_AnomalyDetectorMissingDataAction
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AnomalyDetectorMissingDataAction
<a name="API_AnomalyDetectorMissingDataAction"></a>

Specifies the action to take when data is missing during anomaly detection evaluation.

## Contents
<a name="API_AnomalyDetectorMissingDataAction_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** markAsAnomaly **   <a name="prometheus-Type-AnomalyDetectorMissingDataAction-markAsAnomaly"></a>
Marks missing data points as anomalies.  
Type: Boolean  
Required: No

 ** skip **   <a name="prometheus-Type-AnomalyDetectorMissingDataAction-skip"></a>
Skips evaluation when data is missing.  
Type: Boolean  
Required: No

## See Also
<a name="API_AnomalyDetectorMissingDataAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/AnomalyDetectorMissingDataAction) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/AnomalyDetectorMissingDataAction) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/AnomalyDetectorMissingDataAction) 