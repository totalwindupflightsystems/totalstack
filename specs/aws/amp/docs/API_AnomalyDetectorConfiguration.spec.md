---
id: "@specs/aws/amp/docs/API_AnomalyDetectorConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AnomalyDetectorConfiguration"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# AnomalyDetectorConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_AnomalyDetectorConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AnomalyDetectorConfiguration
<a name="API_AnomalyDetectorConfiguration"></a>

The configuration for the anomaly detection algorithm.

## Contents
<a name="API_AnomalyDetectorConfiguration_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** randomCutForest **   <a name="prometheus-Type-AnomalyDetectorConfiguration-randomCutForest"></a>
The Random Cut Forest algorithm configuration for anomaly detection.  
Type: [RandomCutForestConfiguration](API_RandomCutForestConfiguration.md) object  
Required: No

## See Also
<a name="API_AnomalyDetectorConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/AnomalyDetectorConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/AnomalyDetectorConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/AnomalyDetectorConfiguration) 