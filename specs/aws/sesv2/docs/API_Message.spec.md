---
id: "@specs/aws/sesv2/docs/API_Message"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Message"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# Message

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_Message
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Message
<a name="API_Message"></a>

Represents the email message that you're sending. The `Message` object consists of a subject line and a message body.

## Contents
<a name="API_Message_Contents"></a>

 ** Body **   <a name="SES-Type-Message-Body"></a>
The body of the message. You can specify an HTML version of the message, a text-only version of the message, or both.  
Type: [Body](API_Body.md) object  
Required: Yes

 ** Subject **   <a name="SES-Type-Message-Subject"></a>
The subject line of the email. The subject line can only contain 7-bit ASCII characters. However, you can specify non-ASCII characters in the subject line by using encoded-word syntax, as described in [RFC 2047](https://tools.ietf.org/html/rfc2047).  
Type: [Content](API_Content.md) object  
Required: Yes

 ** Attachments **   <a name="SES-Type-Message-Attachments"></a>
 The List of attachments to include in your email. All recipients will receive the same attachments.  
Type: Array of [Attachment](API_Attachment.md) objects  
Required: No

 ** Headers **   <a name="SES-Type-Message-Headers"></a>
The list of message headers that will be added to the email message.  
Type: Array of [MessageHeader](API_MessageHeader.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 15 items.  
Required: No

## See Also
<a name="API_Message_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/Message) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/Message) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/Message) 