---
id: "@specs/aws/storagegateway/docs/API_DescribeStorediSCSIVolumes"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeStorediSCSIVolumes"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# DescribeStorediSCSIVolumes

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_DescribeStorediSCSIVolumes
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeStorediSCSIVolumes
<a name="API_DescribeStorediSCSIVolumes"></a>

Returns the description of the gateway volumes specified in the request. The list of gateway volumes in the request must be from one gateway. In the response, Storage Gateway returns volume information sorted by volume ARNs. This operation is only supported in stored volume gateway type.

## Request Syntax
<a name="API_DescribeStorediSCSIVolumes_RequestSyntax"></a>

```
{
   "VolumeARNs": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeStorediSCSIVolumes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [VolumeARNs](#API_DescribeStorediSCSIVolumes_RequestSyntax) **   <a name="StorageGateway-DescribeStorediSCSIVolumes-request-VolumeARNs"></a>
An array of strings where each string represents the Amazon Resource Name (ARN) of a stored volume. All of the specified stored volumes must be from the same gateway. Use [ListVolumes](API_ListVolumes.md) to get volume ARNs for a gateway.  
Type: Array of strings  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Pattern: `arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):storagegateway:[a-z\-0-9]+:[0-9]+:gateway\/(.+)\/volume\/vol-(\S+)`   
Required: Yes

## Response Syntax
<a name="API_DescribeStorediSCSIVolumes_ResponseSyntax"></a>

```
{
   "StorediSCSIVolumes": [ 
      { 
         "CreatedDate": number,
         "KMSKey": "string",
         "PreservedExistingData": boolean,
         "SourceSnapshotId": "string",
         "TargetName": "string",
         "VolumeARN": "string",
         "VolumeAttachmentStatus": "string",
         "VolumeDiskId": "string",
         "VolumeId": "string",
         "VolumeiSCSIAttributes": { 
            "ChapEnabled": boolean,
            "LunNumber": number,
            "NetworkInterfaceId": "string",
            "NetworkInterfacePort": number,
            "TargetARN": "string"
         },
         "VolumeProgress": number,
         "VolumeSizeInBytes": number,
         "VolumeStatus": "string",
         "VolumeType": "string",
         "VolumeUsedInBytes": number
      }
   ]
}
```

## Response Elements
<a name="API_DescribeStorediSCSIVolumes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [StorediSCSIVolumes](#API_DescribeStorediSCSIVolumes_ResponseSyntax) **   <a name="StorageGateway-DescribeStorediSCSIVolumes-response-StorediSCSIVolumes"></a>
Describes a single unit of output from [DescribeStorediSCSIVolumes](#API_DescribeStorediSCSIVolumes). The following fields are returned:  
+  `ChapEnabled`: Indicates whether mutual CHAP is enabled for the iSCSI target.
+  `LunNumber`: The logical disk number.
+  `NetworkInterfaceId`: The network interface ID of the stored volume that initiator use to map the stored volume as an iSCSI target.
+  `NetworkInterfacePort`: The port used to communicate with iSCSI targets.
+  `PreservedExistingData`: Indicates when the stored volume was created, existing data on the underlying local disk was preserved.
+  `SourceSnapshotId`: If the stored volume was created from a snapshot, this field contains the snapshot ID used, e.g. `snap-1122aabb`. Otherwise, this field is not included.
+  `StorediSCSIVolumes`: An array of StorediSCSIVolume objects where each object contains metadata about one stored volume.
+  `TargetARN`: The Amazon Resource Name (ARN) of the volume target.
+  `VolumeARN`: The Amazon Resource Name (ARN) of the stored volume.
+  `VolumeDiskId`: The disk ID of the local disk that was specified in the [CreateStorediSCSIVolume](API_CreateStorediSCSIVolume.md) operation.
+  `VolumeId`: The unique identifier of the storage volume, e.g. `vol-1122AABB`.
+  `VolumeiSCSIAttributes`: An [VolumeiSCSIAttributes](API_VolumeiSCSIAttributes.md) object that represents a collection of iSCSI attributes for one stored volume.
+  `VolumeProgress`: Represents the percentage complete if the volume is restoring or bootstrapping that represents the percent of data transferred. This field does not appear in the response if the stored volume is not restoring or bootstrapping.
+  `VolumeSizeInBytes`: The size of the volume in bytes.
+  `VolumeStatus`: One of the `VolumeStatus` values that indicates the state of the volume.
+  `VolumeType`: One of the enumeration values describing the type of the volume. Currently, only `STORED` volumes are supported.
Type: Array of [StorediSCSIVolume](API_StorediSCSIVolume.md) objects

## Errors
<a name="API_DescribeStorediSCSIVolumes_Errors"></a>

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
<a name="API_DescribeStorediSCSIVolumes_Examples"></a>

### Example request
<a name="API_DescribeStorediSCSIVolumes_Example_1"></a>

The following example shows a request that returns a description of a volume.

#### Sample Request
<a name="API_DescribeStorediSCSIVolumes_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: storagegateway.us-east-2.amazonaws.com
x-amz-Date: 20120425T120000Z
Authorization: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Content-type: application/x-amz-json-1.1
x-amz-target: StorageGateway_20130630.DescribeStorediSCSIVolumes

{
    "VolumeARNs": [
        "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB"
    ]
}
```

#### Sample Response
<a name="API_DescribeStorediSCSIVolumes_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Date: Wed, 25 Apr 2012 12:00:02 GMT
Content-type: application/x-amz-json-1.1
Content-length: 507

{
    "StorediSCSIVolumes": [
        {
            "VolumeiSCSIAttributes": {
                "ChapEnabled": "true",
                "NetworkInterfaceId": "10.243.43.207",
                "NetworkInterfacePort": "3260",
                "TargetARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume"
            },
            "KMSEncrypted": "false",
            "PreservedExistingData": "false",
            "VolumeARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB",
            "VolumeDiskId": "pci-0000:03:00.0-scsi-0:0:0:0",
            "VolumeId": "vol-1122AABB",
            "VolumeProgress": "23.7",
            "VolumeSizeInBytes": "1099511627776",
            "VolumeStatus": "BOOTSTRAPPING",
            "VolumeUsedInBytes": "1090000000000"
        }
    ]
}
```

## See Also
<a name="API_DescribeStorediSCSIVolumes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/DescribeStorediSCSIVolumes) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/DescribeStorediSCSIVolumes) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/DescribeStorediSCSIVolumes) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/DescribeStorediSCSIVolumes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/DescribeStorediSCSIVolumes) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/DescribeStorediSCSIVolumes) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/DescribeStorediSCSIVolumes) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/DescribeStorediSCSIVolumes) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/DescribeStorediSCSIVolumes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/DescribeStorediSCSIVolumes) 