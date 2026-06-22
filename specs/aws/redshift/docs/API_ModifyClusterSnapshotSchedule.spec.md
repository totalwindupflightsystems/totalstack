---
id: "@specs/aws/redshift/docs/API_ModifyClusterSnapshotSchedule"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ModifyClusterSnapshotSchedule"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# ModifyClusterSnapshotSchedule

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_ModifyClusterSnapshotSchedule
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ModifyClusterSnapshotSchedule
<a name="API_ModifyClusterSnapshotSchedule"></a>

Modifies a snapshot schedule for a cluster.

## Request Parameters
<a name="API_ModifyClusterSnapshotSchedule_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ClusterIdentifier **   
A unique identifier for the cluster whose snapshot schedule you want to modify.   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** DisassociateSchedule **   
A boolean to indicate whether to remove the assoiciation between the cluster and the schedule.  
Type: Boolean  
Required: No

 ** ScheduleIdentifier **   
A unique alphanumeric identifier for the schedule that you want to associate with the cluster.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

## Errors
<a name="API_ModifyClusterSnapshotSchedule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterNotFound **   
The `ClusterIdentifier` parameter does not refer to an existing cluster.   
HTTP Status Code: 404

 ** InvalidClusterSnapshotScheduleState **   
The cluster snapshot schedule state is not valid.  
HTTP Status Code: 400

 ** SnapshotScheduleNotFound **   
We could not find the specified snapshot schedule.   
HTTP Status Code: 400

## Examples
<a name="API_ModifyClusterSnapshotSchedule_Examples"></a>

### Example
<a name="API_ModifyClusterSnapshotSchedule_Example_1"></a>

This example removes a snapshot schedule from a cluster.

#### Sample Request
<a name="API_ModifyClusterSnapshotSchedule_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=ModifyClusterSnapshotSchedule
&ClusterIdentifier=mycluster
&ScheduleIdentifier=mysnapshotschedule
&DisassociateSchedule=true
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_ModifyClusterSnapshotSchedule_Example_1_Response"></a>

```
<ModifyClusterSnapshotScheduleResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <ResponseMetadata>
    <RequestId>3ec38335-28ea-11ea-b6af-7126da6f11af</RequestId>
  </ResponseMetadata>
</ModifyClusterSnapshotScheduleResponse>
```

## See Also
<a name="API_ModifyClusterSnapshotSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/ModifyClusterSnapshotSchedule) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/ModifyClusterSnapshotSchedule) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/ModifyClusterSnapshotSchedule) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/ModifyClusterSnapshotSchedule) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/ModifyClusterSnapshotSchedule) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/ModifyClusterSnapshotSchedule) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/ModifyClusterSnapshotSchedule) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/ModifyClusterSnapshotSchedule) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/ModifyClusterSnapshotSchedule) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/ModifyClusterSnapshotSchedule) 