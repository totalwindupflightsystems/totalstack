---
id: "@specs/aws/emr/docs/API_InstanceGroupStatus"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS InstanceGroupStatus"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# InstanceGroupStatus

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_InstanceGroupStatus
> **target_lang:** meta — documentation tier. ALL sections preserved.



# InstanceGroupStatus
<a name="API_InstanceGroupStatus"></a>

The details of the instance group status.

## Contents
<a name="API_InstanceGroupStatus_Contents"></a>

 ** State **   <a name="EMR-Type-InstanceGroupStatus-State"></a>
The current state of the instance group.  
Type: String  
Valid Values: `PROVISIONING | BOOTSTRAPPING | RUNNING | RECONFIGURING | RESIZING | SUSPENDED | TERMINATING | TERMINATED | ARRESTED | SHUTTING_DOWN | ENDED`   
Required: No

 ** StateChangeReason **   <a name="EMR-Type-InstanceGroupStatus-StateChangeReason"></a>
The status change reason details for the instance group.  
Type: [InstanceGroupStateChangeReason](API_InstanceGroupStateChangeReason.md) object  
Required: No

 ** Timeline **   <a name="EMR-Type-InstanceGroupStatus-Timeline"></a>
The timeline of the instance group status over time.  
Type: [InstanceGroupTimeline](API_InstanceGroupTimeline.md) object  
Required: No

## See Also
<a name="API_InstanceGroupStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/InstanceGroupStatus) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/InstanceGroupStatus) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/InstanceGroupStatus) 