---
id: "@specs/aws/redshift/docs/API_ClusterSnapshotCopyStatus"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ClusterSnapshotCopyStatus"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# ClusterSnapshotCopyStatus

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_ClusterSnapshotCopyStatus
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ClusterSnapshotCopyStatus
<a name="API_ClusterSnapshotCopyStatus"></a>

Returns the destination region and retention period that are configured for cross-region snapshot copy.

## Contents
<a name="API_ClusterSnapshotCopyStatus_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** DestinationRegion **   
The destination region that snapshots are automatically copied to when cross-region snapshot copy is enabled.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ManualSnapshotRetentionPeriod **   
The number of days that automated snapshots are retained in the destination region after they are copied from a source region. If the value is -1, the manual snapshot is retained indefinitely.   
The value must be either -1 or an integer between 1 and 3,653.  
Type: Integer  
Required: No

 ** RetentionPeriod **   
The number of days that automated snapshots are retained in the destination region after they are copied from a source region.  
Type: Long  
Required: No

 ** SnapshotCopyGrantName **   
The name of the snapshot copy grant.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

## See Also
<a name="API_ClusterSnapshotCopyStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/ClusterSnapshotCopyStatus) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/ClusterSnapshotCopyStatus) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/ClusterSnapshotCopyStatus) 