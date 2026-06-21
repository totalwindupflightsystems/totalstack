---
id: "@specs/aws/cloudtrail/docs/API_SearchSampleQueries"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SearchSampleQueries"
status: active
depends_on:
  - "@specs/aws/cloudtrail/meta"
---

# SearchSampleQueries

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudtrail/docs/API_SearchSampleQueries
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SearchSampleQueries
<a name="API_SearchSampleQueries"></a>

**Important**  
CloudTrail Lake will no longer be open to new customers starting May 31, 2026. If you would like to use CloudTrail Lake, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [CloudTrail Lake availability change](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-service-availability-change.html).

 Searches sample queries and returns a list of sample queries that are sorted by relevance. To search for sample queries, provide a natural language `SearchPhrase` in English. 

## Request Syntax
<a name="API_SearchSampleQueries_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SearchPhrase": "{{string}}"
}
```

## Request Parameters
<a name="API_SearchSampleQueries_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_SearchSampleQueries_RequestSyntax) **   <a name="awscloudtrail-SearchSampleQueries-request-MaxResults"></a>
 The maximum number of results to return on a single page. The default value is 10.   
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 50.  
Required: No

 ** [NextToken](#API_SearchSampleQueries_RequestSyntax) **   <a name="awscloudtrail-SearchSampleQueries-request-NextToken"></a>
 A token you can use to get the next page of results. The length constraint is in characters, not words.   
Type: String  
Length Constraints: Minimum length of 4. Maximum length of 1000.  
Pattern: `.*`   
Required: No

 ** [SearchPhrase](#API_SearchSampleQueries_RequestSyntax) **   <a name="awscloudtrail-SearchSampleQueries-request-SearchPhrase"></a>
 The natural language phrase to use for the semantic search. The phrase must be in English. The length constraint is in characters, not words.  
Type: String  
Length Constraints: Minimum length of 2. Maximum length of 1000.  
Pattern: `^[ -~\n]*$`   
Required: Yes

## Response Syntax
<a name="API_SearchSampleQueries_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "SearchResults": [ 
      { 
         "Description": "string",
         "Name": "string",
         "Relevance": number,
         "SQL": "string"
      }
   ]
}
```

## Response Elements
<a name="API_SearchSampleQueries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_SearchSampleQueries_ResponseSyntax) **   <a name="awscloudtrail-SearchSampleQueries-response-NextToken"></a>
 A token you can use to get the next page of results.  
Type: String  
Length Constraints: Minimum length of 4. Maximum length of 1000.  
Pattern: `.*` 

 ** [SearchResults](#API_SearchSampleQueries_ResponseSyntax) **   <a name="awscloudtrail-SearchSampleQueries-response-SearchResults"></a>
 A list of objects containing the search results ordered from most relevant to least relevant.   
Type: Array of [SearchSampleQueriesSearchResult](API_SearchSampleQueriesSearchResult.md) objects

## Errors
<a name="API_SearchSampleQueries_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **   
The request includes a parameter that is not valid.  
HTTP Status Code: 400

 ** OperationNotPermittedException **   
This exception is thrown when the requested operation is not permitted.  
HTTP Status Code: 400

 ** UnsupportedOperationException **   
This exception is thrown when the requested operation is not supported.  
HTTP Status Code: 400

## See Also
<a name="API_SearchSampleQueries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/SearchSampleQueries) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudtrail-2013-11-01/SearchSampleQueries) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/SearchSampleQueries) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/SearchSampleQueries) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/SearchSampleQueries) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/SearchSampleQueries) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/SearchSampleQueries) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/SearchSampleQueries) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/SearchSampleQueries) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/SearchSampleQueries) 