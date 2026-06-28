---
id: "@specs/aws/storagegateway/docs/API_ListLocalDisks"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListLocalDisks"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# ListLocalDisks

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_ListLocalDisks
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListLocalDisks
<a name="API_ListLocalDisks"></a>

Returns a list of the gateway's local disks. To specify which gateway to describe, you use the Amazon Resource Name (ARN) of the gateway in the body of the request.

The request returns a list of all disks, specifying which are configured as working storage, cache storage, or stored volume or not configured at all. The response includes a `DiskStatus` field. This field can have a value of present (the disk is available to use), missing (the disk is no longer connected to the gateway), or mismatch (the disk node is occupied by a disk that has incorrect metadata or the disk content is corrupted).

## Request Syntax
<a name="API_ListLocalDisks_RequestSyntax"></a>

```
{
   "GatewayARN": "{{string}}"
}
```

## Request Parameters
<a name="API_ListLocalDisks_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [GatewayARN](#API_ListLocalDisks_RequestSyntax) **   <a name="StorageGateway-ListLocalDisks-request-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

## Response Syntax
<a name="API_ListLocalDisks_ResponseSyntax"></a>

```
{
   "Disks": [ 
      { 
         "DiskAllocationResource": "string",
         "DiskAllocationType": "string",
         "DiskAttributeList": [ "string" ],
         "DiskId": "string",
         "DiskNode": "string",
         "DiskPath": "string",
         "DiskSizeInBytes": number,
         "DiskStatus": "string"
      }
   ],
   "GatewayARN": "string"
}
```

## Response Elements
<a name="API_ListLocalDisks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Disks](#API_ListLocalDisks_ResponseSyntax) **   <a name="StorageGateway-ListLocalDisks-response-Disks"></a>
A JSON object containing the following fields:  
+  [ListLocalDisks:Disks](#StorageGateway-ListLocalDisks-response-Disks) 
Type: Array of [Disk](API_Disk.md) objects

 ** [GatewayARN](#API_ListLocalDisks_ResponseSyntax) **   <a name="StorageGateway-ListLocalDisks-response-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.

## Errors
<a name="API_ListLocalDisks_Errors"></a>

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
<a name="API_ListLocalDisks_Examples"></a>

### Return information about a gateway's local disks
<a name="API_ListLocalDisks_Example_1"></a>

The following example shows a request that returns information about a gateway's local disks.

#### Sample Request
<a name="API_ListLocalDisks_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: storagegateway.us-east-2.amazonaws.com
x-amz-Date: 20120425T120000Z
Authorization: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Content-type: application/x-amz-json-1.1
x-amz-target: StorageGateway_20130630.ListLocalDisks

{
    "GatewayARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B"
}
```

#### Sample Response
<a name="API_ListLocalDisks_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Date: Wed, 25 Apr 2012 12:00:02 GMT
Content-type: application/x-amz-json-1.1
Content-length: 398

{
    "Disks": [
        {
            "DiskAllocationType": "CACHE_STORAGE",
            "DiskAttributeList": [
                "AttributeOne",
                "AttributeTwo"
            ],
            "DiskId": "pci-0000:03:00.0-scsi-0:0:0:0",
            "DiskNode": "SCSI(0:0)",
            "DiskPath": "/dev/sda",
            "DiskSizeInBytes": "1099511627776",
            "DiskStatus": "missing"
        },
        {
            "DiskAllocationType": "UPLOAD_BUFFER",
            "DiskAttributeList": "[]",
            "DiskAllocationResource": "",
            "DiskId": "pci-0000:03:00.0-scsi-0:0:1:0",
            "DiskNode": "SCSI(0:1)",
            "DiskPath": "/dev/sdb",
            "DiskSizeInBytes": "1099511627776",
            "DiskStatus": "present"
        }
    ],
    "GatewayARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B"
}
```

## See Also
<a name="API_ListLocalDisks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/ListLocalDisks) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/ListLocalDisks) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/ListLocalDisks) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/ListLocalDisks) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/ListLocalDisks) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/ListLocalDisks) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/ListLocalDisks) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/ListLocalDisks) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/ListLocalDisks) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/ListLocalDisks) 