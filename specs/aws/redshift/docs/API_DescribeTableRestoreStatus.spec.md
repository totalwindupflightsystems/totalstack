---
id: "@specs/aws/redshift/docs/API_DescribeTableRestoreStatus"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeTableRestoreStatus"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DescribeTableRestoreStatus

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DescribeTableRestoreStatus
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeTableRestoreStatus
<a name="API_DescribeTableRestoreStatus"></a>

Lists the status of one or more table restore requests made using the [RestoreTableFromClusterSnapshot](API_RestoreTableFromClusterSnapshot.md) API action. If you don't specify a value for the `TableRestoreRequestId` parameter, then `DescribeTableRestoreStatus` returns the status of all table restore requests ordered by the date and time of the request in ascending order. Otherwise `DescribeTableRestoreStatus` returns the status of the table specified by `TableRestoreRequestId`.

## Request Parameters
<a name="API_DescribeTableRestoreStatus_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ClusterIdentifier **   
The Amazon Redshift cluster that the table is being restored to.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Marker **   
An optional pagination token provided by a previous `DescribeTableRestoreStatus` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by the `MaxRecords` parameter.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** MaxRecords **   
The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.  
Type: Integer  
Required: No

 ** TableRestoreRequestId **   
The identifier of the table restore request to return status for. If you don't specify a `TableRestoreRequestId` value, then `DescribeTableRestoreStatus` returns the status of all in-progress table restore requests.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

## Response Elements
<a name="API_DescribeTableRestoreStatus_ResponseElements"></a>

The following elements are returned by the service.

 ** Marker **   
A pagination token that can be used in a subsequent [DescribeTableRestoreStatus](#API_DescribeTableRestoreStatus) request.  
Type: String  
Length Constraints: Maximum length of 2147483647.

 **TableRestoreStatusDetails.TableRestoreStatus.N**   
A list of status details for one or more table restore requests.  
Type: Array of [TableRestoreStatus](API_TableRestoreStatus.md) objects

## Errors
<a name="API_DescribeTableRestoreStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterNotFound **   
The `ClusterIdentifier` parameter does not refer to an existing cluster.   
HTTP Status Code: 404

 ** TableRestoreNotFoundFault **   
The specified `TableRestoreRequestId` value was not found.  
HTTP Status Code: 400

## Examples
<a name="API_DescribeTableRestoreStatus_Examples"></a>

### Example
<a name="API_DescribeTableRestoreStatus_Example_1"></a>

This example illustrates one usage of DescribeTableRestoreStatus.

#### Sample Request
<a name="API_DescribeTableRestoreStatus_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=DescribeTableRestoreStatus
&ClusterIdentifier=mycluster
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_DescribeTableRestoreStatus_Example_1_Response"></a>

```
<DescribeTableRestoreStatusResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <DescribeTableRestoreStatusResult>
    <TableRestoreStatusDetails>
      <TableRestoreStatus>
        <NewTableName>mytable-clone</NewTableName>
        <ClusterIdentifier>mycluster</ClusterIdentifier>
        <SnapshotIdentifier>mysnapshotid</SnapshotIdentifier>
        <RequestTime>2019-12-27T18:22:12.257Z</RequestTime>
        <SourceTableName>mytable</SourceTableName>
        <SourceDatabaseName>dev</SourceDatabaseName>
        <TableRestoreRequestId>z1116630-0e80-46f4-ba86-bd9670411ebd</TableRestoreRequestId>
        <TargetDatabaseName>dev</TargetDatabaseName>
        <SourceSchemaName>public</SourceSchemaName>
        <TargetSchemaName>public</TargetSchemaName>
        <Status>IN_PROGRESS</Status>
      </TableRestoreStatus>
    </TableRestoreStatusDetails>
  </DescribeTableRestoreStatusResult>
  <ResponseMetadata>
    <RequestId>3a0cf005-28d6-11ea-9caa-c956bec1ce87</RequestId>
  </ResponseMetadata>
</DescribeTableRestoreStatusResponse>
```

## See Also
<a name="API_DescribeTableRestoreStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DescribeTableRestoreStatus) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DescribeTableRestoreStatus) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DescribeTableRestoreStatus) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DescribeTableRestoreStatus) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DescribeTableRestoreStatus) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DescribeTableRestoreStatus) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DescribeTableRestoreStatus) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DescribeTableRestoreStatus) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DescribeTableRestoreStatus) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DescribeTableRestoreStatus) 