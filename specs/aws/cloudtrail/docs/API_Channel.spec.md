---
id: "@specs/aws/cloudtrail/docs/API_Channel"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Channel"
status: active
depends_on:
  - "@specs/aws/cloudtrail/meta"
---

# Channel

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudtrail/docs/API_Channel
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Channel
<a name="API_Channel"></a>

Contains information about a returned CloudTrail channel.

## Contents
<a name="API_Channel_Contents"></a>

 ** ChannelArn **   <a name="awscloudtrail-Type-Channel-ChannelArn"></a>
The Amazon Resource Name (ARN) of a channel.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 256.  
Pattern: `^[a-zA-Z0-9._/\-:]+$`   
Required: No

 ** Name **   <a name="awscloudtrail-Type-Channel-Name"></a>
 The name of the CloudTrail channel. For service-linked channels, the name is `aws-service-channel/service-name/custom-suffix` where `service-name` represents the name of the AWS service that created the channel and `custom-suffix` represents the suffix created by the AWS service.   
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9._\-]+$`   
Required: No

## See Also
<a name="API_Channel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/Channel) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/Channel) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/Channel) 