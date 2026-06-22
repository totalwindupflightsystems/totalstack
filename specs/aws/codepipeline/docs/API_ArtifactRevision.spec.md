---
id: "@specs/aws/codepipeline/docs/API_ArtifactRevision"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ArtifactRevision"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# ArtifactRevision

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_ArtifactRevision
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ArtifactRevision
<a name="API_ArtifactRevision"></a>

Represents revision details of an artifact. 

## Contents
<a name="API_ArtifactRevision_Contents"></a>

 ** created **   <a name="CodePipeline-Type-ArtifactRevision-created"></a>
The date and time when the most recent revision of the artifact was created, in timestamp format.  
Type: Timestamp  
Required: No

 ** name **   <a name="CodePipeline-Type-ArtifactRevision-name"></a>
The name of an artifact. This name might be system-generated, such as "MyApp", or defined by the user when an action is created.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9_\-]+`   
Required: No

 ** revisionChangeIdentifier **   <a name="CodePipeline-Type-ArtifactRevision-revisionChangeIdentifier"></a>
An additional identifier for a revision, such as a commit date or, for artifacts stored in Amazon S3 buckets, the ETag value.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Required: No

 ** revisionId **   <a name="CodePipeline-Type-ArtifactRevision-revisionId"></a>
The revision ID of the artifact.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1500.  
Required: No

 ** revisionSummary **   <a name="CodePipeline-Type-ArtifactRevision-revisionSummary"></a>
Summary information about the most recent revision of the artifact. For GitHub and CodeCommit repositories, the commit message. For Amazon S3 buckets or actions, the user-provided content of a `codepipeline-artifact-revision-summary` key specified in the object metadata.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

 ** revisionUrl **   <a name="CodePipeline-Type-ArtifactRevision-revisionUrl"></a>
The commit ID for the artifact revision. For artifacts stored in GitHub or CodeCommit repositories, the commit ID is linked to a commit details page.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

## See Also
<a name="API_ArtifactRevision_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/ArtifactRevision) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/ArtifactRevision) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/ArtifactRevision) 