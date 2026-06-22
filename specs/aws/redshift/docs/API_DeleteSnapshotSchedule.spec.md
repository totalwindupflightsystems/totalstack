---
id: "@specs/aws/redshift/docs/API_DeleteSnapshotSchedule"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteSnapshotSchedule"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DeleteSnapshotSchedule

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DeleteSnapshotSchedule
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteSnapshotSchedule
<a name="API_DeleteSnapshotSchedule"></a>

Deletes a snapshot schedule.

## Request Parameters
<a name="API_DeleteSnapshotSchedule_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ScheduleIdentifier **   
A unique identifier of the snapshot schedule to delete.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

## Errors
<a name="API_DeleteSnapshotSchedule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidClusterSnapshotScheduleState **   
The cluster snapshot schedule state is not valid.  
HTTP Status Code: 400

 ** SnapshotScheduleNotFound **   
We could not find the specified snapshot schedule.   
HTTP Status Code: 400

## Examples
<a name="API_DeleteSnapshotSchedule_Examples"></a>

### Example
<a name="API_DeleteSnapshotSchedule_Example_1"></a>

This example illustrates one usage of DeleteSnapshotSchedule.

#### Sample Request
<a name="API_DeleteSnapshotSchedule_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=DeleteSnapshotSchedule
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
<a name="API_DeleteSnapshotSchedule_Example_1_Response"></a>

```
<DeleteSnapshotScheduleResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <ResponseMetadata>
    <RequestId>165cd56f-283d-11ea-a940-1b28a85fd753</RequestId>
  </ResponseMetadata>
</DeleteSnapshotScheduleResponse>
```

## See Also
<a name="API_DeleteSnapshotSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DeleteSnapshotSchedule) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DeleteSnapshotSchedule) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DeleteSnapshotSchedule) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DeleteSnapshotSchedule) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DeleteSnapshotSchedule) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DeleteSnapshotSchedule) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DeleteSnapshotSchedule) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DeleteSnapshotSchedule) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DeleteSnapshotSchedule) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DeleteSnapshotSchedule) 