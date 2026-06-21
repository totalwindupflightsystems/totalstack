---
id: "@specs/aws/cloudtrail/docs/API_PublicKey"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PublicKey"
status: active
depends_on:
  - "@specs/aws/cloudtrail/meta"
---

# PublicKey

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudtrail/docs/API_PublicKey
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PublicKey
<a name="API_PublicKey"></a>

Contains information about a returned public key.

## Contents
<a name="API_PublicKey_Contents"></a>

 ** Fingerprint **   <a name="awscloudtrail-Type-PublicKey-Fingerprint"></a>
The fingerprint of the public key.  
Type: String  
Required: No

 ** ValidityEndTime **   <a name="awscloudtrail-Type-PublicKey-ValidityEndTime"></a>
The ending time of validity of the public key.  
Type: Timestamp  
Required: No

 ** ValidityStartTime **   <a name="awscloudtrail-Type-PublicKey-ValidityStartTime"></a>
The starting time of validity of the public key.  
Type: Timestamp  
Required: No

 ** Value **   <a name="awscloudtrail-Type-PublicKey-Value"></a>
The DER encoded public key value in PKCS\#1 format.  
Type: Base64-encoded binary data object  
Required: No

## See Also
<a name="API_PublicKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/PublicKey) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/PublicKey) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/PublicKey) 