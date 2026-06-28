---
id: "@specs/aws/network-firewall/docs/API_TLSInspectionConfigurationMetadata"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS TLSInspectionConfigurationMetadata"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# TLSInspectionConfigurationMetadata

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_TLSInspectionConfigurationMetadata
> **target_lang:** meta — documentation tier. ALL sections preserved.



# TLSInspectionConfigurationMetadata
<a name="API_TLSInspectionConfigurationMetadata"></a>

High-level information about a TLS inspection configuration, returned by `ListTLSInspectionConfigurations`. You can use the information provided in the metadata to retrieve and manage a TLS configuration.

## Contents
<a name="API_TLSInspectionConfigurationMetadata_Contents"></a>

 ** Arn **   <a name="networkfirewall-Type-TLSInspectionConfigurationMetadata-Arn"></a>
The Amazon Resource Name (ARN) of the TLS inspection configuration.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** Name **   <a name="networkfirewall-Type-TLSInspectionConfigurationMetadata-Name"></a>
The descriptive name of the TLS inspection configuration. You can't change the name of a TLS inspection configuration after you create it.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

## See Also
<a name="API_TLSInspectionConfigurationMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/TLSInspectionConfigurationMetadata) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/TLSInspectionConfigurationMetadata) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/TLSInspectionConfigurationMetadata) 