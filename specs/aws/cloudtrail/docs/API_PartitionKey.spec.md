---
id: "@specs/aws/cloudtrail/docs/API_PartitionKey"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PartitionKey"
status: active
depends_on:
  - "@specs/aws/cloudtrail/meta"
---

# PartitionKey

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudtrail/docs/API_PartitionKey
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PartitionKey
<a name="API_PartitionKey"></a>

Contains information about a partition key for an event data store.

## Contents
<a name="API_PartitionKey_Contents"></a>

 ** Name **   <a name="awscloudtrail-Type-PartitionKey-Name"></a>
The name of the partition key.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`   
Required: Yes

 ** Type **   <a name="awscloudtrail-Type-PartitionKey-Type"></a>
The data type of the partition key. For example, `bigint` or `string`.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 255.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`   
Required: Yes

## See Also
<a name="API_PartitionKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/PartitionKey) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/PartitionKey) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/PartitionKey) 