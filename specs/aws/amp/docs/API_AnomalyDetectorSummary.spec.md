---
id: "@specs/aws/amp/docs/API_AnomalyDetectorSummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AnomalyDetectorSummary"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# AnomalyDetectorSummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_AnomalyDetectorSummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AnomalyDetectorSummary
<a name="API_AnomalyDetectorSummary"></a>

Summary information about an anomaly detector for list operations.

## Contents
<a name="API_AnomalyDetectorSummary_Contents"></a>

 ** alias **   <a name="prometheus-Type-AnomalyDetectorSummary-alias"></a>
The user-friendly name of the anomaly detector.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[0-9A-Za-z][-.0-9A-Z_a-z]*`   
Required: Yes

 ** anomalyDetectorId **   <a name="prometheus-Type-AnomalyDetectorSummary-anomalyDetectorId"></a>
The unique identifier of the anomaly detector.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `ad-[0-9A-Za-z][-.0-9A-Z_a-z]*`   
Required: Yes

 ** arn **   <a name="prometheus-Type-AnomalyDetectorSummary-arn"></a>
The Amazon Resource Name (ARN) of the anomaly detector.  
Type: String  
Pattern: `arn:aws[-a-z]*:aps:[-a-z0-9]+:[0-9]{12}:anomalydetector/ws-.+/ad-.+`   
Required: Yes

 ** createdAt **   <a name="prometheus-Type-AnomalyDetectorSummary-createdAt"></a>
The timestamp when the anomaly detector was created.  
Type: Timestamp  
Required: Yes

 ** modifiedAt **   <a name="prometheus-Type-AnomalyDetectorSummary-modifiedAt"></a>
The timestamp when the anomaly detector was last modified.  
Type: Timestamp  
Required: Yes

 ** status **   <a name="prometheus-Type-AnomalyDetectorSummary-status"></a>
The current status of the anomaly detector.  
Type: [AnomalyDetectorStatus](API_AnomalyDetectorStatus.md) object  
Required: Yes

 ** tags **   <a name="prometheus-Type-AnomalyDetectorSummary-tags"></a>
The tags applied to the anomaly detector.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`   
Required: No

## See Also
<a name="API_AnomalyDetectorSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/AnomalyDetectorSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/AnomalyDetectorSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/AnomalyDetectorSummary) 