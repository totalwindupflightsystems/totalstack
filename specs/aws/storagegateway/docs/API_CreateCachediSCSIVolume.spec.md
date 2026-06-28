---
id: "@specs/aws/storagegateway/docs/API_CreateCachediSCSIVolume"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateCachediSCSIVolume"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# CreateCachediSCSIVolume

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_CreateCachediSCSIVolume
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateCachediSCSIVolume
<a name="API_CreateCachediSCSIVolume"></a>

Creates a cached volume on a specified cached volume gateway. This operation is only supported in the cached volume gateway type.

**Note**  
Cache storage must be allocated to the gateway before you can create a cached volume. Use the [AddCache](API_AddCache.md) operation to add cache storage to a gateway.

In the request, you must specify the gateway, size of the volume in bytes, the iSCSI target name, an IP address on which to expose the target, and a unique client token. In response, the gateway creates the volume and returns information about it. This information includes the volume Amazon Resource Name (ARN), its size, and the iSCSI target ARN that initiators can use to connect to the volume target.

Optionally, you can provide the ARN for an existing volume as the `SourceVolumeARN` for this cached volume, which creates an exact copy of the existing volume’s latest recovery point. The `VolumeSizeInBytes` value must be equal to or larger than the size of the copied volume, in bytes.

## Request Syntax
<a name="API_CreateCachediSCSIVolume_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "GatewayARN": "{{string}}",
   "KMSEncrypted": {{boolean}},
   "KMSKey": "{{string}}",
   "NetworkInterfaceId": "{{string}}",
   "SnapshotId": "{{string}}",
   "SourceVolumeARN": "{{string}}",
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "TargetName": "{{string}}",
   "VolumeSizeInBytes": {{number}}
}
```

## Request Parameters
<a name="API_CreateCachediSCSIVolume_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateCachediSCSIVolume_RequestSyntax) **   <a name="StorageGateway-CreateCachediSCSIVolume-request-ClientToken"></a>
A unique identifier that you use to retry a request. If you retry a request, use the same `ClientToken` you specified in the initial request.  
Type: String  
Length Constraints: Minimum length of 5. Maximum length of 100.  
Required: Yes

 ** [GatewayARN](#API_CreateCachediSCSIVolume_RequestSyntax) **   <a name="StorageGateway-CreateCachediSCSIVolume-request-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

 ** [KMSEncrypted](#API_CreateCachediSCSIVolume_RequestSyntax) **   <a name="StorageGateway-CreateCachediSCSIVolume-request-KMSEncrypted"></a>
Set to `true` to use Amazon S3 server-side encryption with your own AWS KMS key, or `false` to use a key managed by Amazon S3. Optional.  
Valid Values: `true` \| `false`   
Type: Boolean  
Required: No

 ** [KMSKey](#API_CreateCachediSCSIVolume_RequestSyntax) **   <a name="StorageGateway-CreateCachediSCSIVolume-request-KMSKey"></a>
The Amazon Resource Name (ARN) of a symmetric AWS KMS key used for Amazon S3 server-side encryption. Storage Gateway does not support asymmetric KMS keys. This value can only be set when `KMSEncrypted` is `true`. Optional.  
Type: String  
Length Constraints: Minimum length of 7. Maximum length of 2048.  
Pattern: `(^arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):kms:([a-zA-Z0-9-]+):([0-9]+):(key|alias)/(\S+)$)|(^alias/(\S+)$)`   
Required: No

 ** [NetworkInterfaceId](#API_CreateCachediSCSIVolume_RequestSyntax) **   <a name="StorageGateway-CreateCachediSCSIVolume-request-NetworkInterfaceId"></a>
The network interface of the gateway on which to expose the iSCSI target. Accepts IPv4 and IPv6 addresses. Use [DescribeGatewayInformation](API_DescribeGatewayInformation.md) to get a list of the network interfaces available on a gateway.  
Valid Values: A valid IP address.  
Type: String  
Required: Yes

 ** [SnapshotId](#API_CreateCachediSCSIVolume_RequestSyntax) **   <a name="StorageGateway-CreateCachediSCSIVolume-request-SnapshotId"></a>
The snapshot ID (e.g. "snap-1122aabb") of the snapshot to restore as the new cached volume. Specify this field if you want to create the iSCSI storage volume from a snapshot; otherwise, do not include this field. To list snapshots for your account use [DescribeSnapshots](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/ApiReference-query-DescribeSnapshots.html) in the *Amazon Elastic Compute Cloud API Reference*.  
Type: String  
Pattern: `\Asnap-([0-9A-Fa-f]{8}|[0-9A-Fa-f]{17})\z`   
Required: No

 ** [SourceVolumeARN](#API_CreateCachediSCSIVolume_RequestSyntax) **   <a name="StorageGateway-CreateCachediSCSIVolume-request-SourceVolumeARN"></a>
The ARN for an existing volume. Specifying this ARN makes the new volume into an exact copy of the specified existing volume's latest recovery point. The `VolumeSizeInBytes` value for this new volume must be equal to or larger than the size of the existing volume, in bytes.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Pattern: `arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):storagegateway:[a-z\-0-9]+:[0-9]+:gateway\/(.+)\/volume\/vol-(\S+)`   
Required: No

 ** [Tags](#API_CreateCachediSCSIVolume_RequestSyntax) **   <a name="StorageGateway-CreateCachediSCSIVolume-request-Tags"></a>
A list of up to 50 tags that you can assign to a cached volume. Each tag is a key-value pair.  
Valid characters for key and value are letters, spaces, and numbers that you can represent in UTF-8 format, and the following special characters: \+ - = . \_ : / @. The maximum length of a tag's key is 128 characters, and the maximum length for a tag's value is 256 characters.
Type: Array of [Tag](API_Tag.md) objects  
Required: No

 ** [TargetName](#API_CreateCachediSCSIVolume_RequestSyntax) **   <a name="StorageGateway-CreateCachediSCSIVolume-request-TargetName"></a>
The name of the iSCSI target used by an initiator to connect to a volume and used as a suffix for the target ARN. For example, specifying `TargetName` as *myvolume* results in the target ARN of `arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume`. The target name must be unique across all volumes on a gateway.  
If you don't specify a value, Storage Gateway uses the value that was previously used for this volume as the new target name.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[-\.;a-z0-9]+$`   
Required: Yes

 ** [VolumeSizeInBytes](#API_CreateCachediSCSIVolume_RequestSyntax) **   <a name="StorageGateway-CreateCachediSCSIVolume-request-VolumeSizeInBytes"></a>
The size of the volume in bytes.  
Type: Long  
Required: Yes

## Response Syntax
<a name="API_CreateCachediSCSIVolume_ResponseSyntax"></a>

```
{
   "TargetARN": "string",
   "VolumeARN": "string"
}
```

## Response Elements
<a name="API_CreateCachediSCSIVolume_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TargetARN](#API_CreateCachediSCSIVolume_ResponseSyntax) **   <a name="StorageGateway-CreateCachediSCSIVolume-response-TargetARN"></a>
The Amazon Resource Name (ARN) of the volume target, which includes the iSCSI name that initiators can use to connect to the target.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 800.

 ** [VolumeARN](#API_CreateCachediSCSIVolume_ResponseSyntax) **   <a name="StorageGateway-CreateCachediSCSIVolume-response-VolumeARN"></a>
The Amazon Resource Name (ARN) of the configured volume.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Pattern: `arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):storagegateway:[a-z\-0-9]+:[0-9]+:gateway\/(.+)\/volume\/vol-(\S+)` 

## Errors
<a name="API_CreateCachediSCSIVolume_Errors"></a>

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
<a name="API_CreateCachediSCSIVolume_Examples"></a>

### Example request
<a name="API_CreateCachediSCSIVolume_Example_1"></a>

The following example shows a request that specifies that a local disk of a gateway be configured as a cached volume.

#### Sample Request
<a name="API_CreateCachediSCSIVolume_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: storagegateway.us-east-2.amazonaws.com
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20120425/us-east-2/storagegateway/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=9cd5a3584d1d67d57e61f120f35102d6b3649066abdd4bf4bbcf05bd9f2f8fe2
x-amz-date: 20120912T120000Z
x-amz-target: StorageGateway_20130630.CreateCachediSCSIVolume

{
    "ClientToken": "cachedvol112233",
    "GatewayARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B",
    "KMSEncrypted": "true",
    "KMSKey": "arn:aws:kms:us-east-1:11111111:key/b72aaa2a-2222-99tt-12345690qwe",
    "NetworkInterfaceId": "10.1.1.1",
    "TargetName": "myvolume",
    "VolumeSizeInBytes": "536870912000"
}
```

#### Sample Response
<a name="API_CreateCachediSCSIVolume_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: gur28r2rqlgb8vvs0mq17hlgij1q8glle1qeu3kpgg6f0kstauu0
Date: Wed, 12 Sep 2012 12:00:02 GMT
Content-Type: application/x-amz-json-1.1
Content-length: 263

{
    "TargetARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume",
    "VolumeARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB"
}
```

## See Also
<a name="API_CreateCachediSCSIVolume_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/CreateCachediSCSIVolume) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/CreateCachediSCSIVolume) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/CreateCachediSCSIVolume) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/CreateCachediSCSIVolume) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/CreateCachediSCSIVolume) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/CreateCachediSCSIVolume) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/CreateCachediSCSIVolume) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/CreateCachediSCSIVolume) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/CreateCachediSCSIVolume) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/CreateCachediSCSIVolume) 