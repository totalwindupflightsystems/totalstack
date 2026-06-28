---
id: "@specs/aws/storagegateway/docs/API_DeleteFileShare"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteFileShare"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# DeleteFileShare

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_DeleteFileShare
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteFileShare
<a name="API_DeleteFileShare"></a>

Deletes a file share from an S3 File Gateway. This operation is only supported for S3 File Gateways.

## Request Syntax
<a name="API_DeleteFileShare_RequestSyntax"></a>

```
{
   "FileShareARN": "{{string}}",
   "ForceDelete": {{boolean}}
}
```

## Request Parameters
<a name="API_DeleteFileShare_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [FileShareARN](#API_DeleteFileShare_RequestSyntax) **   <a name="StorageGateway-DeleteFileShare-request-FileShareARN"></a>
The Amazon Resource Name (ARN) of the file share to be deleted.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

 ** [ForceDelete](#API_DeleteFileShare_RequestSyntax) **   <a name="StorageGateway-DeleteFileShare-request-ForceDelete"></a>
If this value is set to `true`, the operation deletes a file share immediately and aborts all data uploads to AWS. Otherwise, the file share is not deleted until all data is uploaded to AWS. This process aborts the data upload process, and the file share enters the `FORCE_DELETING` status.  
Valid Values: `true` \| `false`   
Type: Boolean  
Required: No

## Response Syntax
<a name="API_DeleteFileShare_ResponseSyntax"></a>

```
{
   "FileShareARN": "string"
}
```

## Response Elements
<a name="API_DeleteFileShare_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FileShareARN](#API_DeleteFileShare_ResponseSyntax) **   <a name="StorageGateway-DeleteFileShare-response-FileShareARN"></a>
The Amazon Resource Name (ARN) of the deleted file share.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.

## Errors
<a name="API_DeleteFileShare_Errors"></a>

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
<a name="API_DeleteFileShare_Examples"></a>

### Delete a file share
<a name="API_DeleteFileShare_Example_1"></a>

In the following request, you delete a file share from a S3 File Gateway.

#### Sample Request
<a name="API_DeleteFileShare_Example_1_Request"></a>

```
{
    "FileShareARN": "arn:aws:storagegateway:us-east-2:111122223333:share/share-XXXXXXXX"
}
```

#### Sample Response
<a name="API_DeleteFileShare_Example_1_Response"></a>

```
{
    "FileShareARN": "arn:aws:storagegateway:us-east-2:111122223333:share/share-XXXXXXXX"
}
```

## See Also
<a name="API_DeleteFileShare_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/DeleteFileShare) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/DeleteFileShare) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/DeleteFileShare) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/DeleteFileShare) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/DeleteFileShare) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/DeleteFileShare) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/DeleteFileShare) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/DeleteFileShare) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/DeleteFileShare) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/DeleteFileShare) 