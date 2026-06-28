---
id: "@specs/aws/storagegateway/docs/API_AddWorkingStorage"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AddWorkingStorage"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# AddWorkingStorage

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_AddWorkingStorage
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AddWorkingStorage
<a name="API_AddWorkingStorage"></a>

Configures one or more gateway local disks as working storage for a gateway. This operation is only supported in the stored volume gateway type. This operation is deprecated in cached volume API version 20120630. Use [AddUploadBuffer](API_AddUploadBuffer.md) instead.

**Note**  
Working storage is also referred to as upload buffer. You can also use the [AddUploadBuffer](API_AddUploadBuffer.md) operation to add upload buffer to a stored volume gateway.

In the request, you specify the gateway Amazon Resource Name (ARN) to which you want to add working storage, and one or more disk IDs that you want to configure as working storage.

## Request Syntax
<a name="API_AddWorkingStorage_RequestSyntax"></a>

```
{
   "DiskIds": [ "{{string}}" ],
   "GatewayARN": "{{string}}"
}
```

## Request Parameters
<a name="API_AddWorkingStorage_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DiskIds](#API_AddWorkingStorage_RequestSyntax) **   <a name="StorageGateway-AddWorkingStorage-request-DiskIds"></a>
An array of strings that identify disks that are to be configured as working storage. Each string has a minimum length of 1 and maximum length of 300. You can get the disk IDs from the [ListLocalDisks](API_ListLocalDisks.md) API.  
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 300.  
Required: Yes

 ** [GatewayARN](#API_AddWorkingStorage_RequestSyntax) **   <a name="StorageGateway-AddWorkingStorage-request-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

## Response Syntax
<a name="API_AddWorkingStorage_ResponseSyntax"></a>

```
{
   "GatewayARN": "string"
}
```

## Response Elements
<a name="API_AddWorkingStorage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GatewayARN](#API_AddWorkingStorage_ResponseSyntax) **   <a name="StorageGateway-AddWorkingStorage-response-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.

## Errors
<a name="API_AddWorkingStorage_Errors"></a>

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
<a name="API_AddWorkingStorage_Examples"></a>

### Example request
<a name="API_AddWorkingStorage_Example_1"></a>

The following example shows a request that specifies that two local disks of a gateway are to be configured as working storage.

#### Sample Request
<a name="API_AddWorkingStorage_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: storagegateway.us-east-2.amazonaws.com
x-amz-Date: 20120425T120000Z
Authorization: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Content-type: application/x-amz-json-1.1
x-amz-target: StorageGateway_20130630.AddWorkingStorage

{
    "GatewayARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B",
    "DiskIds": [
        "pci-0000:03:00.0-scsi-0:0:0:0",
        "pci-0000:04:00.0-scsi-1:0:0:0"
    ]
}
```

#### Sample Response
<a name="API_AddWorkingStorage_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Date: Wed, 25 Apr 2012 12:00:02 GMT
Content-type: application/x-amz-json-1.1
Content-length: 80

{
    "GatewayARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B"
}
```

## See Also
<a name="API_AddWorkingStorage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/AddWorkingStorage) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/AddWorkingStorage) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/AddWorkingStorage) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/AddWorkingStorage) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/AddWorkingStorage) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/AddWorkingStorage) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/AddWorkingStorage) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/AddWorkingStorage) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/AddWorkingStorage) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/AddWorkingStorage) 