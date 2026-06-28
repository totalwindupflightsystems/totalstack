---
id: "@specs/aws/transcribe/docs/API_CreateCallAnalyticsCategory"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateCallAnalyticsCategory"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# CreateCallAnalyticsCategory

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_CreateCallAnalyticsCategory
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateCallAnalyticsCategory
<a name="API_CreateCallAnalyticsCategory"></a>

Creates a new Call Analytics category.

All categories are automatically applied to your Call Analytics transcriptions. Note that in order to apply categories to your transcriptions, you must create them before submitting your transcription request, as categories cannot be applied retroactively.

When creating a new category, you can use the `InputType` parameter to label the category as a `POST_CALL` or a `REAL_TIME` category. `POST_CALL` categories can only be applied to post-call transcriptions and `REAL_TIME` categories can only be applied to real-time transcriptions. If you do not include `InputType`, your category is created as a `POST_CALL` category by default.

Call Analytics categories are composed of rules. For each category, you must create between 1 and 20 rules. Rules can include these parameters: [InterruptionFilter](API_InterruptionFilter.md), [NonTalkTimeFilter](API_NonTalkTimeFilter.md), [SentimentFilter](API_SentimentFilter.md), and [TranscriptFilter](API_TranscriptFilter.md).

To update an existing category, see [UpdateCallAnalyticsCategory](API_UpdateCallAnalyticsCategory.md).

To learn more about Call Analytics categories, see [Creating categories for post-call transcriptions](https://docs.aws.amazon.com/transcribe/latest/dg/tca-categories-batch.html) and [Creating categories for real-time transcriptions](https://docs.aws.amazon.com/transcribe/latest/dg/tca-categories-stream.html).

## Request Syntax
<a name="API_CreateCallAnalyticsCategory_RequestSyntax"></a>

```
{
   "CategoryName": "{{string}}",
   "InputType": "{{string}}",
   "Rules": [ 
      { ... }
   ],
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateCallAnalyticsCategory_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CategoryName](#API_CreateCallAnalyticsCategory_RequestSyntax) **   <a name="transcribe-CreateCallAnalyticsCategory-request-CategoryName"></a>
A unique name, chosen by you, for your Call Analytics category. It's helpful to use a detailed naming system that will make sense to you in the future. For example, it's better to use `sentiment-positive-last30seconds` for a category over a generic name like `test-category`.  
Category names are case sensitive.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+`   
Required: Yes

 ** [InputType](#API_CreateCallAnalyticsCategory_RequestSyntax) **   <a name="transcribe-CreateCallAnalyticsCategory-request-InputType"></a>
Choose whether you want to create a real-time or a post-call category for your Call Analytics transcription.  
Specifying `POST_CALL` assigns your category to post-call transcriptions; categories with this input type cannot be applied to streaming (real-time) transcriptions.  
Specifying `REAL_TIME` assigns your category to streaming transcriptions; categories with this input type cannot be applied to post-call transcriptions.  
If you do not include `InputType`, your category is created as a post-call category by default.  
Type: String  
Valid Values: `REAL_TIME | POST_CALL`   
Required: No

 ** [Rules](#API_CreateCallAnalyticsCategory_RequestSyntax) **   <a name="transcribe-CreateCallAnalyticsCategory-request-Rules"></a>
Rules define a Call Analytics category. When creating a new category, you must create between 1 and 20 rules for that category. For each rule, you specify a filter you want applied to the attributes of a call. For example, you can choose a sentiment filter that detects if a customer's sentiment was positive during the last 30 seconds of the call.  
Type: Array of [Rule](API_Rule.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 20 items.  
Required: Yes

 ** [Tags](#API_CreateCallAnalyticsCategory_RequestSyntax) **   <a name="transcribe-CreateCallAnalyticsCategory-request-Tags"></a>
Adds one or more custom tags, each in the form of a key:value pair, to a new call analytics category at the time you start this new job.  
To learn more about using tags with Amazon Transcribe, refer to [Tagging resources](https://docs.aws.amazon.com/transcribe/latest/dg/tagging.html).  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.  
Required: No

## Response Syntax
<a name="API_CreateCallAnalyticsCategory_ResponseSyntax"></a>

```
{
   "CategoryProperties": { 
      "CategoryName": "string",
      "CreateTime": number,
      "InputType": "string",
      "LastUpdateTime": number,
      "Rules": [ 
         { ... }
      ],
      "Tags": [ 
         { 
            "Key": "string",
            "Value": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_CreateCallAnalyticsCategory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CategoryProperties](#API_CreateCallAnalyticsCategory_ResponseSyntax) **   <a name="transcribe-CreateCallAnalyticsCategory-response-CategoryProperties"></a>
Provides you with the properties of your new category, including its associated rules.  
Type: [CategoryProperties](API_CategoryProperties.md) object

## Errors
<a name="API_CreateCallAnalyticsCategory_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as `IN PROGRESS`). See the exception message field for more information.  
HTTP Status Code: 400

 ** ConflictException **   
A resource already exists with this name. Resource names must be unique within an AWS account.  
HTTP Status Code: 400

 ** InternalFailureException **   
There was an internal error. Check the error message, correct the issue, and try your request again.  
HTTP Status Code: 500

 ** LimitExceededException **   
You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.  
HTTP Status Code: 400

## See Also
<a name="API_CreateCallAnalyticsCategory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transcribe-2017-10-26/CreateCallAnalyticsCategory) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transcribe-2017-10-26/CreateCallAnalyticsCategory) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/CreateCallAnalyticsCategory) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transcribe-2017-10-26/CreateCallAnalyticsCategory) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/CreateCallAnalyticsCategory) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transcribe-2017-10-26/CreateCallAnalyticsCategory) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transcribe-2017-10-26/CreateCallAnalyticsCategory) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transcribe-2017-10-26/CreateCallAnalyticsCategory) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/transcribe-2017-10-26/CreateCallAnalyticsCategory) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/CreateCallAnalyticsCategory) 