---
id: "@specs/aws/codepipeline/docs/API_ApprovalResult"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ApprovalResult"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# ApprovalResult

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_ApprovalResult
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ApprovalResult
<a name="API_ApprovalResult"></a>

Represents information about the result of an approval request.

## Contents
<a name="API_ApprovalResult_Contents"></a>

 ** status **   <a name="CodePipeline-Type-ApprovalResult-status"></a>
The response submitted by a reviewer assigned to an approval action request.  
Type: String  
Valid Values: `Approved | Rejected`   
Required: Yes

 ** summary **   <a name="CodePipeline-Type-ApprovalResult-summary"></a>
The summary of the current status of the approval request.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 512.  
Required: Yes

## See Also
<a name="API_ApprovalResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/ApprovalResult) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/ApprovalResult) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/ApprovalResult) 