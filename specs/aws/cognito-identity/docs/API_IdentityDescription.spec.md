---
id: "@specs/aws/cognito-identity/docs/API_IdentityDescription"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS IdentityDescription"
status: active
depends_on:
  - "@specs/aws/cognito-identity/meta"
---

# IdentityDescription

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cognito-identity/docs/API_IdentityDescription
> **target_lang:** meta — documentation tier. ALL sections preserved.



# IdentityDescription
<a name="API_IdentityDescription"></a>

A description of the identity.

## Contents
<a name="API_IdentityDescription_Contents"></a>

 ** CreationDate **   <a name="CognitoIdentity-Type-IdentityDescription-CreationDate"></a>
Date on which the identity was created.  
Type: Timestamp  
Required: No

 ** IdentityId **   <a name="CognitoIdentity-Type-IdentityDescription-IdentityId"></a>
A unique identifier in the format REGION:GUID.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 55.  
Pattern: `[\w-]+:[0-9a-f-]+`   
Required: No

 ** LastModifiedDate **   <a name="CognitoIdentity-Type-IdentityDescription-LastModifiedDate"></a>
Date on which the identity was last modified.  
Type: Timestamp  
Required: No

 ** Logins **   <a name="CognitoIdentity-Type-IdentityDescription-Logins"></a>
The provider names.  
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Required: No

## See Also
<a name="API_IdentityDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-identity-2014-06-30/IdentityDescription) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-identity-2014-06-30/IdentityDescription) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-identity-2014-06-30/IdentityDescription) 