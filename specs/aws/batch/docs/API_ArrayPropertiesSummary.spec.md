---
id: "@specs/aws/batch/docs/API_ArrayPropertiesSummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ArrayPropertiesSummary"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# ArrayPropertiesSummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_ArrayPropertiesSummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ArrayPropertiesSummary
<a name="API_ArrayPropertiesSummary"></a>

An object that represents the array properties of a job.

## Contents
<a name="API_ArrayPropertiesSummary_Contents"></a>

 ** index **   <a name="Batch-Type-ArrayPropertiesSummary-index"></a>
The job index within the array that's associated with this job. This parameter is returned for children of array jobs.  
Type: Integer  
Required: No

 ** size **   <a name="Batch-Type-ArrayPropertiesSummary-size"></a>
The size of the array job. This parameter is returned for parent array jobs.  
Type: Integer  
Required: No

 ** statusSummary **   <a name="Batch-Type-ArrayPropertiesSummary-statusSummary"></a>
A summary of the number of array job children in each available job status. This parameter is returned for parent array jobs.  
Type: String to integer map  
Required: No

 ** statusSummaryLastUpdatedAt **   <a name="Batch-Type-ArrayPropertiesSummary-statusSummaryLastUpdatedAt"></a>
The Unix timestamp (in milliseconds) for when the `statusSummary` was last updated.  
Type: Long  
Required: No

## See Also
<a name="API_ArrayPropertiesSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/ArrayPropertiesSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/ArrayPropertiesSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/ArrayPropertiesSummary) 