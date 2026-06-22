---
id: "@specs/aws/acm/docs/API_GeneralName"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GeneralName"
status: active
depends_on:
  - "@specs/aws/acm/meta"
---

# GeneralName

> **source:** AWS Documentation
> **spec:id:** @specs/aws/acm/docs/API_GeneralName
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GeneralName
<a name="API_GeneralName"></a>

Describes an ASN.1 X.400 `GeneralName` as defined in [RFC 5280](https://datatracker.ietf.org/doc/html/rfc5280). Only one of the following naming options should be provided.

## Contents
<a name="API_GeneralName_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** DirectoryName **   <a name="ACM-Type-GeneralName-DirectoryName"></a>
Contains information about the certificate subject. The `Subject` field in the certificate identifies the entity that owns or controls the public key in the certificate. The entity can be a user, computer, device, or service. The `Subject` must contain an X.500 distinguished name (DN). A DN is a sequence of relative distinguished names (RDNs). The RDNs are separated by commas in the certificate.  
Type: [DistinguishedName](API_DistinguishedName.md) object  
Required: No

 ** DnsName **   <a name="ACM-Type-GeneralName-DnsName"></a>
Represents `GeneralName` as a DNS name.  
Type: String  
Required: No

 ** IpAddress **   <a name="ACM-Type-GeneralName-IpAddress"></a>
Represents `GeneralName` as an IPv4 or IPv6 address.  
Type: String  
Required: No

 ** OtherName **   <a name="ACM-Type-GeneralName-OtherName"></a>
Represents `GeneralName` using an `OtherName` object.  
Type: [OtherName](API_OtherName.md) object  
Required: No

 ** RegisteredId **   <a name="ACM-Type-GeneralName-RegisteredId"></a>
Represents `GeneralName` as an object identifier (OID).  
Type: String  
Required: No

 ** Rfc822Name **   <a name="ACM-Type-GeneralName-Rfc822Name"></a>
Represents `GeneralName` as an [RFC 822](https://datatracker.ietf.org/doc/html/rfc822) email address.  
Type: String  
Required: No

 ** UniformResourceIdentifier **   <a name="ACM-Type-GeneralName-UniformResourceIdentifier"></a>
Represents `GeneralName` as a URI.  
Type: String  
Required: No

## See Also
<a name="API_GeneralName_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/GeneralName) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/GeneralName) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/GeneralName) 