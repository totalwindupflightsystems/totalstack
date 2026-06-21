---
id: "@specs/aws/shield/docs/API_AttackVectorDescription"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AttackVectorDescription"
status: active
depends_on:
  - "@specs/aws/shield/meta"
---

# AttackVectorDescription

> **source:** AWS Documentation
> **spec:id:** @specs/aws/shield/docs/API_AttackVectorDescription
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AttackVectorDescription
<a name="API_AttackVectorDescription"></a>

Describes the attack.

## Contents
<a name="API_AttackVectorDescription_Contents"></a>

 ** VectorType **   <a name="AWSShield-Type-AttackVectorDescription-VectorType"></a>
The attack type. Valid values:  
+ UDP\_TRAFFIC
+ UDP\_FRAGMENT
+ GENERIC\_UDP\_REFLECTION
+ DNS\_REFLECTION
+ NTP\_REFLECTION
+ CHARGEN\_REFLECTION
+ SSDP\_REFLECTION
+ PORT\_MAPPER
+ RIP\_REFLECTION
+ SNMP\_REFLECTION
+ MSSQL\_REFLECTION
+ NET\_BIOS\_REFLECTION
+ SYN\_FLOOD
+ ACK\_FLOOD
+ REQUEST\_FLOOD
+ HTTP\_REFLECTION
+ UDS\_REFLECTION
+ MEMCACHED\_REFLECTION
Type: String  
Required: Yes

## See Also
<a name="API_AttackVectorDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/AttackVectorDescription) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/AttackVectorDescription) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/AttackVectorDescription) 