---
id: "@specs/aws/emr/docs/API_KerberosAttributes"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS KerberosAttributes"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# KerberosAttributes

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_KerberosAttributes
> **target_lang:** meta — documentation tier. ALL sections preserved.



# KerberosAttributes
<a name="API_KerberosAttributes"></a>

Attributes for Kerberos configuration when Kerberos authentication is enabled using a security configuration. For more information see [Use Kerberos Authentication](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-kerberos.html) in the *Amazon EMR Management Guide*.

## Contents
<a name="API_KerberosAttributes_Contents"></a>

 ** KdcAdminPassword **   <a name="EMR-Type-KerberosAttributes-KdcAdminPassword"></a>
The password used within the cluster for the kadmin service on the cluster-dedicated KDC, which maintains Kerberos principals, password policies, and keytabs for the cluster.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: Yes

 ** Realm **   <a name="EMR-Type-KerberosAttributes-Realm"></a>
The name of the Kerberos realm to which all nodes in a cluster belong. For example, `EC2.INTERNAL`.   
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: Yes

 ** ADDomainJoinPassword **   <a name="EMR-Type-KerberosAttributes-ADDomainJoinPassword"></a>
The Active Directory password for `ADDomainJoinUser`.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** ADDomainJoinUser **   <a name="EMR-Type-KerberosAttributes-ADDomainJoinUser"></a>
Required only when establishing a cross-realm trust with an Active Directory domain. A user with sufficient privileges to join resources to the domain.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** CrossRealmTrustPrincipalPassword **   <a name="EMR-Type-KerberosAttributes-CrossRealmTrustPrincipalPassword"></a>
Required only when establishing a cross-realm trust with a KDC in a different realm. The cross-realm principal password, which must be identical across realms.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

## See Also
<a name="API_KerberosAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/KerberosAttributes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/KerberosAttributes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/KerberosAttributes) 