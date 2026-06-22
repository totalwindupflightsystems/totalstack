---
id: "@specs/aws/codepipeline/docs/API_SourceRevisionOverride"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SourceRevisionOverride"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# SourceRevisionOverride

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_SourceRevisionOverride
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SourceRevisionOverride
<a name="API_SourceRevisionOverride"></a>

A list that allows you to specify, or override, the source revision for a pipeline execution that's being started. A source revision is the version with all the changes to your application code, or source artifact, for the pipeline execution.

**Note**  
For the `S3_OBJECT_VERSION_ID` and `S3_OBJECT_KEY` types of source revisions, either of the types can be used independently, or they can be used together to override the source with a specific ObjectKey and VersionID.

## Contents
<a name="API_SourceRevisionOverride_Contents"></a>

 ** actionName **   <a name="CodePipeline-Type-SourceRevisionOverride-actionName"></a>
The name of the action where the override will be applied.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9.@\-_]+`   
Required: Yes

 ** revisionType **   <a name="CodePipeline-Type-SourceRevisionOverride-revisionType"></a>
The type of source revision, based on the source provider. For example, the revision type for the CodeCommit action provider is the commit ID.  
Type: String  
Valid Values: `COMMIT_ID | IMAGE_DIGEST | S3_OBJECT_VERSION_ID | S3_OBJECT_KEY`   
Required: Yes

 ** revisionValue **   <a name="CodePipeline-Type-SourceRevisionOverride-revisionValue"></a>
The source revision, or version of your source artifact, with the changes that you want to run in the pipeline execution.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1500.  
Required: Yes

## See Also
<a name="API_SourceRevisionOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/SourceRevisionOverride) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/SourceRevisionOverride) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/SourceRevisionOverride) 