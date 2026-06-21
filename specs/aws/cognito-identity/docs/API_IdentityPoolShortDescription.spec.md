---
id: "@specs/aws/cognito-identity/docs/API_IdentityPoolShortDescription"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS IdentityPoolShortDescription"
status: active
depends_on:
  - "@specs/aws/cognito-identity/meta"
---

# IdentityPoolShortDescription

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cognito-identity/docs/API_IdentityPoolShortDescription
> **target_lang:** meta — documentation tier. ALL sections preserved.



# IdentityPoolShortDescription
<a name="API_IdentityPoolShortDescription"></a>

A description of the identity pool.

## Contents
<a name="API_IdentityPoolShortDescription_Contents"></a>

 ** IdentityPoolId **   <a name="CognitoIdentity-Type-IdentityPoolShortDescription-IdentityPoolId"></a>
An identity pool ID in the format REGION:GUID.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 55.  
Pattern: `[\w-]+:[0-9a-f-]+`   
Required: No

 ** IdentityPoolName **   <a name="CognitoIdentity-Type-IdentityPoolShortDescription-IdentityPoolName"></a>
A string that you provide.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[\w\s+=,.@-]+`   
Required: No

## See Also
<a name="API_IdentityPoolShortDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-identity-2014-06-30/IdentityPoolShortDescription) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-identity-2014-06-30/IdentityPoolShortDescription) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-identity-2014-06-30/IdentityPoolShortDescription) 