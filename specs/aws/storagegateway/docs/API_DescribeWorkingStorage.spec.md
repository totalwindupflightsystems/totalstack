---
id: "@specs/aws/storagegateway/docs/API_DescribeWorkingStorage"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeWorkingStorage"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# DescribeWorkingStorage

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_DescribeWorkingStorage
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeWorkingStorage
<a name="API_DescribeWorkingStorage"></a>

Returns information about the working storage of a gateway. This operation is only supported in the stored volumes gateway type. This operation is deprecated in cached volumes API version (20120630). Use DescribeUploadBuffer instead.

**Note**  
Working storage is also referred to as upload buffer. You can also use the DescribeUploadBuffer operation to add upload buffer to a stored volume gateway.

The response includes disk IDs that are configured as working storage, and it includes the amount of working storage allocated and used.

## Request Syntax
<a name="API_DescribeWorkingStorage_RequestSyntax"></a>

```
{
   "GatewayARN": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeWorkingStorage_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [GatewayARN](#API_DescribeWorkingStorage_RequestSyntax) **   <a name="StorageGateway-DescribeWorkingStorage-request-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

## Response Syntax
<a name="API_DescribeWorkingStorage_ResponseSyntax"></a>

```
{
   "DiskIds": [ "string" ],
   "GatewayARN": "string",
   "WorkingStorageAllocatedInBytes": number,
   "WorkingStorageUsedInBytes": number
}
```

## Response Elements
<a name="API_DescribeWorkingStorage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DiskIds](#API_DescribeWorkingStorage_ResponseSyntax) **   <a name="StorageGateway-DescribeWorkingStorage-response-DiskIds"></a>
An array of the gateway's local disk IDs that are configured as working storage. Each local disk ID is specified as a string (minimum length of 1 and maximum length of 300). If no local disks are configured as working storage, then the DiskIds array is empty.  
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 300.

 ** [GatewayARN](#API_DescribeWorkingStorage_ResponseSyntax) **   <a name="StorageGateway-DescribeWorkingStorage-response-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.

 ** [WorkingStorageAllocatedInBytes](#API_DescribeWorkingStorage_ResponseSyntax) **   <a name="StorageGateway-DescribeWorkingStorage-response-WorkingStorageAllocatedInBytes"></a>
The total working storage in bytes allocated for the gateway. If no working storage is configured for the gateway, this field returns 0.  
Type: Long

 ** [WorkingStorageUsedInBytes](#API_DescribeWorkingStorage_ResponseSyntax) **   <a name="StorageGateway-DescribeWorkingStorage-response-WorkingStorageUsedInBytes"></a>
The total working storage in bytes in use by the gateway. If no working storage is configured for the gateway, this field returns 0.  
Type: Long

## Errors
<a name="API_DescribeWorkingStorage_Errors"></a>

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
<a name="API_DescribeWorkingStorage_Examples"></a>

### Example request
<a name="API_DescribeWorkingStorage_Example_1"></a>

The following example shows a request to obtain a description of a gateway's working storage.

#### Sample Request
<a name="API_DescribeWorkingStorage_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: storagegateway.us-east-2.amazonaws.com
x-amz-Date: 20120425T120000Z
Authorization: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Content-type: application/x-amz-json-1.1
x-amz-target: StorageGateway_20130630.DescribeWorkingStorage

{
    "GatewayARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B"
}
```

#### Sample Response
<a name="API_DescribeWorkingStorage_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Date: Wed, 25 Apr 2012 12:00:02 GMT
Content-type: application/x-amz-json-1.1
Content-length: 241

{
    "DiskIds": [
        "pci-0000:03:00.0-scsi-0:0:0:0",
        "pci-0000:03:00.0-scsi-0:0:1:0"
    ],
    "GatewayARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B",
    "WorkingStorageAllocatedInBytes": "2199023255552",
    "WorkingStorageUsedInBytes": "789207040"
}
```

## See Also
<a name="API_DescribeWorkingStorage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/DescribeWorkingStorage) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/DescribeWorkingStorage) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/DescribeWorkingStorage) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/DescribeWorkingStorage) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/DescribeWorkingStorage) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/DescribeWorkingStorage) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/DescribeWorkingStorage) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/DescribeWorkingStorage) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/DescribeWorkingStorage) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/DescribeWorkingStorage) 