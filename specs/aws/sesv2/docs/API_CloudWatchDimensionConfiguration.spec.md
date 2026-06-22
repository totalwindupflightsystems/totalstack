---
id: "@specs/aws/sesv2/docs/API_CloudWatchDimensionConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CloudWatchDimensionConfiguration"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# CloudWatchDimensionConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_CloudWatchDimensionConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CloudWatchDimensionConfiguration
<a name="API_CloudWatchDimensionConfiguration"></a>

An object that defines the dimension configuration to use when you send email events to Amazon CloudWatch.

## Contents
<a name="API_CloudWatchDimensionConfiguration_Contents"></a>

 ** DefaultDimensionValue **   <a name="SES-Type-CloudWatchDimensionConfiguration-DefaultDimensionValue"></a>
The default value of the dimension that is published to Amazon CloudWatch if you don't provide the value of the dimension when you send an email. This value has to meet the following criteria:  
+ Can only contain ASCII letters (a–z, A–Z), numbers (0–9), underscores (\_), or dashes (-), at signs (@), and periods (.).
+ It can contain no more than 255 characters.
Type: String  
Required: Yes

 ** DimensionName **   <a name="SES-Type-CloudWatchDimensionConfiguration-DimensionName"></a>
The name of an Amazon CloudWatch dimension associated with an email sending metric. The name has to meet the following criteria:  
+ It can only contain ASCII letters (a–z, A–Z), numbers (0–9), underscores (\_), or dashes (-).
+ It can contain no more than 255 characters.
Type: String  
Required: Yes

 ** DimensionValueSource **   <a name="SES-Type-CloudWatchDimensionConfiguration-DimensionValueSource"></a>
The location where the Amazon SES API v2 finds the value of a dimension to publish to Amazon CloudWatch. To use the message tags that you specify using an `X-SES-MESSAGE-TAGS` header or a parameter to the `SendEmail` or `SendRawEmail` API, choose `messageTag`. To use your own email headers, choose `emailHeader`. To use link tags, choose `linkTags`.  
Type: String  
Valid Values: `MESSAGE_TAG | EMAIL_HEADER | LINK_TAG`   
Required: Yes

## See Also
<a name="API_CloudWatchDimensionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/CloudWatchDimensionConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/CloudWatchDimensionConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/CloudWatchDimensionConfiguration) 