---
id: "@specs/aws/storagegateway/docs/API_CreateTapeWithBarcode"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateTapeWithBarcode"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# CreateTapeWithBarcode

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_CreateTapeWithBarcode
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateTapeWithBarcode
<a name="API_CreateTapeWithBarcode"></a>

Creates a virtual tape by using your own barcode. You write data to the virtual tape and then archive the tape. A barcode is unique and cannot be reused if it has already been used on a tape. This applies to barcodes used on deleted tapes. This operation is only supported in the tape gateway type.

**Note**  
Cache storage must be allocated to the gateway before you can create a virtual tape. Use the [AddCache](API_AddCache.md) operation to add cache storage to a gateway.

## Request Syntax
<a name="API_CreateTapeWithBarcode_RequestSyntax"></a>

```
{
   "GatewayARN": "{{string}}",
   "KMSEncrypted": {{boolean}},
   "KMSKey": "{{string}}",
   "PoolId": "{{string}}",
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "TapeBarcode": "{{string}}",
   "TapeSizeInBytes": {{number}},
   "Worm": {{boolean}}
}
```

## Request Parameters
<a name="API_CreateTapeWithBarcode_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [GatewayARN](#API_CreateTapeWithBarcode_RequestSyntax) **   <a name="StorageGateway-CreateTapeWithBarcode-request-GatewayARN"></a>
The unique Amazon Resource Name (ARN) that represents the gateway to associate the virtual tape with. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

 ** [KMSEncrypted](#API_CreateTapeWithBarcode_RequestSyntax) **   <a name="StorageGateway-CreateTapeWithBarcode-request-KMSEncrypted"></a>
Set to `true` to use Amazon S3 server-side encryption with your own AWS KMS key, or `false` to use a key managed by Amazon S3. Optional.  
Valid Values: `true` \| `false`   
Type: Boolean  
Required: No

 ** [KMSKey](#API_CreateTapeWithBarcode_RequestSyntax) **   <a name="StorageGateway-CreateTapeWithBarcode-request-KMSKey"></a>
The Amazon Resource Name (ARN) of a symmetric AWS KMS key used for Amazon S3 server-side encryption. Storage Gateway does not support asymmetric KMS keys. This value can only be set when `KMSEncrypted` is `true`. Optional.  
Type: String  
Length Constraints: Minimum length of 7. Maximum length of 2048.  
Pattern: `(^arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):kms:([a-zA-Z0-9-]+):([0-9]+):(key|alias)/(\S+)$)|(^alias/(\S+)$)`   
Required: No

 ** [PoolId](#API_CreateTapeWithBarcode_RequestSyntax) **   <a name="StorageGateway-CreateTapeWithBarcode-request-PoolId"></a>
The ID of the pool that you want to add your tape to for archiving. The tape in this pool is archived in the S3 storage class that is associated with the pool. When you use your backup application to eject the tape, the tape is archived directly into the storage class (S3 Glacier or S3 Deep Archive) that corresponds to the pool.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Required: No

 ** [Tags](#API_CreateTapeWithBarcode_RequestSyntax) **   <a name="StorageGateway-CreateTapeWithBarcode-request-Tags"></a>
A list of up to 50 tags that can be assigned to a virtual tape that has a barcode. Each tag is a key-value pair.  
Valid characters for key and value are letters, spaces, and numbers representable in UTF-8 format, and the following special characters: \+ - = . \_ : / @. The maximum length of a tag's key is 128 characters, and the maximum length for a tag's value is 256.
Type: Array of [Tag](API_Tag.md) objects  
Required: No

 ** [TapeBarcode](#API_CreateTapeWithBarcode_RequestSyntax) **   <a name="StorageGateway-CreateTapeWithBarcode-request-TapeBarcode"></a>
The barcode that you want to assign to the tape.  
Barcodes cannot be reused. This includes barcodes used for tapes that have been deleted.
Type: String  
Length Constraints: Minimum length of 5. Maximum length of 16.  
Pattern: `^[A-Z0-9]*$`   
Required: Yes

 ** [TapeSizeInBytes](#API_CreateTapeWithBarcode_RequestSyntax) **   <a name="StorageGateway-CreateTapeWithBarcode-request-TapeSizeInBytes"></a>
The size, in bytes, of the virtual tape that you want to create.  
The size must be aligned by gigabyte (1024\*1024\*1024 bytes).
Type: Long  
Required: Yes

 ** [Worm](#API_CreateTapeWithBarcode_RequestSyntax) **   <a name="StorageGateway-CreateTapeWithBarcode-request-Worm"></a>
Set to `TRUE` if the tape you are creating is to be configured as a write-once-read-many (WORM) tape.  
Type: Boolean  
Required: No

## Response Syntax
<a name="API_CreateTapeWithBarcode_ResponseSyntax"></a>

```
{
   "TapeARN": "string"
}
```

## Response Elements
<a name="API_CreateTapeWithBarcode_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TapeARN](#API_CreateTapeWithBarcode_ResponseSyntax) **   <a name="StorageGateway-CreateTapeWithBarcode-response-TapeARN"></a>
A unique Amazon Resource Name (ARN) that represents the virtual tape that was created.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Pattern: `arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):storagegateway:[a-z\-0-9]+:[0-9]+:tape\/[0-9A-Z]{5,16}$` 

## Errors
<a name="API_CreateTapeWithBarcode_Errors"></a>

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
<a name="API_CreateTapeWithBarcode_Examples"></a>

### Create a tape with your own barcode in a tape gateway
<a name="API_CreateTapeWithBarcode_Example_1"></a>

In the following request, you add a 100 GB tape cartridge to the tape gateway with the ID sgw-12A3456B. The tape appears in the gateway's virtual tape library. In the request, you set the barcode to "TEST12345".

#### Sample Request
<a name="API_CreateTapeWithBarcode_Example_1_Request"></a>

```
{
    "GatewayARN": "arn:aws:storagegateway:us-east-2:999999999999:gateway/sgw-12A3456B",
    "KMSEncrypted": "true",
    "KMSKey": "arn:aws:kms:us-east-1:11111111:key/b72aaa2a-2222-99tt-12345690qwe",
    "TapeSizeInBytes": "107374182400",
    "PooId": "Deep_Archive",
    "TapeBarcode": "TEST12345"
}
```

#### Sample Response
<a name="API_CreateTapeWithBarcode_Example_1_Response"></a>

```
{
    "TapeARN": [
        "arn:aws:storagegateway:us-east-2:999999999999:tape/TEST12345"
    ]
}
```

## See Also
<a name="API_CreateTapeWithBarcode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/CreateTapeWithBarcode) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/CreateTapeWithBarcode) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/CreateTapeWithBarcode) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/CreateTapeWithBarcode) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/CreateTapeWithBarcode) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/CreateTapeWithBarcode) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/CreateTapeWithBarcode) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/CreateTapeWithBarcode) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/CreateTapeWithBarcode) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/CreateTapeWithBarcode) 