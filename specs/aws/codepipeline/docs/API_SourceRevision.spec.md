---
id: "@specs/aws/codepipeline/docs/API_SourceRevision"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SourceRevision"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# SourceRevision

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_SourceRevision
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SourceRevision
<a name="API_SourceRevision"></a>

Information about the version (or revision) of a source artifact that initiated a pipeline execution.

## Contents
<a name="API_SourceRevision_Contents"></a>

 ** actionName **   <a name="CodePipeline-Type-SourceRevision-actionName"></a>
The name of the action that processed the revision to the source artifact.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9.@\-_]+`   
Required: Yes

 ** revisionId **   <a name="CodePipeline-Type-SourceRevision-revisionId"></a>
The system-generated unique ID that identifies the revision number of the artifact.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1500.  
Required: No

 ** revisionSummary **   <a name="CodePipeline-Type-SourceRevision-revisionSummary"></a>
Summary information about the most recent revision of the artifact. For GitHub and CodeCommit repositories, the commit message. For Amazon S3 buckets or actions, the user-provided content of a `codepipeline-artifact-revision-summary` key specified in the object metadata.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

 ** revisionUrl **   <a name="CodePipeline-Type-SourceRevision-revisionUrl"></a>
The commit ID for the artifact revision. For artifacts stored in GitHub or CodeCommit repositories, the commit ID is linked to a commit details page.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

## See Also
<a name="API_SourceRevision_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/SourceRevision) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/SourceRevision) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/SourceRevision) 