---
id: "@specs/aws/sesv2/docs/API_ReviewDetails"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ReviewDetails"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# ReviewDetails

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_ReviewDetails
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ReviewDetails
<a name="API_ReviewDetails"></a>

An object that contains information about your account details review.

## Contents
<a name="API_ReviewDetails_Contents"></a>

 ** CaseId **   <a name="SES-Type-ReviewDetails-CaseId"></a>
The associated support center case ID (if any).  
Type: String  
Required: No

 ** Status **   <a name="SES-Type-ReviewDetails-Status"></a>
The status of the latest review of your account. The status can be one of the following:  
+  `PENDING` – We have received your appeal and are in the process of reviewing it.
+  `GRANTED` – Your appeal has been reviewed and your production access has been granted.
+  `DENIED` – Your appeal has been reviewed and your production access has been denied.
+  `FAILED` – An internal error occurred and we didn't receive your appeal. You can submit your appeal again.
Type: String  
Valid Values: `PENDING | FAILED | GRANTED | DENIED`   
Required: No

## See Also
<a name="API_ReviewDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/ReviewDetails) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/ReviewDetails) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/ReviewDetails) 