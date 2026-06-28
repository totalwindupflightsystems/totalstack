---
id: "@specs/aws/storagegateway/docs/API_CreateSnapshotFromVolumeRecoveryPoint"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateSnapshotFromVolumeRecoveryPoint"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# CreateSnapshotFromVolumeRecoveryPoint

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_CreateSnapshotFromVolumeRecoveryPoint
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateSnapshotFromVolumeRecoveryPoint
<a name="API_CreateSnapshotFromVolumeRecoveryPoint"></a>

Initiates a snapshot of a gateway from a volume recovery point. This operation is only supported in the cached volume gateway type.

A volume recovery point is a point in time at which all data of the volume is consistent and from which you can create a snapshot. To get a list of volume recovery point for cached volume gateway, use [ListVolumeRecoveryPoints](API_ListVolumeRecoveryPoints.md).

In the `CreateSnapshotFromVolumeRecoveryPoint` request, you identify the volume by providing its Amazon Resource Name (ARN). You must also provide a description for the snapshot. When the gateway takes a snapshot of the specified volume, the snapshot and its description appear in the Storage Gateway console. In response, the gateway returns you a snapshot ID. You can use this snapshot ID to check the snapshot progress or later use it when you want to create a volume from a snapshot.

**Note**  
To list or delete a snapshot, you must use the Amazon EC2 API. For more information, see [DescribeSnapshots](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSnapshots.html) or [DeleteSnapshot](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteSnapshot.html) in the *Amazon Elastic Compute Cloud API Reference*.

## Request Syntax
<a name="API_CreateSnapshotFromVolumeRecoveryPoint_RequestSyntax"></a>

```
{
   "SnapshotDescription": "{{string}}",
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "VolumeARN": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateSnapshotFromVolumeRecoveryPoint_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [SnapshotDescription](#API_CreateSnapshotFromVolumeRecoveryPoint_RequestSyntax) **   <a name="StorageGateway-CreateSnapshotFromVolumeRecoveryPoint-request-SnapshotDescription"></a>
Textual description of the snapshot that appears in the Amazon EC2 console, Elastic Block Store snapshots panel in the **Description** field, and in the Storage Gateway snapshot **Details** pane, **Description** field.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

 ** [Tags](#API_CreateSnapshotFromVolumeRecoveryPoint_RequestSyntax) **   <a name="StorageGateway-CreateSnapshotFromVolumeRecoveryPoint-request-Tags"></a>
A list of up to 50 tags that can be assigned to a snapshot. Each tag is a key-value pair.  
Valid characters for key and value are letters, spaces, and numbers representable in UTF-8 format, and the following special characters: \+ - = . \_ : / @. The maximum length of a tag's key is 128 characters, and the maximum length for a tag's value is 256.
Type: Array of [Tag](API_Tag.md) objects  
Required: No

 ** [VolumeARN](#API_CreateSnapshotFromVolumeRecoveryPoint_RequestSyntax) **   <a name="StorageGateway-CreateSnapshotFromVolumeRecoveryPoint-request-VolumeARN"></a>
The Amazon Resource Name (ARN) of the iSCSI volume target. Use the [DescribeStorediSCSIVolumes](API_DescribeStorediSCSIVolumes.md) operation to return to retrieve the TargetARN for specified VolumeARN.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Pattern: `arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):storagegateway:[a-z\-0-9]+:[0-9]+:gateway\/(.+)\/volume\/vol-(\S+)`   
Required: Yes

## Response Syntax
<a name="API_CreateSnapshotFromVolumeRecoveryPoint_ResponseSyntax"></a>

```
{
   "SnapshotId": "string",
   "VolumeARN": "string",
   "VolumeRecoveryPointTime": "string"
}
```

## Response Elements
<a name="API_CreateSnapshotFromVolumeRecoveryPoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SnapshotId](#API_CreateSnapshotFromVolumeRecoveryPoint_ResponseSyntax) **   <a name="StorageGateway-CreateSnapshotFromVolumeRecoveryPoint-response-SnapshotId"></a>
The ID of the snapshot.  
Type: String  
Pattern: `\Asnap-([0-9A-Fa-f]{8}|[0-9A-Fa-f]{17})\z` 

 ** [VolumeARN](#API_CreateSnapshotFromVolumeRecoveryPoint_ResponseSyntax) **   <a name="StorageGateway-CreateSnapshotFromVolumeRecoveryPoint-response-VolumeARN"></a>
The Amazon Resource Name (ARN) of the iSCSI volume target. Use the [DescribeStorediSCSIVolumes](API_DescribeStorediSCSIVolumes.md) operation to return to retrieve the TargetARN for specified VolumeARN.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Pattern: `arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):storagegateway:[a-z\-0-9]+:[0-9]+:gateway\/(.+)\/volume\/vol-(\S+)` 

 ** [VolumeRecoveryPointTime](#API_CreateSnapshotFromVolumeRecoveryPoint_ResponseSyntax) **   <a name="StorageGateway-CreateSnapshotFromVolumeRecoveryPoint-response-VolumeRecoveryPointTime"></a>
The time the volume was created from the recovery point.  
Type: String

## Errors
<a name="API_CreateSnapshotFromVolumeRecoveryPoint_Errors"></a>

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

 ** ServiceUnavailableError **   
An internal server error has occurred because the service is unavailable. For more information, see the error and message fields.    
 ** error **   
A [StorageGatewayError](API_StorageGatewayError.md) that provides more information about the cause of the error.  
 ** message **   
A human-readable message describing the error that occurred.
HTTP Status Code: 400

## Examples
<a name="API_CreateSnapshotFromVolumeRecoveryPoint_Examples"></a>

### Example request
<a name="API_CreateSnapshotFromVolumeRecoveryPoint_Example_1"></a>

The following example sends a `CreateSnapshotFromVolumeRecoveryPoint` request to take snapshot of the specified an example volume.

#### Sample Request
<a name="API_CreateSnapshotFromVolumeRecoveryPoint_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: storagegateway.us-east-2.amazonaws.com
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20120425/us-east-2/storagegateway/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=9cd5a3584d1d67d57e61f120f35102d6b3649066abdd4bf4bbcf05bd9f2f8fe2
x-amz-date: 20120912T120000Z
x-amz-target: StorageGateway_20130630.CreateSnapshotFromVolumeRecoveryPoint

{
    "VolumeARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB",
    "SnapshotDescription": "snapshot description"
}
```

#### Sample Response
<a name="API_CreateSnapshotFromVolumeRecoveryPoint_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: gur28r2rqlgb8vvs0mq17hlgij1q8glle1qeu3kpgg6f0kstauu0
Date: Wed, 12 Sep 2012 12:00:02 GMT
Content-Type: application/x-amz-json-1.1
Content-length: 137

{
    "SnapshotId": "snap-78e22663",
    "VolumeARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB",
    "VolumeRecoveryPointTime": "2012-06-30T10:10:10.000Z"
}
```

## See Also
<a name="API_CreateSnapshotFromVolumeRecoveryPoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/CreateSnapshotFromVolumeRecoveryPoint) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/CreateSnapshotFromVolumeRecoveryPoint) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/CreateSnapshotFromVolumeRecoveryPoint) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/CreateSnapshotFromVolumeRecoveryPoint) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/CreateSnapshotFromVolumeRecoveryPoint) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/CreateSnapshotFromVolumeRecoveryPoint) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/CreateSnapshotFromVolumeRecoveryPoint) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/CreateSnapshotFromVolumeRecoveryPoint) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/CreateSnapshotFromVolumeRecoveryPoint) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/CreateSnapshotFromVolumeRecoveryPoint) 