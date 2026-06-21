---
id: "@specs/aws/rds/docs/API_DeleteDBClusterAutomatedBackup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteDBClusterAutomatedBackup"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DeleteDBClusterAutomatedBackup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DeleteDBClusterAutomatedBackup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteDBClusterAutomatedBackup
<a name="API_DeleteDBClusterAutomatedBackup"></a>

Deletes automated backups using the `DbClusterResourceId` value of the source DB cluster or the Amazon Resource Name (ARN) of the automated backups.

## Request Parameters
<a name="API_DeleteDBClusterAutomatedBackup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DbClusterResourceId **   
The identifier for the source DB cluster, which can't be changed and which is unique to an AWS Region.  
Type: String  
Required: Yes

## Response Elements
<a name="API_DeleteDBClusterAutomatedBackup_ResponseElements"></a>

The following element is returned by the service.

 ** DBClusterAutomatedBackup **   
An automated backup of a DB cluster. It consists of system backups, transaction logs, and the database cluster properties that existed at the time you deleted the source cluster.  
Type: [DBClusterAutomatedBackup](API_DBClusterAutomatedBackup.md) object

## Errors
<a name="API_DeleteDBClusterAutomatedBackup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterAutomatedBackupNotFoundFault **   
No automated backup for this DB cluster was found.  
HTTP Status Code: 404

 ** InvalidDBClusterAutomatedBackupStateFault **   
The automated backup is in an invalid state. For example, this automated backup is associated with an active cluster.  
HTTP Status Code: 400

## See Also
<a name="API_DeleteDBClusterAutomatedBackup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DeleteDBClusterAutomatedBackup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DeleteDBClusterAutomatedBackup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DeleteDBClusterAutomatedBackup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DeleteDBClusterAutomatedBackup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DeleteDBClusterAutomatedBackup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DeleteDBClusterAutomatedBackup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DeleteDBClusterAutomatedBackup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DeleteDBClusterAutomatedBackup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DeleteDBClusterAutomatedBackup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DeleteDBClusterAutomatedBackup) 