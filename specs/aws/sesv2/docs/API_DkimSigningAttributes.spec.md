---
id: "@specs/aws/sesv2/docs/API_DkimSigningAttributes"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DkimSigningAttributes"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# DkimSigningAttributes

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_DkimSigningAttributes
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DkimSigningAttributes
<a name="API_DkimSigningAttributes"></a>

An object that contains configuration for Bring Your Own DKIM (BYODKIM), or, for Easy DKIM

## Contents
<a name="API_DkimSigningAttributes_Contents"></a>

 ** DomainSigningAttributesOrigin **   <a name="SES-Type-DkimSigningAttributes-DomainSigningAttributesOrigin"></a>
The attribute to use for configuring DKIM for the identity depends on the operation:   

1. For `PutEmailIdentityDkimSigningAttributes`: 
   + None of the values are allowed - use the [https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_PutEmailIdentityDkimSigningAttributes.html#SES-PutEmailIdentityDkimSigningAttributes-request-SigningAttributesOrigin](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_PutEmailIdentityDkimSigningAttributes.html#SES-PutEmailIdentityDkimSigningAttributes-request-SigningAttributesOrigin) parameter instead 

1. For `CreateEmailIdentity` when replicating a parent identity's DKIM configuration: 
   + Allowed values: All values except `AWS_SES` and `EXTERNAL` 
+  `AWS_SES` – Configure DKIM for the identity by using Easy DKIM. 
+  `EXTERNAL` – Configure DKIM for the identity by using Bring Your Own DKIM (BYODKIM). 
+  `AWS_SES_AF_SOUTH_1` – Configure DKIM for the identity by replicating from a parent identity in Africa (Cape Town) region using Deterministic Easy-DKIM (DEED). 
+  `AWS_SES_EU_NORTH_1` – Configure DKIM for the identity by replicating from a parent identity in Europe (Stockholm) region using Deterministic Easy-DKIM (DEED). 
+  `AWS_SES_AP_SOUTH_1` – Configure DKIM for the identity by replicating from a parent identity in Asia Pacific (Mumbai) region using Deterministic Easy-DKIM (DEED). 
+  `AWS_SES_AP_SOUTH_2` – Configure DKIM for the identity by replicating from a parent identity in Asia Pacific (Hyderabad) region using Deterministic Easy-DKIM (DEED). 
+  `AWS_SES_EU_WEST_3` – Configure DKIM for the identity by replicating from a parent identity in Europe (Paris) region using Deterministic Easy-DKIM (DEED). 
+  `AWS_SES_EU_WEST_2` – Configure DKIM for the identity by replicating from a parent identity in Europe (London) region using Deterministic Easy-DKIM (DEED). 
+  `AWS_SES_EU_SOUTH_1` – Configure DKIM for the identity by replicating from a parent identity in Europe (Milan) region using Deterministic Easy-DKIM (DEED). 
+  `AWS_SES_EU_WEST_1` – Configure DKIM for the identity by replicating from a parent identity in Europe (Ireland) region using Deterministic Easy-DKIM (DEED). 
+  `AWS_SES_AP_NORTHEAST_3` – Configure DKIM for the identity by replicating from a parent identity in Asia Pacific (Osaka) region using Deterministic Easy-DKIM (DEED). 
+  `AWS_SES_AP_NORTHEAST_2` – Configure DKIM for the identity by replicating from a parent identity in Asia Pacific (Seoul) region using Deterministic Easy-DKIM (DEED). 
+  `AWS_SES_ME_CENTRAL_1` – Configure DKIM for the identity by replicating from a parent identity in Middle East (UAE) region using Deterministic Easy-DKIM (DEED). 
+  `AWS_SES_ME_SOUTH_1` – Configure DKIM for the identity by replicating from a parent identity in Middle East (Bahrain) region using Deterministic Easy-DKIM (DEED). 
+  `AWS_SES_AP_NORTHEAST_1` – Configure DKIM for the identity by replicating from a parent identity in Asia Pacific (Tokyo) region using Deterministic Easy-DKIM (DEED). 
+  `AWS_SES_IL_CENTRAL_1` – Configure DKIM for the identity by replicating from a parent identity in Israel (Tel Aviv) region using Deterministic Easy-DKIM (DEED). 
+  `AWS_SES_SA_EAST_1` – Configure DKIM for the identity by replicating from a parent identity in South America (São Paulo) region using Deterministic Easy-DKIM (DEED). 
+  `AWS_SES_CA_CENTRAL_1` – Configure DKIM for the identity by replicating from a parent identity in Canada (Central) region using Deterministic Easy-DKIM (DEED). 
+  `AWS_SES_CA_WEST_1` – Configure DKIM for the identity by replicating from a parent identity in Canada (Calgary) region using Deterministic Easy-DKIM (DEED). 
+  `AWS_SES_AP_SOUTHEAST_1` – Configure DKIM for the identity by replicating from a parent identity in Asia Pacific (Singapore) region using Deterministic Easy-DKIM (DEED). 
+  `AWS_SES_AP_SOUTHEAST_2` – Configure DKIM for the identity by replicating from a parent identity in Asia Pacific (Sydney) region using Deterministic Easy-DKIM (DEED). 
+  `AWS_SES_AP_SOUTHEAST_3` – Configure DKIM for the identity by replicating from a parent identity in Asia Pacific (Jakarta) region using Deterministic Easy-DKIM (DEED). 
+  `AWS_SES_AP_SOUTHEAST_5` – Configure DKIM for the identity by replicating from a parent identity in Asia Pacific (Malaysia) region using Deterministic Easy-DKIM (DEED). 
+  `AWS_SES_EU_CENTRAL_1` – Configure DKIM for the identity by replicating from a parent identity in Europe (Frankfurt) region using Deterministic Easy-DKIM (DEED). 
+  `AWS_SES_EU_CENTRAL_2` – Configure DKIM for the identity by replicating from a parent identity in Europe (Zurich) region using Deterministic Easy-DKIM (DEED). 
+  `AWS_SES_US_EAST_1` – Configure DKIM for the identity by replicating from a parent identity in US East (N. Virginia) region using Deterministic Easy-DKIM (DEED). 
+  `AWS_SES_US_EAST_2` – Configure DKIM for the identity by replicating from a parent identity in US East (Ohio) region using Deterministic Easy-DKIM (DEED). 
+  `AWS_SES_US_WEST_1` – Configure DKIM for the identity by replicating from a parent identity in US West (N. California) region using Deterministic Easy-DKIM (DEED). 
+  `AWS_SES_US_WEST_2` – Configure DKIM for the identity by replicating from a parent identity in US West (Oregon) region using Deterministic Easy-DKIM (DEED). 
Type: String  
Valid Values: `AWS_SES | EXTERNAL | AWS_SES_AF_SOUTH_1 | AWS_SES_EU_NORTH_1 | AWS_SES_AP_SOUTH_1 | AWS_SES_EU_WEST_3 | AWS_SES_EU_WEST_2 | AWS_SES_EU_SOUTH_1 | AWS_SES_EU_WEST_1 | AWS_SES_AP_NORTHEAST_3 | AWS_SES_AP_NORTHEAST_2 | AWS_SES_ME_SOUTH_1 | AWS_SES_AP_NORTHEAST_1 | AWS_SES_IL_CENTRAL_1 | AWS_SES_SA_EAST_1 | AWS_SES_CA_CENTRAL_1 | AWS_SES_AP_SOUTHEAST_1 | AWS_SES_AP_SOUTHEAST_2 | AWS_SES_AP_SOUTHEAST_3 | AWS_SES_EU_CENTRAL_1 | AWS_SES_US_EAST_1 | AWS_SES_US_EAST_2 | AWS_SES_US_WEST_1 | AWS_SES_US_WEST_2 | AWS_SES_ME_CENTRAL_1 | AWS_SES_AP_SOUTH_2 | AWS_SES_EU_CENTRAL_2 | AWS_SES_AP_SOUTHEAST_5 | AWS_SES_CA_WEST_1`   
Required: No

 ** DomainSigningPrivateKey **   <a name="SES-Type-DkimSigningAttributes-DomainSigningPrivateKey"></a>
[Bring Your Own DKIM] A private key that's used to generate a DKIM signature.  
The private key must use 1024 or 2048-bit RSA encryption, and must be encoded using base64 encoding.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 20480.  
Pattern: `^[a-zA-Z0-9+\/]+={0,2}$`   
Required: No

 ** DomainSigningSelector **   <a name="SES-Type-DkimSigningAttributes-DomainSigningSelector"></a>
[Bring Your Own DKIM] A string that's used to identify a public key in the DNS configuration for a domain.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9]))$`   
Required: No

 ** NextSigningKeyLength **   <a name="SES-Type-DkimSigningAttributes-NextSigningKeyLength"></a>
[Easy DKIM] The key length of the future DKIM key pair to be generated. This can be changed at most once per day.  
Type: String  
Valid Values: `RSA_1024_BIT | RSA_2048_BIT`   
Required: No

## See Also
<a name="API_DkimSigningAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/DkimSigningAttributes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/DkimSigningAttributes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/DkimSigningAttributes) 