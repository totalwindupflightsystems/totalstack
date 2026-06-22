---
id: "@specs/aws/docdb/docs/API_elastic_ClusterInList"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ClusterInList"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# ClusterInList

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_elastic_ClusterInList
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ClusterInList
<a name="API_elastic_ClusterInList"></a>

A list of Amazon DocumentDB elastic clusters.

## Contents
<a name="API_elastic_ClusterInList_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** clusterArn **   <a name="documentdb-Type-elastic_ClusterInList-clusterArn"></a>
The ARN identifier of the elastic cluster.  
Type: String  
Required: Yes

 ** clusterName **   <a name="documentdb-Type-elastic_ClusterInList-clusterName"></a>
The name of the elastic cluster.  
Type: String  
Required: Yes

 ** status **   <a name="documentdb-Type-elastic_ClusterInList-status"></a>
The status of the elastic cluster.  
Type: String  
Valid Values: `CREATING | ACTIVE | DELETING | UPDATING | VPC_ENDPOINT_LIMIT_EXCEEDED | IP_ADDRESS_LIMIT_EXCEEDED | INVALID_SECURITY_GROUP_ID | INVALID_SUBNET_ID | INACCESSIBLE_ENCRYPTION_CREDS | INACCESSIBLE_SECRET_ARN | INACCESSIBLE_VPC_ENDPOINT | INCOMPATIBLE_NETWORK | MERGING | MODIFYING | SPLITTING | COPYING | STARTING | STOPPING | STOPPED | MAINTENANCE | INACCESSIBLE_ENCRYPTION_CREDENTIALS_RECOVERABLE`   
Required: Yes

## See Also
<a name="API_elastic_ClusterInList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-elastic-2022-11-28/ClusterInList) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-elastic-2022-11-28/ClusterInList) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-elastic-2022-11-28/ClusterInList) 