---
id: "@specs/aws/network-firewall/docs/API_ProxyMetadata"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ProxyMetadata"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# ProxyMetadata

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_ProxyMetadata
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ProxyMetadata
<a name="API_ProxyMetadata"></a>

High-level information about a proxy, returned by operations like create and describe. You can use the information provided in the metadata to retrieve and manage a proxy. You can retrieve all objects for a proxy by calling [DescribeProxy](API_DescribeProxy.md). 

## Contents
<a name="API_ProxyMetadata_Contents"></a>

 ** Arn **   <a name="networkfirewall-Type-ProxyMetadata-Arn"></a>
The Amazon Resource Name (ARN) of a proxy.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** Name **   <a name="networkfirewall-Type-ProxyMetadata-Name"></a>
The descriptive name of the proxy. You can't change the name of a proxy after you create it.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

## See Also
<a name="API_ProxyMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/ProxyMetadata) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/ProxyMetadata) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/ProxyMetadata) 