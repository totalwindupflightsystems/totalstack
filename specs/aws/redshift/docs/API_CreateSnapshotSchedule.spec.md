---
id: "@specs/aws/redshift/docs/API_CreateSnapshotSchedule"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateSnapshotSchedule"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# CreateSnapshotSchedule

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_CreateSnapshotSchedule
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateSnapshotSchedule
<a name="API_CreateSnapshotSchedule"></a>

Create a snapshot schedule that can be associated to a cluster and which overrides the default system backup schedule. 

## Request Parameters
<a name="API_CreateSnapshotSchedule_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DryRun **   
  
Type: Boolean  
Required: No

 ** NextInvocations **   
  
Type: Integer  
Required: No

 **ScheduleDefinitions.ScheduleDefinition.N**   
The definition of the snapshot schedule. The definition is made up of schedule expressions, for example "cron(30 12 \*)" or "rate(12 hours)".   
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ScheduleDescription **   
The description of the snapshot schedule.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ScheduleIdentifier **   
A unique identifier for a snapshot schedule. Only alphanumeric characters are allowed for the identifier.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 **Tags.Tag.N**   
An optional set of tags you can use to search for the schedule.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## Response Elements
<a name="API_CreateSnapshotSchedule_ResponseElements"></a>

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
<a name="API_CreateSnapshotSchedule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidSchedule **   
The schedule you submitted isn't valid.  
HTTP Status Code: 400

 ** InvalidTagFault **   
The tag is invalid.  
HTTP Status Code: 400

 ** ScheduleDefinitionTypeUnsupported **   
The definition you submitted is not supported.  
HTTP Status Code: 400

 ** SnapshotScheduleAlreadyExists **   
The specified snapshot schedule already exists.   
HTTP Status Code: 400

 ** SnapshotScheduleQuotaExceeded **   
You have exceeded the quota of snapshot schedules.   
HTTP Status Code: 400

 ** TagLimitExceededFault **   
You have exceeded the number of tags allowed.  
HTTP Status Code: 400

## Examples
<a name="API_CreateSnapshotSchedule_Examples"></a>

### Example
<a name="API_CreateSnapshotSchedule_Example_1"></a>

This example illustrates one usage of CreateSnapshotSchedule.

#### Sample Request
<a name="API_CreateSnapshotSchedule_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=CreateSnapshotSchedule
&ScheduleDefinitions.ScheduleDefinition.1=rate%2812+hours%29
&ScheduleIdentifier=mysnapshotschedule
&ScheduleDescription=My+schedule+description
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_CreateSnapshotSchedule_Example_1_Response"></a>

```
<CreateSnapshotScheduleResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <CreateSnapshotScheduleResult>
    <ScheduleDefinitions>
      <ScheduleDefinition>rate(12 hours)</ScheduleDefinition>
    </ScheduleDefinitions>
    <ScheduleDescription>My schedule description</ScheduleDescription>
    <ScheduleIdentifier>mysnapshotschedule</ScheduleIdentifier>
    <Tags/>
  </CreateSnapshotScheduleResult>
  <ResponseMetadata>
    <RequestId>6f3e2f58-2837-11ea-9939-5fccefa818c0</RequestId>
  </ResponseMetadata>
</CreateSnapshotScheduleResponse>
```

## See Also
<a name="API_CreateSnapshotSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/CreateSnapshotSchedule) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/CreateSnapshotSchedule) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/CreateSnapshotSchedule) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/CreateSnapshotSchedule) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/CreateSnapshotSchedule) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/CreateSnapshotSchedule) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/CreateSnapshotSchedule) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/CreateSnapshotSchedule) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/CreateSnapshotSchedule) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/CreateSnapshotSchedule) 