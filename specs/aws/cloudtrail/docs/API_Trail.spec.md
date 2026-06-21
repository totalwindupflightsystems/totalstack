---
id: "@specs/aws/cloudtrail/docs/API_Trail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Trail"
status: active
depends_on:
  - "@specs/aws/cloudtrail/meta"
---

# Trail

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudtrail/docs/API_Trail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Trail
<a name="API_Trail"></a>

The settings for a trail.

## Contents
<a name="API_Trail_Contents"></a>

 ** CloudWatchLogsLogGroupArn **   <a name="awscloudtrail-Type-Trail-CloudWatchLogsLogGroupArn"></a>
Specifies an Amazon Resource Name (ARN), a unique identifier that represents the log group to which CloudTrail logs will be delivered.  
Type: String  
Required: No

 ** CloudWatchLogsRoleArn **   <a name="awscloudtrail-Type-Trail-CloudWatchLogsRoleArn"></a>
Specifies the role for the CloudWatch Logs endpoint to assume to write to a user's log group.  
Type: String  
Required: No

 ** HasCustomEventSelectors **   <a name="awscloudtrail-Type-Trail-HasCustomEventSelectors"></a>
Specifies if the trail has custom event selectors.  
Type: Boolean  
Required: No

 ** HasInsightSelectors **   <a name="awscloudtrail-Type-Trail-HasInsightSelectors"></a>
Specifies whether a trail has insight types specified in an `InsightSelector` list.  
Type: Boolean  
Required: No

 ** HomeRegion **   <a name="awscloudtrail-Type-Trail-HomeRegion"></a>
The Region in which the trail was created.  
Type: String  
Required: No

 ** IncludeGlobalServiceEvents **   <a name="awscloudtrail-Type-Trail-IncludeGlobalServiceEvents"></a>
Set to **True** to include AWS API calls from AWS global services such as IAM. Otherwise, **False**.  
Type: Boolean  
Required: No

 ** IsMultiRegionTrail **   <a name="awscloudtrail-Type-Trail-IsMultiRegionTrail"></a>
Specifies whether the trail exists only in one Region or exists in all Regions.  
Type: Boolean  
Required: No

 ** IsOrganizationTrail **   <a name="awscloudtrail-Type-Trail-IsOrganizationTrail"></a>
Specifies whether the trail is an organization trail.  
Type: Boolean  
Required: No

 ** KmsKeyId **   <a name="awscloudtrail-Type-Trail-KmsKeyId"></a>
Specifies the AWS KMS key ID that encrypts the logs and digest files delivered by CloudTrail. The value is a fully specified ARN to a AWS KMS key in the following format.  
 `arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012`   
Type: String  
Required: No

 ** LogFileValidationEnabled **   <a name="awscloudtrail-Type-Trail-LogFileValidationEnabled"></a>
Specifies whether log file validation is enabled.  
Type: Boolean  
Required: No

 ** Name **   <a name="awscloudtrail-Type-Trail-Name"></a>
Name of the trail set by calling [CreateTrail](API_CreateTrail.md). The maximum length is 128 characters.  
Type: String  
Required: No

 ** S3BucketName **   <a name="awscloudtrail-Type-Trail-S3BucketName"></a>
Name of the Amazon S3 bucket into which CloudTrail delivers your trail files. See [Amazon S3 Bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html).  
Type: String  
Required: No

 ** S3KeyPrefix **   <a name="awscloudtrail-Type-Trail-S3KeyPrefix"></a>
Specifies the Amazon S3 key prefix that comes after the name of the bucket you have designated for log file delivery. For more information, see [Finding Your CloudTrail Log Files](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/get-and-view-cloudtrail-log-files.html#cloudtrail-find-log-files). The maximum length is 200 characters.  
Type: String  
Required: No

 ** SnsTopicARN **   <a name="awscloudtrail-Type-Trail-SnsTopicARN"></a>
Specifies the ARN of the Amazon SNS topic that CloudTrail uses to send notifications when log files are delivered. The following is the format of a topic ARN.  
 `arn:aws:sns:us-east-2:123456789012:MyTopic`   
Type: String  
Required: No

 ** SnsTopicName **   <a name="awscloudtrail-Type-Trail-SnsTopicName"></a>
 *This member has been deprecated.*   
This field is no longer in use. Use `SnsTopicARN`.  
Type: String  
Required: No

 ** TrailARN **   <a name="awscloudtrail-Type-Trail-TrailARN"></a>
Specifies the ARN of the trail. The following is the format of a trail ARN.  
 `arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail`   
Type: String  
Required: No

## See Also
<a name="API_Trail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/Trail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/Trail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/Trail) 