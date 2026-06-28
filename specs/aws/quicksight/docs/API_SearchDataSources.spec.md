---
id: "@specs/aws/quicksight/docs/API_SearchDataSources"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SearchDataSources"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# SearchDataSources

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_SearchDataSources
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SearchDataSources
<a name="API_SearchDataSources"></a>

Use the `SearchDataSources` operation to search for data sources that belong to an account.

## Request Syntax
<a name="API_SearchDataSources_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/search/data-sources HTTP/1.1
Content-type: application/json

{
   "Filters": [ 
      { 
         "Name": "{{string}}",
         "Operator": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SearchDataSources_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_SearchDataSources_RequestSyntax) **   <a name="QS-SearchDataSources-request-uri-AwsAccountId"></a>
The AWS account ID.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

## Request Body
<a name="API_SearchDataSources_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Filters](#API_SearchDataSources_RequestSyntax) **   <a name="QS-SearchDataSources-request-Filters"></a>
The filters to apply to the search.  
Type: Array of [DataSourceSearchFilter](API_DataSourceSearchFilter.md) objects  
Array Members: Fixed number of 1 item.  
Required: Yes

 ** [MaxResults](#API_SearchDataSources_RequestSyntax) **   <a name="QS-SearchDataSources-request-MaxResults"></a>
The maximum number of results to be returned per request.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [NextToken](#API_SearchDataSources_RequestSyntax) **   <a name="QS-SearchDataSources-request-NextToken"></a>
A pagination token that can be used in a subsequent request.  
Type: String  
Required: No

## Response Syntax
<a name="API_SearchDataSources_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "DataSourceSummaries": [ 
      { 
         "Arn": "string",
         "CreatedTime": number,
         "DataSourceId": "string",
         "LastUpdatedTime": number,
         "Name": "string",
         "Type": "string"
      }
   ],
   "NextToken": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_SearchDataSources_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_SearchDataSources_ResponseSyntax) **   <a name="QS-SearchDataSources-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [DataSourceSummaries](#API_SearchDataSources_ResponseSyntax) **   <a name="QS-SearchDataSources-response-DataSourceSummaries"></a>
A `DataSourceSummaries` object that returns a summary of a data source.  
Type: Array of [DataSourceSummary](API_DataSourceSummary.md) objects

 ** [NextToken](#API_SearchDataSources_ResponseSyntax) **   <a name="QS-SearchDataSources-response-NextToken"></a>
A pagination token that can be used in a subsequent request.  
Type: String

 ** [RequestId](#API_SearchDataSources_ResponseSyntax) **   <a name="QS-SearchDataSources-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_SearchDataSources_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 401

 ** InternalFailureException **   
An internal failure occurred.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidNextTokenException **   
The `NextToken` value isn't valid.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 400

 ** InvalidParameterValueException **   
One or more parameters has a value that isn't valid.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 400

 ** ResourceNotFoundException **   
One or more resources can't be found.    
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **   
Access is throttled.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_SearchDataSources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/SearchDataSources) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/SearchDataSources) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SearchDataSources) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/SearchDataSources) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SearchDataSources) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/SearchDataSources) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/SearchDataSources) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/SearchDataSources) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/SearchDataSources) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SearchDataSources) 