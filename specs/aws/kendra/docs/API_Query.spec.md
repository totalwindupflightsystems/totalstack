---
id: "@specs/aws/kendra/docs/API_Query"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Query"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# Query

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_Query
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Query
<a name="API_Query"></a>

Searches an index given an input query.

**Note**  
If you are working with large language models (LLMs) or implementing retrieval augmented generation (RAG) systems, you can use Amazon Kendra's [Retrieve](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Retrieve.html) API, which can return longer semantically relevant passages. We recommend using the `Retrieve` API instead of filing a service limit increase to increase the `Query` API document excerpt length.

You can configure boosting or relevance tuning at the query level to override boosting at the index level, filter based on document fields/attributes and faceted search, and filter based on the user or their group access to documents. You can also include certain fields in the response that might provide useful additional information.

A query response contains three types of results.
+ Relevant suggested answers. The answers can be either a text excerpt or table excerpt. The answer can be highlighted in the excerpt.
+ Matching FAQs or questions-answer from your FAQ file.
+ Relevant documents. This result type includes an excerpt of the document with the document title. The searched terms can be highlighted in the excerpt.

You can specify that the query return only one type of result using the `QueryResultTypeFilter` parameter. Each query returns the 100 most relevant results. If you filter result type to only question-answers, a maximum of four results are returned. If you filter result type to only answers, a maximum of three results are returned.

**Important**  
If you're using an Amazon Kendra Gen AI Enterprise Edition index, you can only use `ATTRIBUTE_FILTER` to filter search results by user context. If you're using an Amazon Kendra Gen AI Enterprise Edition index and you try to use `USER_TOKEN` to configure user context policy, Amazon Kendra returns a `ValidationException` error.

## Request Syntax
<a name="API_Query_RequestSyntax"></a>

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
   "CollapseConfiguration": { 
      "DocumentAttributeKey": "{{string}}",
      "Expand": {{boolean}},
      "ExpandConfiguration": { 
         "MaxExpandedResultsPerItem": {{number}},
         "MaxResultItemsToExpand": {{number}}
      },
      "MissingAttributeKeyStrategy": "{{string}}",
      "SortingConfigurations": [ 
         { 
            "DocumentAttributeKey": "{{string}}",
            "SortOrder": "{{string}}"
         }
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
   "Facets": [ 
      { 
         "DocumentAttributeKey": "{{string}}",
         "Facets": [ 
            "Facet"
         ],
         "MaxResults": {{number}}
      }
   ],
   "IndexId": "{{string}}",
   "PageNumber": {{number}},
   "PageSize": {{number}},
   "QueryResultTypeFilter": "{{string}}",
   "QueryText": "{{string}}",
   "RequestedDocumentAttributes": [ "{{string}}" ],
   "SortingConfiguration": { 
      "DocumentAttributeKey": "{{string}}",
      "SortOrder": "{{string}}"
   },
   "SortingConfigurations": [ 
      { 
         "DocumentAttributeKey": "{{string}}",
         "SortOrder": "{{string}}"
      }
   ],
   "SpellCorrectionConfiguration": { 
      "IncludeQuerySpellCheckSuggestions": {{boolean}}
   },
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
   },
   "VisitorId": "{{string}}"
}
```

## Request Parameters
<a name="API_Query_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AttributeFilter](#API_Query_RequestSyntax) **   <a name="kendra-Query-request-AttributeFilter"></a>
Filters search results by document fields/attributes. You can only provide one attribute filter; however, the `AndAllFilters`, `NotFilter`, and `OrAllFilters` parameters contain a list of other filters.  
The `AttributeFilter` parameter means you can create a set of filtering rules that a document must satisfy to be included in the query results.  
For Amazon Kendra Gen AI Enterprise Edition indices use `AttributeFilter` to enable document filtering for end users using `_email_id` or include public documents (`_email_id=null`).
Type: [AttributeFilter](API_AttributeFilter.md) object  
Required: No

 ** [CollapseConfiguration](#API_Query_RequestSyntax) **   <a name="kendra-Query-request-CollapseConfiguration"></a>
Provides configuration to determine how to group results by document attribute value, and how to display them (collapsed or expanded) under a designated primary document for each group.  
Type: [CollapseConfiguration](API_CollapseConfiguration.md) object  
Required: No

 ** [DocumentRelevanceOverrideConfigurations](#API_Query_RequestSyntax) **   <a name="kendra-Query-request-DocumentRelevanceOverrideConfigurations"></a>
Overrides relevance tuning configurations of fields/attributes set at the index level.  
If you use this API to override the relevance tuning configured at the index level, but there is no relevance tuning configured at the index level, then Amazon Kendra does not apply any relevance tuning.  
If there is relevance tuning configured for fields at the index level, and you use this API to override only some of these fields, then for the fields you did not override, the importance is set to 1.  
Type: Array of [DocumentRelevanceConfiguration](API_DocumentRelevanceConfiguration.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 500 items.  
Required: No

 ** [Facets](#API_Query_RequestSyntax) **   <a name="kendra-Query-request-Facets"></a>
An array of documents fields/attributes for faceted search. Amazon Kendra returns a count for each field key specified. This helps your users narrow their search.  
Type: Array of [Facet](API_Facet.md) objects  
Required: No

 ** [IndexId](#API_Query_RequestSyntax) **   <a name="kendra-Query-request-IndexId"></a>
The identifier of the index for the search.  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]*`   
Required: Yes

 ** [PageNumber](#API_Query_RequestSyntax) **   <a name="kendra-Query-request-PageNumber"></a>
Query results are returned in pages the size of the `PageSize` parameter. By default, Amazon Kendra returns the first page of results. Use this parameter to get result pages after the first one.  
Type: Integer  
Required: No

 ** [PageSize](#API_Query_RequestSyntax) **   <a name="kendra-Query-request-PageSize"></a>
Sets the number of results that are returned in each page of results. The default page size is 10. The maximum number of results returned is 100. If you ask for more than 100 results, only 100 are returned.  
Type: Integer  
Required: No

 ** [QueryResultTypeFilter](#API_Query_RequestSyntax) **   <a name="kendra-Query-request-QueryResultTypeFilter"></a>
Sets the type of query result or response. Only results for the specified type are returned.  
Type: String  
Valid Values: `DOCUMENT | QUESTION_ANSWER | ANSWER`   
Required: No

 ** [QueryText](#API_Query_RequestSyntax) **   <a name="kendra-Query-request-QueryText"></a>
The input query text for the search. Amazon Kendra truncates queries at 30 token words, which excludes punctuation and stop words. Truncation still applies if you use Boolean or more advanced, complex queries. For example, `Timeoff AND October AND Category:HR` is counted as 3 tokens: `timeoff`, `october`, `hr`. For more information, see [Searching with advanced query syntax](https://docs.aws.amazon.com/kendra/latest/dg/searching-example.html#searching-index-query-syntax) in the Amazon Kendra Developer Guide.   
Type: String  
Required: No

 ** [RequestedDocumentAttributes](#API_Query_RequestSyntax) **   <a name="kendra-Query-request-RequestedDocumentAttributes"></a>
An array of document fields/attributes to include in the response. You can limit the response to include certain document fields. By default, all document attributes are included in the response.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 100 items.  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `[a-zA-Z0-9_][a-zA-Z0-9_-]*`   
Required: No

 ** [SortingConfiguration](#API_Query_RequestSyntax) **   <a name="kendra-Query-request-SortingConfiguration"></a>
Provides information that determines how the results of the query are sorted. You can set the field that Amazon Kendra should sort the results on, and specify whether the results should be sorted in ascending or descending order. In the case of ties in sorting the results, the results are sorted by relevance.  
If you don't provide sorting configuration, the results are sorted by the relevance that Amazon Kendra determines for the result.  
Type: [SortingConfiguration](API_SortingConfiguration.md) object  
Required: No

 ** [SortingConfigurations](#API_Query_RequestSyntax) **   <a name="kendra-Query-request-SortingConfigurations"></a>
Provides configuration information to determine how the results of a query are sorted.  
You can set upto 3 fields that Amazon Kendra should sort the results on, and specify whether the results should be sorted in ascending or descending order. The sort field quota can be increased.  
If you don't provide a sorting configuration, the results are sorted by the relevance that Amazon Kendra determines for the result. In the case of ties in sorting the results, the results are sorted by relevance.   
Type: Array of [SortingConfiguration](API_SortingConfiguration.md) objects  
Array Members: Minimum number of 1 item.  
Required: No

 ** [SpellCorrectionConfiguration](#API_Query_RequestSyntax) **   <a name="kendra-Query-request-SpellCorrectionConfiguration"></a>
Enables suggested spell corrections for queries.  
Type: [SpellCorrectionConfiguration](API_SpellCorrectionConfiguration.md) object  
Required: No

 ** [UserContext](#API_Query_RequestSyntax) **   <a name="kendra-Query-request-UserContext"></a>
The user context token or user and group information.  
Type: [UserContext](API_UserContext.md) object  
Required: No

 ** [VisitorId](#API_Query_RequestSyntax) **   <a name="kendra-Query-request-VisitorId"></a>
Provides an identifier for a specific user. The `VisitorId` should be a unique identifier, such as a GUID. Don't use personally identifiable information, such as the user's email address, as the `VisitorId`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`   
Required: No

## Response Syntax
<a name="API_Query_ResponseSyntax"></a>

```
{
   "FacetResults": [ 
      { 
         "DocumentAttributeKey": "string",
         "DocumentAttributeValueCountPairs": [ 
            { 
               "Count": number,
               "DocumentAttributeValue": { 
                  "DateValue": number,
                  "LongValue": number,
                  "StringListValue": [ "string" ],
                  "StringValue": "string"
               },
               "FacetResults": [ 
                  "FacetResult"
               ]
            }
         ],
         "DocumentAttributeValueType": "string"
      }
   ],
   "FeaturedResultsItems": [ 
      { 
         "AdditionalAttributes": [ 
            { 
               "Key": "string",
               "Value": { 
                  "TextWithHighlightsValue": { 
                     "Highlights": [ 
                        { 
                           "BeginOffset": number,
                           "EndOffset": number,
                           "TopAnswer": boolean,
                           "Type": "string"
                        }
                     ],
                     "Text": "string"
                  }
               },
               "ValueType": "string"
            }
         ],
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
         "DocumentExcerpt": { 
            "Highlights": [ 
               { 
                  "BeginOffset": number,
                  "EndOffset": number,
                  "TopAnswer": boolean,
                  "Type": "string"
               }
            ],
            "Text": "string"
         },
         "DocumentId": "string",
         "DocumentTitle": { 
            "Highlights": [ 
               { 
                  "BeginOffset": number,
                  "EndOffset": number,
                  "TopAnswer": boolean,
                  "Type": "string"
               }
            ],
            "Text": "string"
         },
         "DocumentURI": "string",
         "FeedbackToken": "string",
         "Id": "string",
         "Type": "string"
      }
   ],
   "QueryId": "string",
   "ResultItems": [ 
      { 
         "AdditionalAttributes": [ 
            { 
               "Key": "string",
               "Value": { 
                  "TextWithHighlightsValue": { 
                     "Highlights": [ 
                        { 
                           "BeginOffset": number,
                           "EndOffset": number,
                           "TopAnswer": boolean,
                           "Type": "string"
                        }
                     ],
                     "Text": "string"
                  }
               },
               "ValueType": "string"
            }
         ],
         "CollapsedResultDetail": { 
            "DocumentAttribute": { 
               "Key": "string",
               "Value": { 
                  "DateValue": number,
                  "LongValue": number,
                  "StringListValue": [ "string" ],
                  "StringValue": "string"
               }
            },
            "ExpandedResults": [ 
               { 
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
                  "DocumentExcerpt": { 
                     "Highlights": [ 
                        { 
                           "BeginOffset": number,
                           "EndOffset": number,
                           "TopAnswer": boolean,
                           "Type": "string"
                        }
                     ],
                     "Text": "string"
                  },
                  "DocumentId": "string",
                  "DocumentTitle": { 
                     "Highlights": [ 
                        { 
                           "BeginOffset": number,
                           "EndOffset": number,
                           "TopAnswer": boolean,
                           "Type": "string"
                        }
                     ],
                     "Text": "string"
                  },
                  "DocumentURI": "string",
                  "Id": "string"
               }
            ]
         },
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
         "DocumentExcerpt": { 
            "Highlights": [ 
               { 
                  "BeginOffset": number,
                  "EndOffset": number,
                  "TopAnswer": boolean,
                  "Type": "string"
               }
            ],
            "Text": "string"
         },
         "DocumentId": "string",
         "DocumentTitle": { 
            "Highlights": [ 
               { 
                  "BeginOffset": number,
                  "EndOffset": number,
                  "TopAnswer": boolean,
                  "Type": "string"
               }
            ],
            "Text": "string"
         },
         "DocumentURI": "string",
         "FeedbackToken": "string",
         "Format": "string",
         "Id": "string",
         "ScoreAttributes": { 
            "ScoreConfidence": "string"
         },
         "TableExcerpt": { 
            "Rows": [ 
               { 
                  "Cells": [ 
                     { 
                        "Header": boolean,
                        "Highlighted": boolean,
                        "TopAnswer": boolean,
                        "Value": "string"
                     }
                  ]
               }
            ],
            "TotalNumberOfRows": number
         },
         "Type": "string"
      }
   ],
   "SpellCorrectedQueries": [ 
      { 
         "Corrections": [ 
            { 
               "BeginOffset": number,
               "CorrectedTerm": "string",
               "EndOffset": number,
               "Term": "string"
            }
         ],
         "SuggestedQueryText": "string"
      }
   ],
   "TotalNumberOfResults": number,
   "Warnings": [ 
      { 
         "Code": "string",
         "Message": "string"
      }
   ]
}
```

## Response Elements
<a name="API_Query_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FacetResults](#API_Query_ResponseSyntax) **   <a name="kendra-Query-response-FacetResults"></a>
Contains the facet results. A `FacetResult` contains the counts for each field/attribute key that was specified in the `Facets` input parameter.  
Type: Array of [FacetResult](API_FacetResult.md) objects

 ** [FeaturedResultsItems](#API_Query_ResponseSyntax) **   <a name="kendra-Query-response-FeaturedResultsItems"></a>
The list of featured result items. Featured results are displayed at the top of the search results page, placed above all other results for certain queries. If there's an exact match of a query, then certain documents are featured in the search results.  
Type: Array of [FeaturedResultsItem](API_FeaturedResultsItem.md) objects

 ** [QueryId](#API_Query_ResponseSyntax) **   <a name="kendra-Query-response-QueryId"></a>
The identifier for the search. You also use `QueryId` to identify the search when using the [SubmitFeedback](https://docs.aws.amazon.com/kendra/latest/APIReference/API_SubmitFeedback.html) API.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 36.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]*` 

 ** [ResultItems](#API_Query_ResponseSyntax) **   <a name="kendra-Query-response-ResultItems"></a>
The results of the search.  
Type: Array of [QueryResultItem](API_QueryResultItem.md) objects

 ** [SpellCorrectedQueries](#API_Query_ResponseSyntax) **   <a name="kendra-Query-response-SpellCorrectedQueries"></a>
A list of information related to suggested spell corrections for a query.  
Type: Array of [SpellCorrectedQuery](API_SpellCorrectedQuery.md) objects

 ** [TotalNumberOfResults](#API_Query_ResponseSyntax) **   <a name="kendra-Query-response-TotalNumberOfResults"></a>
The total number of items found by the search. However, you can only retrieve up to 100 items. For example, if the search found 192 items, you can only retrieve the first 100 of the items.  
Type: Integer

 ** [Warnings](#API_Query_ResponseSyntax) **   <a name="kendra-Query-response-Warnings"></a>
A list of warning codes and their messages on problems with your query.  
Amazon Kendra currently only supports one type of warning, which is a warning on invalid syntax used in the query. For examples of invalid query syntax, see [Searching with advanced query syntax](https://docs.aws.amazon.com/kendra/latest/dg/searching-example.html#searching-index-query-syntax).  
Type: Array of [Warning](API_Warning.md) objects  
Array Members: Fixed number of 1 item.

## Errors
<a name="API_Query_Errors"></a>

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
<a name="API_Query_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kendra-2019-02-03/Query) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kendra-2019-02-03/Query) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/Query) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kendra-2019-02-03/Query) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/Query) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kendra-2019-02-03/Query) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kendra-2019-02-03/Query) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kendra-2019-02-03/Query) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kendra-2019-02-03/Query) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/Query) 