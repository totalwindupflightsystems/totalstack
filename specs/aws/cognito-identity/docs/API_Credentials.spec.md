---
id: "@specs/aws/cognito-identity/docs/API_Credentials"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Credentials"
status: active
depends_on:
  - "@specs/aws/cognito-identity/meta"
---

# Credentials

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cognito-identity/docs/API_Credentials
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Credentials
<a name="API_Credentials"></a>

Credentials for the provided identity ID.

## Contents
<a name="API_Credentials_Contents"></a>

 ** AccessKeyId **   <a name="CognitoIdentity-Type-Credentials-AccessKeyId"></a>
The Access Key portion of the credentials.  
Type: String  
Required: No

 ** Expiration **   <a name="CognitoIdentity-Type-Credentials-Expiration"></a>
The date at which these credentials will expire.  
Type: Timestamp  
Required: No

 ** SecretKey **   <a name="CognitoIdentity-Type-Credentials-SecretKey"></a>
The Secret Access Key portion of the credentials  
Type: String  
Required: No

 ** SessionToken **   <a name="CognitoIdentity-Type-Credentials-SessionToken"></a>
The Session Token portion of the credentials  
Type: String  
Required: No

## See Also
<a name="API_Credentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-identity-2014-06-30/Credentials) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-identity-2014-06-30/Credentials) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-identity-2014-06-30/Credentials) 