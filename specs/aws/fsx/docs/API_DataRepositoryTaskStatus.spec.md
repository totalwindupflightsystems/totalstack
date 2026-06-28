---
id: "@specs/aws/fsx/docs/API_DataRepositoryTaskStatus"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DataRepositoryTaskStatus"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# DataRepositoryTaskStatus

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_DataRepositoryTaskStatus
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DataRepositoryTaskStatus
<a name="API_DataRepositoryTaskStatus"></a>

Provides the task status showing a running total of the total number of files to be processed, the number successfully processed, and the number of files the task failed to process.

## Contents
<a name="API_DataRepositoryTaskStatus_Contents"></a>

 ** FailedCount **   <a name="FSx-Type-DataRepositoryTaskStatus-FailedCount"></a>
A running total of the number of files that the task failed to process.  
Type: Long  
Required: No

 ** LastUpdatedTime **   <a name="FSx-Type-DataRepositoryTaskStatus-LastUpdatedTime"></a>
The time at which the task status was last updated.  
Type: Timestamp  
Required: No

 ** ReleasedCapacity **   <a name="FSx-Type-DataRepositoryTaskStatus-ReleasedCapacity"></a>
The total amount of data, in GiB, released by an Amazon File Cache AUTO\_RELEASE\_DATA task that automatically releases files from the cache.  
Type: Long  
Required: No

 ** SucceededCount **   <a name="FSx-Type-DataRepositoryTaskStatus-SucceededCount"></a>
A running total of the number of files that the task has successfully processed.  
Type: Long  
Required: No

 ** TotalCount **   <a name="FSx-Type-DataRepositoryTaskStatus-TotalCount"></a>
The total number of files that the task will process. While a task is executing, the sum of `SucceededCount` plus `FailedCount` may not equal `TotalCount`. When the task is complete, `TotalCount` equals the sum of `SucceededCount` plus `FailedCount`.  
Type: Long  
Required: No

## See Also
<a name="API_DataRepositoryTaskStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/DataRepositoryTaskStatus) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/DataRepositoryTaskStatus) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/DataRepositoryTaskStatus) 