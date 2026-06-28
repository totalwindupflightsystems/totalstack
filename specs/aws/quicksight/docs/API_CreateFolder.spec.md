---
id: "@specs/aws/quicksight/docs/API_CreateFolder"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateFolder"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# CreateFolder

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_CreateFolder
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateFolder
<a name="API_CreateFolder"></a>

Creates an empty shared folder.

## Request Syntax
<a name="API_CreateFolder_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/folders/{{FolderId}} HTTP/1.1
Content-type: application/json

{
   "FolderType": "{{string}}",
   "Name": "{{string}}",
   "ParentFolderArn": "{{string}}",
   "Permissions": [ 
      { 
         "Actions": [ "{{string}}" ],
         "Principal": "{{string}}"
      }
   ],
   "SharingModel": "{{string}}",
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateFolder_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_CreateFolder_RequestSyntax) **   <a name="QS-CreateFolder-request-uri-AwsAccountId"></a>
The ID for the AWS account where you want to create the folder.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [FolderId](#API_CreateFolder_RequestSyntax) **   <a name="QS-CreateFolder-request-uri-FolderId"></a>
The ID of the folder.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `[\w\-]+`   
Required: Yes

## Request Body
<a name="API_CreateFolder_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [FolderType](#API_CreateFolder_RequestSyntax) **   <a name="QS-CreateFolder-request-FolderType"></a>
The type of folder. By default, `folderType` is `SHARED`.  
Type: String  
Valid Values: `SHARED | RESTRICTED`   
Required: No

 ** [Name](#API_CreateFolder_RequestSyntax) **   <a name="QS-CreateFolder-request-Name"></a>
The name of the folder.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** [ParentFolderArn](#API_CreateFolder_RequestSyntax) **   <a name="QS-CreateFolder-request-ParentFolderArn"></a>
The Amazon Resource Name (ARN) for the parent folder.  
 `ParentFolderArn` can be null. An empty `parentFolderArn` creates a root-level folder.  
Type: String  
Required: No

 ** [Permissions](#API_CreateFolder_RequestSyntax) **   <a name="QS-CreateFolder-request-Permissions"></a>
A structure that describes the principals and the resource-level permissions of a folder.  
To specify no permissions, omit `Permissions`.  
Type: Array of [ResourcePermission](API_ResourcePermission.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 64 items.  
Required: No

 ** [SharingModel](#API_CreateFolder_RequestSyntax) **   <a name="QS-CreateFolder-request-SharingModel"></a>
An optional parameter that determines the sharing scope of the folder. The default value for this parameter is `ACCOUNT`.  
Type: String  
Valid Values: `ACCOUNT | NAMESPACE`   
Required: No

 ** [Tags](#API_CreateFolder_RequestSyntax) **   <a name="QS-CreateFolder-request-Tags"></a>
Tags for the folder.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.  
Required: No

## Response Syntax
<a name="API_CreateFolder_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "Arn": "string",
   "FolderId": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_CreateFolder_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_CreateFolder_ResponseSyntax) **   <a name="QS-CreateFolder-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateFolder_ResponseSyntax) **   <a name="QS-CreateFolder-response-Arn"></a>
The Amazon Resource Name (ARN) for the newly created folder.  
Type: String

 ** [FolderId](#API_CreateFolder_ResponseSyntax) **   <a name="QS-CreateFolder-response-FolderId"></a>
The folder ID for the newly created folder.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `[\w\-]+` 

 ** [RequestId](#API_CreateFolder_ResponseSyntax) **   <a name="QS-CreateFolder-response-RequestId"></a>
The request ID for the newly created folder.  
Type: String

## Errors
<a name="API_CreateFolder_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 401

 ** ConflictException **   
Updating or deleting a resource can cause an inconsistent state.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 409

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
<a name="API_CreateFolder_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/CreateFolder) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/CreateFolder) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CreateFolder) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/CreateFolder) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CreateFolder) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/CreateFolder) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/CreateFolder) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/CreateFolder) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/CreateFolder) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CreateFolder) 