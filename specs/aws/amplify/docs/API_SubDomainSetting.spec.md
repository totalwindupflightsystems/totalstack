---
id: "@specs/aws/amplify/docs/API_SubDomainSetting"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SubDomainSetting"
status: active
depends_on:
  - "@specs/aws/amplify/meta"
---

# SubDomainSetting

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amplify/docs/API_SubDomainSetting
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SubDomainSetting
<a name="API_SubDomainSetting"></a>

 Describes the settings for the subdomain. 

## Contents
<a name="API_SubDomainSetting_Contents"></a>

 ** branchName **   <a name="amplify-Type-SubDomainSetting-branchName"></a>
 The branch name setting for the subdomain.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `(?s).+`   
Required: Yes

 ** prefix **   <a name="amplify-Type-SubDomainSetting-prefix"></a>
 The prefix setting for the subdomain.   
Type: String  
Length Constraints: Maximum length of 255.  
Pattern: `(?s).*`   
Required: Yes

## See Also
<a name="API_SubDomainSetting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplify-2017-07-25/SubDomainSetting) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplify-2017-07-25/SubDomainSetting) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplify-2017-07-25/SubDomainSetting) 