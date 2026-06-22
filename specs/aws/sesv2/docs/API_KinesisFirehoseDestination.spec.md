---
id: "@specs/aws/sesv2/docs/API_KinesisFirehoseDestination"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS KinesisFirehoseDestination"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# KinesisFirehoseDestination

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_KinesisFirehoseDestination
> **target_lang:** meta — documentation tier. ALL sections preserved.



# KinesisFirehoseDestination
<a name="API_KinesisFirehoseDestination"></a>

An object that defines an Amazon Kinesis Data Firehose destination for email events. You can use Amazon Kinesis Data Firehose to stream data to other services, such as Amazon S3 and Amazon Redshift.

## Contents
<a name="API_KinesisFirehoseDestination_Contents"></a>

 ** DeliveryStreamArn **   <a name="SES-Type-KinesisFirehoseDestination-DeliveryStreamArn"></a>
The Amazon Resource Name (ARN) of the Amazon Kinesis Data Firehose stream that the Amazon SES API v2 sends email events to.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: Yes

 ** IamRoleArn **   <a name="SES-Type-KinesisFirehoseDestination-IamRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that the Amazon SES API v2 uses to send email events to the Amazon Kinesis Data Firehose stream.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: Yes

## See Also
<a name="API_KinesisFirehoseDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/KinesisFirehoseDestination) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/KinesisFirehoseDestination) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/KinesisFirehoseDestination) 