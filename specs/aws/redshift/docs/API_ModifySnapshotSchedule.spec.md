---
id: "@specs/aws/redshift/docs/API_ModifySnapshotSchedule"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ModifySnapshotSchedule"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# ModifySnapshotSchedule

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_ModifySnapshotSchedule
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ModifySnapshotSchedule
<a name="API_ModifySnapshotSchedule"></a>

Modifies a snapshot schedule. Any schedule associated with a cluster is modified asynchronously.

## Request Parameters
<a name="API_ModifySnapshotSchedule_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **ScheduleDefinitions.ScheduleDefinition.N**   
An updated list of schedule definitions. A schedule definition is made up of schedule expressions, for example, "cron(30 12 \*)" or "rate(12 hours)".  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** ScheduleIdentifier **   
A unique alphanumeric identifier of the schedule to modify.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

## Response Elements
<a name="API_ModifySnapshotSchedule_ResponseElements"></a>

The following elements are returned by the service.

 ** AssociatedClusterCount **   
The number of clusters associated with the schedule.  
Type: Integer

 **AssociatedClusters.ClusterAssociatedToSchedule.N**   
A list of clusters associated with the schedule. A maximum of 100 clusters is returned.  
Type: Array of [ClusterAssociatedToSchedule](API_ClusterAssociatedToSchedule.md) objects

 **NextInvocations.SnapshotTime.N**   
  
Type: Array of timestamps

 **ScheduleDefinitions.ScheduleDefinition.N**   
A list of ScheduleDefinitions.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.

 ** ScheduleDescription **   
The description of the schedule.  
Type: String  
Length Constraints: Maximum length of 2147483647.

 ** ScheduleIdentifier **   
A unique identifier for the schedule.  
Type: String  
Length Constraints: Maximum length of 2147483647.

 **Tags.Tag.N**   
An optional set of tags describing the schedule.  
Type: Array of [Tag](API_Tag.md) objects

## Errors
<a name="API_ModifySnapshotSchedule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidSchedule **   
The schedule you submitted isn't valid.  
HTTP Status Code: 400

 ** SnapshotScheduleNotFound **   
We could not find the specified snapshot schedule.   
HTTP Status Code: 400

 ** SnapshotScheduleUpdateInProgress **   
The specified snapshot schedule is already being updated.  
HTTP Status Code: 400

## Examples
<a name="API_ModifySnapshotSchedule_Examples"></a>

### Example
<a name="API_ModifySnapshotSchedule_Example_1"></a>

This example sets a snapshot schedule to the rate of every 10 hours.

#### Sample Request
<a name="API_ModifySnapshotSchedule_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=ModifySnapshotSchedule
&ScheduleIdentifier=mysnapshotschedule
&ScheduleDefinitions.ScheduleDefinition.1=rate%2810+hours%29
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_ModifySnapshotSchedule_Example_1_Response"></a>

```
<ModifySnapshotScheduleResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <ModifySnapshotScheduleResult>
    <ScheduleDefinitions>
      <ScheduleDefinition>rate(10 hours)</ScheduleDefinition>
    </ScheduleDefinitions>
    <ScheduleDescription>My schedule description</ScheduleDescription>
    <ScheduleIdentifier>mysnapshotschedule</ScheduleIdentifier>
    <Tags/>
  </ModifySnapshotScheduleResult>
  <ResponseMetadata>
    <RequestId>8c27532d-28f4-11ea-a940-1b28a85fd753</RequestId>
  </ResponseMetadata>
</ModifySnapshotScheduleResponse>
```

## See Also
<a name="API_ModifySnapshotSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/ModifySnapshotSchedule) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/ModifySnapshotSchedule) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/ModifySnapshotSchedule) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/ModifySnapshotSchedule) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/ModifySnapshotSchedule) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/ModifySnapshotSchedule) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/ModifySnapshotSchedule) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/ModifySnapshotSchedule) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/ModifySnapshotSchedule) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/ModifySnapshotSchedule) 