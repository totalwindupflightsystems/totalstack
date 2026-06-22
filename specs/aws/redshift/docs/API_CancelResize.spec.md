---
id: "@specs/aws/redshift/docs/API_CancelResize"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CancelResize"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# CancelResize

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_CancelResize
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CancelResize
<a name="API_CancelResize"></a>

Cancels a resize operation for a cluster.

## Request Parameters
<a name="API_CancelResize_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ClusterIdentifier **   
The unique identifier for the cluster that you want to cancel a resize operation for.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

## Response Elements
<a name="API_CancelResize_ResponseElements"></a>

The following elements are returned by the service.

 ** AvgResizeRateInMegaBytesPerSecond **   
The average rate of the resize operation over the last few minutes, measured in megabytes per second. After the resize operation completes, this value shows the average rate of the entire resize operation.  
Type: Double

 ** DataTransferProgressPercent **   
The percent of data transferred from source cluster to target cluster.  
Type: Double

 ** ElapsedTimeInSeconds **   
The amount of seconds that have elapsed since the resize operation began. After the resize operation completes, this value shows the total actual time, in seconds, for the resize operation.  
Type: Long

 ** EstimatedTimeToCompletionInSeconds **   
The estimated time remaining, in seconds, until the resize operation is complete. This value is calculated based on the average resize rate and the estimated amount of data remaining to be processed. Once the resize operation is complete, this value will be 0.  
Type: Long

 **ImportTablesCompleted.member.N**   
The names of tables that have been completely imported .  
Valid Values: List of table names.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.

 **ImportTablesInProgress.member.N**   
The names of tables that are being currently imported.  
Valid Values: List of table names.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.

 **ImportTablesNotStarted.member.N**   
The names of tables that have not been yet imported.  
Valid Values: List of table names  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.

 ** Message **   
An optional string to provide additional details about the resize action.  
Type: String  
Length Constraints: Maximum length of 2147483647.

 ** ProgressInMegaBytes **   
While the resize operation is in progress, this value shows the current amount of data, in megabytes, that has been processed so far. When the resize operation is complete, this value shows the total amount of data, in megabytes, on the cluster, which may be more or less than TotalResizeDataInMegaBytes (the estimated total amount of data before resize).  
Type: Long

 ** ResizeType **   
An enum with possible values of `ClassicResize` and `ElasticResize`. These values describe the type of resize operation being performed.   
Type: String  
Length Constraints: Maximum length of 2147483647.

 ** Status **   
The status of the resize operation.  
Valid Values: `NONE` \| `IN_PROGRESS` \| `FAILED` \| `SUCCEEDED` \| `CANCELLING`   
Type: String  
Length Constraints: Maximum length of 2147483647.

 ** TargetClusterType **   
The cluster type after the resize operation is complete.  
Valid Values: `multi-node` \| `single-node`   
Type: String  
Length Constraints: Maximum length of 2147483647.

 ** TargetEncryptionType **   
The type of encryption for the cluster after the resize is complete.  
Possible values are `KMS` and `None`.   
Type: String  
Length Constraints: Maximum length of 2147483647.

 ** TargetNodeType **   
The node type that the cluster will have after the resize operation is complete.  
Type: String  
Length Constraints: Maximum length of 2147483647.

 ** TargetNumberOfNodes **   
The number of nodes that the cluster will have after the resize operation is complete.  
Type: Integer

 ** TotalResizeDataInMegaBytes **   
The estimated total amount of data, in megabytes, on the cluster before the resize operation began.  
Type: Long

## Errors
<a name="API_CancelResize_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterNotFound **   
The `ClusterIdentifier` parameter does not refer to an existing cluster.   
HTTP Status Code: 404

 ** InvalidClusterState **   
The specified cluster is not in the `available` state.   
HTTP Status Code: 400

 ** ResizeNotFound **   
A resize operation for the specified cluster is not found.  
HTTP Status Code: 404

 ** UnsupportedOperation **   
The requested operation isn't supported.  
HTTP Status Code: 400

## Examples
<a name="API_CancelResize_Examples"></a>

### Example
<a name="API_CancelResize_Example_1"></a>

This example illustrates one usage of CancelResize.

#### Sample Request
<a name="API_CancelResize_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=CancelResize
&ClusterIdentifier=mycluster
&ManualSnapshotRetentionPeriod=30
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_CancelResize_Example_1_Response"></a>

```
<CancelResizeResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <CancelResizeResult>
    <TargetNodeType>dc2.large</TargetNodeType>
    <TargetEncryptionType>NONE</TargetEncryptionType>
    <TargetClusterType>single-node</TargetClusterType>
    <ResizeType>ClassicResize</ResizeType>
    <Status>CANCELLING</Status>
  </CancelResizeResult>
  <ResponseMetadata>
    <RequestId>2bb73dd4-282d-11ea-9caa-c956bec1ce87</RequestId>
  </ResponseMetadata>
</CancelResizeResponse>
```

## See Also
<a name="API_CancelResize_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/CancelResize) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/CancelResize) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/CancelResize) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/CancelResize) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/CancelResize) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/CancelResize) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/CancelResize) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/CancelResize) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/CancelResize) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/CancelResize) 