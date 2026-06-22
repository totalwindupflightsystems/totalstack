---
id: "@specs/aws/redshift/docs/API_RestoreTableFromClusterSnapshot"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RestoreTableFromClusterSnapshot"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# RestoreTableFromClusterSnapshot

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_RestoreTableFromClusterSnapshot
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RestoreTableFromClusterSnapshot
<a name="API_RestoreTableFromClusterSnapshot"></a>

Creates a new table from a table in an Amazon Redshift cluster snapshot. You must create the new table within the Amazon Redshift cluster that the snapshot was taken from.

You cannot use `RestoreTableFromClusterSnapshot` to restore a table with the same name as an existing table in an Amazon Redshift cluster. That is, you cannot overwrite an existing table in a cluster with a restored table. If you want to replace your original table with a new, restored table, then rename or drop your original table before you call `RestoreTableFromClusterSnapshot`. When you have renamed your original table, then you can pass the original name of the table as the `NewTableName` parameter value in the call to `RestoreTableFromClusterSnapshot`. This way, you can replace the original table with the table created from the snapshot.

You can't use this operation to restore tables with [interleaved sort keys](https://docs.aws.amazon.com/redshift/latest/dg/t_Sorting_data.html#t_Sorting_data-interleaved).

## Request Parameters
<a name="API_RestoreTableFromClusterSnapshot_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ClusterIdentifier **   
The identifier of the Amazon Redshift cluster to restore the table to.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** NewTableName **   
The name of the table to create as a result of the current request.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** SnapshotIdentifier **   
The identifier of the snapshot to restore the table from. This snapshot must have been created from the Amazon Redshift cluster specified by the `ClusterIdentifier` parameter.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** SourceDatabaseName **   
The name of the source database that contains the table to restore from.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** SourceTableName **   
The name of the source table to restore from.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** EnableCaseSensitiveIdentifier **   
Indicates whether name identifiers for database, schema, and table are case sensitive. If `true`, the names are case sensitive. If `false` (default), the names are not case sensitive.  
Type: Boolean  
Required: No

 ** SourceSchemaName **   
The name of the source schema that contains the table to restore from. If you do not specify a `SourceSchemaName` value, the default is `public`.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** TargetDatabaseName **   
The name of the database to restore the table to.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** TargetSchemaName **   
The name of the schema to restore the table to.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

## Response Elements
<a name="API_RestoreTableFromClusterSnapshot_ResponseElements"></a>

The following element is returned by the service.

 ** TableRestoreStatus **   
Describes the status of a [RestoreTableFromClusterSnapshot](#API_RestoreTableFromClusterSnapshot) operation.  
Type: [TableRestoreStatus](API_TableRestoreStatus.md) object

## Errors
<a name="API_RestoreTableFromClusterSnapshot_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterNotFound **   
The `ClusterIdentifier` parameter does not refer to an existing cluster.   
HTTP Status Code: 404

 ** ClusterSnapshotNotFound **   
The snapshot identifier does not refer to an existing cluster snapshot.  
HTTP Status Code: 404

 ** InProgressTableRestoreQuotaExceededFault **   
You have exceeded the allowed number of table restore requests. Wait for your current table restore requests to complete before making a new request.  
HTTP Status Code: 400

 ** InvalidClusterSnapshotState **   
The specified cluster snapshot is not in the `available` state, or other accounts are authorized to access the snapshot.   
HTTP Status Code: 400

 ** InvalidClusterState **   
The specified cluster is not in the `available` state.   
HTTP Status Code: 400

 ** InvalidTableRestoreArgument **   
The value specified for the `sourceDatabaseName`, `sourceSchemaName`, or `sourceTableName` parameter, or a combination of these, doesn't exist in the snapshot.  
HTTP Status Code: 400

 ** UnsupportedOperation **   
The requested operation isn't supported.  
HTTP Status Code: 400

## Examples
<a name="API_RestoreTableFromClusterSnapshot_Examples"></a>

### Example
<a name="API_RestoreTableFromClusterSnapshot_Example_1"></a>

This example illustrates one usage of RestoreTableFromClusterSnapshot.

#### Sample Request
<a name="API_RestoreTableFromClusterSnapshot_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=RestoreTableFromClusterSnapshot
&ClusterIdentifier=mycluster
&SnapshotIdentifier=mysnapshotid
&SourceDatabaseName=dev
&SourceSchemaName=public
&SourceTableName=mytable
&TargetDatabaseName=dev
&TargetSchemaName=public
&NewTableName=mytable-clone
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_RestoreTableFromClusterSnapshot_Example_1_Response"></a>

```
<RestoreTableFromClusterSnapshotResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <RestoreTableFromClusterSnapshotResult>
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
      <Status>PENDING</Status>
    </TableRestoreStatus>
  </RestoreTableFromClusterSnapshotResult>
  <ResponseMetadata>
    <RequestId>cd0df3b1-28d5-11ea-a07c-5d44c0d19e91</RequestId>
  </ResponseMetadata>
</RestoreTableFromClusterSnapshotResponse>
```

## See Also
<a name="API_RestoreTableFromClusterSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/RestoreTableFromClusterSnapshot) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/RestoreTableFromClusterSnapshot) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/RestoreTableFromClusterSnapshot) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/RestoreTableFromClusterSnapshot) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/RestoreTableFromClusterSnapshot) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/RestoreTableFromClusterSnapshot) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/RestoreTableFromClusterSnapshot) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/RestoreTableFromClusterSnapshot) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/RestoreTableFromClusterSnapshot) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/RestoreTableFromClusterSnapshot) 