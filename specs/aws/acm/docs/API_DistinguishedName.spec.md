---
id: "@specs/aws/acm/docs/API_DistinguishedName"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DistinguishedName"
status: active
depends_on:
  - "@specs/aws/acm/meta"
---

# DistinguishedName

> **source:** AWS Documentation
> **spec:id:** @specs/aws/acm/docs/API_DistinguishedName
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DistinguishedName
<a name="API_DistinguishedName"></a>

Contains X.500 distinguished name information.

## Contents
<a name="API_DistinguishedName_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** CommonName **   <a name="ACM-Type-DistinguishedName-CommonName"></a>
The common name (CN) attribute.  
Type: String  
Required: No

 ** Country **   <a name="ACM-Type-DistinguishedName-Country"></a>
The country (C) attribute.  
Type: String  
Required: No

 ** CustomAttributes **   <a name="ACM-Type-DistinguishedName-CustomAttributes"></a>
A list of custom attributes in the distinguished name. Each custom attribute contains an object identifier (OID) and its corresponding value.  
Type: Array of [CustomAttribute](API_CustomAttribute.md) objects  
Required: No

 ** DistinguishedNameQualifier **   <a name="ACM-Type-DistinguishedName-DistinguishedNameQualifier"></a>
The distinguished name qualifier attribute.  
Type: String  
Required: No

 ** DomainComponents **   <a name="ACM-Type-DistinguishedName-DomainComponents"></a>
The domain component attributes.  
Type: Array of strings  
Required: No

 ** GenerationQualifier **   <a name="ACM-Type-DistinguishedName-GenerationQualifier"></a>
The generation qualifier attribute.  
Type: String  
Required: No

 ** GivenName **   <a name="ACM-Type-DistinguishedName-GivenName"></a>
The given name attribute.  
Type: String  
Required: No

 ** Initials **   <a name="ACM-Type-DistinguishedName-Initials"></a>
The initials attribute.  
Type: String  
Required: No

 ** Locality **   <a name="ACM-Type-DistinguishedName-Locality"></a>
The locality (L) attribute.  
Type: String  
Required: No

 ** Organization **   <a name="ACM-Type-DistinguishedName-Organization"></a>
The organization (O) attribute.  
Type: String  
Required: No

 ** OrganizationalUnit **   <a name="ACM-Type-DistinguishedName-OrganizationalUnit"></a>
The organizational unit (OU) attribute.  
Type: String  
Required: No

 ** Pseudonym **   <a name="ACM-Type-DistinguishedName-Pseudonym"></a>
The pseudonym attribute.  
Type: String  
Required: No

 ** SerialNumber **   <a name="ACM-Type-DistinguishedName-SerialNumber"></a>
The serial number attribute.  
Type: String  
Required: No

 ** State **   <a name="ACM-Type-DistinguishedName-State"></a>
The state or province (ST) attribute.  
Type: String  
Required: No

 ** Surname **   <a name="ACM-Type-DistinguishedName-Surname"></a>
The surname attribute.  
Type: String  
Required: No

 ** Title **   <a name="ACM-Type-DistinguishedName-Title"></a>
The title attribute.  
Type: String  
Required: No

## See Also
<a name="API_DistinguishedName_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/DistinguishedName) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/DistinguishedName) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/DistinguishedName) 