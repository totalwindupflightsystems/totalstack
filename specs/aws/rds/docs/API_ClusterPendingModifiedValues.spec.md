---
id: "@specs/aws/rds/docs/API_ClusterPendingModifiedValues"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ClusterPendingModifiedValues"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# ClusterPendingModifiedValues

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_ClusterPendingModifiedValues
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ClusterPendingModifiedValues
<a name="API_ClusterPendingModifiedValues"></a>

This data type is used as a response element in the `ModifyDBCluster` operation and contains changes that will be applied during the next maintenance window.

## Contents
<a name="API_ClusterPendingModifiedValues_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** AllocatedStorage **   
The allocated storage size in gibibytes (GiB) for all database engines except Amazon Aurora. For Aurora, `AllocatedStorage` always returns 1, because Aurora DB cluster storage size isn't fixed, but instead automatically adjusts as needed.  
Type: Integer  
Required: No

 ** BackupRetentionPeriod **   
The number of days for which automatic DB snapshots are retained.  
Type: Integer  
Required: No

 ** CertificateDetails **   
The details of the DB instance’s server certificate.  
For more information, see [Using SSL/TLS to encrypt a connection to a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html) in the *Amazon RDS User Guide* and [ Using SSL/TLS to encrypt a connection to a DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html) in the *Amazon Aurora User Guide*.  
Type: [CertificateDetails](API_CertificateDetails.md) object  
Required: No

 ** DBClusterIdentifier **   
The DBClusterIdentifier value for the DB cluster.  
Type: String  
Required: No

 ** EngineVersion **   
The database engine version.  
Type: String  
Required: No

 ** IAMDatabaseAuthenticationEnabled **   
Indicates whether mapping of AWS Identity and Access Management (IAM) accounts to database accounts is enabled.  
Type: Boolean  
Required: No

 ** Iops **   
The Provisioned IOPS (I/O operations per second) value. This setting is only for non-Aurora Multi-AZ DB clusters.  
Type: Integer  
Required: No

 ** MasterUserPassword **   
The master credentials for the DB cluster.  
Type: String  
Required: No

 ** PendingCloudwatchLogsExports **   
A list of the log types whose configuration is still pending. In other words, these log types are in the process of being activated or deactivated.  
Type: [PendingCloudwatchLogsExports](API_PendingCloudwatchLogsExports.md) object  
Required: No

 ** RdsCustomClusterConfiguration **   
Reserved for future use.  
Type: [RdsCustomClusterConfiguration](API_RdsCustomClusterConfiguration.md) object  
Required: No

 ** StorageType **   
The storage type for the DB cluster.  
Type: String  
Required: No

## See Also
<a name="API_ClusterPendingModifiedValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/ClusterPendingModifiedValues) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/ClusterPendingModifiedValues) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/ClusterPendingModifiedValues) 