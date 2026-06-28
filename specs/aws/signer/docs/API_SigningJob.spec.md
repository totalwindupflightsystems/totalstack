---
id: "@specs/aws/signer/docs/API_SigningJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SigningJob"
status: active
depends_on:
  - "@specs/aws/signer/meta"
---

# SigningJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/signer/docs/API_SigningJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SigningJob
<a name="API_SigningJob"></a>

Contains information about a signing job.

## Contents
<a name="API_SigningJob_Contents"></a>

 ** createdAt **   <a name="signer-Type-SigningJob-createdAt"></a>
The date and time that the signing job was created.  
Type: Timestamp  
Required: No

 ** isRevoked **   <a name="signer-Type-SigningJob-isRevoked"></a>
Indicates whether the signing job is revoked.  
Type: Boolean  
Required: No

 ** jobId **   <a name="signer-Type-SigningJob-jobId"></a>
The ID of the signing job.  
Type: String  
Required: No

 ** jobInvoker **   <a name="signer-Type-SigningJob-jobInvoker"></a>
The AWS account ID of the job invoker.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: No

 ** jobOwner **   <a name="signer-Type-SigningJob-jobOwner"></a>
The AWS account ID of the job owner.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: No

 ** platformDisplayName **   <a name="signer-Type-SigningJob-platformDisplayName"></a>
The name of a signing platform.  
Type: String  
Required: No

 ** platformId **   <a name="signer-Type-SigningJob-platformId"></a>
The unique identifier for a signing platform.  
Type: String  
Required: No

 ** profileName **   <a name="signer-Type-SigningJob-profileName"></a>
The name of the signing profile that created a signing job.  
Type: String  
Length Constraints: Minimum length of 2. Maximum length of 64.  
Pattern: `^[a-zA-Z0-9_]{2,}`   
Required: No

 ** profileVersion **   <a name="signer-Type-SigningJob-profileVersion"></a>
The version of the signing profile that created a signing job.  
Type: String  
Length Constraints: Fixed length of 10.  
Pattern: `^[a-zA-Z0-9]{10}$`   
Required: No

 ** signatureExpiresAt **   <a name="signer-Type-SigningJob-signatureExpiresAt"></a>
The time when the signature of a signing job expires.  
Type: Timestamp  
Required: No

 ** signedObject **   <a name="signer-Type-SigningJob-signedObject"></a>
A `SignedObject` structure that contains information about a signing job's signed code image.  
Type: [SignedObject](API_SignedObject.md) object  
Required: No

 ** signingMaterial **   <a name="signer-Type-SigningJob-signingMaterial"></a>
A `SigningMaterial` object that contains the Amazon Resource Name (ARN) of the certificate used for the signing job.  
Type: [SigningMaterial](API_SigningMaterial.md) object  
Required: No

 ** source **   <a name="signer-Type-SigningJob-source"></a>
A `Source` that contains information about a signing job's code image source.  
Type: [Source](API_Source.md) object  
Required: No

 ** status **   <a name="signer-Type-SigningJob-status"></a>
The status of the signing job.  
Type: String  
Valid Values: `InProgress | Failed | Succeeded`   
Required: No

## See Also
<a name="API_SigningJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signer-2017-08-25/SigningJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signer-2017-08-25/SigningJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signer-2017-08-25/SigningJob) 