---
id: "@specs/aws/sesv2/docs/API_MessageTag"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS MessageTag"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# MessageTag

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_MessageTag
> **target_lang:** meta — documentation tier. ALL sections preserved.



# MessageTag
<a name="API_MessageTag"></a>

Contains the name and value of a tag that you apply to an email. You can use message tags when you publish email sending events. 

## Contents
<a name="API_MessageTag_Contents"></a>

 ** Name **   <a name="SES-Type-MessageTag-Name"></a>
The name of the message tag. The message tag name has to meet the following criteria:  
+ It can only contain ASCII letters (a–z, A–Z), numbers (0–9), underscores (\_), or dashes (-).
+ It can contain no more than 256 characters.
Type: String  
Required: Yes

 ** Value **   <a name="SES-Type-MessageTag-Value"></a>
The value of the message tag. The message tag value has to meet the following criteria:  
+ It can only contain ASCII letters (a–z, A–Z), numbers (0–9), underscores (\_), or dashes (-).
+ It can contain no more than 256 characters.
Type: String  
Required: Yes

## See Also
<a name="API_MessageTag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/MessageTag) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/MessageTag) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/MessageTag) 