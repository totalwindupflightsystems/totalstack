---
id: "@specs/aws/signer/docs/API_SigningProfile"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SigningProfile"
status: active
depends_on:
  - "@specs/aws/signer/meta"
---

# SigningProfile

> **source:** AWS Documentation
> **spec:id:** @specs/aws/signer/docs/API_SigningProfile
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SigningProfile
<a name="API_SigningProfile"></a>

Contains information about the ACM certificates and signing configuration parameters that can be used by a given code signing user.

## Contents
<a name="API_SigningProfile_Contents"></a>

 ** arn **   <a name="signer-Type-SigningProfile-arn"></a>
The Amazon Resource Name (ARN) for the signing profile.  
Type: String  
Required: No

 ** platformDisplayName **   <a name="signer-Type-SigningProfile-platformDisplayName"></a>
The name of the signing platform.  
Type: String  
Required: No

 ** platformId **   <a name="signer-Type-SigningProfile-platformId"></a>
The ID of a platform that is available for use by a signing profile.  
Type: String  
Required: No

 ** profileName **   <a name="signer-Type-SigningProfile-profileName"></a>
The name of the signing profile.  
Type: String  
Length Constraints: Minimum length of 2. Maximum length of 64.  
Pattern: `^[a-zA-Z0-9_]{2,}`   
Required: No

 ** profileVersion **   <a name="signer-Type-SigningProfile-profileVersion"></a>
The version of a signing profile.  
Type: String  
Length Constraints: Fixed length of 10.  
Pattern: `^[a-zA-Z0-9]{10}$`   
Required: No

 ** profileVersionArn **   <a name="signer-Type-SigningProfile-profileVersionArn"></a>
The ARN of a signing profile, including the profile version.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Required: No

 ** signatureValidityPeriod **   <a name="signer-Type-SigningProfile-signatureValidityPeriod"></a>
The validity period for a signing job created using this signing profile.  
Type: [SignatureValidityPeriod](API_SignatureValidityPeriod.md) object  
Required: No

 ** signingMaterial **   <a name="signer-Type-SigningProfile-signingMaterial"></a>
The ACM certificate that is available for use by a signing profile.  
Type: [SigningMaterial](API_SigningMaterial.md) object  
Required: No

 ** signingParameters **   <a name="signer-Type-SigningProfile-signingParameters"></a>
The parameters that are available for use by a Signer user.  
Type: String to string map  
Required: No

 ** status **   <a name="signer-Type-SigningProfile-status"></a>
The status of a signing profile.  
Type: String  
Valid Values: `Active | Canceled | Revoked`   
Required: No

 ** tags **   <a name="signer-Type-SigningProfile-tags"></a>
A list of tags associated with the signing profile.  
Type: String to string map  
Map Entries: Maximum number of 200 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`   
Value Length Constraints: Maximum length of 256.  
Required: No

## See Also
<a name="API_SigningProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signer-2017-08-25/SigningProfile) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signer-2017-08-25/SigningProfile) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signer-2017-08-25/SigningProfile) 