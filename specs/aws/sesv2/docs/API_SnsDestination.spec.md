---
id: "@specs/aws/sesv2/docs/API_SnsDestination"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SnsDestination"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# SnsDestination

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_SnsDestination
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SnsDestination
<a name="API_SnsDestination"></a>

An object that defines an Amazon SNS destination for email events. You can use Amazon SNS to send notifications when certain email events occur.

## Contents
<a name="API_SnsDestination_Contents"></a>

 ** TopicArn **   <a name="SES-Type-SnsDestination-TopicArn"></a>
The Amazon Resource Name (ARN) of the Amazon SNS topic to publish email events to. For more information about Amazon SNS topics, see the [Amazon SNS Developer Guide](https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html).  
Type: String  
Length Constraints: Minimum length of 1.  
Required: Yes

## See Also
<a name="API_SnsDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/SnsDestination) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/SnsDestination) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/SnsDestination) 