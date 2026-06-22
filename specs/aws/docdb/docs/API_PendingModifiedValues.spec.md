---
id: "@specs/aws/docdb/docs/API_PendingModifiedValues"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PendingModifiedValues"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# PendingModifiedValues

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_PendingModifiedValues
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PendingModifiedValues
<a name="API_PendingModifiedValues"></a>

 One or more modified settings for an instance. These modified settings have been requested, but haven't been applied yet.

## Contents
<a name="API_PendingModifiedValues_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** AllocatedStorage **   
 Contains the new `AllocatedStorage` size for then instance that will be applied or is currently being applied.   
Type: Integer  
Required: No

 ** BackupRetentionPeriod **   
Specifies the pending number of days for which automated backups are retained.  
Type: Integer  
Required: No

 ** CACertificateIdentifier **   
Specifies the identifier of the certificate authority (CA) certificate for the DB instance.  
Type: String  
Required: No

 ** DBInstanceClass **   
 Contains the new `DBInstanceClass` for the instance that will be applied or is currently being applied.   
Type: String  
Required: No

 ** DBInstanceIdentifier **   
 Contains the new `DBInstanceIdentifier` for the instance that will be applied or is currently being applied.   
Type: String  
Required: No

 ** DBSubnetGroupName **   
The new subnet group for the instance.   
Type: String  
Required: No

 ** EngineVersion **   
Indicates the database engine version.  
Type: String  
Required: No

 ** Iops **   
Specifies the new Provisioned IOPS value for the instance that will be applied or is currently being applied.  
Type: Integer  
Required: No

 ** LicenseModel **   
The license model for the instance.  
Valid values: `license-included`, `bring-your-own-license`, `general-public-license`   
Type: String  
Required: No

 ** MasterUserPassword **   
Contains the pending or currently in-progress change of the master credentials for the instance.  
Type: String  
Required: No

 ** MultiAZ **   
Indicates that the Single-AZ instance is to change to a Multi-AZ deployment.  
Type: Boolean  
Required: No

 ** PendingCloudwatchLogsExports **   
A list of the log types whose configuration is still pending. These log types are in the process of being activated or deactivated.  
Type: [PendingCloudwatchLogsExports](API_PendingCloudwatchLogsExports.md) object  
Required: No

 ** Port **   
Specifies the pending port for the instance.  
Type: Integer  
Required: No

 ** StorageType **   
Specifies the storage type to be associated with the instance.  
Type: String  
Required: No

## See Also
<a name="API_PendingModifiedValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/PendingModifiedValues) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/PendingModifiedValues) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/PendingModifiedValues) 