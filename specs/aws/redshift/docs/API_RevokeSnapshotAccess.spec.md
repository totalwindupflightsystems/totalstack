---
id: "@specs/aws/redshift/docs/API_RevokeSnapshotAccess"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RevokeSnapshotAccess"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# RevokeSnapshotAccess

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_RevokeSnapshotAccess
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RevokeSnapshotAccess
<a name="API_RevokeSnapshotAccess"></a>

Removes the ability of the specified AWS account to restore the specified snapshot. If the account is currently restoring the snapshot, the restore will run to completion.

 For more information about working with snapshots, go to [Amazon Redshift Snapshots](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html) in the *Amazon Redshift Cluster Management Guide*.

## Request Parameters
<a name="API_RevokeSnapshotAccess_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AccountWithRestoreAccess **   
The identifier of the AWS account that can no longer restore the specified snapshot.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** SnapshotArn **   
The Amazon Resource Name (ARN) of the snapshot associated with the message to revoke access.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** SnapshotClusterIdentifier **   
The identifier of the cluster the snapshot was created from. This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than \* for the cluster name.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** SnapshotIdentifier **   
The identifier of the snapshot that the account can no longer access.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

## Response Elements
<a name="API_RevokeSnapshotAccess_ResponseElements"></a>

The following element is returned by the service.

 ** Snapshot **   
Describes a snapshot.  
Type: [Snapshot](API_Snapshot.md) object

## Errors
<a name="API_RevokeSnapshotAccess_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessToSnapshotDenied **   
The owner of the specified snapshot has not authorized your account to access the snapshot.  
HTTP Status Code: 400

 ** AuthorizationNotFound **   
The specified CIDR IP range or EC2 security group is not authorized for the specified cluster security group.  
HTTP Status Code: 404

 ** ClusterSnapshotNotFound **   
The snapshot identifier does not refer to an existing cluster snapshot.  
HTTP Status Code: 404

 ** UnsupportedOperation **   
The requested operation isn't supported.  
HTTP Status Code: 400

## See Also
<a name="API_RevokeSnapshotAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/RevokeSnapshotAccess) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/RevokeSnapshotAccess) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/RevokeSnapshotAccess) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/RevokeSnapshotAccess) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/RevokeSnapshotAccess) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/RevokeSnapshotAccess) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/RevokeSnapshotAccess) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/RevokeSnapshotAccess) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/RevokeSnapshotAccess) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/RevokeSnapshotAccess) 