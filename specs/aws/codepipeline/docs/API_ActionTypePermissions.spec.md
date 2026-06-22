---
id: "@specs/aws/codepipeline/docs/API_ActionTypePermissions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ActionTypePermissions"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# ActionTypePermissions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_ActionTypePermissions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ActionTypePermissions
<a name="API_ActionTypePermissions"></a>

Details identifying the users with permissions to use the action type.

## Contents
<a name="API_ActionTypePermissions_Contents"></a>

 ** allowedAccounts **   <a name="CodePipeline-Type-ActionTypePermissions-allowedAccounts"></a>
A list of AWS account IDs with access to use the action type in their pipelines.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 1000 items.  
Pattern: `[0-9]{12}|\*`   
Required: Yes

## See Also
<a name="API_ActionTypePermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/ActionTypePermissions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/ActionTypePermissions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/ActionTypePermissions) 