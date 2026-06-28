---
id: "@specs/aws/quicksight/docs/API_SearchFolders"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SearchFolders"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# SearchFolders

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_SearchFolders
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SearchFolders
<a name="API_SearchFolders"></a>

Searches the subfolders in a folder.

## Request Syntax
<a name="API_SearchFolders_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/search/folders HTTP/1.1
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
<a name="API_SearchFolders_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_SearchFolders_RequestSyntax) **   <a name="QS-SearchFolders-request-uri-AwsAccountId"></a>
The ID for the AWS account that contains the folder.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

## Request Body
<a name="API_SearchFolders_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Filters](#API_SearchFolders_RequestSyntax) **   <a name="QS-SearchFolders-request-Filters"></a>
The filters to apply to the search. Currently, you can search only by the parent folder ARN. For example, `"Filters": [ { "Name": "PARENT_FOLDER_ARN", "Operator": "StringEquals", "Value": "arn:aws:quicksight:us-east-1:1:folder/folderId" } ]`.  
Type: Array of [FolderSearchFilter](API_FolderSearchFilter.md) objects  
Array Members: Maximum number of 100 items.  
Required: Yes

 ** [MaxResults](#API_SearchFolders_RequestSyntax) **   <a name="QS-SearchFolders-request-MaxResults"></a>
The maximum number of results to be returned per request.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [NextToken](#API_SearchFolders_RequestSyntax) **   <a name="QS-SearchFolders-request-NextToken"></a>
The token for the next set of results, or null if there are no more results.  
Type: String  
Required: No

## Response Syntax
<a name="API_SearchFolders_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "FolderSummaryList": [ 
      { 
         "Arn": "string",
         "CreatedTime": number,
         "FolderId": "string",
         "FolderType": "string",
         "LastUpdatedTime": number,
         "Name": "string",
         "SharingModel": "string"
      }
   ],
   "NextToken": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_SearchFolders_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_SearchFolders_ResponseSyntax) **   <a name="QS-SearchFolders-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [FolderSummaryList](#API_SearchFolders_ResponseSyntax) **   <a name="QS-SearchFolders-response-FolderSummaryList"></a>
A structure that contains all of the folders in the AWS account. This structure provides basic information about the folders.  
Type: Array of [FolderSummary](API_FolderSummary.md) objects  
Array Members: Maximum number of 100 items.

 ** [NextToken](#API_SearchFolders_ResponseSyntax) **   <a name="QS-SearchFolders-response-NextToken"></a>
The token for the next set of results, or null if there are no more results.  
Type: String

 ** [RequestId](#API_SearchFolders_ResponseSyntax) **   <a name="QS-SearchFolders-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_SearchFolders_Errors"></a>

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

 ** InvalidRequestException **   
You don't have this feature activated for your account. To fix this issue, contact AWS support.    
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
<a name="API_SearchFolders_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/SearchFolders) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/SearchFolders) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SearchFolders) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/SearchFolders) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SearchFolders) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/SearchFolders) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/SearchFolders) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/SearchFolders) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/SearchFolders) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SearchFolders) 