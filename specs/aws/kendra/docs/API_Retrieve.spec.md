---
id: "@specs/aws/kendra/docs/API_Retrieve"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Retrieve"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# Retrieve

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_Retrieve
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Retrieve
<a name="API_Retrieve"></a>

Retrieves relevant passages or text excerpts given an input query.

This API is similar to the [Query](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Query.html) API. However, by default, the `Query` API only returns excerpt passages of up to 100 token words. With the `Retrieve` API, you can retrieve longer passages of up to 200 token words and up to 100 semantically relevant passages. This doesn't include question-answer or FAQ type responses from your index. The passages are text excerpts that can be semantically extracted from multiple documents and multiple parts of the same document. If in extreme cases your documents produce zero passages using the `Retrieve` API, you can alternatively use the `Query` API and its types of responses.

You can also do the following:
+ Override boosting at the index level
+ Filter based on document fields or attributes
+ Filter based on the user or their group access to documents
+ View the confidence score bucket for a retrieved passage result. The confidence bucket provides a relative ranking that indicates how confident Amazon Kendra is that the response is relevant to the query.
**Note**  
Confidence score buckets are currently available only for English.

You can also include certain fields in the response that might provide useful additional information.

The `Retrieve` API shares the number of [query capacity units](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CapacityUnitsConfiguration.html) that you set for your index. For more information on what's included in a single capacity unit and the default base capacity for an index, see [Adjusting capacity](https://docs.aws.amazon.com/kendra/latest/dg/adjusting-capacity.html).

**Important**  
If you're using an Amazon Kendra Gen AI Enterprise Edition index, you can only use `ATTRIBUTE_FILTER` to filter search results by user context. If you're using an Amazon Kendra Gen AI Enterprise Edition index and you try to use `USER_TOKEN` to configure user context policy, Amazon Kendra returns a `ValidationException` error.

## Request Syntax
<a name="API_Retrieve_RequestSyntax"></a>

```
{
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
   "DocumentRelevanceOverrideConfigurations": [ 
      { 
         "Name": "{{string}}",
         "Relevance": { 
            "Duration": "{{string}}",
            "Freshness": {{boolean}},
            "Importance": {{number}},
            "RankOrder": "{{string}}",
            "ValueImportanceMap": { 
               "{{string}}" : {{number}} 
            }
         }
      }
   ],
   "IndexId": "{{string}}",
   "PageNumber": {{number}},
   "PageSize": {{number}},
   "QueryText": "{{string}}",
   "RequestedDocumentAttributes": [ "{{string}}" ],
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
}
```

## Request Parameters
<a name="API_Retrieve_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AttributeFilter](#API_Retrieve_RequestSyntax) **   <a name="kendra-Retrieve-request-AttributeFilter"></a>
Filters search results by document fields/attributes. You can only provide one attribute filter; however, the `AndAllFilters`, `NotFilter`, and `OrAllFilters` parameters contain a list of other filters.  
The `AttributeFilter` parameter means you can create a set of filtering rules that a document must satisfy to be included in the query results.  
For Amazon Kendra Gen AI Enterprise Edition indices use `AttributeFilter` to enable document filtering for end users using `_email_id` or include public documents (`_email_id=null`).
Type: [AttributeFilter](API_AttributeFilter.md) object  
Required: No

 ** [DocumentRelevanceOverrideConfigurations](#API_Retrieve_RequestSyntax) **   <a name="kendra-Retrieve-request-DocumentRelevanceOverrideConfigurations"></a>
Overrides relevance tuning configurations of fields/attributes set at the index level.  
If you use this API to override the relevance tuning configured at the index level, but there is no relevance tuning configured at the index level, then Amazon Kendra does not apply any relevance tuning.  
If there is relevance tuning configured for fields at the index level, and you use this API to override only some of these fields, then for the fields you did not override, the importance is set to 1.  
Type: Array of [DocumentRelevanceConfiguration](API_DocumentRelevanceConfiguration.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 500 items.  
Required: No

 ** [IndexId](#API_Retrieve_RequestSyntax) **   <a name="kendra-Retrieve-request-IndexId"></a>
The identifier of the index to retrieve relevant passages for the search.  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]*`   
Required: Yes

 ** [PageNumber](#API_Retrieve_RequestSyntax) **   <a name="kendra-Retrieve-request-PageNumber"></a>
Retrieved relevant passages are returned in pages the size of the `PageSize` parameter. By default, Amazon Kendra returns the first page of results. Use this parameter to get result pages after the first one.  
Type: Integer  
Required: No

 ** [PageSize](#API_Retrieve_RequestSyntax) **   <a name="kendra-Retrieve-request-PageSize"></a>
Sets the number of retrieved relevant passages that are returned in each page of results. The default page size is 10. The maximum number of results returned is 100. If you ask for more than 100 results, only 100 are returned.  
Type: Integer  
Required: No

 ** [QueryText](#API_Retrieve_RequestSyntax) **   <a name="kendra-Retrieve-request-QueryText"></a>
The input query text to retrieve relevant passages for the search. Amazon Kendra truncates queries at 30 token words, which excludes punctuation and stop words. Truncation still applies if you use Boolean or more advanced, complex queries. For example, `Timeoff AND October AND Category:HR` is counted as 3 tokens: `timeoff`, `october`, `hr`. For more information, see [Searching with advanced query syntax](https://docs.aws.amazon.com/kendra/latest/dg/searching-example.html#searching-index-query-syntax) in the Amazon Kendra Developer Guide.   
Type: String  
Required: Yes

 ** [RequestedDocumentAttributes](#API_Retrieve_RequestSyntax) **   <a name="kendra-Retrieve-request-RequestedDocumentAttributes"></a>
A list of document fields/attributes to include in the response. You can limit the response to include certain document fields. By default, all document fields are included in the response.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 100 items.  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `[a-zA-Z0-9_][a-zA-Z0-9_-]*`   
Required: No

 ** [UserContext](#API_Retrieve_RequestSyntax) **   <a name="kendra-Retrieve-request-UserContext"></a>
The user context token or user and group information.  
Type: [UserContext](API_UserContext.md) object  
Required: No

## Response Syntax
<a name="API_Retrieve_ResponseSyntax"></a>

```
{
   "QueryId": "string",
   "ResultItems": [ 
      { 
         "Content": "string",
         "DocumentAttributes": [ 
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
         "DocumentTitle": "string",
         "DocumentURI": "string",
         "Id": "string",
         "ScoreAttributes": { 
            "ScoreConfidence": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_Retrieve_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [QueryId](#API_Retrieve_ResponseSyntax) **   <a name="kendra-Retrieve-response-QueryId"></a>
The identifier of query used for the search. You also use `QueryId` to identify the search when using the [Submitfeedback](https://docs.aws.amazon.com/kendra/latest/APIReference/API_SubmitFeedback.html) API.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 36.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]*` 

 ** [ResultItems](#API_Retrieve_ResponseSyntax) **   <a name="kendra-Retrieve-response-ResultItems"></a>
The results of the retrieved relevant passages for the search.  
Type: Array of [RetrieveResultItem](API_RetrieveResultItem.md) objects

## Errors
<a name="API_Retrieve_Errors"></a>

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
<a name="API_Retrieve_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kendra-2019-02-03/Retrieve) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kendra-2019-02-03/Retrieve) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/Retrieve) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kendra-2019-02-03/Retrieve) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/Retrieve) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kendra-2019-02-03/Retrieve) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kendra-2019-02-03/Retrieve) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kendra-2019-02-03/Retrieve) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kendra-2019-02-03/Retrieve) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/Retrieve) 