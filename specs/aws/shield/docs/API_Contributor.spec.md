---
id: "@specs/aws/shield/docs/API_Contributor"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Contributor"
status: active
depends_on:
  - "@specs/aws/shield/meta"
---

# Contributor

> **source:** AWS Documentation
> **spec:id:** @specs/aws/shield/docs/API_Contributor
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Contributor
<a name="API_Contributor"></a>

A contributor to the attack and their contribution. 

## Contents
<a name="API_Contributor_Contents"></a>

 ** Name **   <a name="AWSShield-Type-Contributor-Name"></a>
The name of the contributor. The type of name that you'll find here depends on the `AttackPropertyIdentifier` setting in the `AttackProperty` where this contributor is defined. For example, if the `AttackPropertyIdentifier` is `SOURCE_COUNTRY`, the `Name` could be `United States`.  
Type: String  
Required: No

 ** Value **   <a name="AWSShield-Type-Contributor-Value"></a>
The contribution of this contributor expressed in [Protection](API_Protection.md) units. For example `10,000`.  
Type: Long  
Required: No

## See Also
<a name="API_Contributor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/Contributor) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/Contributor) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/Contributor) 