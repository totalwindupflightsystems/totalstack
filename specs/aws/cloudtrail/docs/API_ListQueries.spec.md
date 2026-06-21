---
id: "@specs/aws/cloudtrail/docs/API_ListQueries"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListQueries"
status: active
depends_on:
  - "@specs/aws/cloudtrail/meta"
---

# ListQueries

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudtrail/docs/API_ListQueries
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListQueries
<a name="API_ListQueries"></a>

**Important**  
CloudTrail Lake will no longer be open to new customers starting May 31, 2026. If you would like to use CloudTrail Lake, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [CloudTrail Lake availability change](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-service-availability-change.html).

Returns a list of queries and query statuses for the past seven days. You must specify an ARN value for `EventDataStore`. Optionally, to shorten the list of results, you can specify a time range, formatted as timestamps, by adding `StartTime` and `EndTime` parameters, and a `QueryStatus` value. Valid values for `QueryStatus` include `QUEUED`, `RUNNING`, `FINISHED`, `FAILED`, `TIMED_OUT`, or `CANCELLED`.

## Request Syntax
<a name="API_ListQueries_RequestSyntax"></a>

```
{
   "EndTime": {{number}},
   "EventDataStore": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "QueryStatus": "{{string}}",
   "StartTime": {{number}}
}
```

## Request Parameters
<a name="API_ListQueries_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EndTime](#API_ListQueries_RequestSyntax) **   <a name="awscloudtrail-ListQueries-request-EndTime"></a>
Use with `StartTime` to bound a `ListQueries` request, and limit its results to only those queries run within a specified time period.  
Type: Timestamp  
Required: No

 ** [EventDataStore](#API_ListQueries_RequestSyntax) **   <a name="awscloudtrail-ListQueries-request-EventDataStore"></a>
The ARN (or the ID suffix of the ARN) of an event data store on which queries were run.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 256.  
Pattern: `^[a-zA-Z0-9._/\-:]+$`   
Required: Yes

 ** [MaxResults](#API_ListQueries_RequestSyntax) **   <a name="awscloudtrail-ListQueries-request-MaxResults"></a>
The maximum number of queries to show on a page.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 1000.  
Required: No

 ** [NextToken](#API_ListQueries_RequestSyntax) **   <a name="awscloudtrail-ListQueries-request-NextToken"></a>
A token you can use to get the next page of results.  
Type: String  
Length Constraints: Minimum length of 4. Maximum length of 1000.  
Pattern: `.*`   
Required: No

 ** [QueryStatus](#API_ListQueries_RequestSyntax) **   <a name="awscloudtrail-ListQueries-request-QueryStatus"></a>
The status of queries that you want to return in results. Valid values for `QueryStatus` include `QUEUED`, `RUNNING`, `FINISHED`, `FAILED`, `TIMED_OUT`, or `CANCELLED`.  
Type: String  
Valid Values: `QUEUED | RUNNING | FINISHED | FAILED | CANCELLED | TIMED_OUT`   
Required: No

 ** [StartTime](#API_ListQueries_RequestSyntax) **   <a name="awscloudtrail-ListQueries-request-StartTime"></a>
Use with `EndTime` to bound a `ListQueries` request, and limit its results to only those queries run within a specified time period.  
Type: Timestamp  
Required: No

## Response Syntax
<a name="API_ListQueries_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Queries": [ 
      { 
         "CreationTime": number,
         "QueryId": "string",
         "QueryStatus": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListQueries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListQueries_ResponseSyntax) **   <a name="awscloudtrail-ListQueries-response-NextToken"></a>
A token you can use to get the next page of results.  
Type: String  
Length Constraints: Minimum length of 4. Maximum length of 1000.  
Pattern: `.*` 

 ** [Queries](#API_ListQueries_ResponseSyntax) **   <a name="awscloudtrail-ListQueries-response-Queries"></a>
Lists matching query results, and shows query ID, status, and creation time of each query.  
Type: Array of [Query](API_Query.md) objects

## Errors
<a name="API_ListQueries_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EventDataStoreARNInvalidException **   
The specified event data store ARN is not valid or does not map to an event data store in your account.  
HTTP Status Code: 400

 ** EventDataStoreNotFoundException **   
The specified event data store was not found.  
HTTP Status Code: 400

 ** InactiveEventDataStoreException **   
The event data store is inactive.  
HTTP Status Code: 400

 ** InvalidDateRangeException **   
A date range for the query was specified that is not valid. Be sure that the start time is chronologically before the end time. For more information about writing a query, see [Create or edit a query](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-create-edit-query.html) in the * AWS CloudTrail User Guide*.  
HTTP Status Code: 400

 ** InvalidMaxResultsException **   
This exception is thrown if the limit specified is not valid.  
HTTP Status Code: 400

 ** InvalidNextTokenException **   
A token that is not valid, or a token that was previously used in a request with different parameters. This exception is thrown if the token is not valid.  
HTTP Status Code: 400

 ** InvalidParameterException **   
The request includes a parameter that is not valid.  
HTTP Status Code: 400

 ** InvalidQueryStatusException **   
The query status is not valid for the operation.  
HTTP Status Code: 400

 ** NoManagementAccountSLRExistsException **   
 This exception is thrown when the management account does not have a service-linked role.   
HTTP Status Code: 400

 ** OperationNotPermittedException **   
This exception is thrown when the requested operation is not permitted.  
HTTP Status Code: 400

 ** UnsupportedOperationException **   
This exception is thrown when the requested operation is not supported.  
HTTP Status Code: 400

## See Also
<a name="API_ListQueries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/ListQueries) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudtrail-2013-11-01/ListQueries) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/ListQueries) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/ListQueries) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/ListQueries) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/ListQueries) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/ListQueries) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/ListQueries) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/ListQueries) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/ListQueries) 