---
id: "@specs/aws/cloudtrail/docs/API_UpdateTrail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateTrail"
status: active
depends_on:
  - "@specs/aws/cloudtrail/meta"
---

# UpdateTrail

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudtrail/docs/API_UpdateTrail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateTrail
<a name="API_UpdateTrail"></a>

Updates trail settings that control what events you are logging, and how to handle log files. Changes to a trail do not require stopping the CloudTrail service. Use this action to designate an existing bucket for log delivery. If the existing bucket has previously been a target for CloudTrail log files, an IAM policy exists for the bucket. `UpdateTrail` must be called from the Region in which the trail was created; otherwise, an `InvalidHomeRegionException` is thrown.

## Request Syntax
<a name="API_UpdateTrail_RequestSyntax"></a>

```
{
   "CloudWatchLogsLogGroupArn": "{{string}}",
   "CloudWatchLogsRoleArn": "{{string}}",
   "EnableLogFileValidation": {{boolean}},
   "IncludeGlobalServiceEvents": {{boolean}},
   "IsMultiRegionTrail": {{boolean}},
   "IsOrganizationTrail": {{boolean}},
   "KmsKeyId": "{{string}}",
   "Name": "{{string}}",
   "S3BucketName": "{{string}}",
   "S3KeyPrefix": "{{string}}",
   "SnsTopicName": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateTrail_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CloudWatchLogsLogGroupArn](#API_UpdateTrail_RequestSyntax) **   <a name="awscloudtrail-UpdateTrail-request-CloudWatchLogsLogGroupArn"></a>
Specifies a log group name using an Amazon Resource Name (ARN), a unique identifier that represents the log group to which CloudTrail logs are delivered. You must use a log group that exists in your account.  
Not required unless you specify `CloudWatchLogsRoleArn`.  
Type: String  
Required: No

 ** [CloudWatchLogsRoleArn](#API_UpdateTrail_RequestSyntax) **   <a name="awscloudtrail-UpdateTrail-request-CloudWatchLogsRoleArn"></a>
Specifies the role for the CloudWatch Logs endpoint to assume to write to a user's log group. You must use a role that exists in your account.  
Type: String  
Required: No

 ** [EnableLogFileValidation](#API_UpdateTrail_RequestSyntax) **   <a name="awscloudtrail-UpdateTrail-request-EnableLogFileValidation"></a>
Specifies whether log file validation is enabled. The default is false.  
When you disable log file integrity validation, the chain of digest files is broken after one hour. CloudTrail does not create digest files for log files that were delivered during a period in which log file integrity validation was disabled. For example, if you enable log file integrity validation at noon on January 1, disable it at noon on January 2, and re-enable it at noon on January 10, digest files will not be created for the log files delivered from noon on January 2 to noon on January 10. The same applies whenever you stop CloudTrail logging or delete a trail.
Type: Boolean  
Required: No

 ** [IncludeGlobalServiceEvents](#API_UpdateTrail_RequestSyntax) **   <a name="awscloudtrail-UpdateTrail-request-IncludeGlobalServiceEvents"></a>
Specifies whether the trail is publishing events from global services such as IAM to the log files.  
Type: Boolean  
Required: No

 ** [IsMultiRegionTrail](#API_UpdateTrail_RequestSyntax) **   <a name="awscloudtrail-UpdateTrail-request-IsMultiRegionTrail"></a>
Specifies whether the trail applies only to the current Region or to all Regions. The default is false. If the trail exists only in the current Region and this value is set to true, shadow trails (replications of the trail) will be created in the other Regions. If the trail exists in all Regions and this value is set to false, the trail will remain in the Region where it was created, and its shadow trails in other Regions will be deleted. As a best practice, consider using trails that log events in all Regions.  
Type: Boolean  
Required: No

 ** [IsOrganizationTrail](#API_UpdateTrail_RequestSyntax) **   <a name="awscloudtrail-UpdateTrail-request-IsOrganizationTrail"></a>
Specifies whether the trail is applied to all accounts in an organization in AWS Organizations, or only for the current AWS account. The default is false, and cannot be true unless the call is made on behalf of an AWS account that is the management account for an organization in AWS Organizations. If the trail is not an organization trail and this is set to `true`, the trail will be created in all AWS accounts that belong to the organization. If the trail is an organization trail and this is set to `false`, the trail will remain in the current AWS account but be deleted from all member accounts in the organization.  
Only the management account for the organization can convert an organization trail to a non-organization trail, or convert a non-organization trail to an organization trail.
Type: Boolean  
Required: No

 ** [KmsKeyId](#API_UpdateTrail_RequestSyntax) **   <a name="awscloudtrail-UpdateTrail-request-KmsKeyId"></a>
Specifies the AWS KMS key ID to use to encrypt the logs and digest files delivered by CloudTrail. The value can be an alias name prefixed by "alias/", a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier.  
CloudTrail also supports AWS KMS multi-Region keys. For more information about multi-Region keys, see [Using multi-Region keys](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html) in the * AWS Key Management Service Developer Guide*.  
Examples:  
+ alias/MyAliasName
+ arn:aws:kms:us-east-2:123456789012:alias/MyAliasName
+ arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012
+ 12345678-1234-1234-1234-123456789012
Type: String  
Required: No

 ** [Name](#API_UpdateTrail_RequestSyntax) **   <a name="awscloudtrail-UpdateTrail-request-Name"></a>
Specifies the name of the trail or trail ARN. If `Name` is a trail name, the string must meet the following requirements:  
+ Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (\_), or dashes (-)
+ Start with a letter or number, and end with a letter or number
+ Be between 3 and 128 characters
+ Have no adjacent periods, underscores or dashes. Names like `my-_namespace` and `my--namespace` are not valid.
+ Not be in IP address format (for example, 192.168.5.4)
If `Name` is a trail ARN, it must be in the following format.  
 `arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail`   
Type: String  
Required: Yes

 ** [S3BucketName](#API_UpdateTrail_RequestSyntax) **   <a name="awscloudtrail-UpdateTrail-request-S3BucketName"></a>
Specifies the name of the Amazon S3 bucket designated for publishing log files. See [Amazon S3 Bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html).  
Type: String  
Required: No

 ** [S3KeyPrefix](#API_UpdateTrail_RequestSyntax) **   <a name="awscloudtrail-UpdateTrail-request-S3KeyPrefix"></a>
Specifies the Amazon S3 key prefix that comes after the name of the bucket you have designated for log file delivery. For more information, see [Finding Your CloudTrail Log Files](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/get-and-view-cloudtrail-log-files.html#cloudtrail-find-log-files). The maximum length is 200 characters.  
Type: String  
Required: No

 ** [SnsTopicName](#API_UpdateTrail_RequestSyntax) **   <a name="awscloudtrail-UpdateTrail-request-SnsTopicName"></a>
Specifies the name or ARN of the Amazon SNS topic defined for notification of log file delivery. The maximum length is 256 characters.  
Type: String  
Required: No

## Response Syntax
<a name="API_UpdateTrail_ResponseSyntax"></a>

```
{
   "CloudWatchLogsLogGroupArn": "string",
   "CloudWatchLogsRoleArn": "string",
   "IncludeGlobalServiceEvents": boolean,
   "IsMultiRegionTrail": boolean,
   "IsOrganizationTrail": boolean,
   "KmsKeyId": "string",
   "LogFileValidationEnabled": boolean,
   "Name": "string",
   "S3BucketName": "string",
   "S3KeyPrefix": "string",
   "SnsTopicARN": "string",
   "SnsTopicName": "string",
   "TrailARN": "string"
}
```

## Response Elements
<a name="API_UpdateTrail_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CloudWatchLogsLogGroupArn](#API_UpdateTrail_ResponseSyntax) **   <a name="awscloudtrail-UpdateTrail-response-CloudWatchLogsLogGroupArn"></a>
Specifies the Amazon Resource Name (ARN) of the log group to which CloudTrail logs are delivered.  
Type: String

 ** [CloudWatchLogsRoleArn](#API_UpdateTrail_ResponseSyntax) **   <a name="awscloudtrail-UpdateTrail-response-CloudWatchLogsRoleArn"></a>
Specifies the role for the CloudWatch Logs endpoint to assume to write to a user's log group.  
Type: String

 ** [IncludeGlobalServiceEvents](#API_UpdateTrail_ResponseSyntax) **   <a name="awscloudtrail-UpdateTrail-response-IncludeGlobalServiceEvents"></a>
Specifies whether the trail is publishing events from global services such as IAM to the log files.  
Type: Boolean

 ** [IsMultiRegionTrail](#API_UpdateTrail_ResponseSyntax) **   <a name="awscloudtrail-UpdateTrail-response-IsMultiRegionTrail"></a>
Specifies whether the trail exists in one Region or in all Regions.  
Type: Boolean

 ** [IsOrganizationTrail](#API_UpdateTrail_ResponseSyntax) **   <a name="awscloudtrail-UpdateTrail-response-IsOrganizationTrail"></a>
Specifies whether the trail is an organization trail.  
Type: Boolean

 ** [KmsKeyId](#API_UpdateTrail_ResponseSyntax) **   <a name="awscloudtrail-UpdateTrail-response-KmsKeyId"></a>
Specifies the AWS KMS key ID that encrypts the logs and digest files delivered by CloudTrail. The value is a fully specified ARN to a AWS KMS key in the following format.  
 `arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012`   
Type: String

 ** [LogFileValidationEnabled](#API_UpdateTrail_ResponseSyntax) **   <a name="awscloudtrail-UpdateTrail-response-LogFileValidationEnabled"></a>
Specifies whether log file integrity validation is enabled.  
Type: Boolean

 ** [Name](#API_UpdateTrail_ResponseSyntax) **   <a name="awscloudtrail-UpdateTrail-response-Name"></a>
Specifies the name of the trail.  
Type: String

 ** [S3BucketName](#API_UpdateTrail_ResponseSyntax) **   <a name="awscloudtrail-UpdateTrail-response-S3BucketName"></a>
Specifies the name of the Amazon S3 bucket designated for publishing log files.  
Type: String

 ** [S3KeyPrefix](#API_UpdateTrail_ResponseSyntax) **   <a name="awscloudtrail-UpdateTrail-response-S3KeyPrefix"></a>
Specifies the Amazon S3 key prefix that comes after the name of the bucket you have designated for log file delivery. For more information, see [Finding Your IAM Log Files](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/get-and-view-cloudtrail-log-files.html#cloudtrail-find-log-files).  
Type: String

 ** [SnsTopicARN](#API_UpdateTrail_ResponseSyntax) **   <a name="awscloudtrail-UpdateTrail-response-SnsTopicARN"></a>
Specifies the ARN of the Amazon SNS topic that CloudTrail uses to send notifications when log files are delivered. The following is the format of a topic ARN.  
 `arn:aws:sns:us-east-2:123456789012:MyTopic`   
Type: String

 ** [SnsTopicName](#API_UpdateTrail_ResponseSyntax) **   <a name="awscloudtrail-UpdateTrail-response-SnsTopicName"></a>
 *This parameter has been deprecated.*   
This field is no longer in use. Use `SnsTopicARN`.  
Type: String

 ** [TrailARN](#API_UpdateTrail_ResponseSyntax) **   <a name="awscloudtrail-UpdateTrail-response-TrailARN"></a>
Specifies the ARN of the trail that was updated. The following is the format of a trail ARN.  
 `arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail`   
Type: String

## Errors
<a name="API_UpdateTrail_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CloudTrailAccessNotEnabledException **   
This exception is thrown when trusted access has not been enabled between AWS CloudTrail and AWS Organizations. For more information, see [How to enable or disable trusted access](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html#orgs_how-to-enable-disable-trusted-access) in the * AWS Organizations User Guide* and [Prepare For Creating a Trail For Your Organization](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-an-organizational-trail-prepare.html) in the * AWS CloudTrail User Guide*.  
HTTP Status Code: 400

 ** CloudTrailARNInvalidException **   
This exception is thrown when an operation is called with an ARN that is not valid.  
The following is the format of a trail ARN: `arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail`   
The following is the format of an event data store ARN: `arn:aws:cloudtrail:us-east-2:123456789012:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE`   
The following is the format of a dashboard ARN: `arn:aws:cloudtrail:us-east-1:123456789012:dashboard/exampleDash`   
The following is the format of a channel ARN: `arn:aws:cloudtrail:us-east-2:123456789012:channel/01234567890`   
HTTP Status Code: 400

 ** CloudTrailInvalidClientTokenIdException **   
This exception is thrown when a call results in the `InvalidClientTokenId` error code. This can occur when you are creating or updating a trail to send notifications to an Amazon SNS topic that is in a suspended AWS account.  
HTTP Status Code: 400

 ** CloudWatchLogsDeliveryUnavailableException **   
Cannot set a CloudWatch Logs delivery for this Region.  
HTTP Status Code: 400

 ** ConflictException **   
This exception is thrown when the specified resource is not ready for an operation. This can occur when you try to run an operation on a resource before CloudTrail has time to fully load the resource, or because another operation is modifying the resource. If this exception occurs, wait a few minutes, and then try the operation again.  
HTTP Status Code: 400

 ** InsufficientDependencyServiceAccessPermissionException **   
This exception is thrown when the IAM identity that is used to create the organization resource lacks one or more required permissions for creating an organization resource in a required service.  
HTTP Status Code: 400

 ** InsufficientEncryptionPolicyException **   
For the `CreateTrail` `PutInsightSelectors`, `UpdateTrail`, `StartQuery`, and `StartImport` operations, this exception is thrown when the policy on the S3 bucket or AWS KMS key does not have sufficient permissions for the operation.  
For all other operations, this exception is thrown when the policy for the AWS KMS key does not have sufficient permissions for the operation.  
HTTP Status Code: 400

 ** InsufficientS3BucketPolicyException **   
This exception is thrown when the policy on the S3 bucket is not sufficient.  
HTTP Status Code: 400

 ** InsufficientSnsTopicPolicyException **   
This exception is thrown when the policy on the Amazon SNS topic is not sufficient.  
HTTP Status Code: 400

 ** InvalidCloudWatchLogsLogGroupArnException **   
This exception is thrown when the provided CloudWatch Logs log group is not valid.  
HTTP Status Code: 400

 ** InvalidCloudWatchLogsRoleArnException **   
This exception is thrown when the provided role is not valid.  
HTTP Status Code: 400

 ** InvalidEventSelectorsException **   
This exception is thrown when the `PutEventSelectors` operation is called with a number of event selectors, advanced event selectors, or data resources that is not valid. The combination of event selectors or advanced event selectors and data resources is not valid. A trail can have up to 5 event selectors. If a trail uses advanced event selectors, a maximum of 500 total values for all conditions in all advanced event selectors is allowed. A trail is limited to 250 data resources. These data resources can be distributed across event selectors, but the overall total cannot exceed 250.  
You can:  
+ Specify a valid number of event selectors (1 to 5) for a trail.
+ Specify a valid number of data resources (1 to 250) for an event selector. The limit of number of resources on an individual event selector is configurable up to 250. However, this upper limit is allowed only if the total number of data resources does not exceed 250 across all event selectors for a trail.
+ Specify up to 500 values for all conditions in all advanced event selectors for a trail.
+ Specify a valid value for a parameter. For example, specifying the `ReadWriteType` parameter with a value of `read-only` is not valid.
HTTP Status Code: 400

 ** InvalidHomeRegionException **   
This exception is thrown when an operation is called on a trail from a Region other than the Region in which the trail was created.  
HTTP Status Code: 400

 ** InvalidKmsKeyIdException **   
This exception is thrown when the AWS KMS key ARN is not valid.  
HTTP Status Code: 400

 ** InvalidParameterCombinationException **   
This exception is thrown when the combination of parameters provided is not valid.  
HTTP Status Code: 400

 ** InvalidParameterException **   
The request includes a parameter that is not valid.  
HTTP Status Code: 400

 ** InvalidS3BucketNameException **   
This exception is thrown when the provided S3 bucket name is not valid.  
HTTP Status Code: 400

 ** InvalidS3PrefixException **   
This exception is thrown when the provided S3 prefix is not valid.  
HTTP Status Code: 400

 ** InvalidSnsTopicNameException **   
This exception is thrown when the provided SNS topic name is not valid.  
HTTP Status Code: 400

 ** InvalidTrailNameException **   
This exception is thrown when the provided trail name is not valid. Trail names must meet the following requirements:  
+ Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (\_), or dashes (-)
+ Start with a letter or number, and end with a letter or number
+ Be between 3 and 128 characters
+ Have no adjacent periods, underscores or dashes. Names like `my-_namespace` and `my--namespace` are not valid.
+ Not be in IP address format (for example, 192.168.5.4)
HTTP Status Code: 400

 ** KmsException **   
This exception is thrown when there is an issue with the specified AWS KMS key and the trail or event data store can't be updated.  
HTTP Status Code: 400

 ** KmsKeyDisabledException **   
 *This error has been deprecated.*   
This exception is no longer in use.  
HTTP Status Code: 400

 ** KmsKeyNotFoundException **   
This exception is thrown when the AWS KMS key does not exist, when the S3 bucket and the AWS KMS key are not in the same Region, or when the AWS KMS key associated with the Amazon SNS topic either does not exist or is not in the same Region.  
HTTP Status Code: 400

 ** NoManagementAccountSLRExistsException **   
 This exception is thrown when the management account does not have a service-linked role.   
HTTP Status Code: 400

 ** NotOrganizationMasterAccountException **   
This exception is thrown when the AWS account making the request to create or update an organization trail or event data store is not the management account for an organization in AWS Organizations. For more information, see [Prepare For Creating a Trail For Your Organization](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-an-organizational-trail-prepare.html) or [Organization event data stores](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-organizations.html).  
HTTP Status Code: 400

 ** OperationNotPermittedException **   
This exception is thrown when the requested operation is not permitted.  
HTTP Status Code: 400

 ** OrganizationNotInAllFeaturesModeException **   
This exception is thrown when AWS Organizations is not configured to support all features. All features must be enabled in Organizations to support creating an organization trail or event data store.  
HTTP Status Code: 400

 ** OrganizationsNotInUseException **   
This exception is thrown when the request is made from an AWS account that is not a member of an organization. To make this request, sign in using the credentials of an account that belongs to an organization.  
HTTP Status Code: 400

 ** S3BucketDoesNotExistException **   
This exception is thrown when the specified S3 bucket does not exist.  
HTTP Status Code: 400

 ** ThrottlingException **   
 This exception is thrown when the request rate exceeds the limit.   
HTTP Status Code: 400

 ** TrailNotFoundException **   
This exception is thrown when the trail with the given name is not found.  
HTTP Status Code: 400

 ** TrailNotProvidedException **   
This exception is no longer in use.  
HTTP Status Code: 400

 ** UnsupportedOperationException **   
This exception is thrown when the requested operation is not supported.  
HTTP Status Code: 400

## See Also
<a name="API_UpdateTrail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/UpdateTrail) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudtrail-2013-11-01/UpdateTrail) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/UpdateTrail) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/UpdateTrail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/UpdateTrail) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/UpdateTrail) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/UpdateTrail) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/UpdateTrail) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/UpdateTrail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/UpdateTrail) 