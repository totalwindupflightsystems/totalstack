---
id: "@specs/aws/storagegateway/docs/API_DisassociateFileSystem"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DisassociateFileSystem"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# DisassociateFileSystem

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_DisassociateFileSystem
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DisassociateFileSystem
<a name="API_DisassociateFileSystem"></a>

Disassociates an Amazon FSx file system from the specified gateway. After the disassociation process finishes, the gateway can no longer access the Amazon FSx file system. This operation is only supported in the FSx File Gateway type.

## Request Syntax
<a name="API_DisassociateFileSystem_RequestSyntax"></a>

```
{
   "FileSystemAssociationARN": "{{string}}",
   "ForceDelete": {{boolean}}
}
```

## Request Parameters
<a name="API_DisassociateFileSystem_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [FileSystemAssociationARN](#API_DisassociateFileSystem_RequestSyntax) **   <a name="StorageGateway-DisassociateFileSystem-request-FileSystemAssociationARN"></a>
The Amazon Resource Name (ARN) of the file system association to be deleted.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

 ** [ForceDelete](#API_DisassociateFileSystem_RequestSyntax) **   <a name="StorageGateway-DisassociateFileSystem-request-ForceDelete"></a>
If this value is set to true, the operation disassociates an Amazon FSx file system immediately. It ends all data uploads to the file system, and the file system association enters the `FORCE_DELETING` status. If this value is set to false, the Amazon FSx file system does not disassociate until all data is uploaded.  
Type: Boolean  
Required: No

## Response Syntax
<a name="API_DisassociateFileSystem_ResponseSyntax"></a>

```
{
   "FileSystemAssociationARN": "string"
}
```

## Response Elements
<a name="API_DisassociateFileSystem_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FileSystemAssociationARN](#API_DisassociateFileSystem_ResponseSyntax) **   <a name="StorageGateway-DisassociateFileSystem-response-FileSystemAssociationARN"></a>
The Amazon Resource Name (ARN) of the deleted file system association.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.

## Errors
<a name="API_DisassociateFileSystem_Errors"></a>

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
<a name="API_DisassociateFileSystem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/DisassociateFileSystem) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/DisassociateFileSystem) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/DisassociateFileSystem) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/DisassociateFileSystem) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/DisassociateFileSystem) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/DisassociateFileSystem) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/DisassociateFileSystem) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/DisassociateFileSystem) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/DisassociateFileSystem) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/DisassociateFileSystem) 