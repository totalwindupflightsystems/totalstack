---
id: "@specs/aws/signer/docs/API_SigningProfileRevocationRecord"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SigningProfileRevocationRecord"
status: active
depends_on:
  - "@specs/aws/signer/meta"
---

# SigningProfileRevocationRecord

> **source:** AWS Documentation
> **spec:id:** @specs/aws/signer/docs/API_SigningProfileRevocationRecord
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SigningProfileRevocationRecord
<a name="API_SigningProfileRevocationRecord"></a>

Revocation information for a signing profile.

## Contents
<a name="API_SigningProfileRevocationRecord_Contents"></a>

 ** revocationEffectiveFrom **   <a name="signer-Type-SigningProfileRevocationRecord-revocationEffectiveFrom"></a>
The time when revocation becomes effective.  
Type: Timestamp  
Required: No

 ** revokedAt **   <a name="signer-Type-SigningProfileRevocationRecord-revokedAt"></a>
The time when the signing profile was revoked.  
Type: Timestamp  
Required: No

 ** revokedBy **   <a name="signer-Type-SigningProfileRevocationRecord-revokedBy"></a>
The identity of the revoker.  
Type: String  
Required: No

## See Also
<a name="API_SigningProfileRevocationRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signer-2017-08-25/SigningProfileRevocationRecord) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signer-2017-08-25/SigningProfileRevocationRecord) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signer-2017-08-25/SigningProfileRevocationRecord) 