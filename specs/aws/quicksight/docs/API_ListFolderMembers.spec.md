---
id: "@specs/aws/quicksight/docs/API_ListFolderMembers"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListFolderMembers"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# ListFolderMembers

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_ListFolderMembers
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListFolderMembers
<a name="API_ListFolderMembers"></a>

List all assets (`DASHBOARD`, `ANALYSIS`, and `DATASET`) in a folder. 

## Request Syntax
<a name="API_ListFolderMembers_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/folders/{{FolderId}}/members?max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListFolderMembers_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_ListFolderMembers_RequestSyntax) **   <a name="QS-ListFolderMembers-request-uri-AwsAccountId"></a>
The ID for the AWS account that contains the folder.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [FolderId](#API_ListFolderMembers_RequestSyntax) **   <a name="QS-ListFolderMembers-request-uri-FolderId"></a>
The ID of the folder.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `[\w\-]+`   
Required: Yes

 ** [MaxResults](#API_ListFolderMembers_RequestSyntax) **   <a name="QS-ListFolderMembers-request-uri-MaxResults"></a>
The maximum number of results to be returned per request.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListFolderMembers_RequestSyntax) **   <a name="QS-ListFolderMembers-request-uri-NextToken"></a>
The token for the next set of results, or null if there are no more results.

## Request Body
<a name="API_ListFolderMembers_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListFolderMembers_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "FolderMemberList": [ 
      { 
         "MemberArn": "string",
         "MemberId": "string"
      }
   ],
   "NextToken": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_ListFolderMembers_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_ListFolderMembers_ResponseSyntax) **   <a name="QS-ListFolderMembers-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [FolderMemberList](#API_ListFolderMembers_ResponseSyntax) **   <a name="QS-ListFolderMembers-response-FolderMemberList"></a>
A structure that contains all of the folder members (dashboards, analyses, and datasets) in the folder.  
Type: Array of [MemberIdArnPair](API_MemberIdArnPair.md) objects  
Array Members: Maximum number of 100 items.

 ** [NextToken](#API_ListFolderMembers_ResponseSyntax) **   <a name="QS-ListFolderMembers-response-NextToken"></a>
The token for the next set of results, or null if there are no more results.  
Type: String

 ** [RequestId](#API_ListFolderMembers_ResponseSyntax) **   <a name="QS-ListFolderMembers-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_ListFolderMembers_Errors"></a>

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

 ** UnsupportedUserEditionException **   
This error indicates that you are calling an operation on an Amazon Quick Suite subscription where the edition doesn't include support for that operation. Amazon Quick Suite currently has Standard Edition and Enterprise Edition. Not every operation and capability is available in every edition.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 403

## See Also
<a name="API_ListFolderMembers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/ListFolderMembers) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/ListFolderMembers) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ListFolderMembers) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/ListFolderMembers) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ListFolderMembers) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/ListFolderMembers) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/ListFolderMembers) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/ListFolderMembers) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/ListFolderMembers) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ListFolderMembers) 