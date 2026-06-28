---
id: "@specs/aws/quicksight/docs/API_CreateFolderMembership"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateFolderMembership"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# CreateFolderMembership

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_CreateFolderMembership
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateFolderMembership
<a name="API_CreateFolderMembership"></a>

Adds an asset, such as a dashboard, analysis, or dataset into a folder.

## Request Syntax
<a name="API_CreateFolderMembership_RequestSyntax"></a>

```
PUT /accounts/{{AwsAccountId}}/folders/{{FolderId}}/members/{{MemberType}}/{{MemberId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_CreateFolderMembership_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_CreateFolderMembership_RequestSyntax) **   <a name="QS-CreateFolderMembership-request-uri-AwsAccountId"></a>
The ID for the AWS account that contains the folder.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [FolderId](#API_CreateFolderMembership_RequestSyntax) **   <a name="QS-CreateFolderMembership-request-uri-FolderId"></a>
The ID of the folder.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `[\w\-]+`   
Required: Yes

 ** [MemberId](#API_CreateFolderMembership_RequestSyntax) **   <a name="QS-CreateFolderMembership-request-uri-MemberId"></a>
The ID of the asset that you want to add to the folder.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `[\w\-]+`   
Required: Yes

 ** [MemberType](#API_CreateFolderMembership_RequestSyntax) **   <a name="QS-CreateFolderMembership-request-uri-MemberType"></a>
The member type of the asset that you want to add to a folder.  
Valid Values: `DASHBOARD | ANALYSIS | DATASET | DATASOURCE | TOPIC`   
Required: Yes

## Request Body
<a name="API_CreateFolderMembership_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_CreateFolderMembership_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "FolderMember": { 
      "MemberId": "string",
      "MemberType": "string"
   },
   "RequestId": "string",
   "Status": number
}
```

## Response Elements
<a name="API_CreateFolderMembership_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FolderMember](#API_CreateFolderMembership_ResponseSyntax) **   <a name="QS-CreateFolderMembership-response-FolderMember"></a>
Information about the member in the folder.  
Type: [FolderMember](API_FolderMember.md) object

 ** [RequestId](#API_CreateFolderMembership_ResponseSyntax) **   <a name="QS-CreateFolderMembership-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

 ** [Status](#API_CreateFolderMembership_ResponseSyntax) **   <a name="QS-CreateFolderMembership-response-Status"></a>
The HTTP status of the request.  
Type: Integer

## Errors
<a name="API_CreateFolderMembership_Errors"></a>

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

 ** InvalidParameterValueException **   
One or more parameters has a value that isn't valid.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 400

 ** LimitExceededException **   
A limit is exceeded.    
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
Limit exceeded.
HTTP Status Code: 409

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

 ** UnsupportedUserEditionException **   
This error indicates that you are calling an operation on an Amazon Quick Suite subscription where the edition doesn't include support for that operation. Amazon Quick Suite currently has Standard Edition and Enterprise Edition. Not every operation and capability is available in every edition.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 403

## See Also
<a name="API_CreateFolderMembership_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/CreateFolderMembership) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/CreateFolderMembership) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CreateFolderMembership) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/CreateFolderMembership) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CreateFolderMembership) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/CreateFolderMembership) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/CreateFolderMembership) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/CreateFolderMembership) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/CreateFolderMembership) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CreateFolderMembership) 