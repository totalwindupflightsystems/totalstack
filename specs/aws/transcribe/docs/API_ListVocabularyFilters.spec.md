---
id: "@specs/aws/transcribe/docs/API_ListVocabularyFilters"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListVocabularyFilters"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# ListVocabularyFilters

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_ListVocabularyFilters
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListVocabularyFilters
<a name="API_ListVocabularyFilters"></a>

Provides a list of custom vocabulary filters that match the specified criteria. If no criteria are specified, all custom vocabularies are returned.

To get detailed information about a specific custom vocabulary filter, use the [GetVocabularyFilter](API_GetVocabularyFilter.md) operation.

## Request Syntax
<a name="API_ListVocabularyFilters_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NameContains": "{{string}}",
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListVocabularyFilters_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListVocabularyFilters_RequestSyntax) **   <a name="transcribe-ListVocabularyFilters-request-MaxResults"></a>
The maximum number of custom vocabulary filters to return in each page of results. If there are fewer results than the value that you specify, only the actual results are returned. If you do not specify a value, a default of 5 is used.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [NameContains](#API_ListVocabularyFilters_RequestSyntax) **   <a name="transcribe-ListVocabularyFilters-request-NameContains"></a>
Returns only the custom vocabulary filters that contain the specified string. The search is not case sensitive.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+`   
Required: No

 ** [NextToken](#API_ListVocabularyFilters_RequestSyntax) **   <a name="transcribe-ListVocabularyFilters-request-NextToken"></a>
If your `ListVocabularyFilters` request returns more results than can be displayed, `NextToken` is displayed in the response with an associated string. To get the next page of results, copy this string and repeat your request, including `NextToken` with the value of the copied string. Repeat as needed to view all your results.  
Type: String  
Length Constraints: Maximum length of 8192.  
Pattern: `.+`   
Required: No

## Response Syntax
<a name="API_ListVocabularyFilters_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "VocabularyFilters": [ 
      { 
         "LanguageCode": "string",
         "LastModifiedTime": number,
         "VocabularyFilterName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListVocabularyFilters_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListVocabularyFilters_ResponseSyntax) **   <a name="transcribe-ListVocabularyFilters-response-NextToken"></a>
If `NextToken` is present in your response, it indicates that not all results are displayed. To view the next set of results, copy the string associated with the `NextToken` parameter in your results output, then run your request again including `NextToken` with the value of the copied string. Repeat as needed to view all your results.  
Type: String  
Length Constraints: Maximum length of 8192.  
Pattern: `.+` 

 ** [VocabularyFilters](#API_ListVocabularyFilters_ResponseSyntax) **   <a name="transcribe-ListVocabularyFilters-response-VocabularyFilters"></a>
Provides information about the custom vocabulary filters that match the criteria specified in your request.  
Type: Array of [VocabularyFilterInfo](API_VocabularyFilterInfo.md) objects

## Errors
<a name="API_ListVocabularyFilters_Errors"></a>

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

## See Also
<a name="API_ListVocabularyFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transcribe-2017-10-26/ListVocabularyFilters) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transcribe-2017-10-26/ListVocabularyFilters) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/ListVocabularyFilters) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transcribe-2017-10-26/ListVocabularyFilters) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/ListVocabularyFilters) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transcribe-2017-10-26/ListVocabularyFilters) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transcribe-2017-10-26/ListVocabularyFilters) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transcribe-2017-10-26/ListVocabularyFilters) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/transcribe-2017-10-26/ListVocabularyFilters) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/ListVocabularyFilters) 