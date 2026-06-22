---
id: "@specs/aws/codepipeline/docs/API_ActionTypeIdentifier"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ActionTypeIdentifier"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# ActionTypeIdentifier

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_ActionTypeIdentifier
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ActionTypeIdentifier
<a name="API_ActionTypeIdentifier"></a>

Specifies the category, owner, provider, and version of the action type.

## Contents
<a name="API_ActionTypeIdentifier_Contents"></a>

 ** category **   <a name="CodePipeline-Type-ActionTypeIdentifier-category"></a>
Defines what kind of action can be taken in the stage, one of the following:  
+  `Source` 
+  `Build` 
+  `Test` 
+  `Deploy` 
+  `Approval` 
+  `Invoke` 
Type: String  
Valid Values: `Source | Build | Deploy | Test | Invoke | Approval | Compute`   
Required: Yes

 ** owner **   <a name="CodePipeline-Type-ActionTypeIdentifier-owner"></a>
The creator of the action type being called: `AWS` or `ThirdParty`.  
Type: String  
Pattern: `AWS|ThirdParty`   
Required: Yes

 ** provider **   <a name="CodePipeline-Type-ActionTypeIdentifier-provider"></a>
The provider of the action type being called. The provider name is supplied when the action type is created.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 35.  
Pattern: `[0-9A-Za-z_-]+`   
Required: Yes

 ** version **   <a name="CodePipeline-Type-ActionTypeIdentifier-version"></a>
A string that describes the action type version.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 9.  
Pattern: `[0-9A-Za-z_-]+`   
Required: Yes

## See Also
<a name="API_ActionTypeIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/ActionTypeIdentifier) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/ActionTypeIdentifier) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/ActionTypeIdentifier) 