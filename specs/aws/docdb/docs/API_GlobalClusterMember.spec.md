---
id: "@specs/aws/docdb/docs/API_GlobalClusterMember"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GlobalClusterMember"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# GlobalClusterMember

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_GlobalClusterMember
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GlobalClusterMember
<a name="API_GlobalClusterMember"></a>

A data structure with information about any primary and secondary clusters associated with an Amazon DocumentDB global clusters. 

## Contents
<a name="API_GlobalClusterMember_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** DBClusterArn **   
The Amazon Resource Name (ARN) for each Amazon DocumentDB cluster.  
Type: String  
Required: No

 ** IsWriter **   
 Specifies whether the Amazon DocumentDB cluster is the primary cluster (that is, has read-write capability) for the Amazon DocumentDB global cluster with which it is associated.   
Type: Boolean  
Required: No

 ** Readers.member.N **   
The Amazon Resource Name (ARN) for each read-only secondary cluster associated with the Amazon DocumentDB global cluster.  
Type: Array of strings  
Required: No

 ** SynchronizationStatus **   
The status of synchronization of each Amazon DocumentDB cluster in the global cluster.  
Type: String  
Valid Values: `connected | pending-resync`   
Required: No

## See Also
<a name="API_GlobalClusterMember_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/GlobalClusterMember) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/GlobalClusterMember) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/GlobalClusterMember) 