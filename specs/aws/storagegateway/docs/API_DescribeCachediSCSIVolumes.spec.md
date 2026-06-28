---
id: "@specs/aws/storagegateway/docs/API_DescribeCachediSCSIVolumes"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeCachediSCSIVolumes"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# DescribeCachediSCSIVolumes

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_DescribeCachediSCSIVolumes
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeCachediSCSIVolumes
<a name="API_DescribeCachediSCSIVolumes"></a>

Returns a description of the gateway volumes specified in the request. This operation is only supported in the cached volume gateway types.

The list of gateway volumes in the request must be from one gateway. In the response, Storage Gateway returns volume information sorted by volume Amazon Resource Name (ARN).

## Request Syntax
<a name="API_DescribeCachediSCSIVolumes_RequestSyntax"></a>

```
{
   "VolumeARNs": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeCachediSCSIVolumes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [VolumeARNs](#API_DescribeCachediSCSIVolumes_RequestSyntax) **   <a name="StorageGateway-DescribeCachediSCSIVolumes-request-VolumeARNs"></a>
An array of strings where each string represents the Amazon Resource Name (ARN) of a cached volume. All of the specified cached volumes must be from the same gateway. Use [ListVolumes](API_ListVolumes.md) to get volume ARNs for a gateway.  
Type: Array of strings  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Pattern: `arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):storagegateway:[a-z\-0-9]+:[0-9]+:gateway\/(.+)\/volume\/vol-(\S+)`   
Required: Yes

## Response Syntax
<a name="API_DescribeCachediSCSIVolumes_ResponseSyntax"></a>

```
{
   "CachediSCSIVolumes": [ 
      { 
         "CreatedDate": number,
         "KMSKey": "string",
         "SourceSnapshotId": "string",
         "TargetName": "string",
         "VolumeARN": "string",
         "VolumeAttachmentStatus": "string",
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
<a name="API_DescribeCachediSCSIVolumes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CachediSCSIVolumes](#API_DescribeCachediSCSIVolumes_ResponseSyntax) **   <a name="StorageGateway-DescribeCachediSCSIVolumes-response-CachediSCSIVolumes"></a>
An array of objects where each object contains metadata about one cached volume.  
Type: Array of [CachediSCSIVolume](API_CachediSCSIVolume.md) objects

## Errors
<a name="API_DescribeCachediSCSIVolumes_Errors"></a>

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
<a name="API_DescribeCachediSCSIVolumes_Examples"></a>

### Example request
<a name="API_DescribeCachediSCSIVolumes_Example_1"></a>

The following example shows a request that returns a description of a volume.

#### Sample Request
<a name="API_DescribeCachediSCSIVolumes_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: storagegateway.us-east-2.amazonaws.com
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20120425/us-east-2/storagegateway/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=9cd5a3584d1d67d57e61f120f35102d6b3649066abdd4bf4bbcf05bd9f2f8fe2
x-amz-date: 20120912T120000Z
x-amz-target: StorageGateway_20130630.DescribeCachediSCSIVolumes

{
    "VolumeARNs": [
        "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB"
    ]
}
```

#### Sample Response
<a name="API_DescribeCachediSCSIVolumes_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: gur28r2rqlgb8vvs0mq17hlgij1q8glle1qeu3kpgg6f0kstauu0
Date: Wed, 12 Sep 2012 12:00:02 GMT
Content-Type: application/x-amz-json-1.1
Content-length: 664

{
    "CachediSCSIVolumes": [
        {
            "VolumeiSCSIAttributes": {
                "ChapEnabled": "true",
                "LunNumber": "0",
                "NetworkInterfaceId": "10.243.43.207",
                "NetworkInterfacePort": "3260",
                "TargetARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume"
            },
            "KMSKey": "arn:aws:kms:us-east-1:11111111:key/b72aaa2a-2222-99tt-12345690qwe",
            "VolumeARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB",
            "VolumeDiskId": "pci-0000:03:00.0-scsi-0:0:0:0",
            "VolumeId": "vol-1122AABB",
            "VolumeSizeInBytes": "1099511627776",
            "VolumeStatus": "AVAILABLE",
            "VolumeType": "CACHED iSCSI",
            "VolumeUsedInBytes": "1090000000000"
        }
    ]
}
```

## See Also
<a name="API_DescribeCachediSCSIVolumes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/DescribeCachediSCSIVolumes) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/DescribeCachediSCSIVolumes) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/DescribeCachediSCSIVolumes) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/DescribeCachediSCSIVolumes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/DescribeCachediSCSIVolumes) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/DescribeCachediSCSIVolumes) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/DescribeCachediSCSIVolumes) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/DescribeCachediSCSIVolumes) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/DescribeCachediSCSIVolumes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/DescribeCachediSCSIVolumes) 