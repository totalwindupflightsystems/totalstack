---
id: "@specs/aws/sesv2/docs/API_EmailContent"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EmailContent"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# EmailContent

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_EmailContent
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EmailContent
<a name="API_EmailContent"></a>

An object that defines the entire content of the email, including the message headers, body content, and attachments. For a simple email message, you specify the subject and provide both text and HTML versions of the message body. You can also add attachments to simple and templated messages. For a raw message, you provide a complete MIME-formatted message, which can include custom headers and attachments.

## Contents
<a name="API_EmailContent_Contents"></a>

 ** Raw **   <a name="SES-Type-EmailContent-Raw"></a>
The raw email message. The message has to meet the following criteria:  
+ The message has to contain a header and a body, separated by one blank line.
+ All of the required header fields must be present in the message.
+ Each part of a multipart MIME message must be formatted properly.
+ If you include attachments, they must be in a file format that the Amazon SES API v2 supports. 
+ The raw data of the message needs to base64-encoded if you are accessing Amazon SES directly through the HTTPS interface. If you are accessing Amazon SES using an AWS SDK, the SDK takes care of the base 64-encoding for you.
+ If any of the MIME parts in your message contain content that is outside of the 7-bit ASCII character range, you should encode that content to ensure that recipients' email clients render the message properly.
+ The length of any single line of text in the message can't exceed 1,000 characters. This restriction is defined in [RFC 5321](https://tools.ietf.org/html/rfc5321).
Type: [RawMessage](API_RawMessage.md) object  
Required: No

 ** Simple **   <a name="SES-Type-EmailContent-Simple"></a>
The simple email message. The message consists of a subject, message body and attachments list.  
Type: [Message](API_Message.md) object  
Required: No

 ** Template **   <a name="SES-Type-EmailContent-Template"></a>
The template to use for the email message.  
Type: [Template](API_Template.md) object  
Required: No

## See Also
<a name="API_EmailContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/EmailContent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/EmailContent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/EmailContent) 