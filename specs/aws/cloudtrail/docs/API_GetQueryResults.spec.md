---
id: "@specs/aws/cloudtrail/docs/API_GetQueryResults"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetQueryResults"
status: active
depends_on:
  - "@specs/aws/cloudtrail/meta"
---

# GetQueryResults

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudtrail/docs/API_GetQueryResults
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetQueryResults
<a name="API_GetQueryResults"></a>

**Important**  
CloudTrail Lake will no longer be open to new customers starting May 31, 2026. If you would like to use CloudTrail Lake, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [CloudTrail Lake availability change](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-service-availability-change.html).

Gets event data results of a query. You must specify the `QueryID` value returned by the `StartQuery` operation.

## Request Syntax
<a name="API_GetQueryResults_RequestSyntax"></a>

```
{
   "EventDataStore": "{{string}}",
   "EventDataStoreOwnerAccountId": "{{string}}",
   "MaxQueryResults": {{number}},
   "NextToken": "{{string}}",
   "QueryId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetQueryResults_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EventDataStore](#API_GetQueryResults_RequestSyntax) **   <a name="awscloudtrail-GetQueryResults-request-EventDataStore"></a>
 *This parameter has been deprecated.*   
The ARN (or ID suffix of the ARN) of the event data store against which the query was run.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 256.  
Pattern: `^[a-zA-Z0-9._/\-:]+$`   
Required: No

 ** [EventDataStoreOwnerAccountId](#API_GetQueryResults_RequestSyntax) **   <a name="awscloudtrail-GetQueryResults-request-EventDataStoreOwnerAccountId"></a>
 The account ID of the event data store owner.   
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 16.  
Pattern: `\d+`   
Required: No

 ** [MaxQueryResults](#API_GetQueryResults_RequestSyntax) **   <a name="awscloudtrail-GetQueryResults-request-MaxQueryResults"></a>
The maximum number of query results to display on a single page.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 1000.  
Required: No

 ** [NextToken](#API_GetQueryResults_RequestSyntax) **   <a name="awscloudtrail-GetQueryResults-request-NextToken"></a>
A token you can use to get the next page of query results.  
Type: String  
Length Constraints: Minimum length of 4. Maximum length of 1000.  
Pattern: `.*`   
Required: No

 ** [QueryId](#API_GetQueryResults_RequestSyntax) **   <a name="awscloudtrail-GetQueryResults-request-QueryId"></a>
The ID of the query for which you want to get results.  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `^[a-f0-9\-]+$`   
Required: Yes

## Response Syntax
<a name="API_GetQueryResults_ResponseSyntax"></a>

```
{
   "ErrorMessage": "string",
   "NextToken": "string",
   "QueryResultRows": [ 
      [ 
         { 
            "string" : "string" 
         }
      ]
   ],
   "QueryStatistics": { 
      "BytesScanned": number,
      "ResultsCount": number,
      "TotalResultsCount": number
   },
   "QueryStatus": "string"
}
```

## Response Elements
<a name="API_GetQueryResults_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ErrorMessage](#API_GetQueryResults_ResponseSyntax) **   <a name="awscloudtrail-GetQueryResults-response-ErrorMessage"></a>
The error message returned if a query failed.  
Type: String  
Length Constraints: Minimum length of 4. Maximum length of 1000.  
Pattern: `.*` 

 ** [NextToken](#API_GetQueryResults_ResponseSyntax) **   <a name="awscloudtrail-GetQueryResults-response-NextToken"></a>
A token you can use to get the next page of query results.  
Type: String  
Length Constraints: Minimum length of 4. Maximum length of 1000.  
Pattern: `.*` 

 ** [QueryResultRows](#API_GetQueryResults_ResponseSyntax) **   <a name="awscloudtrail-GetQueryResults-response-QueryResultRows"></a>
Contains the individual event results of the query.  
Type: Array of arrays of string to string maps

 ** [QueryStatistics](#API_GetQueryResults_ResponseSyntax) **   <a name="awscloudtrail-GetQueryResults-response-QueryStatistics"></a>
Shows the count of query results.  
Type: [QueryStatistics](API_QueryStatistics.md) object

 ** [QueryStatus](#API_GetQueryResults_ResponseSyntax) **   <a name="awscloudtrail-GetQueryResults-response-QueryStatus"></a>
The status of the query. Values include `QUEUED`, `RUNNING`, `FINISHED`, `FAILED`, `TIMED_OUT`, or `CANCELLED`.  
Type: String  
Valid Values: `QUEUED | RUNNING | FINISHED | FAILED | CANCELLED | TIMED_OUT` 

## Errors
<a name="API_GetQueryResults_Errors"></a>

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

 ** InsufficientEncryptionPolicyException **   
For the `CreateTrail` `PutInsightSelectors`, `UpdateTrail`, `StartQuery`, and `StartImport` operations, this exception is thrown when the policy on the S3 bucket or AWS KMS key does not have sufficient permissions for the operation.  
For all other operations, this exception is thrown when the policy for the AWS KMS key does not have sufficient permissions for the operation.  
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

 ** NoManagementAccountSLRExistsException **   
 This exception is thrown when the management account does not have a service-linked role.   
HTTP Status Code: 400

 ** OperationNotPermittedException **   
This exception is thrown when the requested operation is not permitted.  
HTTP Status Code: 400

 ** QueryIdNotFoundException **   
The query ID does not exist or does not map to a query.  
HTTP Status Code: 400

 ** UnsupportedOperationException **   
This exception is thrown when the requested operation is not supported.  
HTTP Status Code: 400

## See Also
<a name="API_GetQueryResults_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/GetQueryResults) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudtrail-2013-11-01/GetQueryResults) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/GetQueryResults) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/GetQueryResults) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/GetQueryResults) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/GetQueryResults) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/GetQueryResults) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/GetQueryResults) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/GetQueryResults) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/GetQueryResults) 