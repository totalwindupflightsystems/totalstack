---
id: "@specs/aws/codepipeline/docs/API_RuleRevision"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RuleRevision"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# RuleRevision

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_RuleRevision
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RuleRevision
<a name="API_RuleRevision"></a>

The change to a rule that creates a revision of the rule.

## Contents
<a name="API_RuleRevision_Contents"></a>

 ** created **   <a name="CodePipeline-Type-RuleRevision-created"></a>
The date and time when the most recent version of the rule was created, in timestamp format.  
Type: Timestamp  
Required: Yes

 ** revisionChangeId **   <a name="CodePipeline-Type-RuleRevision-revisionChangeId"></a>
The unique identifier of the change that set the state to this revision (for example, a deployment ID or timestamp).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Required: Yes

 ** revisionId **   <a name="CodePipeline-Type-RuleRevision-revisionId"></a>
The system-generated unique ID that identifies the revision number of the rule.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1500.  
Required: Yes

## See Also
<a name="API_RuleRevision_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/RuleRevision) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/RuleRevision) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/RuleRevision) 