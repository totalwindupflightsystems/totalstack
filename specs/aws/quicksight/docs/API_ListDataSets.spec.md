---
id: "@specs/aws/quicksight/docs/API_ListDataSets"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListDataSets"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# ListDataSets

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_ListDataSets
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListDataSets
<a name="API_ListDataSets"></a>

Lists all of the datasets belonging to the current AWS account in an AWS Region.

The permissions resource is `arn:aws:quicksight:region:aws-account-id:dataset/*`.

## Request Syntax
<a name="API_ListDataSets_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/data-sets?max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDataSets_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_ListDataSets_RequestSyntax) **   <a name="QS-ListDataSets-request-uri-AwsAccountId"></a>
The AWS account ID.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [MaxResults](#API_ListDataSets_RequestSyntax) **   <a name="QS-ListDataSets-request-uri-MaxResults"></a>
The maximum number of results to be returned per request.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListDataSets_RequestSyntax) **   <a name="QS-ListDataSets-request-uri-NextToken"></a>
The token for the next set of results, or null if there are no more results.

## Request Body
<a name="API_ListDataSets_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDataSets_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "DataSetSummaries": [ 
      { 
         "Arn": "string",
         "ColumnLevelPermissionRulesApplied": boolean,
         "CreatedTime": number,
         "DataSetId": "string",
         "ImportMode": "string",
         "LastUpdatedTime": number,
         "Name": "string",
         "RowLevelPermissionDataSet": { 
            "Arn": "string",
            "FormatVersion": "string",
            "Namespace": "string",
            "PermissionPolicy": "string",
            "Status": "string"
         },
         "RowLevelPermissionDataSetMap": { 
            "string" : { 
               "Arn": "string",
               "FormatVersion": "string",
               "Namespace": "string",
               "PermissionPolicy": "string",
               "Status": "string"
            }
         },
         "RowLevelPermissionTagConfigurationApplied": boolean,
         "UseAs": "string"
      }
   ],
   "NextToken": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_ListDataSets_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_ListDataSets_ResponseSyntax) **   <a name="QS-ListDataSets-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [DataSetSummaries](#API_ListDataSets_ResponseSyntax) **   <a name="QS-ListDataSets-response-DataSetSummaries"></a>
The list of dataset summaries.  
Type: Array of [DataSetSummary](API_DataSetSummary.md) objects

 ** [NextToken](#API_ListDataSets_ResponseSyntax) **   <a name="QS-ListDataSets-response-NextToken"></a>
The token for the next set of results, or null if there are no more results.  
Type: String

 ** [RequestId](#API_ListDataSets_ResponseSyntax) **   <a name="QS-ListDataSets-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_ListDataSets_Errors"></a>

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

 ** ThrottlingException **   
Access is throttled.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 429

## Examples
<a name="API_ListDataSets_Examples"></a>

### Example
<a name="API_ListDataSets_Example_1"></a>

This example illustrates one usage of ListDataSets.

#### Sample Request
<a name="API_ListDataSets_Example_1_Request"></a>

```
GET /accounts/{AwsAccountId}/data-sets?next-token={NextToken};max-results={MaxResults} HTTP/1.1
Content-type: application/json
```

## See Also
<a name="API_ListDataSets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/ListDataSets) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/ListDataSets) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ListDataSets) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/ListDataSets) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ListDataSets) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/ListDataSets) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/ListDataSets) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/ListDataSets) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/ListDataSets) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ListDataSets) 