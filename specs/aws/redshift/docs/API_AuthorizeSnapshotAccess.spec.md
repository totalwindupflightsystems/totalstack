---
id: "@specs/aws/redshift/docs/API_AuthorizeSnapshotAccess"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AuthorizeSnapshotAccess"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# AuthorizeSnapshotAccess

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_AuthorizeSnapshotAccess
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AuthorizeSnapshotAccess
<a name="API_AuthorizeSnapshotAccess"></a>

Authorizes the specified AWS account to restore the specified snapshot.

 For more information about working with snapshots, go to [Amazon Redshift Snapshots](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html) in the *Amazon Redshift Cluster Management Guide*.

## Request Parameters
<a name="API_AuthorizeSnapshotAccess_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AccountWithRestoreAccess **   
The identifier of the AWS account authorized to restore the specified snapshot.  
To share a snapshot with Support, specify amazon-redshift-support.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** SnapshotArn **   
The Amazon Resource Name (ARN) of the snapshot to authorize access to.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** SnapshotClusterIdentifier **   
The identifier of the cluster the snapshot was created from.  
+  *If the snapshot to access doesn't exist and the associated IAM policy doesn't allow access to all (\*) snapshots* - This parameter is required. Otherwise, permissions aren't available to check if the snapshot exists.
+  *If the snapshot to access exists* - This parameter isn't required. Redshift can retrieve the cluster identifier and use it to validate snapshot authorization.
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** SnapshotIdentifier **   
The identifier of the snapshot the account is authorized to restore.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

## Response Elements
<a name="API_AuthorizeSnapshotAccess_ResponseElements"></a>

The following element is returned by the service.

 ** Snapshot **   
Describes a snapshot.  
Type: [Snapshot](API_Snapshot.md) object

## Errors
<a name="API_AuthorizeSnapshotAccess_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthorizationAlreadyExists **   
The specified CIDR block or EC2 security group is already authorized for the specified cluster security group.  
HTTP Status Code: 400

 ** AuthorizationQuotaExceeded **   
The authorization quota for the cluster security group has been reached.  
HTTP Status Code: 400

 ** ClusterSnapshotNotFound **   
The snapshot identifier does not refer to an existing cluster snapshot.  
HTTP Status Code: 404

 ** DependentServiceRequestThrottlingFault **   
The request cannot be completed because a dependent service is throttling requests made by Amazon Redshift on your behalf. Wait and retry the request.  
HTTP Status Code: 400

 ** InvalidClusterSnapshotState **   
The specified cluster snapshot is not in the `available` state, or other accounts are authorized to access the snapshot.   
HTTP Status Code: 400

 ** LimitExceededFault **   
The encryption key has exceeded its grant limit in AWS KMS.  
HTTP Status Code: 400

 ** UnsupportedOperation **   
The requested operation isn't supported.  
HTTP Status Code: 400

## See Also
<a name="API_AuthorizeSnapshotAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/AuthorizeSnapshotAccess) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/AuthorizeSnapshotAccess) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/AuthorizeSnapshotAccess) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/AuthorizeSnapshotAccess) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/AuthorizeSnapshotAccess) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/AuthorizeSnapshotAccess) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/AuthorizeSnapshotAccess) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/AuthorizeSnapshotAccess) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/AuthorizeSnapshotAccess) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/AuthorizeSnapshotAccess) 