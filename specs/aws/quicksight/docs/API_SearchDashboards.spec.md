---
id: "@specs/aws/quicksight/docs/API_SearchDashboards"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SearchDashboards"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# SearchDashboards

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_SearchDashboards
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SearchDashboards
<a name="API_SearchDashboards"></a>

Searches for dashboards that belong to a user. 

**Note**  
This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.

## Request Syntax
<a name="API_SearchDashboards_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/search/dashboards HTTP/1.1
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
<a name="API_SearchDashboards_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_SearchDashboards_RequestSyntax) **   <a name="QS-SearchDashboards-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the user whose dashboards you're searching for.   
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

## Request Body
<a name="API_SearchDashboards_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Filters](#API_SearchDashboards_RequestSyntax) **   <a name="QS-SearchDashboards-request-Filters"></a>
The filters to apply to the search. Currently, you can search only by user name, for example, `"Filters": [ { "Name": "QUICKSIGHT_USER", "Operator": "StringEquals", "Value": "arn:aws:quicksight:us-east-1:1:user/default/UserName1" } ]`   
Type: Array of [DashboardSearchFilter](API_DashboardSearchFilter.md) objects  
Array Members: Fixed number of 1 item.  
Required: Yes

 ** [MaxResults](#API_SearchDashboards_RequestSyntax) **   <a name="QS-SearchDashboards-request-MaxResults"></a>
The maximum number of results to be returned per request.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [NextToken](#API_SearchDashboards_RequestSyntax) **   <a name="QS-SearchDashboards-request-NextToken"></a>
The token for the next set of results, or null if there are no more results.  
Type: String  
Required: No

## Response Syntax
<a name="API_SearchDashboards_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "DashboardSummaryList": [ 
      { 
         "Arn": "string",
         "CreatedTime": number,
         "DashboardId": "string",
         "LastPublishedTime": number,
         "LastUpdatedTime": number,
         "Name": "string",
         "PublishedVersionNumber": number
      }
   ],
   "NextToken": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_SearchDashboards_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_SearchDashboards_ResponseSyntax) **   <a name="QS-SearchDashboards-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [DashboardSummaryList](#API_SearchDashboards_ResponseSyntax) **   <a name="QS-SearchDashboards-response-DashboardSummaryList"></a>
The list of dashboards owned by the user specified in `Filters` in your request.  
Type: Array of [DashboardSummary](API_DashboardSummary.md) objects  
Array Members: Maximum number of 100 items.

 ** [NextToken](#API_SearchDashboards_ResponseSyntax) **   <a name="QS-SearchDashboards-response-NextToken"></a>
The token for the next set of results, or null if there are no more results.  
Type: String

 ** [RequestId](#API_SearchDashboards_ResponseSyntax) **   <a name="QS-SearchDashboards-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_SearchDashboards_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** UnsupportedUserEditionException **   
This error indicates that you are calling an operation on an Amazon Quick Suite subscription where the edition doesn't include support for that operation. Amazon Quick Suite currently has Standard Edition and Enterprise Edition. Not every operation and capability is available in every edition.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 403

## See Also
<a name="API_SearchDashboards_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/SearchDashboards) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/SearchDashboards) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SearchDashboards) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/SearchDashboards) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SearchDashboards) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/SearchDashboards) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/SearchDashboards) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/SearchDashboards) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/SearchDashboards) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SearchDashboards) 