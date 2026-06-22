---
id: "@specs/aws/emr/docs/API_PersistentAppUI"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PersistentAppUI"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# PersistentAppUI

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_PersistentAppUI
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PersistentAppUI
<a name="API_PersistentAppUI"></a>

Holds persistent application user interface information. Applications installed on the Amazon EMR cluster publish user interfaces as web sites to monitor cluster activity.

## Contents
<a name="API_PersistentAppUI_Contents"></a>

 ** AuthorId **   <a name="EMR-Type-PersistentAppUI-AuthorId"></a>
The author ID for the persistent application user interface object.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** CreationTime **   <a name="EMR-Type-PersistentAppUI-CreationTime"></a>
The creation date and time for the persistent application user interface object.  
Type: Timestamp  
Required: No

 ** LastModifiedTime **   <a name="EMR-Type-PersistentAppUI-LastModifiedTime"></a>
The date and time the persistent application user interface object was last changed.  
Type: Timestamp  
Required: No

 ** LastStateChangeReason **   <a name="EMR-Type-PersistentAppUI-LastStateChangeReason"></a>
The reason the persistent application user interface object was last changed.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** PersistentAppUIId **   <a name="EMR-Type-PersistentAppUI-PersistentAppUIId"></a>
The identifier for the persistent application user interface object.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** PersistentAppUIStatus **   <a name="EMR-Type-PersistentAppUI-PersistentAppUIStatus"></a>
The status for the persistent application user interface object.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** PersistentAppUITypeList **   <a name="EMR-Type-PersistentAppUI-PersistentAppUITypeList"></a>
The type list for the persistent application user interface object. Valid values include SHS, YTS, or TEZ.  
Type: Array of strings  
Valid Values: `SHS | TEZ | YTS`   
Required: No

 ** Tags **   <a name="EMR-Type-PersistentAppUI-Tags"></a>
A collection of tags for the persistent application user interface object.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## See Also
<a name="API_PersistentAppUI_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/PersistentAppUI) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/PersistentAppUI) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/PersistentAppUI) 