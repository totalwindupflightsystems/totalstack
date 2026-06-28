---
id: "@specs/aws/storagegateway/docs/API_NotifyWhenUploaded"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS NotifyWhenUploaded"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# NotifyWhenUploaded

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_NotifyWhenUploaded
> **target_lang:** meta — documentation tier. ALL sections preserved.



# NotifyWhenUploaded
<a name="API_NotifyWhenUploaded"></a>

Sends you notification through Amazon EventBridge when all files written to your file share have been uploaded to Amazon S3.

Storage Gateway can send a notification through Amazon EventBridge when all files written to your file share up to that point in time have been uploaded to Amazon S3. These files include files written to the file share up to the time that you make a request for notification. When the upload is done, Storage Gateway sends you notification through EventBridge. You can configure EventBridge to send the notification through event targets such as Amazon SNS or AWS Lambda function. This operation is only supported for S3 File Gateways.

For more information, see [Getting file upload notification](https://docs.aws.amazon.com/filegateway/latest/files3/monitoring-file-gateway.html#get-notification) in the *Amazon S3 File Gateway User Guide*.

## Request Syntax
<a name="API_NotifyWhenUploaded_RequestSyntax"></a>

```
{
   "FileShareARN": "{{string}}"
}
```

## Request Parameters
<a name="API_NotifyWhenUploaded_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [FileShareARN](#API_NotifyWhenUploaded_RequestSyntax) **   <a name="StorageGateway-NotifyWhenUploaded-request-FileShareARN"></a>
The Amazon Resource Name (ARN) of the file share.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

## Response Syntax
<a name="API_NotifyWhenUploaded_ResponseSyntax"></a>

```
{
   "FileShareARN": "string",
   "NotificationId": "string"
}
```

## Response Elements
<a name="API_NotifyWhenUploaded_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FileShareARN](#API_NotifyWhenUploaded_ResponseSyntax) **   <a name="StorageGateway-NotifyWhenUploaded-response-FileShareARN"></a>
The Amazon Resource Name (ARN) of the file share.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.

 ** [NotificationId](#API_NotifyWhenUploaded_ResponseSyntax) **   <a name="StorageGateway-NotifyWhenUploaded-response-NotificationId"></a>
The randomly generated ID of the notification that was sent. This ID is in UUID format.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_NotifyWhenUploaded_Errors"></a>

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
<a name="API_NotifyWhenUploaded_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/NotifyWhenUploaded) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/NotifyWhenUploaded) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/NotifyWhenUploaded) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/NotifyWhenUploaded) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/NotifyWhenUploaded) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/NotifyWhenUploaded) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/NotifyWhenUploaded) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/NotifyWhenUploaded) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/NotifyWhenUploaded) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/NotifyWhenUploaded) 