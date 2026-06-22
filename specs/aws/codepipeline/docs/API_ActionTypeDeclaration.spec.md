---
id: "@specs/aws/codepipeline/docs/API_ActionTypeDeclaration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ActionTypeDeclaration"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# ActionTypeDeclaration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_ActionTypeDeclaration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ActionTypeDeclaration
<a name="API_ActionTypeDeclaration"></a>

The parameters for the action type definition that are provided when the action type is created or updated.

## Contents
<a name="API_ActionTypeDeclaration_Contents"></a>

 ** executor **   <a name="CodePipeline-Type-ActionTypeDeclaration-executor"></a>
Information about the executor for an action type that was created with any supported integration model.  
Type: [ActionTypeExecutor](API_ActionTypeExecutor.md) object  
Required: Yes

 ** id **   <a name="CodePipeline-Type-ActionTypeDeclaration-id"></a>
The action category, owner, provider, and version of the action type to be updated.  
Type: [ActionTypeIdentifier](API_ActionTypeIdentifier.md) object  
Required: Yes

 ** inputArtifactDetails **   <a name="CodePipeline-Type-ActionTypeDeclaration-inputArtifactDetails"></a>
Details for the artifacts, such as application files, to be worked on by the action. For example, the minimum and maximum number of input artifacts allowed.  
Type: [ActionTypeArtifactDetails](API_ActionTypeArtifactDetails.md) object  
Required: Yes

 ** outputArtifactDetails **   <a name="CodePipeline-Type-ActionTypeDeclaration-outputArtifactDetails"></a>
Details for the output artifacts, such as a built application, that are the result of the action. For example, the minimum and maximum number of output artifacts allowed.  
Type: [ActionTypeArtifactDetails](API_ActionTypeArtifactDetails.md) object  
Required: Yes

 ** description **   <a name="CodePipeline-Type-ActionTypeDeclaration-description"></a>
The description for the action type to be updated.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Required: No

 ** permissions **   <a name="CodePipeline-Type-ActionTypeDeclaration-permissions"></a>
Details identifying the accounts with permissions to use the action type.  
Type: [ActionTypePermissions](API_ActionTypePermissions.md) object  
Required: No

 ** properties **   <a name="CodePipeline-Type-ActionTypeDeclaration-properties"></a>
The properties of the action type to be updated.  
Type: Array of [ActionTypeProperty](API_ActionTypeProperty.md) objects  
Array Members: Maximum number of 10 items.  
Required: No

 ** urls **   <a name="CodePipeline-Type-ActionTypeDeclaration-urls"></a>
The links associated with the action type to be updated.  
Type: [ActionTypeUrls](API_ActionTypeUrls.md) object  
Required: No

## See Also
<a name="API_ActionTypeDeclaration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/ActionTypeDeclaration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/ActionTypeDeclaration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/ActionTypeDeclaration) 