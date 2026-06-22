---
id: "@specs/aws/redshift/docs/API_DescribeSnapshotSchedules"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeSnapshotSchedules"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DescribeSnapshotSchedules

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DescribeSnapshotSchedules
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeSnapshotSchedules
<a name="API_DescribeSnapshotSchedules"></a>

Returns a list of snapshot schedules. 

## Request Parameters
<a name="API_DescribeSnapshotSchedules_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ClusterIdentifier **   
The unique identifier for the cluster whose snapshot schedules you want to view.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Marker **   
A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the `marker` parameter and retrying the command. If the `marker` field is empty, all response records have been retrieved for the request.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** MaxRecords **   
The maximum number or response records to return in each call. If the number of remaining response records exceeds the specified `MaxRecords` value, a value is returned in a `marker` field of the response. You can retrieve the next set of records by retrying the command with the returned `marker` value.  
Type: Integer  
Required: No

 ** ScheduleIdentifier **   
A unique identifier for a snapshot schedule.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 **TagKeys.TagKey.N**   
The key value for a snapshot schedule tag.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: No

 **TagValues.TagValue.N**   
The value corresponding to the key of the snapshot schedule tag.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: No

## Response Elements
<a name="API_DescribeSnapshotSchedules_ResponseElements"></a>

The following elements are returned by the service.

 ** Marker **   
A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the `marker` parameter and retrying the command. If the `marker` field is empty, all response records have been retrieved for the request.  
Type: String  
Length Constraints: Maximum length of 2147483647.

 **SnapshotSchedules.SnapshotSchedule.N**   
A list of SnapshotSchedules.  
Type: Array of [SnapshotSchedule](API_SnapshotSchedule.md) objects

## Errors
<a name="API_DescribeSnapshotSchedules_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeSnapshotSchedules_Examples"></a>

### Example
<a name="API_DescribeSnapshotSchedules_Example_1"></a>

This example illustrates one usage of DescribeSnapshotSchedules.

#### Sample Request
<a name="API_DescribeSnapshotSchedules_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=DescribeSnapshotSchedules
&ClusterIdentifier=mycluster
&ScheduleIdentifier=mysnapshotschedule
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_DescribeSnapshotSchedules_Example_1_Response"></a>

```
<DescribeSnapshotSchedulesResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <DescribeSnapshotSchedulesResult>
    <SnapshotSchedules>
      <SnapshotSchedule>
        <ScheduleDefinitions>
          <ScheduleDefinition>rate(12 hours)</ScheduleDefinition>
        </ScheduleDefinitions>
        <ScheduleDescription>My schedule description</ScheduleDescription>
        <AssociatedClusterCount>1</AssociatedClusterCount>
        <AssociatedClusters>
          <ClusterAssociatedToSchedule>
            <ScheduleAssociationState>ACTIVE</ScheduleAssociationState>
            <ClusterIdentifier>mycluster</ClusterIdentifier>
          </ClusterAssociatedToSchedule>
        </AssociatedClusters>
        <ScheduleIdentifier>mysnapshotschedule</ScheduleIdentifier>
        <Tags/>
      </SnapshotSchedule>
    </SnapshotSchedules>
  </DescribeSnapshotSchedulesResult>
  <ResponseMetadata>
    <RequestId>65030ae0-28d3-11ea-9caa-c956bec1ce87</RequestId>
  </ResponseMetadata>
</DescribeSnapshotSchedulesResponse>
```

## See Also
<a name="API_DescribeSnapshotSchedules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DescribeSnapshotSchedules) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DescribeSnapshotSchedules) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DescribeSnapshotSchedules) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DescribeSnapshotSchedules) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DescribeSnapshotSchedules) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DescribeSnapshotSchedules) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DescribeSnapshotSchedules) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DescribeSnapshotSchedules) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DescribeSnapshotSchedules) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DescribeSnapshotSchedules) 