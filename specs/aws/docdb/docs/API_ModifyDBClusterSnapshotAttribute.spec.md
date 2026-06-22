---
id: "@specs/aws/docdb/docs/API_ModifyDBClusterSnapshotAttribute"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ModifyDBClusterSnapshotAttribute"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# ModifyDBClusterSnapshotAttribute

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_ModifyDBClusterSnapshotAttribute
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ModifyDBClusterSnapshotAttribute
<a name="API_ModifyDBClusterSnapshotAttribute"></a>

Adds an attribute and values to, or removes an attribute and values from, a manual cluster snapshot.

To share a manual cluster snapshot with other AWS accounts, specify `restore` as the `AttributeName`, and use the `ValuesToAdd` parameter to add a list of IDs of the AWS accounts that are authorized to restore the manual cluster snapshot. Use the value `all` to make the manual cluster snapshot public, which means that it can be copied or restored by all AWS accounts. Do not add the `all` value for any manual cluster snapshots that contain private information that you don't want available to all AWS accounts. If a manual cluster snapshot is encrypted, it can be shared, but only by specifying a list of authorized AWS account IDs for the `ValuesToAdd` parameter. You can't use `all` as a value for that parameter in this case.

## Request Parameters
<a name="API_ModifyDBClusterSnapshotAttribute_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AttributeName **   
The name of the cluster snapshot attribute to modify.  
To manage authorization for other AWS accounts to copy or restore a manual cluster snapshot, set this value to `restore`.  
Type: String  
Required: Yes

 ** DBClusterSnapshotIdentifier **   
The identifier for the cluster snapshot to modify the attributes for.  
Type: String  
Required: Yes

 **ValuesToAdd.AttributeValue.N**   
A list of cluster snapshot attributes to add to the attribute specified by `AttributeName`.  
To authorize other AWS accounts to copy or restore a manual cluster snapshot, set this list to include one or more AWS account IDs. To make the manual cluster snapshot restorable by any AWS account, set it to `all`. Do not add the `all` value for any manual cluster snapshots that contain private information that you don't want to be available to all AWS accounts.  
Type: Array of strings  
Required: No

 **ValuesToRemove.AttributeValue.N**   
A list of cluster snapshot attributes to remove from the attribute specified by `AttributeName`.  
To remove authorization for other AWS accounts to copy or restore a manual cluster snapshot, set this list to include one or more AWS account identifiers. To remove authorization for any AWS account to copy or restore the cluster snapshot, set it to `all` . If you specify `all`, an AWS account whose account ID is explicitly added to the `restore` attribute can still copy or restore a manual cluster snapshot.  
Type: Array of strings  
Required: No

## Response Elements
<a name="API_ModifyDBClusterSnapshotAttribute_ResponseElements"></a>

The following element is returned by the service.

 ** DBClusterSnapshotAttributesResult **   
Detailed information about the attributes that are associated with a cluster snapshot.  
Type: [DBClusterSnapshotAttributesResult](API_DBClusterSnapshotAttributesResult.md) object

## Errors
<a name="API_ModifyDBClusterSnapshotAttribute_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterSnapshotNotFoundFault **   
 `DBClusterSnapshotIdentifier` doesn't refer to an existing cluster snapshot.   
HTTP Status Code: 404

 ** InvalidDBClusterSnapshotStateFault **   
The provided value isn't a valid cluster snapshot state.  
HTTP Status Code: 400

 ** SharedSnapshotQuotaExceeded **   
You have exceeded the maximum number of accounts that you can share a manual DB snapshot with.   
HTTP Status Code: 400

## See Also
<a name="API_ModifyDBClusterSnapshotAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/docdb-2014-10-31/ModifyDBClusterSnapshotAttribute) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/docdb-2014-10-31/ModifyDBClusterSnapshotAttribute) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/ModifyDBClusterSnapshotAttribute) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/docdb-2014-10-31/ModifyDBClusterSnapshotAttribute) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/ModifyDBClusterSnapshotAttribute) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/docdb-2014-10-31/ModifyDBClusterSnapshotAttribute) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/docdb-2014-10-31/ModifyDBClusterSnapshotAttribute) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/docdb-2014-10-31/ModifyDBClusterSnapshotAttribute) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/docdb-2014-10-31/ModifyDBClusterSnapshotAttribute) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/ModifyDBClusterSnapshotAttribute) 