---
id: "@specs/aws/docdb/docs/API_CopyDBClusterSnapshot"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CopyDBClusterSnapshot"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# CopyDBClusterSnapshot

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_CopyDBClusterSnapshot
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CopyDBClusterSnapshot
<a name="API_CopyDBClusterSnapshot"></a>

Copies a snapshot of a cluster.

To copy a cluster snapshot from a shared manual cluster snapshot, `SourceDBClusterSnapshotIdentifier` must be the Amazon Resource Name (ARN) of the shared cluster snapshot. You can only copy a shared DB cluster snapshot, whether encrypted or not, in the same AWS Region.

To cancel the copy operation after it is in progress, delete the target cluster snapshot identified by `TargetDBClusterSnapshotIdentifier` while that cluster snapshot is in the *copying* status.

## Request Parameters
<a name="API_CopyDBClusterSnapshot_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** SourceDBClusterSnapshotIdentifier **   
The identifier of the cluster snapshot to copy. This parameter is not case sensitive.  
Constraints:  
+ Must specify a valid cluster snapshot in the *available* state.
+ If the source cluster snapshot is in the same AWS Region as the copy, specify a valid snapshot identifier.
+ If the source cluster snapshot is in a different AWS Region or owned by another AWS account, specify the snapshot ARN.
Example: `my-cluster-snapshot1`   
Type: String  
Required: Yes

 ** TargetDBClusterSnapshotIdentifier **   
The identifier of the new cluster snapshot to create from the source cluster snapshot. This parameter is not case sensitive.  
Constraints:  
+ Must contain from 1 to 63 letters, numbers, or hyphens. 
+ The first character must be a letter.
+ Cannot end with a hyphen or contain two consecutive hyphens. 
Example: `my-cluster-snapshot2`   
Type: String  
Required: Yes

 ** CopyTags **   
Set to `true` to copy all tags from the source cluster snapshot to the target cluster snapshot, and otherwise `false`. The default is `false`.  
Type: Boolean  
Required: No

 ** KmsKeyId **   
The AWS KMS key ID for an encrypted cluster snapshot. The AWS KMS key ID is the Amazon Resource Name (ARN), AWS KMS key identifier, or the AWS KMS key alias for the AWS KMS encryption key.   
If you copy an encrypted cluster snapshot from your AWS account, you can specify a value for `KmsKeyId` to encrypt the copy with a new AWS KMS encryption key. If you don't specify a value for `KmsKeyId`, then the copy of the cluster snapshot is encrypted with the same AWS KMS key as the source cluster snapshot.  
If you copy an encrypted cluster snapshot that is shared from another AWS account, then you must specify a value for `KmsKeyId`.  
To copy an encrypted cluster snapshot to another AWS Region, set `KmsKeyId` to the AWS KMS key ID that you want to use to encrypt the copy of the cluster snapshot in the destination Region. AWS KMS encryption keys are specific to the AWS Region that they are created in, and you can't use encryption keys from one AWS Region in another AWS Region.  
If you copy an unencrypted cluster snapshot and specify a value for the `KmsKeyId` parameter, an error is returned.  
Type: String  
Required: No

 ** PreSignedUrl **   
The URL that contains a Signature Version 4 signed request for the`CopyDBClusterSnapshot` API action in the AWS Region that contains the source cluster snapshot to copy. You must use the `PreSignedUrl` parameter when copying a cluster snapshot from another AWS Region.  
If you are using an AWS SDK tool or the AWS CLI, you can specify `SourceRegion` (or `--source-region` for the AWS CLI) instead of specifying `PreSignedUrl` manually. Specifying `SourceRegion` autogenerates a pre-signed URL that is a valid request for the operation that can be executed in the source AWS Region.  
The presigned URL must be a valid request for the `CopyDBClusterSnapshot` API action that can be executed in the source AWS Region that contains the cluster snapshot to be copied. The presigned URL request must contain the following parameter values:  
+  `SourceRegion` - The ID of the region that contains the snapshot to be copied.
+  `SourceDBClusterSnapshotIdentifier` - The identifier for the the encrypted cluster snapshot to be copied. This identifier must be in the Amazon Resource Name (ARN) format for the source AWS Region. For example, if you are copying an encrypted cluster snapshot from the us-east-1 AWS Region, then your `SourceDBClusterSnapshotIdentifier` looks something like the following: `arn:aws:rds:us-east-1:12345678012:sample-cluster:sample-cluster-snapshot`.
+  `TargetDBClusterSnapshotIdentifier` - The identifier for the new cluster snapshot to be created. This parameter isn't case sensitive.
Type: String  
Required: No

 **Tags.Tag.N**   
The tags to be assigned to the cluster snapshot.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## Response Elements
<a name="API_CopyDBClusterSnapshot_ResponseElements"></a>

The following element is returned by the service.

 ** DBClusterSnapshot **   
Detailed information about a cluster snapshot.   
Type: [DBClusterSnapshot](API_DBClusterSnapshot.md) object

## Errors
<a name="API_CopyDBClusterSnapshot_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterSnapshotAlreadyExistsFault **   
You already have a cluster snapshot with the given identifier.  
HTTP Status Code: 400

 ** DBClusterSnapshotNotFoundFault **   
 `DBClusterSnapshotIdentifier` doesn't refer to an existing cluster snapshot.   
HTTP Status Code: 404

 ** InvalidDBClusterSnapshotStateFault **   
The provided value isn't a valid cluster snapshot state.  
HTTP Status Code: 400

 ** InvalidDBClusterStateFault **   
The cluster isn't in a valid state.  
HTTP Status Code: 400

 ** KMSKeyNotAccessibleFault **   
An error occurred when accessing an AWS KMS key.  
HTTP Status Code: 400

 ** SnapshotQuotaExceeded **   
The request would cause you to exceed the allowed number of snapshots.  
HTTP Status Code: 400

## See Also
<a name="API_CopyDBClusterSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/docdb-2014-10-31/CopyDBClusterSnapshot) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/docdb-2014-10-31/CopyDBClusterSnapshot) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/CopyDBClusterSnapshot) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/docdb-2014-10-31/CopyDBClusterSnapshot) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/CopyDBClusterSnapshot) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/docdb-2014-10-31/CopyDBClusterSnapshot) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/docdb-2014-10-31/CopyDBClusterSnapshot) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/docdb-2014-10-31/CopyDBClusterSnapshot) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/docdb-2014-10-31/CopyDBClusterSnapshot) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/CopyDBClusterSnapshot) 