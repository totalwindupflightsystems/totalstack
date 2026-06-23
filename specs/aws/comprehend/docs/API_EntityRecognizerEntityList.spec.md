---
id: "@specs/aws/comprehend/docs/API_EntityRecognizerEntityList"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EntityRecognizerEntityList"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# EntityRecognizerEntityList

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_EntityRecognizerEntityList
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EntityRecognizerEntityList
<a name="API_EntityRecognizerEntityList"></a>

Describes the entity list submitted with an entity recognizer.

## Contents
<a name="API_EntityRecognizerEntityList_Contents"></a>

 ** S3Uri **   <a name="comprehend-Type-EntityRecognizerEntityList-S3Uri"></a>
Specifies the Amazon S3 location where the entity list is located. The URI must be in the same Region as the API endpoint that you are calling.  
Type: String  
Length Constraints: Maximum length of 1024.  
Pattern: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`   
Required: Yes

## See Also
<a name="API_EntityRecognizerEntityList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/EntityRecognizerEntityList) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/EntityRecognizerEntityList) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/EntityRecognizerEntityList) 