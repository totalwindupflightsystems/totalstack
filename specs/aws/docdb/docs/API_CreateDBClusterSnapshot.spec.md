---
id: "@specs/aws/docdb/docs/API_CreateDBClusterSnapshot"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateDBClusterSnapshot"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# CreateDBClusterSnapshot

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_CreateDBClusterSnapshot
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateDBClusterSnapshot
<a name="API_CreateDBClusterSnapshot"></a>

Creates a snapshot of a cluster. 

## Request Parameters
<a name="API_CreateDBClusterSnapshot_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterIdentifier **   
The identifier of the cluster to create a snapshot for. This parameter is not case sensitive.  
Constraints:  
+ Must match the identifier of an existing `DBCluster`.
Example: `my-cluster`   
Type: String  
Required: Yes

 ** DBClusterSnapshotIdentifier **   
The identifier of the cluster snapshot. This parameter is stored as a lowercase string.  
Constraints:  
+ Must contain from 1 to 63 letters, numbers, or hyphens.
+ The first character must be a letter.
+ Cannot end with a hyphen or contain two consecutive hyphens. 
Example: `my-cluster-snapshot1`   
Type: String  
Required: Yes

 **Tags.Tag.N**   
The tags to be assigned to the cluster snapshot.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## Response Elements
<a name="API_CreateDBClusterSnapshot_ResponseElements"></a>

The following element is returned by the service.

 ** DBClusterSnapshot **   
Detailed information about a cluster snapshot.   
Type: [DBClusterSnapshot](API_DBClusterSnapshot.md) object

## Errors
<a name="API_CreateDBClusterSnapshot_Errors"></a>

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
<a name="API_CreateDBClusterSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/docdb-2014-10-31/CreateDBClusterSnapshot) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/docdb-2014-10-31/CreateDBClusterSnapshot) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/CreateDBClusterSnapshot) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/docdb-2014-10-31/CreateDBClusterSnapshot) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/CreateDBClusterSnapshot) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/docdb-2014-10-31/CreateDBClusterSnapshot) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/docdb-2014-10-31/CreateDBClusterSnapshot) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/docdb-2014-10-31/CreateDBClusterSnapshot) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/docdb-2014-10-31/CreateDBClusterSnapshot) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/CreateDBClusterSnapshot) 