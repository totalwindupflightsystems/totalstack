---
id: "@specs/aws/amp/docs/API_AnomalyDetectorDescription"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AnomalyDetectorDescription"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# AnomalyDetectorDescription

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_AnomalyDetectorDescription
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AnomalyDetectorDescription
<a name="API_AnomalyDetectorDescription"></a>

Detailed information about an anomaly detector.

## Contents
<a name="API_AnomalyDetectorDescription_Contents"></a>

 ** alias **   <a name="prometheus-Type-AnomalyDetectorDescription-alias"></a>
The user-friendly name of the anomaly detector.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[0-9A-Za-z][-.0-9A-Z_a-z]*`   
Required: Yes

 ** anomalyDetectorId **   <a name="prometheus-Type-AnomalyDetectorDescription-anomalyDetectorId"></a>
The unique identifier of the anomaly detector.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `ad-[0-9A-Za-z][-.0-9A-Z_a-z]*`   
Required: Yes

 ** arn **   <a name="prometheus-Type-AnomalyDetectorDescription-arn"></a>
The Amazon Resource Name (ARN) of the anomaly detector.  
Type: String  
Pattern: `arn:aws[-a-z]*:aps:[-a-z0-9]+:[0-9]{12}:anomalydetector/ws-.+/ad-.+`   
Required: Yes

 ** createdAt **   <a name="prometheus-Type-AnomalyDetectorDescription-createdAt"></a>
The timestamp when the anomaly detector was created.  
Type: Timestamp  
Required: Yes

 ** modifiedAt **   <a name="prometheus-Type-AnomalyDetectorDescription-modifiedAt"></a>
The timestamp when the anomaly detector was last modified.  
Type: Timestamp  
Required: Yes

 ** status **   <a name="prometheus-Type-AnomalyDetectorDescription-status"></a>
The current status of the anomaly detector.  
Type: [AnomalyDetectorStatus](API_AnomalyDetectorStatus.md) object  
Required: Yes

 ** configuration **   <a name="prometheus-Type-AnomalyDetectorDescription-configuration"></a>
The algorithm configuration of the anomaly detector.  
Type: [AnomalyDetectorConfiguration](API_AnomalyDetectorConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** evaluationIntervalInSeconds **   <a name="prometheus-Type-AnomalyDetectorDescription-evaluationIntervalInSeconds"></a>
The frequency, in seconds, at which the anomaly detector evaluates metrics.  
Type: Integer  
Valid Range: Minimum value of 30. Maximum value of 86400.  
Required: No

 ** labels **   <a name="prometheus-Type-AnomalyDetectorDescription-labels"></a>
The Amazon Managed Service for Prometheus metric labels associated with the anomaly detector.  
Type: String to string map  
Key Length Constraints: Minimum length of 1. Maximum length of 7168.  
Key Pattern: `(?!__)[a-zA-Z_][a-zA-Z0-9_]*`   
Value Length Constraints: Minimum length of 1. Maximum length of 7168.  
Required: No

 ** missingDataAction **   <a name="prometheus-Type-AnomalyDetectorDescription-missingDataAction"></a>
The action taken when data is missing during evaluation.  
Type: [AnomalyDetectorMissingDataAction](API_AnomalyDetectorMissingDataAction.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** tags **   <a name="prometheus-Type-AnomalyDetectorDescription-tags"></a>
The tags applied to the anomaly detector.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`   
Required: No

## See Also
<a name="API_AnomalyDetectorDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/AnomalyDetectorDescription) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/AnomalyDetectorDescription) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/AnomalyDetectorDescription) 