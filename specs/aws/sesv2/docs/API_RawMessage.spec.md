---
id: "@specs/aws/sesv2/docs/API_RawMessage"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RawMessage"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# RawMessage

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_RawMessage
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RawMessage
<a name="API_RawMessage"></a>

Represents the raw content of an email message.

## Contents
<a name="API_RawMessage_Contents"></a>

 ** Data **   <a name="SES-Type-RawMessage-Data"></a>
The raw email message. The message has to meet the following criteria:  
+ The message has to contain a header and a body, separated by one blank line.
+ All of the required header fields must be present in the message.
+ Each part of a multipart MIME message must be formatted properly.
+ Attachments must be in a file format that the Amazon SES supports.
+ The raw data of the message needs to base64-encoded if you are accessing Amazon SES directly through the HTTPS interface. If you are accessing Amazon SES using an AWS SDK, the SDK takes care of the base 64-encoding for you.
+ If any of the MIME parts in your message contain content that is outside of the 7-bit ASCII character range, you should encode that content to ensure that recipients' email clients render the message properly.
+ The length of any single line of text in the message can't exceed 1,000 characters. This restriction is defined in [RFC 5321](https://tools.ietf.org/html/rfc5321).
Type: Base64-encoded binary data object  
Required: Yes

## See Also
<a name="API_RawMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/RawMessage) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/RawMessage) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/RawMessage) 