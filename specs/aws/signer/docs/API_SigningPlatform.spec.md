---
id: "@specs/aws/signer/docs/API_SigningPlatform"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SigningPlatform"
status: active
depends_on:
  - "@specs/aws/signer/meta"
---

# SigningPlatform

> **source:** AWS Documentation
> **spec:id:** @specs/aws/signer/docs/API_SigningPlatform
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SigningPlatform
<a name="API_SigningPlatform"></a>

Contains information about the signing configurations and parameters that are used to perform a code-signing job.

## Contents
<a name="API_SigningPlatform_Contents"></a>

 ** category **   <a name="signer-Type-SigningPlatform-category"></a>
The category of a signing platform.  
Type: String  
Valid Values: `AWSIoT`   
Required: No

 ** displayName **   <a name="signer-Type-SigningPlatform-displayName"></a>
The display name of a signing platform.  
Type: String  
Required: No

 ** maxSizeInMB **   <a name="signer-Type-SigningPlatform-maxSizeInMB"></a>
The maximum size (in MB) of code that can be signed by a signing platform.  
Type: Integer  
Required: No

 ** partner **   <a name="signer-Type-SigningPlatform-partner"></a>
Any partner entities linked to a signing platform.  
Type: String  
Required: No

 ** platformId **   <a name="signer-Type-SigningPlatform-platformId"></a>
The ID of a signing platform.  
Type: String  
Required: No

 ** revocationSupported **   <a name="signer-Type-SigningPlatform-revocationSupported"></a>
Indicates whether revocation is supported for the platform.  
Type: Boolean  
Required: No

 ** signingConfiguration **   <a name="signer-Type-SigningPlatform-signingConfiguration"></a>
The configuration of a signing platform. This includes the designated hash algorithm and encryption algorithm of a signing platform.  
Type: [SigningConfiguration](API_SigningConfiguration.md) object  
Required: No

 ** signingImageFormat **   <a name="signer-Type-SigningPlatform-signingImageFormat"></a>
The image format of a AWS Signer platform or profile.  
Type: [SigningImageFormat](API_SigningImageFormat.md) object  
Required: No

 ** target **   <a name="signer-Type-SigningPlatform-target"></a>
The types of targets that can be signed by a signing platform.  
Type: String  
Required: No

## See Also
<a name="API_SigningPlatform_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signer-2017-08-25/SigningPlatform) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signer-2017-08-25/SigningPlatform) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signer-2017-08-25/SigningPlatform) 