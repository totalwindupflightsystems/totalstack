---
id: "@specs/aws/rds/docs/API_DBClusterSnapshotAttributesResult"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DBClusterSnapshotAttributesResult"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DBClusterSnapshotAttributesResult

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DBClusterSnapshotAttributesResult
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DBClusterSnapshotAttributesResult
<a name="API_DBClusterSnapshotAttributesResult"></a>

Contains the results of a successful call to the `DescribeDBClusterSnapshotAttributes` API action.

Manual DB cluster snapshot attributes are used to authorize other AWS accounts to copy or restore a manual DB cluster snapshot. For more information, see the `ModifyDBClusterSnapshotAttribute` API action.

## Contents
<a name="API_DBClusterSnapshotAttributesResult_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** DBClusterSnapshotAttributes.DBClusterSnapshotAttribute.N **   
The list of attributes and values for the manual DB cluster snapshot.  
Type: Array of [DBClusterSnapshotAttribute](API_DBClusterSnapshotAttribute.md) objects  
Required: No

 ** DBClusterSnapshotIdentifier **   
The identifier of the manual DB cluster snapshot that the attributes apply to.  
Type: String  
Required: No

## See Also
<a name="API_DBClusterSnapshotAttributesResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DBClusterSnapshotAttributesResult) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DBClusterSnapshotAttributesResult) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DBClusterSnapshotAttributesResult) 