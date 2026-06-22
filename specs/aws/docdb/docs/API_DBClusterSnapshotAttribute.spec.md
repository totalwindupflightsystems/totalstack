---
id: "@specs/aws/docdb/docs/API_DBClusterSnapshotAttribute"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DBClusterSnapshotAttribute"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# DBClusterSnapshotAttribute

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_DBClusterSnapshotAttribute
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DBClusterSnapshotAttribute
<a name="API_DBClusterSnapshotAttribute"></a>

Contains the name and values of a manual cluster snapshot attribute.

Manual cluster snapshot attributes are used to authorize other AWS accounts to restore a manual cluster snapshot.

## Contents
<a name="API_DBClusterSnapshotAttribute_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** AttributeName **   
The name of the manual cluster snapshot attribute.  
The attribute named `restore` refers to the list of AWS accounts that have permission to copy or restore the manual cluster snapshot.  
Type: String  
Required: No

 ** AttributeValues.AttributeValue.N **   
The values for the manual cluster snapshot attribute.  
If the `AttributeName` field is set to `restore`, then this element returns a list of IDs of the AWS accounts that are authorized to copy or restore the manual cluster snapshot. If a value of `all` is in the list, then the manual cluster snapshot is public and available for any AWS account to copy or restore.  
Type: Array of strings  
Required: No

## See Also
<a name="API_DBClusterSnapshotAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/DBClusterSnapshotAttribute) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/DBClusterSnapshotAttribute) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/DBClusterSnapshotAttribute) 