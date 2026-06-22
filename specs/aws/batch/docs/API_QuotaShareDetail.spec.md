---
id: "@specs/aws/batch/docs/API_QuotaShareDetail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS QuotaShareDetail"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# QuotaShareDetail

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_QuotaShareDetail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# QuotaShareDetail
<a name="API_QuotaShareDetail"></a>

Detailed information about a quota share, including its configuration, state, and capacity limits.

## Contents
<a name="API_QuotaShareDetail_Contents"></a>

 ** capacityLimits **   <a name="Batch-Type-QuotaShareDetail-capacityLimits"></a>
A list that specifies the quantity and type of compute capacity allocated to the quota share.  
Type: Array of [QuotaShareCapacityLimit](API_QuotaShareCapacityLimit.md) objects  
Required: No

 ** jobQueueArn **   <a name="Batch-Type-QuotaShareDetail-jobQueueArn"></a>
The Amazon Resource Name (ARN) of the job queue associated with the quota share.  
Type: String  
Required: No

 ** preemptionConfiguration **   <a name="Batch-Type-QuotaShareDetail-preemptionConfiguration"></a>
Specifies the preemption behavior for jobs in a quota share.  
Type: [QuotaSharePreemptionConfiguration](API_QuotaSharePreemptionConfiguration.md) object  
Required: No

 ** quotaShareArn **   <a name="Batch-Type-QuotaShareDetail-quotaShareArn"></a>
The Amazon Resource Name (ARN) of the quota share.  
Type: String  
Required: No

 ** quotaShareName **   <a name="Batch-Type-QuotaShareDetail-quotaShareName"></a>
The name of the quota share.  
Type: String  
Required: No

 ** resourceSharingConfiguration **   <a name="Batch-Type-QuotaShareDetail-resourceSharingConfiguration"></a>
Specifies whether a quota share reserves, lends, or both lends and borrows idle compute capacity.  
Type: [QuotaShareResourceSharingConfiguration](API_QuotaShareResourceSharingConfiguration.md) object  
Required: No

 ** state **   <a name="Batch-Type-QuotaShareDetail-state"></a>
The state of the quota share.  
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: No

 ** status **   <a name="Batch-Type-QuotaShareDetail-status"></a>
The current status of the quota share.  
Type: String  
Valid Values: `CREATING | VALID | INVALID | UPDATING | DELETING`   
Required: No

## See Also
<a name="API_QuotaShareDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/QuotaShareDetail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/QuotaShareDetail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/QuotaShareDetail) 