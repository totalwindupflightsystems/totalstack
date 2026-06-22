---
id: "@specs/aws/docdb/docs/API_elastic_Shard"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Shard"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# Shard

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_elastic_Shard
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Shard
<a name="API_elastic_Shard"></a>

The name of the shard.

## Contents
<a name="API_elastic_Shard_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** createTime **   <a name="documentdb-Type-elastic_Shard-createTime"></a>
The time when the shard was created in Universal Coordinated Time (UTC).  
Type: String  
Required: Yes

 ** shardId **   <a name="documentdb-Type-elastic_Shard-shardId"></a>
The ID of the shard.  
Type: String  
Required: Yes

 ** status **   <a name="documentdb-Type-elastic_Shard-status"></a>
The current status of the shard.  
Type: String  
Valid Values: `CREATING | ACTIVE | DELETING | UPDATING | VPC_ENDPOINT_LIMIT_EXCEEDED | IP_ADDRESS_LIMIT_EXCEEDED | INVALID_SECURITY_GROUP_ID | INVALID_SUBNET_ID | INACCESSIBLE_ENCRYPTION_CREDS | INACCESSIBLE_SECRET_ARN | INACCESSIBLE_VPC_ENDPOINT | INCOMPATIBLE_NETWORK | MERGING | MODIFYING | SPLITTING | COPYING | STARTING | STOPPING | STOPPED | MAINTENANCE | INACCESSIBLE_ENCRYPTION_CREDENTIALS_RECOVERABLE`   
Required: Yes

## See Also
<a name="API_elastic_Shard_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-elastic-2022-11-28/Shard) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-elastic-2022-11-28/Shard) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-elastic-2022-11-28/Shard) 