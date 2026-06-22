---
id: "@specs/aws/codepipeline/docs/API_JobDetails"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS JobDetails"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# JobDetails

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_JobDetails
> **target_lang:** meta — documentation tier. ALL sections preserved.



# JobDetails
<a name="API_JobDetails"></a>

Represents information about the details of a job.

## Contents
<a name="API_JobDetails_Contents"></a>

 ** accountId **   <a name="CodePipeline-Type-JobDetails-accountId"></a>
The AWS account ID associated with the job.  
Type: String  
Pattern: `[0-9]{12}`   
Required: No

 ** data **   <a name="CodePipeline-Type-JobDetails-data"></a>
Represents other information about a job required for a job worker to complete the job.   
Type: [JobData](API_JobData.md) object  
Required: No

 ** id **   <a name="CodePipeline-Type-JobDetails-id"></a>
The unique system-generated ID of the job.  
Type: String  
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`   
Required: No

## See Also
<a name="API_JobDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/JobDetails) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/JobDetails) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/JobDetails) 