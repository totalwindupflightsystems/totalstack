---
id: "@specs/aws/codepipeline/docs/API_ThirdPartyJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ThirdPartyJob"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# ThirdPartyJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_ThirdPartyJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ThirdPartyJob
<a name="API_ThirdPartyJob"></a>

A response to a `PollForThirdPartyJobs` request returned by CodePipeline when there is a job to be worked on by a partner action.

## Contents
<a name="API_ThirdPartyJob_Contents"></a>

 ** clientId **   <a name="CodePipeline-Type-ThirdPartyJob-clientId"></a>
The `clientToken` portion of the `clientId` and `clientToken` pair used to verify that the calling entity is allowed access to the job and its details.  
Type: String  
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`   
Required: No

 ** jobId **   <a name="CodePipeline-Type-ThirdPartyJob-jobId"></a>
The identifier used to identify the job in CodePipeline.  
Type: String  
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`   
Required: No

## See Also
<a name="API_ThirdPartyJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/ThirdPartyJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/ThirdPartyJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/ThirdPartyJob) 