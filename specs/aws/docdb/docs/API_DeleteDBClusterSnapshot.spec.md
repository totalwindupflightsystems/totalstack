---
id: "@specs/aws/docdb/docs/API_DeleteDBClusterSnapshot"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteDBClusterSnapshot"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# DeleteDBClusterSnapshot

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_DeleteDBClusterSnapshot
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteDBClusterSnapshot
<a name="API_DeleteDBClusterSnapshot"></a>

Deletes a cluster snapshot. If the snapshot is being copied, the copy operation is terminated.

**Note**  
The cluster snapshot must be in the `available` state to be deleted.

## Request Parameters
<a name="API_DeleteDBClusterSnapshot_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterSnapshotIdentifier **   
The identifier of the cluster snapshot to delete.  
Constraints: Must be the name of an existing cluster snapshot in the `available` state.  
Type: String  
Required: Yes

## Response Elements
<a name="API_DeleteDBClusterSnapshot_ResponseElements"></a>

The following element is returned by the service.

 ** DBClusterSnapshot **   
Detailed information about a cluster snapshot.   
Type: [DBClusterSnapshot](API_DBClusterSnapshot.md) object

## Errors
<a name="API_DeleteDBClusterSnapshot_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterSnapshotNotFoundFault **   
 `DBClusterSnapshotIdentifier` doesn't refer to an existing cluster snapshot.   
HTTP Status Code: 404

 ** InvalidDBClusterSnapshotStateFault **   
The provided value isn't a valid cluster snapshot state.  
HTTP Status Code: 400

## See Also
<a name="API_DeleteDBClusterSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/docdb-2014-10-31/DeleteDBClusterSnapshot) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/docdb-2014-10-31/DeleteDBClusterSnapshot) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/DeleteDBClusterSnapshot) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/docdb-2014-10-31/DeleteDBClusterSnapshot) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/DeleteDBClusterSnapshot) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/docdb-2014-10-31/DeleteDBClusterSnapshot) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/docdb-2014-10-31/DeleteDBClusterSnapshot) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/docdb-2014-10-31/DeleteDBClusterSnapshot) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/docdb-2014-10-31/DeleteDBClusterSnapshot) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/DeleteDBClusterSnapshot) 