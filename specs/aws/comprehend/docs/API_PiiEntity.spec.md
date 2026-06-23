---
id: "@specs/aws/comprehend/docs/API_PiiEntity"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PiiEntity"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# PiiEntity

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_PiiEntity
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PiiEntity
<a name="API_PiiEntity"></a>

Provides information about a PII entity.

## Contents
<a name="API_PiiEntity_Contents"></a>

 ** BeginOffset **   <a name="comprehend-Type-PiiEntity-BeginOffset"></a>
The zero-based offset from the beginning of the source text to the first character in the entity.  
Type: Integer  
Required: No

 ** EndOffset **   <a name="comprehend-Type-PiiEntity-EndOffset"></a>
The zero-based offset from the beginning of the source text to the last character in the entity.  
Type: Integer  
Required: No

 ** Score **   <a name="comprehend-Type-PiiEntity-Score"></a>
The level of confidence that Amazon Comprehend has in the accuracy of the detection.  
Type: Float  
Required: No

 ** Type **   <a name="comprehend-Type-PiiEntity-Type"></a>
The entity's type.  
Type: String  
Valid Values: `BANK_ACCOUNT_NUMBER | BANK_ROUTING | CREDIT_DEBIT_NUMBER | CREDIT_DEBIT_CVV | CREDIT_DEBIT_EXPIRY | PIN | EMAIL | ADDRESS | NAME | PHONE | SSN | DATE_TIME | PASSPORT_NUMBER | DRIVER_ID | URL | AGE | USERNAME | PASSWORD | AWS_ACCESS_KEY | AWS_SECRET_KEY | IP_ADDRESS | MAC_ADDRESS | ALL | LICENSE_PLATE | VEHICLE_IDENTIFICATION_NUMBER | UK_NATIONAL_INSURANCE_NUMBER | CA_SOCIAL_INSURANCE_NUMBER | US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER | UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER | IN_PERMANENT_ACCOUNT_NUMBER | IN_NREGA | INTERNATIONAL_BANK_ACCOUNT_NUMBER | SWIFT_CODE | UK_NATIONAL_HEALTH_SERVICE_NUMBER | CA_HEALTH_NUMBER | IN_AADHAAR | IN_VOTER_NUMBER`   
Required: No

## See Also
<a name="API_PiiEntity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/PiiEntity) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/PiiEntity) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/PiiEntity) 