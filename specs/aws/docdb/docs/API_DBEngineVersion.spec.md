---
id: "@specs/aws/docdb/docs/API_DBEngineVersion"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DBEngineVersion"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# DBEngineVersion

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_DBEngineVersion
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DBEngineVersion
<a name="API_DBEngineVersion"></a>

 Detailed information about an engine version. 

## Contents
<a name="API_DBEngineVersion_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** DBEngineDescription **   
The description of the database engine.  
Type: String  
Required: No

 ** DBEngineVersionDescription **   
The description of the database engine version.  
Type: String  
Required: No

 ** DBParameterGroupFamily **   
The name of the parameter group family for the database engine.  
Type: String  
Required: No

 ** Engine **   
The name of the database engine.  
Type: String  
Required: No

 ** EngineVersion **   
The version number of the database engine.  
Type: String  
Required: No

 ** ExportableLogTypes.member.N **   
The types of logs that the database engine has available for export to Amazon CloudWatch Logs.  
Type: Array of strings  
Required: No

 ** ServerlessV2FeaturesSupport **   
Specifies any Amazon DocumentDB Serverless properties or limits that differ between Amazon DocumentDB engine versions. You can test the values of this attribute when deciding which Amazon DocumentDB version to use in a new or upgraded cluster. You can also retrieve the version of an existing cluster and check whether that version supports certain Amazon DocumentDB Serverless features before you attempt to use those features.  
Type: [ServerlessV2FeaturesSupport](API_ServerlessV2FeaturesSupport.md) object  
Required: No

 ** SupportedCACertificateIdentifiers.member.N **   
A list of the supported CA certificate identifiers.  
For more information, see [Updating Your Amazon DocumentDB TLS Certificates](https://docs.aws.amazon.com/documentdb/latest/devguide/ca_cert_rotation.html) and [ Encrypting Data in Transit](https://docs.aws.amazon.com/documentdb/latest/devguide/security.encryption.ssl.html) in the *Amazon DocumentDB Developer Guide*.  
Type: Array of strings  
Required: No

 ** SupportsCertificateRotationWithoutRestart **   
Indicates whether the engine version supports rotating the server certificate without rebooting the DB instance.  
Type: Boolean  
Required: No

 ** SupportsLogExportsToCloudwatchLogs **   
A value that indicates whether the engine version supports exporting the log types specified by `ExportableLogTypes` to CloudWatch Logs.  
Type: Boolean  
Required: No

 ** ValidUpgradeTarget.UpgradeTarget.N **   
A list of engine versions that this database engine version can be upgraded to.  
Type: Array of [UpgradeTarget](API_UpgradeTarget.md) objects  
Required: No

## See Also
<a name="API_DBEngineVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/DBEngineVersion) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/DBEngineVersion) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/DBEngineVersion) 