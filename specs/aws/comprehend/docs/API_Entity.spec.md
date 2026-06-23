---
id: "@specs/aws/comprehend/docs/API_Entity"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Entity"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# Entity

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_Entity
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Entity
<a name="API_Entity"></a>

Provides information about an entity. 

 

## Contents
<a name="API_Entity_Contents"></a>

 ** BeginOffset **   <a name="comprehend-Type-Entity-BeginOffset"></a>
The zero-based offset from the beginning of the source text to the first character in the entity.  
This field is empty for non-text input.  
Type: Integer  
Required: No

 ** BlockReferences **   <a name="comprehend-Type-Entity-BlockReferences"></a>
A reference to each block for this entity. This field is empty for plain-text input.  
Type: Array of [BlockReference](API_BlockReference.md) objects  
Required: No

 ** EndOffset **   <a name="comprehend-Type-Entity-EndOffset"></a>
The zero-based offset from the beginning of the source text to the last character in the entity.  
This field is empty for non-text input.  
Type: Integer  
Required: No

 ** Score **   <a name="comprehend-Type-Entity-Score"></a>
The level of confidence that Amazon Comprehend has in the accuracy of the detection.  
Type: Float  
Required: No

 ** Text **   <a name="comprehend-Type-Entity-Text"></a>
The text of the entity.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

 ** Type **   <a name="comprehend-Type-Entity-Type"></a>
The entity type. For entity detection using the built-in model, this field contains one of the standard entity types listed below.  
For custom entity detection, this field contains one of the entity types that you specified when you trained your custom model.  
Type: String  
Valid Values: `PERSON | LOCATION | ORGANIZATION | COMMERCIAL_ITEM | EVENT | DATE | QUANTITY | TITLE | OTHER`   
Required: No

## See Also
<a name="API_Entity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/Entity) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/Entity) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/Entity) 