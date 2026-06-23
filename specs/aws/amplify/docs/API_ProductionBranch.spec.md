---
id: "@specs/aws/amplify/docs/API_ProductionBranch"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ProductionBranch"
status: active
depends_on:
  - "@specs/aws/amplify/meta"
---

# ProductionBranch

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amplify/docs/API_ProductionBranch
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ProductionBranch
<a name="API_ProductionBranch"></a>

Describes the information about a production branch for an Amplify app. 

## Contents
<a name="API_ProductionBranch_Contents"></a>

 ** branchName **   <a name="amplify-Type-ProductionBranch-branchName"></a>
The branch name for the production branch.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `(?s).+`   
Required: No

 ** lastDeployTime **   <a name="amplify-Type-ProductionBranch-lastDeployTime"></a>
The last deploy time of the production branch.   
Type: Timestamp  
Required: No

 ** status **   <a name="amplify-Type-ProductionBranch-status"></a>
The status of the production branch.   
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 7.  
Pattern: `.{3,7}`   
Required: No

 ** thumbnailUrl **   <a name="amplify-Type-ProductionBranch-thumbnailUrl"></a>
The thumbnail URL for the production branch.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.  
Required: No

## See Also
<a name="API_ProductionBranch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplify-2017-07-25/ProductionBranch) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplify-2017-07-25/ProductionBranch) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplify-2017-07-25/ProductionBranch) 