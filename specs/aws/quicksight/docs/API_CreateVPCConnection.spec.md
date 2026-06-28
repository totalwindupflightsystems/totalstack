---
id: "@specs/aws/quicksight/docs/API_CreateVPCConnection"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateVPCConnection"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# CreateVPCConnection

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_CreateVPCConnection
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateVPCConnection
<a name="API_CreateVPCConnection"></a>

Creates a new VPC connection.

## Request Syntax
<a name="API_CreateVPCConnection_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/vpc-connections HTTP/1.1
Content-type: application/json

{
   "DnsResolvers": [ "{{string}}" ],
   "Name": "{{string}}",
   "RoleArn": "{{string}}",
   "SecurityGroupIds": [ "{{string}}" ],
   "SubnetIds": [ "{{string}}" ],
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "VPCConnectionId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateVPCConnection_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_CreateVPCConnection_RequestSyntax) **   <a name="QS-CreateVPCConnection-request-uri-AwsAccountId"></a>
The AWS account ID of the account where you want to create a new VPC connection.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

## Request Body
<a name="API_CreateVPCConnection_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Name](#API_CreateVPCConnection_RequestSyntax) **   <a name="QS-CreateVPCConnection-request-Name"></a>
The display name for the VPC connection.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Required: Yes

 ** [RoleArn](#API_CreateVPCConnection_RequestSyntax) **   <a name="QS-CreateVPCConnection-request-RoleArn"></a>
The IAM role to associate with the VPC connection.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Required: Yes

 ** [SecurityGroupIds](#API_CreateVPCConnection_RequestSyntax) **   <a name="QS-CreateVPCConnection-request-SecurityGroupIds"></a>
A list of security group IDs for the VPC connection.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 16 items.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `^sg-[0-9a-z]*$`   
Required: Yes

 ** [SubnetIds](#API_CreateVPCConnection_RequestSyntax) **   <a name="QS-CreateVPCConnection-request-SubnetIds"></a>
A list of subnet IDs for the VPC connection.  
Type: Array of strings  
Array Members: Minimum number of 2 items. Maximum number of 15 items.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `^subnet-[0-9a-z]*$`   
Required: Yes

 ** [VPCConnectionId](#API_CreateVPCConnection_RequestSyntax) **   <a name="QS-CreateVPCConnection-request-VPCConnectionId"></a>
The ID of the VPC connection that you're creating. This ID is a unique identifier for each AWS Region in an AWS account.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1000.  
Pattern: `[\w\-]+`   
Required: Yes

 ** [DnsResolvers](#API_CreateVPCConnection_RequestSyntax) **   <a name="QS-CreateVPCConnection-request-DnsResolvers"></a>
A list of IP addresses of DNS resolver endpoints for the VPC connection.  
Type: Array of strings  
Array Members: Maximum number of 15 items.  
Length Constraints: Minimum length of 7. Maximum length of 15.  
Required: No

 ** [Tags](#API_CreateVPCConnection_RequestSyntax) **   <a name="QS-CreateVPCConnection-request-Tags"></a>
A map of the key-value pairs for the resource tag or tags assigned to the VPC connection.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.  
Required: No

## Response Syntax
<a name="API_CreateVPCConnection_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "Arn": "string",
   "AvailabilityStatus": "string",
   "CreationStatus": "string",
   "RequestId": "string",
   "VPCConnectionId": "string"
}
```

## Response Elements
<a name="API_CreateVPCConnection_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_CreateVPCConnection_ResponseSyntax) **   <a name="QS-CreateVPCConnection-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateVPCConnection_ResponseSyntax) **   <a name="QS-CreateVPCConnection-response-Arn"></a>
The Amazon Resource Name (ARN) of the VPC connection.  
Type: String

 ** [AvailabilityStatus](#API_CreateVPCConnection_ResponseSyntax) **   <a name="QS-CreateVPCConnection-response-AvailabilityStatus"></a>
The availability status of the VPC connection.  
Type: String  
Valid Values: `AVAILABLE | UNAVAILABLE | PARTIALLY_AVAILABLE` 

 ** [CreationStatus](#API_CreateVPCConnection_ResponseSyntax) **   <a name="QS-CreateVPCConnection-response-CreationStatus"></a>
The status of the creation of the VPC connection.  
Type: String  
Valid Values: `CREATION_IN_PROGRESS | CREATION_SUCCESSFUL | CREATION_FAILED | UPDATE_IN_PROGRESS | UPDATE_SUCCESSFUL | UPDATE_FAILED | DELETION_IN_PROGRESS | DELETION_FAILED | DELETED` 

 ** [RequestId](#API_CreateVPCConnection_ResponseSyntax) **   <a name="QS-CreateVPCConnection-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

 ** [VPCConnectionId](#API_CreateVPCConnection_ResponseSyntax) **   <a name="QS-CreateVPCConnection-response-VPCConnectionId"></a>
The ID for the VPC connection that you're creating. This ID is unique per AWS Region for each AWS account.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1000.  
Pattern: `[\w\-]+` 

## Errors
<a name="API_CreateVPCConnection_Errors"></a>

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
<a name="API_CreateVPCConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/CreateVPCConnection) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/CreateVPCConnection) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CreateVPCConnection) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/CreateVPCConnection) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CreateVPCConnection) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/CreateVPCConnection) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/CreateVPCConnection) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/CreateVPCConnection) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/CreateVPCConnection) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CreateVPCConnection) 