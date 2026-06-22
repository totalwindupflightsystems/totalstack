---
id: "@specs/aws/redshift/docs/API_PendingModifiedValues"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PendingModifiedValues"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# PendingModifiedValues

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_PendingModifiedValues
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PendingModifiedValues
<a name="API_PendingModifiedValues"></a>

Describes cluster attributes that are in a pending state. A change to one or more the attributes was requested and is in progress or will be applied.

## Contents
<a name="API_PendingModifiedValues_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** AutomatedSnapshotRetentionPeriod **   
The pending or in-progress change of the automated snapshot retention period.  
Type: Integer  
Required: No

 ** ClusterIdentifier **   
The pending or in-progress change of the new identifier for the cluster.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ClusterType **   
The pending or in-progress change of the cluster type.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ClusterVersion **   
The pending or in-progress change of the service version.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** EncryptionType **   
The encryption type for a cluster. Possible values are: KMS and None.   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** EnhancedVpcRouting **   
An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see [Enhanced VPC Routing](https://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html) in the Amazon Redshift Cluster Management Guide.  
If this option is `true`, enhanced VPC routing is enabled.   
Default: false  
Type: Boolean  
Required: No

 ** MaintenanceTrackName **   
The name of the maintenance track that the cluster will change to during the next maintenance window.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** MasterUserPassword **   
The pending or in-progress change of the admin user password for the cluster.  
Type: String  
Required: No

 ** NodeType **   
The pending or in-progress change of the cluster's node type.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** NumberOfNodes **   
The pending or in-progress change of the number of nodes in the cluster.  
Type: Integer  
Required: No

 ** PubliclyAccessible **   
The pending or in-progress change of the ability to connect to the cluster from the public network.  
Type: Boolean  
Required: No

## See Also
<a name="API_PendingModifiedValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/PendingModifiedValues) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/PendingModifiedValues) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/PendingModifiedValues) 