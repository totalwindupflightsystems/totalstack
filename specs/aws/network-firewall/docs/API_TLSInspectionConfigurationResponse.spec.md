---
id: "@specs/aws/network-firewall/docs/API_TLSInspectionConfigurationResponse"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS TLSInspectionConfigurationResponse"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# TLSInspectionConfigurationResponse

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_TLSInspectionConfigurationResponse
> **target_lang:** meta — documentation tier. ALL sections preserved.



# TLSInspectionConfigurationResponse
<a name="API_TLSInspectionConfigurationResponse"></a>

The high-level properties of a TLS inspection configuration. This, along with the `TLSInspectionConfiguration`, define the TLS inspection configuration. You can retrieve all objects for a TLS inspection configuration by calling `DescribeTLSInspectionConfiguration`.

## Contents
<a name="API_TLSInspectionConfigurationResponse_Contents"></a>

 ** TLSInspectionConfigurationArn **   <a name="networkfirewall-Type-TLSInspectionConfigurationResponse-TLSInspectionConfigurationArn"></a>
The Amazon Resource Name (ARN) of the TLS inspection configuration.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: Yes

 ** TLSInspectionConfigurationId **   <a name="networkfirewall-Type-TLSInspectionConfigurationResponse-TLSInspectionConfigurationId"></a>
A unique identifier for the TLS inspection configuration. This ID is returned in the responses to create and list commands. You provide it to operations such as update and delete.  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$`   
Required: Yes

 ** TLSInspectionConfigurationName **   <a name="networkfirewall-Type-TLSInspectionConfigurationResponse-TLSInspectionConfigurationName"></a>
The descriptive name of the TLS inspection configuration. You can't change the name of a TLS inspection configuration after you create it.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: Yes

 ** CertificateAuthority **   <a name="networkfirewall-Type-TLSInspectionConfigurationResponse-CertificateAuthority"></a>
Contains metadata about an AWS Certificate Manager certificate.  
Type: [TlsCertificateData](API_TlsCertificateData.md) object  
Required: No

 ** Certificates **   <a name="networkfirewall-Type-TLSInspectionConfigurationResponse-Certificates"></a>
A list of the certificates associated with the TLS inspection configuration.  
Type: Array of [TlsCertificateData](API_TlsCertificateData.md) objects  
Required: No

 ** Description **   <a name="networkfirewall-Type-TLSInspectionConfigurationResponse-Description"></a>
A description of the TLS inspection configuration.   
Type: String  
Length Constraints: Maximum length of 512.  
Pattern: `^.*$`   
Required: No

 ** EncryptionConfiguration **   <a name="networkfirewall-Type-TLSInspectionConfigurationResponse-EncryptionConfiguration"></a>
A complex type that contains the AWS KMS encryption configuration settings for your TLS inspection configuration.  
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object  
Required: No

 ** LastModifiedTime **   <a name="networkfirewall-Type-TLSInspectionConfigurationResponse-LastModifiedTime"></a>
The last time that the TLS inspection configuration was changed.  
Type: Timestamp  
Required: No

 ** NumberOfAssociations **   <a name="networkfirewall-Type-TLSInspectionConfigurationResponse-NumberOfAssociations"></a>
The number of firewall policies that use this TLS inspection configuration.  
Type: Integer  
Required: No

 ** Tags **   <a name="networkfirewall-Type-TLSInspectionConfigurationResponse-Tags"></a>
The key:value pairs to associate with the resource.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.  
Required: No

 ** TLSInspectionConfigurationStatus **   <a name="networkfirewall-Type-TLSInspectionConfigurationResponse-TLSInspectionConfigurationStatus"></a>
Detailed information about the current status of a [TLSInspectionConfiguration](API_TLSInspectionConfiguration.md). You can retrieve this for a TLS inspection configuration by calling [DescribeTLSInspectionConfiguration](API_DescribeTLSInspectionConfiguration.md) and providing the TLS inspection configuration name and ARN.  
Type: String  
Valid Values: `ACTIVE | DELETING | ERROR`   
Required: No

## See Also
<a name="API_TLSInspectionConfigurationResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/TLSInspectionConfigurationResponse) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/TLSInspectionConfigurationResponse) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/TLSInspectionConfigurationResponse) 