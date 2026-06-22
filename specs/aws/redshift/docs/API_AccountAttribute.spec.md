---
id: "@specs/aws/redshift/docs/API_AccountAttribute"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AccountAttribute"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# AccountAttribute

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_AccountAttribute
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AccountAttribute
<a name="API_AccountAttribute"></a>

A name value pair that describes an aspect of an account. 

## Contents
<a name="API_AccountAttribute_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** AttributeName **   
The name of the attribute.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** AttributeValues.AttributeValueTarget.N **   
A list of attribute values.  
Type: Array of [AttributeValueTarget](API_AttributeValueTarget.md) objects  
Required: No

## See Also
<a name="API_AccountAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/AccountAttribute) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/AccountAttribute) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/AccountAttribute) 