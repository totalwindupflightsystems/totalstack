---
id: "@specs/aws/storagegateway/docs/API_CreateSnapshot"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateSnapshot"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# CreateSnapshot

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_CreateSnapshot
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateSnapshot
<a name="API_CreateSnapshot"></a>

Initiates a snapshot of a volume.

Storage Gateway provides the ability to back up point-in-time snapshots of your data to Amazon Simple Storage (Amazon S3) for durable off-site recovery, and also import the data to an Amazon Elastic Block Store (EBS) volume in Amazon Elastic Compute Cloud (EC2). You can take snapshots of your gateway volume on a scheduled or ad hoc basis. This API enables you to take an ad hoc snapshot. For more information, see [Editing a snapshot schedule](https://docs.aws.amazon.com/storagegateway/latest/userguide/managing-volumes.html#SchedulingSnapshot).

In the `CreateSnapshot` request, you identify the volume by providing its Amazon Resource Name (ARN). You must also provide description for the snapshot. When Storage Gateway takes the snapshot of specified volume, the snapshot and description appears in the Storage Gateway console. In response, Storage Gateway returns you a snapshot ID. You can use this snapshot ID to check the snapshot progress or later use it when you want to create a volume from a snapshot. This operation is only supported in stored and cached volume gateway type.

**Note**  
To list or delete a snapshot, you must use the Amazon EC2 API. For more information, see [DescribeSnapshots](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSnapshots.html) or [DeleteSnapshot](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteSnapshot.html) in the *Amazon Elastic Compute Cloud API Reference*.

**Important**  
Volume and snapshot IDs are changing to a longer length ID format. For more information, see the important note on the [Welcome](https://docs.aws.amazon.com/storagegateway/latest/APIReference/Welcome.html) page.

## Request Syntax
<a name="API_CreateSnapshot_RequestSyntax"></a>

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
<a name="API_CreateSnapshot_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [SnapshotDescription](#API_CreateSnapshot_RequestSyntax) **   <a name="StorageGateway-CreateSnapshot-request-SnapshotDescription"></a>
Textual description of the snapshot that appears in the Amazon EC2 console, Elastic Block Store snapshots panel in the **Description** field, and in the Storage Gateway snapshot **Details** pane, **Description** field.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

 ** [Tags](#API_CreateSnapshot_RequestSyntax) **   <a name="StorageGateway-CreateSnapshot-request-Tags"></a>
A list of up to 50 tags that can be assigned to a snapshot. Each tag is a key-value pair.  
Valid characters for key and value are letters, spaces, and numbers representable in UTF-8 format, and the following special characters: \+ - = . \_ : / @. The maximum length of a tag's key is 128 characters, and the maximum length for a tag's value is 256.
Type: Array of [Tag](API_Tag.md) objects  
Required: No

 ** [VolumeARN](#API_CreateSnapshot_RequestSyntax) **   <a name="StorageGateway-CreateSnapshot-request-VolumeARN"></a>
The Amazon Resource Name (ARN) of the volume. Use the [ListVolumes](API_ListVolumes.md) operation to return a list of gateway volumes.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Pattern: `arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):storagegateway:[a-z\-0-9]+:[0-9]+:gateway\/(.+)\/volume\/vol-(\S+)`   
Required: Yes

## Response Syntax
<a name="API_CreateSnapshot_ResponseSyntax"></a>

```
{
   "SnapshotId": "string",
   "VolumeARN": "string"
}
```

## Response Elements
<a name="API_CreateSnapshot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SnapshotId](#API_CreateSnapshot_ResponseSyntax) **   <a name="StorageGateway-CreateSnapshot-response-SnapshotId"></a>
The snapshot ID that is used to refer to the snapshot in future operations such as describing snapshots (Amazon Elastic Compute Cloud API `DescribeSnapshots`) or creating a volume from a snapshot ([CreateStorediSCSIVolume](API_CreateStorediSCSIVolume.md)).  
Type: String  
Pattern: `\Asnap-([0-9A-Fa-f]{8}|[0-9A-Fa-f]{17})\z` 

 ** [VolumeARN](#API_CreateSnapshot_ResponseSyntax) **   <a name="StorageGateway-CreateSnapshot-response-VolumeARN"></a>
The Amazon Resource Name (ARN) of the volume of which the snapshot was taken.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Pattern: `arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):storagegateway:[a-z\-0-9]+:[0-9]+:gateway\/(.+)\/volume\/vol-(\S+)` 

## Errors
<a name="API_CreateSnapshot_Errors"></a>

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
<a name="API_CreateSnapshot_Examples"></a>

### Example request
<a name="API_CreateSnapshot_Example_1"></a>

The following example sends a `CreateSnapshot` request to take snapshot of the specified an example volume.

#### Sample Request
<a name="API_CreateSnapshot_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: storagegateway.us-east-2.amazonaws.com
x-amz-Date: 20120425T120000Z
Authorization: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Content-type: application/x-amz-json-1.1
x-amz-target: StorageGateway_20130630.CreateSnapshot

{
    "VolumeARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB",
    "SnapshotDescription": "snapshot description"
}
```

#### Sample Response
<a name="API_CreateSnapshot_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Date: Wed, 25 Apr 2012 12:00:02 GMT
Content-type: application/x-amz-json-1.1
Content-length: 128

{
    "VolumeARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB",
    "SnapshotId": "snap-78e22663"
}
```

## See Also
<a name="API_CreateSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/CreateSnapshot) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/CreateSnapshot) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/CreateSnapshot) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/CreateSnapshot) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/CreateSnapshot) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/CreateSnapshot) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/CreateSnapshot) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/CreateSnapshot) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/CreateSnapshot) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/CreateSnapshot) 