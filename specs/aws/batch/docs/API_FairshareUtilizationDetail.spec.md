---
id: "@specs/aws/batch/docs/API_FairshareUtilizationDetail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS FairshareUtilizationDetail"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# FairshareUtilizationDetail

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_FairshareUtilizationDetail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# FairshareUtilizationDetail
<a name="API_FairshareUtilizationDetail"></a>

The fairshare utilization for a job queue, including the number of active shares and top capacity utilization.

## Contents
<a name="API_FairshareUtilizationDetail_Contents"></a>

 ** activeShareCount **   <a name="Batch-Type-FairshareUtilizationDetail-activeShareCount"></a>
The total number of active shares in the fairshare scheduling job queue that are currently utilizing capacity.  
Type: Long  
Required: No

 ** topCapacityUtilization **   <a name="Batch-Type-FairshareUtilizationDetail-topCapacityUtilization"></a>
A list of the top 20 shares with the highest capacity utilization, ordered by usage amount.  
Type: Array of [FairshareCapacityUtilization](API_FairshareCapacityUtilization.md) objects  
Required: No

## See Also
<a name="API_FairshareUtilizationDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/FairshareUtilizationDetail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/FairshareUtilizationDetail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/FairshareUtilizationDetail) 