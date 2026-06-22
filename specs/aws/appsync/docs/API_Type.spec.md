---
id: "@specs/aws/appsync/docs/API_Type"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Type"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# Type

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_Type
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Type
<a name="API_Type"></a>

Describes a type.

## Contents
<a name="API_Type_Contents"></a>

 ** arn **   <a name="appsync-Type-Type-arn"></a>
The type Amazon Resource Name (ARN).  
Type: String  
Required: No

 ** definition **   <a name="appsync-Type-Type-definition"></a>
The type definition.  
Type: String  
Required: No

 ** description **   <a name="appsync-Type-Type-description"></a>
The type description.  
Type: String  
Required: No

 ** format **   <a name="appsync-Type-Type-format"></a>
The type format: SDL or JSON.  
Type: String  
Valid Values: `SDL | JSON`   
Required: No

 ** name **   <a name="appsync-Type-Type-name"></a>
The type name.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 65536.  
Pattern: `[_A-Za-z][_0-9A-Za-z]*`   
Required: No

## See Also
<a name="API_Type_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/Type) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/Type) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/Type) 