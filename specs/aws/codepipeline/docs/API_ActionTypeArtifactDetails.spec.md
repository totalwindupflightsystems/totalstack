---
id: "@specs/aws/codepipeline/docs/API_ActionTypeArtifactDetails"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ActionTypeArtifactDetails"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# ActionTypeArtifactDetails

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_ActionTypeArtifactDetails
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ActionTypeArtifactDetails
<a name="API_ActionTypeArtifactDetails"></a>

Information about parameters for artifacts associated with the action type, such as the minimum and maximum artifacts allowed.

## Contents
<a name="API_ActionTypeArtifactDetails_Contents"></a>

 ** maximumCount **   <a name="CodePipeline-Type-ActionTypeArtifactDetails-maximumCount"></a>
The maximum number of artifacts that can be used with the actiontype. For example, you should specify a minimum and maximum of zero input artifacts for an action type with a category of `source`.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 10.  
Required: Yes

 ** minimumCount **   <a name="CodePipeline-Type-ActionTypeArtifactDetails-minimumCount"></a>
The minimum number of artifacts that can be used with the action type. For example, you should specify a minimum and maximum of zero input artifacts for an action type with a category of `source`.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 10.  
Required: Yes

## See Also
<a name="API_ActionTypeArtifactDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/ActionTypeArtifactDetails) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/ActionTypeArtifactDetails) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/ActionTypeArtifactDetails) 