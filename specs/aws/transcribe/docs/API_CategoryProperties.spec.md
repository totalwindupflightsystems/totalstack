---
id: "@specs/aws/transcribe/docs/API_CategoryProperties"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CategoryProperties"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# CategoryProperties

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_CategoryProperties
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CategoryProperties
<a name="API_CategoryProperties"></a>

Provides you with the properties of the Call Analytics category you specified in your request. This includes the list of rules that define the specified category.

## Contents
<a name="API_CategoryProperties_Contents"></a>

 ** CategoryName **   <a name="transcribe-Type-CategoryProperties-CategoryName"></a>
The name of the Call Analytics category. Category names are case sensitive and must be unique within an AWS account.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+`   
Required: No

 ** CreateTime **   <a name="transcribe-Type-CategoryProperties-CreateTime"></a>
The date and time the specified Call Analytics category was created.  
Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC`. For example, `2022-05-04T12:32:58.761000-07:00` represents 12:32 PM UTC-7 on May 4, 2022.  
Type: Timestamp  
Required: No

 ** InputType **   <a name="transcribe-Type-CategoryProperties-InputType"></a>
The input type associated with the specified category. `POST_CALL` refers to a category that is applied to batch transcriptions; `REAL_TIME` refers to a category that is applied to streaming transcriptions.  
Type: String  
Valid Values: `REAL_TIME | POST_CALL`   
Required: No

 ** LastUpdateTime **   <a name="transcribe-Type-CategoryProperties-LastUpdateTime"></a>
The date and time the specified Call Analytics category was last updated.  
Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC`. For example, `2022-05-05T12:45:32.691000-07:00` represents 12:45 PM UTC-7 on May 5, 2022.  
Type: Timestamp  
Required: No

 ** Rules **   <a name="transcribe-Type-CategoryProperties-Rules"></a>
The rules used to define a Call Analytics category. Each category can have between 1 and 20 rules.  
Type: Array of [Rule](API_Rule.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 20 items.  
Required: No

 ** Tags **   <a name="transcribe-Type-CategoryProperties-Tags"></a>
The tags, each in the form of a key:value pair, assigned to the specified call analytics category.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.  
Required: No

## See Also
<a name="API_CategoryProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/CategoryProperties) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/CategoryProperties) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/CategoryProperties) 