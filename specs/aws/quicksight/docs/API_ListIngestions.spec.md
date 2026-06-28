---
id: "@specs/aws/quicksight/docs/API_ListIngestions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListIngestions"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# ListIngestions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_ListIngestions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListIngestions
<a name="API_ListIngestions"></a>

Lists the history of SPICE ingestions for a dataset. Limited to 5 TPS per user and 25 TPS per account.

## Request Syntax
<a name="API_ListIngestions_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/data-sets/{{DataSetId}}/ingestions?max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListIngestions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_ListIngestions_RequestSyntax) **   <a name="QS-ListIngestions-request-uri-AwsAccountId"></a>
The AWS account ID.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [DataSetId](#API_ListIngestions_RequestSyntax) **   <a name="QS-ListIngestions-request-uri-DataSetId"></a>
The ID of the dataset used in the ingestion.  
Required: Yes

 ** [MaxResults](#API_ListIngestions_RequestSyntax) **   <a name="QS-ListIngestions-request-uri-MaxResults"></a>
The maximum number of results to be returned per request.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListIngestions_RequestSyntax) **   <a name="QS-ListIngestions-request-uri-NextToken"></a>
The token for the next set of results, or null if there are no more results.

## Request Body
<a name="API_ListIngestions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListIngestions_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "Ingestions": [ 
      { 
         "Arn": "string",
         "CreatedTime": number,
         "ErrorInfo": { 
            "Message": "string",
            "Type": "string"
         },
         "IngestionId": "string",
         "IngestionSizeInBytes": number,
         "IngestionStatus": "string",
         "IngestionTimeInSeconds": number,
         "QueueInfo": { 
            "QueuedIngestion": "string",
            "WaitingOnIngestion": "string"
         },
         "RequestSource": "string",
         "RequestType": "string",
         "RowInfo": { 
            "RowsDropped": number,
            "RowsIngested": number,
            "TotalRowsInDataset": number
         }
      }
   ],
   "NextToken": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_ListIngestions_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_ListIngestions_ResponseSyntax) **   <a name="QS-ListIngestions-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [Ingestions](#API_ListIngestions_ResponseSyntax) **   <a name="QS-ListIngestions-response-Ingestions"></a>
A list of the ingestions.  
Type: Array of [Ingestion](API_Ingestion.md) objects

 ** [NextToken](#API_ListIngestions_ResponseSyntax) **   <a name="QS-ListIngestions-response-NextToken"></a>
The token for the next set of results, or null if there are no more results.  
Type: String

 ** [RequestId](#API_ListIngestions_ResponseSyntax) **   <a name="QS-ListIngestions-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_ListIngestions_Errors"></a>

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

 ** ResourceExistsException **   
The resource specified already exists.     
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
The resource type for this request.
HTTP Status Code: 409

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

## Examples
<a name="API_ListIngestions_Examples"></a>

### Example
<a name="API_ListIngestions_Example_1"></a>

This example illustrates one usage of ListIngestions.

#### Sample Request
<a name="API_ListIngestions_Example_1_Request"></a>

```
GET /accounts/*AwsAccountId*/data-sets/*DataSetID*/ingestions?next-token=*NextToken*;max-results=*MaxResults*" HTTP/1.1
```

## See Also
<a name="API_ListIngestions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/ListIngestions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/ListIngestions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ListIngestions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/ListIngestions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ListIngestions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/ListIngestions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/ListIngestions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/ListIngestions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/ListIngestions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ListIngestions) 