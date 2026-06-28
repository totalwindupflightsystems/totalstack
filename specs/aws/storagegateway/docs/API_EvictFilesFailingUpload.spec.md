---
id: "@specs/aws/storagegateway/docs/API_EvictFilesFailingUpload"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EvictFilesFailingUpload"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# EvictFilesFailingUpload

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_EvictFilesFailingUpload
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EvictFilesFailingUpload
<a name="API_EvictFilesFailingUpload"></a>

Starts a process that cleans the specified file share's cache of file entries that are failing upload to Amazon S3. This API operation reports success if the request is received with valid arguments, and there are no other cache clean operations currently in-progress for the specified file share. After a successful request, the cache clean operation occurs asynchronously and reports progress using CloudWatch logs and notifications.

**Important**  
If `ForceRemove` is set to `True`, the cache clean operation will delete file data from the gateway which might otherwise be recoverable. We recommend using this operation only after all other methods to clear files failing upload have been exhausted, and if your business need outweighs the potential data loss.

## Request Syntax
<a name="API_EvictFilesFailingUpload_RequestSyntax"></a>

```
{
   "FileShareARN": "{{string}}",
   "ForceRemove": {{boolean}}
}
```

## Request Parameters
<a name="API_EvictFilesFailingUpload_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [FileShareARN](#API_EvictFilesFailingUpload_RequestSyntax) **   <a name="StorageGateway-EvictFilesFailingUpload-request-FileShareARN"></a>
The Amazon Resource Name (ARN) of the file share for which you want to start the cache clean operation.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

 ** [ForceRemove](#API_EvictFilesFailingUpload_RequestSyntax) **   <a name="StorageGateway-EvictFilesFailingUpload-request-ForceRemove"></a>
Specifies whether cache entries with full or partial file data currently stored on the gateway will be forcibly removed by the cache clean operation.  
Valid arguments:  
+  `False` - The cache clean operation skips cache entries failing upload if they are associated with data currently stored on the gateway. This preserves the cached data.
+  `True` - The cache clean operation removes cache entries failing upload even if they are associated with data currently stored on the gateway. This deletes the cached data.
**Important**  
If `ForceRemove` is set to `True`, the cache clean operation will delete file data from the gateway which might otherwise be recoverable.
Type: Boolean  
Required: No

## Response Syntax
<a name="API_EvictFilesFailingUpload_ResponseSyntax"></a>

```
{
   "NotificationId": "string"
}
```

## Response Elements
<a name="API_EvictFilesFailingUpload_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NotificationId](#API_EvictFilesFailingUpload_ResponseSyntax) **   <a name="StorageGateway-EvictFilesFailingUpload-response-NotificationId"></a>
The randomly generated ID of the CloudWatch notification associated with the cache clean operation. This ID is in UUID format.  
Type: String

## Errors
<a name="API_EvictFilesFailingUpload_Errors"></a>

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
<a name="API_EvictFilesFailingUpload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/EvictFilesFailingUpload) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/EvictFilesFailingUpload) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/EvictFilesFailingUpload) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/EvictFilesFailingUpload) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/EvictFilesFailingUpload) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/EvictFilesFailingUpload) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/EvictFilesFailingUpload) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/EvictFilesFailingUpload) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/EvictFilesFailingUpload) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/EvictFilesFailingUpload) 