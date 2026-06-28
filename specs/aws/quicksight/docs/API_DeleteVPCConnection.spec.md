---
id: "@specs/aws/quicksight/docs/API_DeleteVPCConnection"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteVPCConnection"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# DeleteVPCConnection

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_DeleteVPCConnection
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteVPCConnection
<a name="API_DeleteVPCConnection"></a>

Deletes a VPC connection.

## Request Syntax
<a name="API_DeleteVPCConnection_RequestSyntax"></a>

```
DELETE /accounts/{{AwsAccountId}}/vpc-connections/{{VPCConnectionId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteVPCConnection_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_DeleteVPCConnection_RequestSyntax) **   <a name="QS-DeleteVPCConnection-request-uri-AwsAccountId"></a>
The AWS account ID of the account where you want to delete a VPC connection.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [VPCConnectionId](#API_DeleteVPCConnection_RequestSyntax) **   <a name="QS-DeleteVPCConnection-request-uri-VPCConnectionId"></a>
The ID of the VPC connection that you're creating. This ID is a unique identifier for each AWS Region in an AWS account.  
Length Constraints: Minimum length of 1. Maximum length of 1000.  
Required: Yes

## Request Body
<a name="API_DeleteVPCConnection_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteVPCConnection_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "Arn": "string",
   "AvailabilityStatus": "string",
   "DeletionStatus": "string",
   "RequestId": "string",
   "VPCConnectionId": "string"
}
```

## Response Elements
<a name="API_DeleteVPCConnection_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_DeleteVPCConnection_ResponseSyntax) **   <a name="QS-DeleteVPCConnection-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [Arn](#API_DeleteVPCConnection_ResponseSyntax) **   <a name="QS-DeleteVPCConnection-response-Arn"></a>
The Amazon Resource Name (ARN) of the deleted VPC connection.  
Type: String

 ** [AvailabilityStatus](#API_DeleteVPCConnection_ResponseSyntax) **   <a name="QS-DeleteVPCConnection-response-AvailabilityStatus"></a>
The availability status of the VPC connection.  
Type: String  
Valid Values: `AVAILABLE | UNAVAILABLE | PARTIALLY_AVAILABLE` 

 ** [DeletionStatus](#API_DeleteVPCConnection_ResponseSyntax) **   <a name="QS-DeleteVPCConnection-response-DeletionStatus"></a>
The deletion status of the VPC connection.  
Type: String  
Valid Values: `CREATION_IN_PROGRESS | CREATION_SUCCESSFUL | CREATION_FAILED | UPDATE_IN_PROGRESS | UPDATE_SUCCESSFUL | UPDATE_FAILED | DELETION_IN_PROGRESS | DELETION_FAILED | DELETED` 

 ** [RequestId](#API_DeleteVPCConnection_ResponseSyntax) **   <a name="QS-DeleteVPCConnection-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

 ** [VPCConnectionId](#API_DeleteVPCConnection_ResponseSyntax) **   <a name="QS-DeleteVPCConnection-response-VPCConnectionId"></a>
The ID of the VPC connection that you're creating. This ID is a unique identifier for each AWS Region in an AWS account.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1000.

## Errors
<a name="API_DeleteVPCConnection_Errors"></a>

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
<a name="API_DeleteVPCConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DeleteVPCConnection) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DeleteVPCConnection) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DeleteVPCConnection) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DeleteVPCConnection) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DeleteVPCConnection) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DeleteVPCConnection) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DeleteVPCConnection) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DeleteVPCConnection) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DeleteVPCConnection) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DeleteVPCConnection) 