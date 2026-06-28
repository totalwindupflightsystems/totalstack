---
id: "@specs/aws/storagegateway/docs/API_RefreshCache"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RefreshCache"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# RefreshCache

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_RefreshCache
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RefreshCache
<a name="API_RefreshCache"></a>

Refreshes the cached inventory of objects for the specified file share. This operation finds objects in the Amazon S3 bucket that were added, removed, or replaced since the gateway last listed the bucket's contents and cached the results. This operation does not import files into the S3 File Gateway cache storage. It only updates the cached inventory to reflect changes in the inventory of the objects in the S3 bucket. This operation is only supported in the S3 File Gateway types.

You can subscribe to be notified through an Amazon CloudWatch event when your `RefreshCache` operation completes. For more information, see [Getting notified about file operations](https://docs.aws.amazon.com/filegateway/latest/files3/monitoring-file-gateway.html#get-notification) in the *Amazon S3 File Gateway User Guide*. This operation is Only supported for S3 File Gateways.

When this API is called, it only initiates the refresh operation. When the API call completes and returns a success code, it doesn't necessarily mean that the file refresh has completed. You should use the refresh-complete notification to determine that the operation has completed before you check for new files on the gateway file share. You can subscribe to be notified through a CloudWatch event when your `RefreshCache` operation completes.

Throttle limit: This API is asynchronous, so the gateway will accept no more than two refreshes at any time. We recommend using the refresh-complete CloudWatch event notification before issuing additional requests. For more information, see [Getting notified about file operations](https://docs.aws.amazon.com/filegateway/latest/files3/monitoring-file-gateway.html#get-notification) in the *Amazon S3 File Gateway User Guide*.

**Important**  
Wait at least 60 seconds between consecutive RefreshCache API requests.
If you invoke the RefreshCache API when two requests are already being processed, any new request will cause an `InvalidGatewayRequestException` error because too many requests were sent to the server.

**Note**  
The S3 bucket name does not need to be included when entering the list of folders in the FolderList parameter.

For more information, see [Getting notified about file operations](https://docs.aws.amazon.com/filegateway/latest/files3/monitoring-file-gateway.html#get-notification) in the *Amazon S3 File Gateway User Guide*.

## Request Syntax
<a name="API_RefreshCache_RequestSyntax"></a>

```
{
   "FileShareARN": "{{string}}",
   "FolderList": [ "{{string}}" ],
   "Recursive": {{boolean}}
}
```

## Request Parameters
<a name="API_RefreshCache_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [FileShareARN](#API_RefreshCache_RequestSyntax) **   <a name="StorageGateway-RefreshCache-request-FileShareARN"></a>
The Amazon Resource Name (ARN) of the file share you want to refresh.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

 ** [FolderList](#API_RefreshCache_RequestSyntax) **   <a name="StorageGateway-RefreshCache-request-FolderList"></a>
A comma-separated list of the paths of folders to refresh in the cache. The default is [`"/"`]. The default refreshes objects and folders at the root of the Amazon S3 bucket. If `Recursive` is set to `true`, the entire S3 bucket that the file share has access to is refreshed.  
Do not include `/` when specifying folder names. For example, you would specify `samplefolder` rather than `samplefolder/`.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 50 items.  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Required: No

 ** [Recursive](#API_RefreshCache_RequestSyntax) **   <a name="StorageGateway-RefreshCache-request-Recursive"></a>
A value that specifies whether to recursively refresh folders in the cache. The refresh includes folders that were in the cache the last time the gateway listed the folder's contents. If this value set to `true`, each folder that is listed in `FolderList` is recursively updated. Otherwise, subfolders listed in `FolderList` are not refreshed. Only objects that are in folders listed directly under `FolderList` are found and used for the update. The default is `true`.  
Valid Values: `true` \| `false`   
Type: Boolean  
Required: No

## Response Syntax
<a name="API_RefreshCache_ResponseSyntax"></a>

```
{
   "FileShareARN": "string",
   "NotificationId": "string"
}
```

## Response Elements
<a name="API_RefreshCache_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FileShareARN](#API_RefreshCache_ResponseSyntax) **   <a name="StorageGateway-RefreshCache-response-FileShareARN"></a>
The Amazon Resource Name (ARN) of the file share.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.

 ** [NotificationId](#API_RefreshCache_ResponseSyntax) **   <a name="StorageGateway-RefreshCache-response-NotificationId"></a>
The randomly generated ID of the notification that was sent. This ID is in UUID format.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_RefreshCache_Errors"></a>

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
<a name="API_RefreshCache_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/RefreshCache) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/RefreshCache) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/RefreshCache) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/RefreshCache) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/RefreshCache) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/RefreshCache) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/RefreshCache) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/RefreshCache) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/RefreshCache) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/RefreshCache) 