---
id: "@specs/aws/sesv2/docs/API_EventDetails"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EventDetails"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# EventDetails

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_EventDetails
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EventDetails
<a name="API_EventDetails"></a>

 Contains a `Bounce` object if the event type is `BOUNCE`. Contains a `Complaint` object if the event type is `COMPLAINT`. 

## Contents
<a name="API_EventDetails_Contents"></a>

 ** Bounce **   <a name="SES-Type-EventDetails-Bounce"></a>
Information about a `Bounce` event.  
Type: [Bounce](API_Bounce.md) object  
Required: No

 ** Complaint **   <a name="SES-Type-EventDetails-Complaint"></a>
Information about a `Complaint` event.  
Type: [Complaint](API_Complaint.md) object  
Required: No

## See Also
<a name="API_EventDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/EventDetails) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/EventDetails) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/EventDetails) 