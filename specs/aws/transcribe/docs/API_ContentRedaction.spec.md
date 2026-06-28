---
id: "@specs/aws/transcribe/docs/API_ContentRedaction"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ContentRedaction"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# ContentRedaction

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_ContentRedaction
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ContentRedaction
<a name="API_ContentRedaction"></a>

Makes it possible to redact or flag specified personally identifiable information (PII) in your transcript. If you use `ContentRedaction`, you must also include the sub-parameters: `RedactionOutput` and `RedactionType`. You can optionally include `PiiEntityTypes` to choose which types of PII you want to redact.

## Contents
<a name="API_ContentRedaction_Contents"></a>

 ** RedactionOutput **   <a name="transcribe-Type-ContentRedaction-RedactionOutput"></a>
Specify if you want only a redacted transcript, or if you want a redacted and an unredacted transcript.  
When you choose `redacted` Amazon Transcribe creates only a redacted transcript.  
When you choose `redacted_and_unredacted` Amazon Transcribe creates a redacted and an unredacted transcript (as two separate files).  
Type: String  
Valid Values: `redacted | redacted_and_unredacted`   
Required: Yes

 ** RedactionType **   <a name="transcribe-Type-ContentRedaction-RedactionType"></a>
Specify the category of information you want to redact; `PII` (personally identifiable information) is the only valid value. You can use `PiiEntityTypes` to choose which types of PII you want to redact. If you do not include `PiiEntityTypes` in your request, all PII is redacted.  
Type: String  
Valid Values: `PII`   
Required: Yes

 ** PiiEntityTypes **   <a name="transcribe-Type-ContentRedaction-PiiEntityTypes"></a>
Specify which types of personally identifiable information (PII) you want to redact in your transcript. You can include as many types as you'd like, or you can select `ALL`. If you do not include `PiiEntityTypes` in your request, all PII is redacted.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 11 items.  
Valid Values: `BANK_ACCOUNT_NUMBER | BANK_ROUTING | CREDIT_DEBIT_NUMBER | CREDIT_DEBIT_CVV | CREDIT_DEBIT_EXPIRY | PIN | EMAIL | ADDRESS | NAME | PHONE | SSN | ALL`   
Required: No

## See Also
<a name="API_ContentRedaction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/ContentRedaction) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/ContentRedaction) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/ContentRedaction) 