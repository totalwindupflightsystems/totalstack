---
id: "@specs/aws/sesv2/docs/API_Complaint"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Complaint"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# Complaint

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_Complaint
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Complaint
<a name="API_Complaint"></a>

Information about a `Complaint` event.

## Contents
<a name="API_Complaint_Contents"></a>

 ** ComplaintFeedbackType **   <a name="SES-Type-Complaint-ComplaintFeedbackType"></a>
 The value of the `Feedback-Type` field from the feedback report received from the ISP.   
Type: String  
Required: No

 ** ComplaintSubType **   <a name="SES-Type-Complaint-ComplaintSubType"></a>
 Can either be `null` or `OnAccountSuppressionList`. If the value is `OnAccountSuppressionList`, SES accepted the message, but didn't attempt to send it because it was on the account-level suppression list.   
Type: String  
Required: No

## See Also
<a name="API_Complaint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/Complaint) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/Complaint) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/Complaint) 