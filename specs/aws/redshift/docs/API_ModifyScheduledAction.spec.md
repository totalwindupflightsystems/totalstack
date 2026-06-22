---
id: "@specs/aws/redshift/docs/API_ModifyScheduledAction"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ModifyScheduledAction"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# ModifyScheduledAction

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_ModifyScheduledAction
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ModifyScheduledAction
<a name="API_ModifyScheduledAction"></a>

Modifies a scheduled action. 

## Request Parameters
<a name="API_ModifyScheduledAction_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ScheduledActionName **   
The name of the scheduled action to modify.   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** Enable **   
A modified enable flag of the scheduled action. If true, the scheduled action is active. If false, the scheduled action is disabled.   
Type: Boolean  
Required: No

 ** EndTime **   
A modified end time of the scheduled action. For more information about this parameter, see [ScheduledAction](API_ScheduledAction.md).   
Type: Timestamp  
Required: No

 ** IamRole **   
A different IAM role to assume to run the target action. For more information about this parameter, see [ScheduledAction](API_ScheduledAction.md).  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Schedule **   
A modified schedule in either `at( )` or `cron( )` format. For more information about this parameter, see [ScheduledAction](API_ScheduledAction.md).  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ScheduledActionDescription **   
A modified description of the scheduled action.   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** StartTime **   
A modified start time of the scheduled action. For more information about this parameter, see [ScheduledAction](API_ScheduledAction.md).   
Type: Timestamp  
Required: No

 ** TargetAction **   
A modified JSON format of the scheduled action. For more information about this parameter, see [ScheduledAction](API_ScheduledAction.md).   
Type: [ScheduledActionType](API_ScheduledActionType.md) object  
Required: No

## Response Elements
<a name="API_ModifyScheduledAction_ResponseElements"></a>

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
<a name="API_ModifyScheduledAction_Errors"></a>

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

 ** ScheduledActionNotFound **   
The scheduled action cannot be found.   
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

## Examples
<a name="API_ModifyScheduledAction_Examples"></a>

### Example
<a name="API_ModifyScheduledAction_Example_1"></a>

This example adds description to an existing scheduled action.

#### Sample Request
<a name="API_ModifyScheduledAction_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=ModifyScheduledAction
&ScheduledActionName=myscheduledaction
&ScheduledActionDescription=My+scheduled+action
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_ModifyScheduledAction_Example_1_Response"></a>

```
<ModifyScheduledActionResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <ModifyScheduledActionResult>
    <IamRole>arn:aws:iam::123456789012:role/myRedshiftRole</IamRole>
    <Schedule>at(2019-12-31T00:00:00)</Schedule>
    <ScheduledActionName>myscheduledaction</ScheduledActionName>
    <TargetAction>
      <ResizeCluster>
        <ClusterType>multi-node</ClusterType>
        <ClusterIdentifier>mycluster</ClusterIdentifier>
        <Classic>true</Classic>
        <NumberOfNodes>3</NumberOfNodes>
        <NodeType>dc2.large</NodeType>
      </ResizeCluster>
    </TargetAction>
    <NextInvocations>
      <ScheduledActionTime>2019-12-31T00:00:00Z</ScheduledActionTime>
    </NextInvocations>
    <State>ACTIVE</State>
    <ScheduledActionDescription>My scheduled action</ScheduledActionDescription>
  </ModifyScheduledActionResult>
  <ResponseMetadata>
    <RequestId>a2388ba8-28f3-11ea-8a28-2fd1719d0e86</RequestId>
  </ResponseMetadata>
</ModifyScheduledActionResponse>
```

## See Also
<a name="API_ModifyScheduledAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/ModifyScheduledAction) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/ModifyScheduledAction) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/ModifyScheduledAction) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/ModifyScheduledAction) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/ModifyScheduledAction) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/ModifyScheduledAction) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/ModifyScheduledAction) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/ModifyScheduledAction) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/ModifyScheduledAction) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/ModifyScheduledAction) 