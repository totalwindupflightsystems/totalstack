---
id: "@specs/aws/rds/docs/API_DBClusterMember"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DBClusterMember"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DBClusterMember

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DBClusterMember
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DBClusterMember
<a name="API_DBClusterMember"></a>

Contains information about an instance that is part of a DB cluster.

## Contents
<a name="API_DBClusterMember_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** DBClusterParameterGroupStatus **   
Specifies the status of the DB cluster parameter group for this member of the DB cluster.  
Type: String  
Required: No

 ** DBInstanceIdentifier **   
Specifies the instance identifier for this member of the DB cluster.  
Type: String  
Required: No

 ** IsClusterWriter **   
Indicates whether the cluster member is the primary DB instance for the DB cluster.  
Type: Boolean  
Required: No

 ** PromotionTier **   
A value that specifies the order in which an Aurora Replica is promoted to the primary instance after a failure of the existing primary instance. For more information, see [ Fault Tolerance for an Aurora DB Cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Backups.html#Aurora.Managing.FaultTolerance) in the *Amazon Aurora User Guide*.  
Type: Integer  
Required: No

## See Also
<a name="API_DBClusterMember_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DBClusterMember) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DBClusterMember) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DBClusterMember) 