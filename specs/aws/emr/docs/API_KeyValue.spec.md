---
id: "@specs/aws/emr/docs/API_KeyValue"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS KeyValue"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# KeyValue

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_KeyValue
> **target_lang:** meta — documentation tier. ALL sections preserved.



# KeyValue
<a name="API_KeyValue"></a>

A key-value pair.

## Contents
<a name="API_KeyValue_Contents"></a>

 ** Key **   <a name="EMR-Type-KeyValue-Key"></a>
The unique identifier of a key-value pair.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** Value **   <a name="EMR-Type-KeyValue-Value"></a>
The value part of the identified key.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

## See Also
<a name="API_KeyValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/KeyValue) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/KeyValue) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/KeyValue) 