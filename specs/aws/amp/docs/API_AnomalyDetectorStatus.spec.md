---
id: "@specs/aws/amp/docs/API_AnomalyDetectorStatus"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AnomalyDetectorStatus"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# AnomalyDetectorStatus

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_AnomalyDetectorStatus
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AnomalyDetectorStatus
<a name="API_AnomalyDetectorStatus"></a>

The status information of an anomaly detector.

## Contents
<a name="API_AnomalyDetectorStatus_Contents"></a>

 ** statusCode **   <a name="prometheus-Type-AnomalyDetectorStatus-statusCode"></a>
The status code of the anomaly detector.  
Type: String  
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | CREATION_FAILED | UPDATE_FAILED | DELETION_FAILED`   
Required: Yes

 ** statusReason **   <a name="prometheus-Type-AnomalyDetectorStatus-statusReason"></a>
A description of the current status of the anomaly detector.  
Type: String  
Required: No

## See Also
<a name="API_AnomalyDetectorStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/AnomalyDetectorStatus) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/AnomalyDetectorStatus) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/AnomalyDetectorStatus) 