---
id: "@specs/aws/storagegateway/docs/API_UpdateFileSystemAssociation"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateFileSystemAssociation"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# UpdateFileSystemAssociation

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_UpdateFileSystemAssociation
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateFileSystemAssociation
<a name="API_UpdateFileSystemAssociation"></a>

Updates a file system association. This operation is only supported in the FSx File Gateways.

## Request Syntax
<a name="API_UpdateFileSystemAssociation_RequestSyntax"></a>

```
{
   "AuditDestinationARN": "{{string}}",
   "CacheAttributes": { 
      "CacheStaleTimeoutInSeconds": {{number}}
   },
   "FileSystemAssociationARN": "{{string}}",
   "Password": "{{string}}",
   "UserName": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateFileSystemAssociation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AuditDestinationARN](#API_UpdateFileSystemAssociation_RequestSyntax) **   <a name="StorageGateway-UpdateFileSystemAssociation-request-AuditDestinationARN"></a>
The Amazon Resource Name (ARN) of the storage used for the audit logs.  
Type: String  
Length Constraints: Maximum length of 1024.  
Required: No

 ** [CacheAttributes](#API_UpdateFileSystemAssociation_RequestSyntax) **   <a name="StorageGateway-UpdateFileSystemAssociation-request-CacheAttributes"></a>
The refresh cache information for the file share or FSx file systems.  
Type: [CacheAttributes](API_CacheAttributes.md) object  
Required: No

 ** [FileSystemAssociationARN](#API_UpdateFileSystemAssociation_RequestSyntax) **   <a name="StorageGateway-UpdateFileSystemAssociation-request-FileSystemAssociationARN"></a>
The Amazon Resource Name (ARN) of the file system association that you want to update.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

 ** [Password](#API_UpdateFileSystemAssociation_RequestSyntax) **   <a name="StorageGateway-UpdateFileSystemAssociation-request-Password"></a>
The password of the user credential.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^[ -~]+$`   
Required: No

 ** [UserName](#API_UpdateFileSystemAssociation_RequestSyntax) **   <a name="StorageGateway-UpdateFileSystemAssociation-request-UserName"></a>
The user name of the user credential that has permission to access the root share D$ of the Amazon FSx file system. The user account must belong to the Amazon FSx delegated admin user group.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^\w[\w\.\- ]*$`   
Required: No

## Response Syntax
<a name="API_UpdateFileSystemAssociation_ResponseSyntax"></a>

```
{
   "FileSystemAssociationARN": "string"
}
```

## Response Elements
<a name="API_UpdateFileSystemAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FileSystemAssociationARN](#API_UpdateFileSystemAssociation_ResponseSyntax) **   <a name="StorageGateway-UpdateFileSystemAssociation-response-FileSystemAssociationARN"></a>
The ARN of the updated file system association.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.

## Errors
<a name="API_UpdateFileSystemAssociation_Errors"></a>

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

## See Also
<a name="API_UpdateFileSystemAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/UpdateFileSystemAssociation) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/UpdateFileSystemAssociation) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/UpdateFileSystemAssociation) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/UpdateFileSystemAssociation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/UpdateFileSystemAssociation) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/UpdateFileSystemAssociation) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/UpdateFileSystemAssociation) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/UpdateFileSystemAssociation) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/UpdateFileSystemAssociation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/UpdateFileSystemAssociation) 