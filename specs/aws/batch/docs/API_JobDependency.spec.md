---
id: "@specs/aws/batch/docs/API_JobDependency"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS JobDependency"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# JobDependency

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_JobDependency
> **target_lang:** meta — documentation tier. ALL sections preserved.



# JobDependency
<a name="API_JobDependency"></a>

An object that represents an AWS Batch job dependency.

## Contents
<a name="API_JobDependency_Contents"></a>

 ** jobId **   <a name="Batch-Type-JobDependency-jobId"></a>
The job ID of the AWS Batch job that's associated with this dependency.  
Type: String  
Required: No

 ** type **   <a name="Batch-Type-JobDependency-type"></a>
The type of the job dependency.  
Type: String  
Valid Values: `N_TO_N | SEQUENTIAL`   
Required: No

## See Also
<a name="API_JobDependency_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/JobDependency) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/JobDependency) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/JobDependency) 