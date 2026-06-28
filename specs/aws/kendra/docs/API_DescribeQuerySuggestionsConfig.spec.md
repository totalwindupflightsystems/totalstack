---
id: "@specs/aws/kendra/docs/API_DescribeQuerySuggestionsConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeQuerySuggestionsConfig"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# DescribeQuerySuggestionsConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_DescribeQuerySuggestionsConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeQuerySuggestionsConfig
<a name="API_DescribeQuerySuggestionsConfig"></a>

Gets information on the settings of query suggestions for an index.

This is used to check the current settings applied to query suggestions.

 `DescribeQuerySuggestionsConfig` is currently not supported in the AWS GovCloud (US-West) region.

## Request Syntax
<a name="API_DescribeQuerySuggestionsConfig_RequestSyntax"></a>

```
{
   "IndexId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeQuerySuggestionsConfig_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [IndexId](#API_DescribeQuerySuggestionsConfig_RequestSyntax) **   <a name="kendra-DescribeQuerySuggestionsConfig-request-IndexId"></a>
The identifier of the index with query suggestions that you want to get information on.  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]*`   
Required: Yes

## Response Syntax
<a name="API_DescribeQuerySuggestionsConfig_ResponseSyntax"></a>

```
{
   "AttributeSuggestionsConfig": { 
      "AttributeSuggestionsMode": "string",
      "SuggestableConfigList": [ 
         { 
            "AttributeName": "string",
            "Suggestable": boolean
         }
      ]
   },
   "IncludeQueriesWithoutUserInformation": boolean,
   "LastClearTime": number,
   "LastSuggestionsBuildTime": number,
   "MinimumNumberOfQueryingUsers": number,
   "MinimumQueryCount": number,
   "Mode": "string",
   "QueryLogLookBackWindowInDays": number,
   "Status": "string",
   "TotalSuggestionsCount": number
}
```

## Response Elements
<a name="API_DescribeQuerySuggestionsConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AttributeSuggestionsConfig](#API_DescribeQuerySuggestionsConfig_ResponseSyntax) **   <a name="kendra-DescribeQuerySuggestionsConfig-response-AttributeSuggestionsConfig"></a>
Configuration information for the document fields/attributes that you want to base query suggestions on.  
Type: [AttributeSuggestionsDescribeConfig](API_AttributeSuggestionsDescribeConfig.md) object

 ** [IncludeQueriesWithoutUserInformation](#API_DescribeQuerySuggestionsConfig_ResponseSyntax) **   <a name="kendra-DescribeQuerySuggestionsConfig-response-IncludeQueriesWithoutUserInformation"></a>
 `TRUE` to use all queries, otherwise use only queries that include user information to generate the query suggestions.  
Type: Boolean

 ** [LastClearTime](#API_DescribeQuerySuggestionsConfig_ResponseSyntax) **   <a name="kendra-DescribeQuerySuggestionsConfig-response-LastClearTime"></a>
The Unix timestamp when query suggestions for an index was last cleared.  
After you clear suggestions, Amazon Kendra learns new suggestions based on new queries added to the query log from the time you cleared suggestions. Amazon Kendra only considers re-occurences of a query from the time you cleared suggestions.   
Type: Timestamp

 ** [LastSuggestionsBuildTime](#API_DescribeQuerySuggestionsConfig_ResponseSyntax) **   <a name="kendra-DescribeQuerySuggestionsConfig-response-LastSuggestionsBuildTime"></a>
The Unix timestamp when query suggestions for an index was last updated.  
Amazon Kendra automatically updates suggestions every 24 hours, after you change a setting or after you apply a [block list](https://docs.aws.amazon.com/kendra/latest/dg/query-suggestions.html#query-suggestions-blocklist).  
Type: Timestamp

 ** [MinimumNumberOfQueryingUsers](#API_DescribeQuerySuggestionsConfig_ResponseSyntax) **   <a name="kendra-DescribeQuerySuggestionsConfig-response-MinimumNumberOfQueryingUsers"></a>
The minimum number of unique users who must search a query in order for the query to be eligible to suggest to your users.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 10000.

 ** [MinimumQueryCount](#API_DescribeQuerySuggestionsConfig_ResponseSyntax) **   <a name="kendra-DescribeQuerySuggestionsConfig-response-MinimumQueryCount"></a>
The minimum number of times a query must be searched in order for the query to be eligible to suggest to your users.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 10000.

 ** [Mode](#API_DescribeQuerySuggestionsConfig_ResponseSyntax) **   <a name="kendra-DescribeQuerySuggestionsConfig-response-Mode"></a>
Whether query suggestions are currently in `ENABLED` mode or `LEARN_ONLY` mode.  
By default, Amazon Kendra enables query suggestions.`LEARN_ONLY` turns off query suggestions for your users. You can change the mode using the [UpdateQuerySuggestionsConfig](https://docs.aws.amazon.com/kendra/latest/dg/API_UpdateQuerySuggestionsConfig.html) API.  
Type: String  
Valid Values: `ENABLED | LEARN_ONLY` 

 ** [QueryLogLookBackWindowInDays](#API_DescribeQuerySuggestionsConfig_ResponseSyntax) **   <a name="kendra-DescribeQuerySuggestionsConfig-response-QueryLogLookBackWindowInDays"></a>
How recent your queries are in your query log time window (in days).  
Type: Integer

 ** [Status](#API_DescribeQuerySuggestionsConfig_ResponseSyntax) **   <a name="kendra-DescribeQuerySuggestionsConfig-response-Status"></a>
Whether the status of query suggestions settings is currently `ACTIVE` or `UPDATING`.  
Active means the current settings apply and Updating means your changed settings are in the process of applying.  
Type: String  
Valid Values: `ACTIVE | UPDATING` 

 ** [TotalSuggestionsCount](#API_DescribeQuerySuggestionsConfig_ResponseSyntax) **   <a name="kendra-DescribeQuerySuggestionsConfig-response-TotalSuggestionsCount"></a>
The current total count of query suggestions for an index.  
This count can change when you update your query suggestions settings, if you filter out certain queries from suggestions using a block list, and as the query log accumulates more queries for Amazon Kendra to learn from.  
If the count is much lower than you expected, it could be because Amazon Kendra needs more queries in the query history to learn from or your current query suggestions settings are too strict.  
Type: Integer

## Errors
<a name="API_DescribeQuerySuggestionsConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.  
HTTP Status Code: 400

 ** InternalServerException **   
An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact [Support](http://aws.amazon.com/contact-us/) for help.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.  
HTTP Status Code: 400

 ** ThrottlingException **   
The request was denied due to request throttling. Please reduce the number of requests and try again.  
HTTP Status Code: 400

 ** ValidationException **   
The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.  
HTTP Status Code: 400

## See Also
<a name="API_DescribeQuerySuggestionsConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kendra-2019-02-03/DescribeQuerySuggestionsConfig) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kendra-2019-02-03/DescribeQuerySuggestionsConfig) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/DescribeQuerySuggestionsConfig) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kendra-2019-02-03/DescribeQuerySuggestionsConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/DescribeQuerySuggestionsConfig) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kendra-2019-02-03/DescribeQuerySuggestionsConfig) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kendra-2019-02-03/DescribeQuerySuggestionsConfig) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kendra-2019-02-03/DescribeQuerySuggestionsConfig) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kendra-2019-02-03/DescribeQuerySuggestionsConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/DescribeQuerySuggestionsConfig) 