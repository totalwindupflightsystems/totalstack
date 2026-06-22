---
id: "@specs/aws/sesv2/docs/API_IdentityInfo"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS IdentityInfo"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# IdentityInfo

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_IdentityInfo
> **target_lang:** meta — documentation tier. ALL sections preserved.



# IdentityInfo
<a name="API_IdentityInfo"></a>

Information about an email identity.

## Contents
<a name="API_IdentityInfo_Contents"></a>

 ** IdentityName **   <a name="SES-Type-IdentityInfo-IdentityName"></a>
The address or domain of the identity.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

 ** IdentityType **   <a name="SES-Type-IdentityInfo-IdentityType"></a>
The email identity type. Note: the `MANAGED_DOMAIN` type is not supported for email identity types.  
Type: String  
Valid Values: `EMAIL_ADDRESS | DOMAIN | MANAGED_DOMAIN`   
Required: No

 ** SendingEnabled **   <a name="SES-Type-IdentityInfo-SendingEnabled"></a>
Indicates whether or not you can send email from the identity.  
An *identity* is an email address or domain that you send email from. Before you can send email from an identity, you have to demostrate that you own the identity, and that you authorize Amazon SES to send email from that identity.  
Type: Boolean  
Required: No

 ** VerificationStatus **   <a name="SES-Type-IdentityInfo-VerificationStatus"></a>
The verification status of the identity. The status can be one of the following:  
+  `PENDING` – The verification process was initiated, but Amazon SES hasn't yet been able to verify the identity.
+  `SUCCESS` – The verification process completed successfully.
+  `FAILED` – The verification process failed.
+  `TEMPORARY_FAILURE` – A temporary issue is preventing Amazon SES from determining the verification status of the identity.
+  `NOT_STARTED` – The verification process hasn't been initiated for the identity.
Type: String  
Valid Values: `PENDING | SUCCESS | FAILED | TEMPORARY_FAILURE | NOT_STARTED`   
Required: No

## See Also
<a name="API_IdentityInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/IdentityInfo) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/IdentityInfo) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/IdentityInfo) 