---
id: "@specs/aws/redshift/docs/API_CreateScheduledAction"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateScheduledAction"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# CreateScheduledAction

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_CreateScheduledAction
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateScheduledAction
<a name="API_CreateScheduledAction"></a>

Creates a scheduled action. A scheduled action contains a schedule and an Amazon Redshift API action. For example, you can create a schedule of when to run the `ResizeCluster` API operation. 

## Request Parameters
<a name="API_CreateScheduledAction_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** IamRole **   
The IAM role to assume to run the target action. For more information about this parameter, see [ScheduledAction](API_ScheduledAction.md).   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** Schedule **   
The schedule in `at( )` or `cron( )` format. For more information about this parameter, see [ScheduledAction](API_ScheduledAction.md).  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** ScheduledActionName **   
The name of the scheduled action. The name must be unique within an account. For more information about this parameter, see [ScheduledAction](API_ScheduledAction.md).   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** TargetAction **   
A JSON format string of the Amazon Redshift API operation with input parameters. For more information about this parameter, see [ScheduledAction](API_ScheduledAction.md).   
Type: [ScheduledActionType](API_ScheduledActionType.md) object  
Required: Yes

 ** Enable **   
If true, the schedule is enabled. If false, the scheduled action does not trigger. For more information about `state` of the scheduled action, see [ScheduledAction](API_ScheduledAction.md).   
Type: Boolean  
Required: No

 ** EndTime **   
The end time in UTC of the scheduled action. After this time, the scheduled action does not trigger. For more information about this parameter, see [ScheduledAction](API_ScheduledAction.md).   
Type: Timestamp  
Required: No

 ** ScheduledActionDescription **   
The description of the scheduled action.   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** StartTime **   
The start time in UTC of the scheduled action. Before this time, the scheduled action does not trigger. For more information about this parameter, see [ScheduledAction](API_ScheduledAction.md).  
Type: Timestamp  
Required: No

## Response Elements
<a name="API_CreateScheduledAction_ResponseElements"></a>

The following elements are returned by the service.

 ** EndTime **   
The end time in UTC when the schedule is no longer active. After this time, the scheduled action does not trigger.   
Type: Timestamp

 ** IamRole **   
The IAM role to assume to run the scheduled action. This IAM role must have permission to run the Amazon Redshift API operation in the scheduled action. This IAM role must allow the Amazon Redshift scheduler (Principal scheduler.redshift.amazonaws.com) to assume permissions on your behalf. For more information about the IAM role to use with the Amazon Redshift scheduler, see [Using Identity-Based Policies for Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-identity-based.html) in the *Amazon Redshift Cluster Management Guide*.   
Type: String  
Length Constraints: Maximum length of 2147483647.

 **NextInvocations.ScheduledActionTime.N**   
List of times when the scheduled action will run.   
Type: Array of timestamps

 ** Schedule **   
The schedule for a one-time (at format) or recurring (cron format) scheduled action. Schedule invocations must be separated by at least one hour.  
Format of at expressions is "`at(yyyy-mm-ddThh:mm:ss)`". For example, "`at(2016-03-04T17:27:00)`".  
Format of cron expressions is "`cron(Minutes Hours Day-of-month Month Day-of-week Year)`". For example, "`cron(0 10 ? * MON *)`". For more information, see [Cron Expressions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions) in the *Amazon CloudWatch Events User Guide*.  
Type: String  
Length Constraints: Maximum length of 2147483647.

 ** ScheduledActionDescription **   
The description of the scheduled action.   
Type: String  
Length Constraints: Maximum length of 2147483647.

 ** ScheduledActionName **   
The name of the scheduled action.   
Type: String  
Length Constraints: Maximum length of 2147483647.

 ** StartTime **   
The start time in UTC when the schedule is active. Before this time, the scheduled action does not trigger.   
Type: Timestamp

 ** State **   
The state of the scheduled action. For example, `DISABLED`.   
Type: String  
Valid Values: `ACTIVE | DISABLED` 

 ** TargetAction **   
A JSON format string of the Amazon Redshift API operation with input parameters.   
"`{\"ResizeCluster\":{\"NodeType\":\"ra3.4xlarge\",\"ClusterIdentifier\":\"my-test-cluster\",\"NumberOfNodes\":3}}`".   
Type: [ScheduledActionType](API_ScheduledActionType.md) object

## Errors
<a name="API_CreateScheduledAction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterNotFound **   
The `ClusterIdentifier` parameter does not refer to an existing cluster.   
HTTP Status Code: 404

 ** InvalidSchedule **   
The schedule you submitted isn't valid.  
HTTP Status Code: 400

 ** InvalidScheduledAction **   
The scheduled action is not valid.   
HTTP Status Code: 400

 ** ScheduledActionAlreadyExists **   
The scheduled action already exists.   
HTTP Status Code: 400

 ** ScheduledActionQuotaExceeded **   
The quota for scheduled actions exceeded.   
HTTP Status Code: 400

 ** ScheduledActionTypeUnsupported **   
The action type specified for a scheduled action is not supported.   
HTTP Status Code: 400

 ** UnauthorizedOperation **   
Your account is not authorized to perform the requested operation.  
HTTP Status Code: 400

 ** UnsupportedOperation **   
The requested operation isn't supported.  
HTTP Status Code: 400

## See Also
<a name="API_CreateScheduledAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/CreateScheduledAction) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/CreateScheduledAction) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/CreateScheduledAction) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/CreateScheduledAction) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/CreateScheduledAction) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/CreateScheduledAction) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/CreateScheduledAction) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/CreateScheduledAction) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/CreateScheduledAction) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/CreateScheduledAction) 