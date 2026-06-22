---
id: "@specs/aws/codepipeline/docs/API_ThirdPartyJobDetails"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ThirdPartyJobDetails"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# ThirdPartyJobDetails

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_ThirdPartyJobDetails
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ThirdPartyJobDetails
<a name="API_ThirdPartyJobDetails"></a>

The details of a job sent in response to a `GetThirdPartyJobDetails` request.

## Contents
<a name="API_ThirdPartyJobDetails_Contents"></a>

 ** data **   <a name="CodePipeline-Type-ThirdPartyJobDetails-data"></a>
The data to be returned by the third party job worker.  
Type: [ThirdPartyJobData](API_ThirdPartyJobData.md) object  
Required: No

 ** id **   <a name="CodePipeline-Type-ThirdPartyJobDetails-id"></a>
The identifier used to identify the job details in CodePipeline.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Required: No

 ** nonce **   <a name="CodePipeline-Type-ThirdPartyJobDetails-nonce"></a>
A system-generated random number that CodePipeline uses to ensure that the job is being worked on by only one job worker. Use this number in an [AcknowledgeThirdPartyJob](API_AcknowledgeThirdPartyJob.md) request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 50.  
Required: No

## See Also
<a name="API_ThirdPartyJobDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/ThirdPartyJobDetails) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/ThirdPartyJobDetails) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/ThirdPartyJobDetails) 