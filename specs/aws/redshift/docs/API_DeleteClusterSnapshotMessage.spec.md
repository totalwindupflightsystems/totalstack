---
id: "@specs/aws/redshift/docs/API_DeleteClusterSnapshotMessage"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteClusterSnapshotMessage"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DeleteClusterSnapshotMessage

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DeleteClusterSnapshotMessage
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteClusterSnapshotMessage
<a name="API_DeleteClusterSnapshotMessage"></a>



## Contents
<a name="API_DeleteClusterSnapshotMessage_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** SnapshotIdentifier **   
The unique identifier of the manual snapshot to be deleted.  
Constraints: Must be the name of an existing snapshot that is in the `available`, `failed`, or `cancelled` state.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** SnapshotClusterIdentifier **   
The unique identifier of the cluster the snapshot was created from. This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than \* for the cluster name.  
Constraints: Must be the name of valid cluster.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

## See Also
<a name="API_DeleteClusterSnapshotMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DeleteClusterSnapshotMessage) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DeleteClusterSnapshotMessage) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DeleteClusterSnapshotMessage) 