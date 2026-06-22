---
id: "@specs/aws/docdb/docs/API_DescribeDBClusterSnapshotAttributes"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeDBClusterSnapshotAttributes"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# DescribeDBClusterSnapshotAttributes

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_DescribeDBClusterSnapshotAttributes
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeDBClusterSnapshotAttributes
<a name="API_DescribeDBClusterSnapshotAttributes"></a>

Returns a list of cluster snapshot attribute names and values for a manual DB cluster snapshot.

When you share snapshots with other AWS accounts, `DescribeDBClusterSnapshotAttributes` returns the `restore` attribute and a list of IDs for the AWS accounts that are authorized to copy or restore the manual cluster snapshot. If `all` is included in the list of values for the `restore` attribute, then the manual cluster snapshot is public and can be copied or restored by all AWS accounts.

## Request Parameters
<a name="API_DescribeDBClusterSnapshotAttributes_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterSnapshotIdentifier **   
The identifier for the cluster snapshot to describe the attributes for.  
Type: String  
Required: Yes

## Response Elements
<a name="API_DescribeDBClusterSnapshotAttributes_ResponseElements"></a>

The following element is returned by the service.

 ** DBClusterSnapshotAttributesResult **   
Detailed information about the attributes that are associated with a cluster snapshot.  
Type: [DBClusterSnapshotAttributesResult](API_DBClusterSnapshotAttributesResult.md) object

## Errors
<a name="API_DescribeDBClusterSnapshotAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterSnapshotNotFoundFault **   
 `DBClusterSnapshotIdentifier` doesn't refer to an existing cluster snapshot.   
HTTP Status Code: 404

## See Also
<a name="API_DescribeDBClusterSnapshotAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/docdb-2014-10-31/DescribeDBClusterSnapshotAttributes) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/docdb-2014-10-31/DescribeDBClusterSnapshotAttributes) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/DescribeDBClusterSnapshotAttributes) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/docdb-2014-10-31/DescribeDBClusterSnapshotAttributes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/DescribeDBClusterSnapshotAttributes) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/docdb-2014-10-31/DescribeDBClusterSnapshotAttributes) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/docdb-2014-10-31/DescribeDBClusterSnapshotAttributes) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/docdb-2014-10-31/DescribeDBClusterSnapshotAttributes) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/docdb-2014-10-31/DescribeDBClusterSnapshotAttributes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/DescribeDBClusterSnapshotAttributes) 