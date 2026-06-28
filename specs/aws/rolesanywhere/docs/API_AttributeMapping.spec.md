---
id: "@specs/aws/rolesanywhere/docs/API_AttributeMapping"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AttributeMapping"
status: active
depends_on:
  - "@specs/aws/rolesanywhere/meta"
---

# AttributeMapping

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rolesanywhere/docs/API_AttributeMapping
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AttributeMapping
<a name="API_AttributeMapping"></a>

A mapping applied to the authenticating end-entity certificate.

## Contents
<a name="API_AttributeMapping_Contents"></a>

 ** certificateField **   <a name="rolesanywhere-Type-AttributeMapping-certificateField"></a>
Fields (x509Subject, x509Issuer and x509SAN) within X.509 certificates.  
Type: String  
Valid Values: `x509Subject | x509Issuer | x509SAN`   
Required: No

 ** mappingRules **   <a name="rolesanywhere-Type-AttributeMapping-mappingRules"></a>
A list of mapping entries for every supported specifier or sub-field.  
Type: Array of [MappingRule](API_MappingRule.md) objects  
Required: No

## See Also
<a name="API_AttributeMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rolesanywhere-2018-05-10/AttributeMapping) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rolesanywhere-2018-05-10/AttributeMapping) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rolesanywhere-2018-05-10/AttributeMapping) 