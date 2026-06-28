---
id: "@specs/aws/network-firewall/docs/API_ProxyConfigurationMetadata"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ProxyConfigurationMetadata"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# ProxyConfigurationMetadata

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_ProxyConfigurationMetadata
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ProxyConfigurationMetadata
<a name="API_ProxyConfigurationMetadata"></a>

High-level information about a proxy configuration, returned by operations like create and describe. You can use the information provided in the metadata to retrieve and manage a proxy configuration. You can retrieve all objects for a proxy configuration by calling [DescribeProxyConfiguration](API_DescribeProxyConfiguration.md). 

## Contents
<a name="API_ProxyConfigurationMetadata_Contents"></a>

 ** Arn **   <a name="networkfirewall-Type-ProxyConfigurationMetadata-Arn"></a>
The Amazon Resource Name (ARN) of a proxy configuration.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** Name **   <a name="networkfirewall-Type-ProxyConfigurationMetadata-Name"></a>
The descriptive name of the proxy configuration. You can't change the name of a proxy configuration after you create it.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

## See Also
<a name="API_ProxyConfigurationMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/ProxyConfigurationMetadata) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/ProxyConfigurationMetadata) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/ProxyConfigurationMetadata) 