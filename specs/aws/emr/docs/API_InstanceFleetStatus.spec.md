---
id: "@specs/aws/emr/docs/API_InstanceFleetStatus"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS InstanceFleetStatus"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# InstanceFleetStatus

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_InstanceFleetStatus
> **target_lang:** meta — documentation tier. ALL sections preserved.



# InstanceFleetStatus
<a name="API_InstanceFleetStatus"></a>

The status of the instance fleet.

**Note**  
The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions.

## Contents
<a name="API_InstanceFleetStatus_Contents"></a>

 ** State **   <a name="EMR-Type-InstanceFleetStatus-State"></a>
A code representing the instance fleet status.  
+  `PROVISIONING`—The instance fleet is provisioning Amazon EC2 resources and is not yet ready to run jobs.
+  `BOOTSTRAPPING`—Amazon EC2 instances and other resources have been provisioned and the bootstrap actions specified for the instances are underway.
+  `RUNNING`—Amazon EC2 instances and other resources are running. They are either executing jobs or waiting to execute jobs.
+  `RESIZING`—A resize operation is underway. Amazon EC2 instances are either being added or removed.
+  `SUSPENDED`—A resize operation could not complete. Existing Amazon EC2 instances are running, but instances can't be added or removed.
+  `TERMINATING`—The instance fleet is terminating Amazon EC2 instances.
+  `TERMINATED`—The instance fleet is no longer active, and all Amazon EC2 instances have been terminated.
Type: String  
Valid Values: `PROVISIONING | BOOTSTRAPPING | RUNNING | RESIZING | RECONFIGURING | SUSPENDED | TERMINATING | TERMINATED`   
Required: No

 ** StateChangeReason **   <a name="EMR-Type-InstanceFleetStatus-StateChangeReason"></a>
Provides status change reason details for the instance fleet.  
Type: [InstanceFleetStateChangeReason](API_InstanceFleetStateChangeReason.md) object  
Required: No

 ** Timeline **   <a name="EMR-Type-InstanceFleetStatus-Timeline"></a>
Provides historical timestamps for the instance fleet, including the time of creation, the time it became ready to run jobs, and the time of termination.  
Type: [InstanceFleetTimeline](API_InstanceFleetTimeline.md) object  
Required: No

## See Also
<a name="API_InstanceFleetStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/InstanceFleetStatus) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/InstanceFleetStatus) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/InstanceFleetStatus) 