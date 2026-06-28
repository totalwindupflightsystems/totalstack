---
id: "@specs/aws/transcribe/docs/API_UpdateCallAnalyticsCategory"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateCallAnalyticsCategory"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# UpdateCallAnalyticsCategory

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_UpdateCallAnalyticsCategory
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateCallAnalyticsCategory
<a name="API_UpdateCallAnalyticsCategory"></a>

Updates the specified Call Analytics category with new rules. Note that the `UpdateCallAnalyticsCategory` operation overwrites all existing rules contained in the specified category. You cannot append additional rules onto an existing category.

To create a new category, see [CreateCallAnalyticsCategory](API_CreateCallAnalyticsCategory.md).

## Request Syntax
<a name="API_UpdateCallAnalyticsCategory_RequestSyntax"></a>

```
{
   "CategoryName": "{{string}}",
   "InputType": "{{string}}",
   "Rules": [ 
      { ... }
   ]
}
```

## Request Parameters
<a name="API_UpdateCallAnalyticsCategory_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CategoryName](#API_UpdateCallAnalyticsCategory_RequestSyntax) **   <a name="transcribe-UpdateCallAnalyticsCategory-request-CategoryName"></a>
The name of the Call Analytics category you want to update. Category names are case sensitive.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+`   
Required: Yes

 ** [InputType](#API_UpdateCallAnalyticsCategory_RequestSyntax) **   <a name="transcribe-UpdateCallAnalyticsCategory-request-InputType"></a>
Choose whether you want to update a real-time or a post-call category. The input type you specify must match the input type specified when the category was created. For example, if you created a category with the `POST_CALL` input type, you must use `POST_CALL` as the input type when updating this category.  
Type: String  
Valid Values: `REAL_TIME | POST_CALL`   
Required: No

 ** [Rules](#API_UpdateCallAnalyticsCategory_RequestSyntax) **   <a name="transcribe-UpdateCallAnalyticsCategory-request-Rules"></a>
The rules used for the updated Call Analytics category. The rules you provide in this field replace the ones that are currently being used in the specified category.  
Type: Array of [Rule](API_Rule.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 20 items.  
Required: Yes

## Response Syntax
<a name="API_UpdateCallAnalyticsCategory_ResponseSyntax"></a>

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
<a name="API_UpdateCallAnalyticsCategory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CategoryProperties](#API_UpdateCallAnalyticsCategory_ResponseSyntax) **   <a name="transcribe-UpdateCallAnalyticsCategory-response-CategoryProperties"></a>
Provides you with the properties of the Call Analytics category you specified in your `UpdateCallAnalyticsCategory` request.  
Type: [CategoryProperties](API_CategoryProperties.md) object

## Errors
<a name="API_UpdateCallAnalyticsCategory_Errors"></a>

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

 ** NotFoundException **   
We can't find the requested resource. Check that the specified name is correct and try your request again.  
HTTP Status Code: 400

## See Also
<a name="API_UpdateCallAnalyticsCategory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transcribe-2017-10-26/UpdateCallAnalyticsCategory) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transcribe-2017-10-26/UpdateCallAnalyticsCategory) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/UpdateCallAnalyticsCategory) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transcribe-2017-10-26/UpdateCallAnalyticsCategory) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/UpdateCallAnalyticsCategory) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transcribe-2017-10-26/UpdateCallAnalyticsCategory) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transcribe-2017-10-26/UpdateCallAnalyticsCategory) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transcribe-2017-10-26/UpdateCallAnalyticsCategory) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/transcribe-2017-10-26/UpdateCallAnalyticsCategory) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/UpdateCallAnalyticsCategory) 