---
id: "@specs/aws/codepipeline/docs/API_ActionTypeUrls"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ActionTypeUrls"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# ActionTypeUrls

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_ActionTypeUrls
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ActionTypeUrls
<a name="API_ActionTypeUrls"></a>

Returns information about URLs for web pages that display to customers as links on the pipeline view, such as an external configuration page for the action type.

## Contents
<a name="API_ActionTypeUrls_Contents"></a>

 ** configurationUrl **   <a name="CodePipeline-Type-ActionTypeUrls-configurationUrl"></a>
The URL returned to the CodePipeline console that contains a link to the page where customers can configure the external action.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

 ** entityUrlTemplate **   <a name="CodePipeline-Type-ActionTypeUrls-entityUrlTemplate"></a>
The URL returned to the CodePipeline console that provides a deep link to the resources of the external system, such as a status page. This link is provided as part of the action display in the pipeline.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

 ** executionUrlTemplate **   <a name="CodePipeline-Type-ActionTypeUrls-executionUrlTemplate"></a>
The link to an execution page for the action type in progress. For example, for a CodeDeploy action, this link is shown on the pipeline view page in the CodePipeline console, and it links to a CodeDeploy status page.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

 ** revisionUrlTemplate **   <a name="CodePipeline-Type-ActionTypeUrls-revisionUrlTemplate"></a>
The URL returned to the CodePipeline console that contains a link to the page where customers can update or change the configuration of the external action.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

## See Also
<a name="API_ActionTypeUrls_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/ActionTypeUrls) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/ActionTypeUrls) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/ActionTypeUrls) 