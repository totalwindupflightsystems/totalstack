---
id: "@specs/aws/storagegateway/docs/API_AssociateFileSystem"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AssociateFileSystem"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# AssociateFileSystem

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_AssociateFileSystem
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AssociateFileSystem
<a name="API_AssociateFileSystem"></a>

Associate an Amazon FSx file system with the FSx File Gateway. After the association process is complete, the file shares on the Amazon FSx file system are available for access through the gateway. This operation only supports the FSx File Gateway type.

## Request Syntax
<a name="API_AssociateFileSystem_RequestSyntax"></a>

```
{
   "AuditDestinationARN": "{{string}}",
   "CacheAttributes": { 
      "CacheStaleTimeoutInSeconds": {{number}}
   },
   "ClientToken": "{{string}}",
   "EndpointNetworkConfiguration": { 
      "IpAddresses": [ "{{string}}" ]
   },
   "GatewayARN": "{{string}}",
   "LocationARN": "{{string}}",
   "Password": "{{string}}",
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "UserName": "{{string}}"
}
```

## Request Parameters
<a name="API_AssociateFileSystem_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AuditDestinationARN](#API_AssociateFileSystem_RequestSyntax) **   <a name="StorageGateway-AssociateFileSystem-request-AuditDestinationARN"></a>
The Amazon Resource Name (ARN) of the storage used for the audit logs.  
Type: String  
Length Constraints: Maximum length of 1024.  
Required: No

 ** [CacheAttributes](#API_AssociateFileSystem_RequestSyntax) **   <a name="StorageGateway-AssociateFileSystem-request-CacheAttributes"></a>
The refresh cache information for the file share or FSx file systems.  
Type: [CacheAttributes](API_CacheAttributes.md) object  
Required: No

 ** [ClientToken](#API_AssociateFileSystem_RequestSyntax) **   <a name="StorageGateway-AssociateFileSystem-request-ClientToken"></a>
A unique string value that you supply that is used by the FSx File Gateway to ensure idempotent file system association creation.  
Type: String  
Length Constraints: Minimum length of 5. Maximum length of 100.  
Required: Yes

 ** [EndpointNetworkConfiguration](#API_AssociateFileSystem_RequestSyntax) **   <a name="StorageGateway-AssociateFileSystem-request-EndpointNetworkConfiguration"></a>
Specifies the network configuration information for the gateway associated with the Amazon FSx file system.  
If multiple file systems are associated with this gateway, this parameter's `IpAddresses` field is required.
Type: [EndpointNetworkConfiguration](API_EndpointNetworkConfiguration.md) object  
Required: No

 ** [GatewayARN](#API_AssociateFileSystem_RequestSyntax) **   <a name="StorageGateway-AssociateFileSystem-request-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

 ** [LocationARN](#API_AssociateFileSystem_RequestSyntax) **   <a name="StorageGateway-AssociateFileSystem-request-LocationARN"></a>
The Amazon Resource Name (ARN) of the Amazon FSx file system to associate with the FSx File Gateway.  
Type: String  
Length Constraints: Minimum length of 8. Maximum length of 512.  
Required: Yes

 ** [Password](#API_AssociateFileSystem_RequestSyntax) **   <a name="StorageGateway-AssociateFileSystem-request-Password"></a>
The password of the user credential.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^[ -~]+$`   
Required: Yes

 ** [Tags](#API_AssociateFileSystem_RequestSyntax) **   <a name="StorageGateway-AssociateFileSystem-request-Tags"></a>
A list of up to 50 tags that can be assigned to the file system association. Each tag is a key-value pair.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

 ** [UserName](#API_AssociateFileSystem_RequestSyntax) **   <a name="StorageGateway-AssociateFileSystem-request-UserName"></a>
The user name of the user credential that has permission to access the root share D$ of the Amazon FSx file system. The user account must belong to the Amazon FSx delegated admin user group.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^\w[\w\.\- ]*$`   
Required: Yes

## Response Syntax
<a name="API_AssociateFileSystem_ResponseSyntax"></a>

```
{
   "FileSystemAssociationARN": "string"
}
```

## Response Elements
<a name="API_AssociateFileSystem_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FileSystemAssociationARN](#API_AssociateFileSystem_ResponseSyntax) **   <a name="StorageGateway-AssociateFileSystem-response-FileSystemAssociationARN"></a>
The ARN of the newly created file system association.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.

## Errors
<a name="API_AssociateFileSystem_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **   
An internal server error has occurred during the request. For more information, see the error and message fields.    
 ** error **   
A [StorageGatewayError](API_StorageGatewayError.md) that provides more information about the cause of the error.  
 ** message **   
A human-readable message describing the error that occurred.
HTTP Status Code: 400

 ** InvalidGatewayRequestException **   
An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.    
 ** error **   
A [StorageGatewayError](API_StorageGatewayError.md) that provides more detail about the cause of the error.  
 ** message **   
A human-readable message describing the error that occurred.
HTTP Status Code: 400

## Examples
<a name="API_AssociateFileSystem_Examples"></a>

### Example
<a name="API_AssociateFileSystem_Example_1"></a>

This example illustrates one usage of AssociateFileSystem.

#### Sample Request
<a name="API_AssociateFileSystem_Example_1_Request"></a>

```
__Sample Request__
{
 "UserName": "Admin",
 "Password": "Password123",
 "ClientToken": "foo-fsx-101",
 "GatewayARN": "arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-7A8D6313",
 "LocationARN": "arn:aws:fsx:us-east-1:111122223333:file-system/fs-0bb4bf5cedebd814f",
 
}
```

### Example
<a name="API_AssociateFileSystem_Example_2"></a>

This example illustrates one usage of AssociateFileSystem.

#### Sample Response
<a name="API_AssociateFileSystem_Example_2_Response"></a>

```
__Sample Response__
{
  "FileSystemAssociationARNList": ["arn:aws:storagegateway:us-east-1:111122223333:fs-association/fsa-1122AABBCCDDEEFFG"]
}
```

## See Also
<a name="API_AssociateFileSystem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/AssociateFileSystem) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/AssociateFileSystem) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/AssociateFileSystem) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/AssociateFileSystem) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/AssociateFileSystem) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/AssociateFileSystem) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/AssociateFileSystem) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/AssociateFileSystem) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/AssociateFileSystem) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/AssociateFileSystem) 