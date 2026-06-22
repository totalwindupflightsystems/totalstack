---
id: "@specs/aws/codepipeline/docs/API_Job"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Job"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# Job

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_Job
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Job
<a name="API_Job"></a>

Represents information about a job.

## Contents
<a name="API_Job_Contents"></a>

 ** accountId **   <a name="CodePipeline-Type-Job-accountId"></a>
The ID of the AWS account to use when performing the job.  
Type: String  
Pattern: `[0-9]{12}`   
Required: No

 ** data **   <a name="CodePipeline-Type-Job-data"></a>
Other data about a job.  
Type: [JobData](API_JobData.md) object  
Required: No

 ** id **   <a name="CodePipeline-Type-Job-id"></a>
The unique system-generated ID of the job.  
Type: String  
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`   
Required: No

 ** nonce **   <a name="CodePipeline-Type-Job-nonce"></a>
A system-generated random number that CodePipeline uses to ensure that the job is being worked on by only one job worker. Use this number in an [AcknowledgeJob](API_AcknowledgeJob.md) request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 50.  
Required: No

## See Also
<a name="API_Job_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/Job) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/Job) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/Job) 