---
id: "@specs/aws/kendra/docs/API_GetQuerySuggestions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetQuerySuggestions"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# GetQuerySuggestions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_GetQuerySuggestions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetQuerySuggestions
<a name="API_GetQuerySuggestions"></a>

Fetches the queries that are suggested to your users.

 `GetQuerySuggestions` is currently not supported in the AWS GovCloud (US-West) region.

## Request Syntax
<a name="API_GetQuerySuggestions_RequestSyntax"></a>

```
{
   "AttributeSuggestionsConfig": { 
      "AdditionalResponseAttributes": [ "{{string}}" ],
      "AttributeFilter": { 
         "AndAllFilters": [ 
            "AttributeFilter"
         ],
         "ContainsAll": { 
            "Key": "{{string}}",
            "Value": { 
               "DateValue": {{number}},
               "LongValue": {{number}},
               "StringListValue": [ "{{string}}" ],
               "StringValue": "{{string}}"
            }
         },
         "ContainsAny": { 
            "Key": "{{string}}",
            "Value": { 
               "DateValue": {{number}},
               "LongValue": {{number}},
               "StringListValue": [ "{{string}}" ],
               "StringValue": "{{string}}"
            }
         },
         "EqualsTo": { 
            "Key": "{{string}}",
            "Value": { 
               "DateValue": {{number}},
               "LongValue": {{number}},
               "StringListValue": [ "{{string}}" ],
               "StringValue": "{{string}}"
            }
         },
         "GreaterThan": { 
            "Key": "{{string}}",
            "Value": { 
               "DateValue": {{number}},
               "LongValue": {{number}},
               "StringListValue": [ "{{string}}" ],
               "StringValue": "{{string}}"
            }
         },
         "GreaterThanOrEquals": { 
            "Key": "{{string}}",
            "Value": { 
               "DateValue": {{number}},
               "LongValue": {{number}},
               "StringListValue": [ "{{string}}" ],
               "StringValue": "{{string}}"
            }
         },
         "LessThan": { 
            "Key": "{{string}}",
            "Value": { 
               "DateValue": {{number}},
               "LongValue": {{number}},
               "StringListValue": [ "{{string}}" ],
               "StringValue": "{{string}}"
            }
         },
         "LessThanOrEquals": { 
            "Key": "{{string}}",
            "Value": { 
               "DateValue": {{number}},
               "LongValue": {{number}},
               "StringListValue": [ "{{string}}" ],
               "StringValue": "{{string}}"
            }
         },
         "NotFilter": "AttributeFilter",
         "OrAllFilters": [ 
            "AttributeFilter"
         ]
      },
      "SuggestionAttributes": [ "{{string}}" ],
      "UserContext": { 
         "DataSourceGroups": [ 
            { 
               "DataSourceId": "{{string}}",
               "GroupId": "{{string}}"
            }
         ],
         "Groups": [ "{{string}}" ],
         "Token": "{{string}}",
         "UserId": "{{string}}"
      }
   },
   "IndexId": "{{string}}",
   "MaxSuggestionsCount": {{number}},
   "QueryText": "{{string}}",
   "SuggestionTypes": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_GetQuerySuggestions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AttributeSuggestionsConfig](#API_GetQuerySuggestions_RequestSyntax) **   <a name="kendra-GetQuerySuggestions-request-AttributeSuggestionsConfig"></a>
Configuration information for the document fields/attributes that you want to base query suggestions on.  
Type: [AttributeSuggestionsGetConfig](API_AttributeSuggestionsGetConfig.md) object  
Required: No

 ** [IndexId](#API_GetQuerySuggestions_RequestSyntax) **   <a name="kendra-GetQuerySuggestions-request-IndexId"></a>
The identifier of the index you want to get query suggestions from.  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]*`   
Required: Yes

 ** [MaxSuggestionsCount](#API_GetQuerySuggestions_RequestSyntax) **   <a name="kendra-GetQuerySuggestions-request-MaxSuggestionsCount"></a>
The maximum number of query suggestions you want to show to your users.  
Type: Integer  
Required: No

 ** [QueryText](#API_GetQuerySuggestions_RequestSyntax) **   <a name="kendra-GetQuerySuggestions-request-QueryText"></a>
The text of a user's query to generate query suggestions.  
A query is suggested if the query prefix matches what a user starts to type as their query.  
Amazon Kendra does not show any suggestions if a user types fewer than two characters or more than 60 characters. A query must also have at least one search result and contain at least one word of more than four characters.  
Type: String  
Pattern: `^\P{C}*$`   
Required: Yes

 ** [SuggestionTypes](#API_GetQuerySuggestions_RequestSyntax) **   <a name="kendra-GetQuerySuggestions-request-SuggestionTypes"></a>
The suggestions type to base query suggestions on. The suggestion types are query history or document fields/attributes. You can set one type or the other.  
If you set query history as your suggestions type, Amazon Kendra suggests queries relevant to your users based on popular queries in the query history.  
If you set document fields/attributes as your suggestions type, Amazon Kendra suggests queries relevant to your users based on the contents of document fields.  
Type: Array of strings  
Valid Values: `QUERY | DOCUMENT_ATTRIBUTES`   
Required: No

## Response Syntax
<a name="API_GetQuerySuggestions_ResponseSyntax"></a>

```
{
   "QuerySuggestionsId": "string",
   "Suggestions": [ 
      { 
         "Id": "string",
         "SourceDocuments": [ 
            { 
               "AdditionalAttributes": [ 
                  { 
                     "Key": "string",
                     "Value": { 
                        "DateValue": number,
                        "LongValue": number,
                        "StringListValue": [ "string" ],
                        "StringValue": "string"
                     }
                  }
               ],
               "DocumentId": "string",
               "SuggestionAttributes": [ "string" ]
            }
         ],
         "Value": { 
            "Text": { 
               "Highlights": [ 
                  { 
                     "BeginOffset": number,
                     "EndOffset": number
                  }
               ],
               "Text": "string"
            }
         }
      }
   ]
}
```

## Response Elements
<a name="API_GetQuerySuggestions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [QuerySuggestionsId](#API_GetQuerySuggestions_ResponseSyntax) **   <a name="kendra-GetQuerySuggestions-response-QuerySuggestionsId"></a>
The identifier for a list of query suggestions for an index.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 36.

 ** [Suggestions](#API_GetQuerySuggestions_ResponseSyntax) **   <a name="kendra-GetQuerySuggestions-response-Suggestions"></a>
A list of query suggestions for an index.  
Type: Array of [Suggestion](API_Suggestion.md) objects

## Errors
<a name="API_GetQuerySuggestions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.  
HTTP Status Code: 400

 ** ConflictException **   
A conflict occurred with the request. Please fix any inconsistences with your resources and try again.  
HTTP Status Code: 400

 ** InternalServerException **   
An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact [Support](http://aws.amazon.com/contact-us/) for help.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.  
HTTP Status Code: 400

 ** ServiceQuotaExceededException **   
You have exceeded the set limits for your Amazon Kendra service. Please see [Quotas](https://docs.aws.amazon.com/kendra/latest/dg/quotas.html) for more information, or contact [Support](http://aws.amazon.com/contact-us/) to inquire about an increase of limits.  
HTTP Status Code: 400

 ** ThrottlingException **   
The request was denied due to request throttling. Please reduce the number of requests and try again.  
HTTP Status Code: 400

 ** ValidationException **   
The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.  
HTTP Status Code: 400

## See Also
<a name="API_GetQuerySuggestions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kendra-2019-02-03/GetQuerySuggestions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kendra-2019-02-03/GetQuerySuggestions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/GetQuerySuggestions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kendra-2019-02-03/GetQuerySuggestions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/GetQuerySuggestions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kendra-2019-02-03/GetQuerySuggestions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kendra-2019-02-03/GetQuerySuggestions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kendra-2019-02-03/GetQuerySuggestions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kendra-2019-02-03/GetQuerySuggestions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/GetQuerySuggestions) 