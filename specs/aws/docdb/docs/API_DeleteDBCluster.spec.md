---
id: "@specs/aws/docdb/docs/API_DeleteDBCluster"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteDBCluster"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# DeleteDBCluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_DeleteDBCluster
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteDBCluster
<a name="API_DeleteDBCluster"></a>

Deletes a previously provisioned cluster. When you delete a cluster, all automated backups for that cluster are deleted and can't be recovered. Manual DB cluster snapshots of the specified cluster are not deleted.



## Request Parameters
<a name="API_DeleteDBCluster_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterIdentifier **   
The cluster identifier for the cluster to be deleted. This parameter isn't case sensitive.  
Constraints:  
+ Must match an existing `DBClusterIdentifier`.
Type: String  
Required: Yes

 ** FinalDBSnapshotIdentifier **   
 The cluster snapshot identifier of the new cluster snapshot created when `SkipFinalSnapshot` is set to `false`.   
 Specifying this parameter and also setting the `SkipFinalShapshot` parameter to `true` results in an error. 
Constraints:  
+ Must be from 1 to 255 letters, numbers, or hyphens.
+ The first character must be a letter.
+ Cannot end with a hyphen or contain two consecutive hyphens.
Type: String  
Required: No

 ** SkipFinalSnapshot **   
 Determines whether a final cluster snapshot is created before the cluster is deleted. If `true` is specified, no cluster snapshot is created. If `false` is specified, a cluster snapshot is created before the DB cluster is deleted.   
If `SkipFinalSnapshot` is `false`, you must specify a `FinalDBSnapshotIdentifier` parameter.
Default: `false`   
Type: Boolean  
Required: No

## Response Elements
<a name="API_DeleteDBCluster_ResponseElements"></a>

The following element is returned by the service.

 ** DBCluster **   
Detailed information about a cluster.   
Type: [DBCluster](API_DBCluster.md) object

## Errors
<a name="API_DeleteDBCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterNotFoundFault **   
 `DBClusterIdentifier` doesn't refer to an existing cluster.   
HTTP Status Code: 404

 ** DBClusterSnapshotAlreadyExistsFault **   
You already have a cluster snapshot with the given identifier.  
HTTP Status Code: 400

 ** InvalidDBClusterSnapshotStateFault **   
The provided value isn't a valid cluster snapshot state.  
HTTP Status Code: 400

 ** InvalidDBClusterStateFault **   
The cluster isn't in a valid state.  
HTTP Status Code: 400

 ** SnapshotQuotaExceeded **   
The request would cause you to exceed the allowed number of snapshots.  
HTTP Status Code: 400

## See Also
<a name="API_DeleteDBCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/docdb-2014-10-31/DeleteDBCluster) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/docdb-2014-10-31/DeleteDBCluster) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/DeleteDBCluster) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/docdb-2014-10-31/DeleteDBCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/DeleteDBCluster) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/docdb-2014-10-31/DeleteDBCluster) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/docdb-2014-10-31/DeleteDBCluster) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/docdb-2014-10-31/DeleteDBCluster) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/docdb-2014-10-31/DeleteDBCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/DeleteDBCluster) 