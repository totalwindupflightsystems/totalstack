---
id: "@specs/aws/kendra/docs/API_Principal"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Principal"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# Principal

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_Principal
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Principal
<a name="API_Principal"></a>

Provides user and group information for [user context filtering](https://docs.aws.amazon.com/kendra/latest/dg/user-context-filter.html).

## Contents
<a name="API_Principal_Contents"></a>

 ** Access **   <a name="kendra-Type-Principal-Access"></a>
Whether to allow or deny document access to the principal.  
Type: String  
Valid Values: `ALLOW | DENY`   
Required: Yes

 ** Name **   <a name="kendra-Type-Principal-Name"></a>
The name of the user or group.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^\P{C}*$`   
Required: Yes

 ** Type **   <a name="kendra-Type-Principal-Type"></a>
The type of principal.  
Type: String  
Valid Values: `USER | GROUP`   
Required: Yes

 ** DataSourceId **   <a name="kendra-Type-Principal-DataSourceId"></a>
The identifier of the data source the principal should access documents from.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`   
Required: No

## See Also
<a name="API_Principal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/Principal) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/Principal) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/Principal) 