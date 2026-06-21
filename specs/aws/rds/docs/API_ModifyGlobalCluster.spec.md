---
id: "@specs/aws/rds/docs/API_ModifyGlobalCluster"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ModifyGlobalCluster"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# ModifyGlobalCluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_ModifyGlobalCluster
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ModifyGlobalCluster
<a name="API_ModifyGlobalCluster"></a>

Modifies a setting for an Amazon Aurora global database cluster. You can change one or more database configuration parameters by specifying these parameters and the new values in the request. For more information on Amazon Aurora, see [ What is Amazon Aurora?](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) in the *Amazon Aurora User Guide*.

**Note**  
This operation only applies to Aurora global database clusters.

## Request Parameters
<a name="API_ModifyGlobalCluster_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** GlobalClusterIdentifier **   
The cluster identifier for the global cluster to modify. This parameter isn't case-sensitive.  
Constraints:  
+ Must match the identifier of an existing global database cluster.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[A-Za-z][0-9A-Za-z-:._]*`   
Required: Yes

 ** AllowMajorVersionUpgrade **   
Specifies whether to allow major version upgrades.  
Constraints: Must be enabled if you specify a value for the `EngineVersion` parameter that's a different major version than the global cluster's current version.  
If you upgrade the major version of a global database, the cluster and DB instance parameter groups are set to the default parameter groups for the new version. Apply any custom parameter groups after completing the upgrade.  
Type: Boolean  
Required: No

 ** DeletionProtection **   
Specifies whether to enable deletion protection for the global database cluster. The global database cluster can't be deleted when deletion protection is enabled.  
Type: Boolean  
Required: No

 ** EngineVersion **   
The version number of the database engine to which you want to upgrade.   
To list all of the available engine versions for `aurora-mysql` (for MySQL-based Aurora global databases), use the following command:  
 `aws rds describe-db-engine-versions --engine aurora-mysql --query '*[]|[?SupportsGlobalDatabases == `true`].[EngineVersion]'`   
To list all of the available engine versions for `aurora-postgresql` (for PostgreSQL-based Aurora global databases), use the following command:  
 `aws rds describe-db-engine-versions --engine aurora-postgresql --query '*[]|[?SupportsGlobalDatabases == `true`].[EngineVersion]'`   
Type: String  
Required: No

 ** NewGlobalClusterIdentifier **   
The new cluster identifier for the global database cluster. This value is stored as a lowercase string.  
Constraints:  
+ Must contain from 1 to 63 letters, numbers, or hyphens.
+ The first character must be a letter.
+ Can't end with a hyphen or contain two consecutive hyphens.
Example: `my-cluster2`   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[A-Za-z][0-9A-Za-z-:._]*`   
Required: No

## Response Elements
<a name="API_ModifyGlobalCluster_ResponseElements"></a>

The following element is returned by the service.

 ** GlobalCluster **   
A data type representing an Aurora global database.  
Type: [GlobalCluster](API_GlobalCluster.md) object

## Errors
<a name="API_ModifyGlobalCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** GlobalClusterAlreadyExistsFault **   
The `GlobalClusterIdentifier` already exists. Specify a new global database identifier (unique name) to create a new global database cluster or to rename an existing one.  
HTTP Status Code: 400

 ** GlobalClusterNotFoundFault **   
The `GlobalClusterIdentifier` doesn't refer to an existing global database cluster.  
HTTP Status Code: 404

 ** InvalidDBClusterStateFault **   
The requested operation can't be performed while the cluster is in this state.  
HTTP Status Code: 400

 ** InvalidDBInstanceState **   
The DB instance isn't in a valid state.  
HTTP Status Code: 400

 ** InvalidGlobalClusterStateFault **   
The global cluster is in an invalid state and can't perform the requested operation.  
HTTP Status Code: 400

## See Also
<a name="API_ModifyGlobalCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/ModifyGlobalCluster) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/ModifyGlobalCluster) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/ModifyGlobalCluster) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/ModifyGlobalCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/ModifyGlobalCluster) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/ModifyGlobalCluster) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/ModifyGlobalCluster) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/ModifyGlobalCluster) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/ModifyGlobalCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/ModifyGlobalCluster) 