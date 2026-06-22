---
id: "@specs/aws/codepipeline/docs/API_CurrentRevision"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CurrentRevision"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# CurrentRevision

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_CurrentRevision
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CurrentRevision
<a name="API_CurrentRevision"></a>

Represents information about a current revision.

## Contents
<a name="API_CurrentRevision_Contents"></a>

 ** changeIdentifier **   <a name="CodePipeline-Type-CurrentRevision-changeIdentifier"></a>
The change identifier for the current revision.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Required: Yes

 ** revision **   <a name="CodePipeline-Type-CurrentRevision-revision"></a>
The revision ID of the current version of an artifact.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1500.  
Required: Yes

 ** created **   <a name="CodePipeline-Type-CurrentRevision-created"></a>
The date and time when the most recent revision of the artifact was created, in timestamp format.  
Type: Timestamp  
Required: No

 ** revisionSummary **   <a name="CodePipeline-Type-CurrentRevision-revisionSummary"></a>
The summary of the most recent revision of the artifact.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

## See Also
<a name="API_CurrentRevision_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/CurrentRevision) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/CurrentRevision) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/CurrentRevision) 