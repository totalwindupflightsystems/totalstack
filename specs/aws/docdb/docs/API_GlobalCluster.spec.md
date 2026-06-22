---
id: "@specs/aws/docdb/docs/API_GlobalCluster"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GlobalCluster"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# GlobalCluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_GlobalCluster
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GlobalCluster
<a name="API_GlobalCluster"></a>

A data type representing an Amazon DocumentDB global cluster.

## Contents
<a name="API_GlobalCluster_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** DatabaseName **   
The default database name within the new global cluster.  
Type: String  
Required: No

 ** DeletionProtection **   
The deletion protection setting for the new global cluster.  
Type: Boolean  
Required: No

 ** Engine **   
The Amazon DocumentDB database engine used by the global cluster.   
Type: String  
Required: No

 ** EngineVersion **   
Indicates the database engine version.  
Type: String  
Required: No

 ** FailoverState **   
A data object containing all properties for the current state of an in-process or pending switchover or failover process for this global cluster. This object is empty unless the `SwitchoverGlobalCluster` or `FailoverGlobalCluster` operation was called on this global cluster.  
Type: [FailoverState](API_FailoverState.md) object  
Required: No

 ** GlobalClusterArn **   
The Amazon Resource Name (ARN) for the global cluster.  
Type: String  
Required: No

 ** GlobalClusterIdentifier **   
Contains a user-supplied global cluster identifier. This identifier is the unique key that identifies a global cluster.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[A-Za-z][0-9A-Za-z-:._]*`   
Required: No

 ** GlobalClusterMembers.GlobalClusterMember.N **   
The list of cluster IDs for secondary clusters within the global cluster. Currently limited to one item.   
Type: Array of [GlobalClusterMember](API_GlobalClusterMember.md) objects  
Required: No

 ** GlobalClusterResourceId **   
The AWS RegionRegion-unique, immutable identifier for the global database cluster. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS customer master key (CMK) for the cluster is accessed.   
Type: String  
Required: No

 ** Status **   
Specifies the current state of this global cluster.  
Type: String  
Required: No

 ** StorageEncrypted **   
The storage encryption setting for the global cluster.  
Type: Boolean  
Required: No

 ** TagList.Tag.N **   
A list of global cluster tags.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## See Also
<a name="API_GlobalCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/GlobalCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/GlobalCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/GlobalCluster) 