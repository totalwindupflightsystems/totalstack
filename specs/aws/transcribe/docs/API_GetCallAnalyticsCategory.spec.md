---
id: "@specs/aws/transcribe/docs/API_GetCallAnalyticsCategory"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetCallAnalyticsCategory"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# GetCallAnalyticsCategory

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_GetCallAnalyticsCategory
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetCallAnalyticsCategory
<a name="API_GetCallAnalyticsCategory"></a>

Provides information about the specified Call Analytics category.

To get a list of your Call Analytics categories, use the [ListCallAnalyticsCategories](API_ListCallAnalyticsCategories.md) operation.

## Request Syntax
<a name="API_GetCallAnalyticsCategory_RequestSyntax"></a>

```
{
   "CategoryName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetCallAnalyticsCategory_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CategoryName](#API_GetCallAnalyticsCategory_RequestSyntax) **   <a name="transcribe-GetCallAnalyticsCategory-request-CategoryName"></a>
The name of the Call Analytics category you want information about. Category names are case sensitive.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+`   
Required: Yes

## Response Syntax
<a name="API_GetCallAnalyticsCategory_ResponseSyntax"></a>

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
<a name="API_GetCallAnalyticsCategory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CategoryProperties](#API_GetCallAnalyticsCategory_ResponseSyntax) **   <a name="transcribe-GetCallAnalyticsCategory-response-CategoryProperties"></a>
Provides you with the properties of the Call Analytics category you specified in your `GetCallAnalyticsCategory` request.  
Type: [CategoryProperties](API_CategoryProperties.md) object

## Errors
<a name="API_GetCallAnalyticsCategory_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as `IN PROGRESS`). See the exception message field for more information.  
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
<a name="API_GetCallAnalyticsCategory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transcribe-2017-10-26/GetCallAnalyticsCategory) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transcribe-2017-10-26/GetCallAnalyticsCategory) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/GetCallAnalyticsCategory) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transcribe-2017-10-26/GetCallAnalyticsCategory) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/GetCallAnalyticsCategory) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transcribe-2017-10-26/GetCallAnalyticsCategory) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transcribe-2017-10-26/GetCallAnalyticsCategory) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transcribe-2017-10-26/GetCallAnalyticsCategory) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/transcribe-2017-10-26/GetCallAnalyticsCategory) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/GetCallAnalyticsCategory) 