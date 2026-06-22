---
id: "@specs/aws/sesv2/docs/API_MessageHeader"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS MessageHeader"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# MessageHeader

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_MessageHeader
> **target_lang:** meta — documentation tier. ALL sections preserved.



# MessageHeader
<a name="API_MessageHeader"></a>

Contains the name and value of a message header that you add to an email.

## Contents
<a name="API_MessageHeader_Contents"></a>

 ** Name **   <a name="SES-Type-MessageHeader-Name"></a>
The name of the message header. The message header name has to meet the following criteria:  
+ Can contain any printable ASCII character (33 - 126) except for colon (:).
+ Can contain no more than 126 characters.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 126.  
Pattern: `^[!-9;-@A-~]+$`   
Required: Yes

 ** Value **   <a name="SES-Type-MessageHeader-Value"></a>
The value of the message header. The message header value has to meet the following criteria:  
+ Can contain any printable ASCII character.
+ Can contain no more than 995 characters.
+ The combined length of the header name and value must not exceed 996 characters.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 995.  
Pattern: `[ -~]*`   
Required: Yes

## See Also
<a name="API_MessageHeader_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/MessageHeader) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/MessageHeader) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/MessageHeader) 