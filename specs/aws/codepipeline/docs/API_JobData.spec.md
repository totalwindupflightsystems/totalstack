---
id: "@specs/aws/codepipeline/docs/API_JobData"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS JobData"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# JobData

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_JobData
> **target_lang:** meta — documentation tier. ALL sections preserved.



# JobData
<a name="API_JobData"></a>

Represents other information about a job required for a job worker to complete the job.

## Contents
<a name="API_JobData_Contents"></a>

 ** actionConfiguration **   <a name="CodePipeline-Type-JobData-actionConfiguration"></a>
Represents information about an action configuration.  
Type: [ActionConfiguration](API_ActionConfiguration.md) object  
Required: No

 ** actionTypeId **   <a name="CodePipeline-Type-JobData-actionTypeId"></a>
Represents information about an action type.  
Type: [ActionTypeId](API_ActionTypeId.md) object  
Required: No

 ** artifactCredentials **   <a name="CodePipeline-Type-JobData-artifactCredentials"></a>
Represents an AWS session credentials object. These credentials are temporary credentials that are issued by AWS Secure Token Service (STS). They can be used to access input and output artifacts in the S3 bucket used to store artifacts for the pipeline in CodePipeline.  
Type: [AWSSessionCredentials](API_AWSSessionCredentials.md) object  
Required: No

 ** continuationToken **   <a name="CodePipeline-Type-JobData-continuationToken"></a>
A system-generated token, such as a deployment ID, required by a job to continue the job asynchronously.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

 ** encryptionKey **   <a name="CodePipeline-Type-JobData-encryptionKey"></a>
Represents information about the key used to encrypt data in the artifact store, such as an AWS KMS key.   
Type: [EncryptionKey](API_EncryptionKey.md) object  
Required: No

 ** inputArtifacts **   <a name="CodePipeline-Type-JobData-inputArtifacts"></a>
The artifact supplied to the job.  
Type: Array of [Artifact](API_Artifact.md) objects  
Required: No

 ** outputArtifacts **   <a name="CodePipeline-Type-JobData-outputArtifacts"></a>
The output of the job.  
Type: Array of [Artifact](API_Artifact.md) objects  
Required: No

 ** pipelineContext **   <a name="CodePipeline-Type-JobData-pipelineContext"></a>
Represents information about a pipeline to a job worker.  
Includes `pipelineArn` and `pipelineExecutionId` for custom jobs.
Type: [PipelineContext](API_PipelineContext.md) object  
Required: No

## See Also
<a name="API_JobData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/JobData) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/JobData) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/JobData) 