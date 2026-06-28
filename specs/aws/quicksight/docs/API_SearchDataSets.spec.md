---
id: "@specs/aws/quicksight/docs/API_SearchDataSets"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SearchDataSets"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# SearchDataSets

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_SearchDataSets
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SearchDataSets
<a name="API_SearchDataSets"></a>

Use the `SearchDataSets` operation to search for datasets that belong to an account.

## Request Syntax
<a name="API_SearchDataSets_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/search/data-sets HTTP/1.1
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
<a name="API_SearchDataSets_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_SearchDataSets_RequestSyntax) **   <a name="QS-SearchDataSets-request-uri-AwsAccountId"></a>
The AWS account ID.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

## Request Body
<a name="API_SearchDataSets_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Filters](#API_SearchDataSets_RequestSyntax) **   <a name="QS-SearchDataSets-request-Filters"></a>
The filters to apply to the search.  
Type: Array of [DataSetSearchFilter](API_DataSetSearchFilter.md) objects  
Array Members: Fixed number of 1 item.  
Required: Yes

 ** [MaxResults](#API_SearchDataSets_RequestSyntax) **   <a name="QS-SearchDataSets-request-MaxResults"></a>
The maximum number of results to be returned per request.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [NextToken](#API_SearchDataSets_RequestSyntax) **   <a name="QS-SearchDataSets-request-NextToken"></a>
A pagination token that can be used in a subsequent request.  
Type: String  
Required: No

## Response Syntax
<a name="API_SearchDataSets_ResponseSyntax"></a>

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
<a name="API_SearchDataSets_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_SearchDataSets_ResponseSyntax) **   <a name="QS-SearchDataSets-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [DataSetSummaries](#API_SearchDataSets_ResponseSyntax) **   <a name="QS-SearchDataSets-response-DataSetSummaries"></a>
A `DataSetSummaries` object that returns a summary of a dataset.  
Type: Array of [DataSetSummary](API_DataSetSummary.md) objects

 ** [NextToken](#API_SearchDataSets_ResponseSyntax) **   <a name="QS-SearchDataSets-response-NextToken"></a>
A pagination token that can be used in a subsequent request.  
Type: String

 ** [RequestId](#API_SearchDataSets_ResponseSyntax) **   <a name="QS-SearchDataSets-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_SearchDataSets_Errors"></a>

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
<a name="API_SearchDataSets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/SearchDataSets) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/SearchDataSets) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SearchDataSets) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/SearchDataSets) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SearchDataSets) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/SearchDataSets) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/SearchDataSets) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/SearchDataSets) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/SearchDataSets) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SearchDataSets) 