---
id: "@specs/aws/signer/docs/API_SigningJobRevocationRecord"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SigningJobRevocationRecord"
status: active
depends_on:
  - "@specs/aws/signer/meta"
---

# SigningJobRevocationRecord

> **source:** AWS Documentation
> **spec:id:** @specs/aws/signer/docs/API_SigningJobRevocationRecord
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SigningJobRevocationRecord
<a name="API_SigningJobRevocationRecord"></a>

Revocation information for a signing job.

## Contents
<a name="API_SigningJobRevocationRecord_Contents"></a>

 ** reason **   <a name="signer-Type-SigningJobRevocationRecord-reason"></a>
A caller-supplied reason for revocation.  
Type: String  
Required: No

 ** revokedAt **   <a name="signer-Type-SigningJobRevocationRecord-revokedAt"></a>
The time of revocation.  
Type: Timestamp  
Required: No

 ** revokedBy **   <a name="signer-Type-SigningJobRevocationRecord-revokedBy"></a>
The identity of the revoker.  
Type: String  
Required: No

## See Also
<a name="API_SigningJobRevocationRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signer-2017-08-25/SigningJobRevocationRecord) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signer-2017-08-25/SigningJobRevocationRecord) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signer-2017-08-25/SigningJobRevocationRecord) 