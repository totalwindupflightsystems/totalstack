---
id: "@specs/aws/kendra/docs/API_Correction"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Correction"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# Correction

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_Correction
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Correction
<a name="API_Correction"></a>

A corrected misspelled word in a query.

## Contents
<a name="API_Correction_Contents"></a>

 ** BeginOffset **   <a name="kendra-Type-Correction-BeginOffset"></a>
The zero-based location in the response string or text where the corrected word starts.  
Type: Integer  
Required: No

 ** CorrectedTerm **   <a name="kendra-Type-Correction-CorrectedTerm"></a>
The string or text of a corrected misspelled word in a query.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

 ** EndOffset **   <a name="kendra-Type-Correction-EndOffset"></a>
The zero-based location in the response string or text where the corrected word ends.  
Type: Integer  
Required: No

 ** Term **   <a name="kendra-Type-Correction-Term"></a>
The string or text of a misspelled word in a query.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

## See Also
<a name="API_Correction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/Correction) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/Correction) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/Correction) 