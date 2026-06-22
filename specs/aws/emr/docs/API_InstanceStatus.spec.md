---
id: "@specs/aws/emr/docs/API_InstanceStatus"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS InstanceStatus"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# InstanceStatus

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_InstanceStatus
> **target_lang:** meta — documentation tier. ALL sections preserved.



# InstanceStatus
<a name="API_InstanceStatus"></a>

The instance status details.

## Contents
<a name="API_InstanceStatus_Contents"></a>

 ** State **   <a name="EMR-Type-InstanceStatus-State"></a>
The current state of the instance.  
Type: String  
Valid Values: `AWAITING_FULFILLMENT | PROVISIONING | BOOTSTRAPPING | RUNNING | TERMINATED`   
Required: No

 ** StateChangeReason **   <a name="EMR-Type-InstanceStatus-StateChangeReason"></a>
The details of the status change reason for the instance.  
Type: [InstanceStateChangeReason](API_InstanceStateChangeReason.md) object  
Required: No

 ** Timeline **   <a name="EMR-Type-InstanceStatus-Timeline"></a>
The timeline of the instance status over time.  
Type: [InstanceTimeline](API_InstanceTimeline.md) object  
Required: No

## See Also
<a name="API_InstanceStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/InstanceStatus) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/InstanceStatus) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/InstanceStatus) 