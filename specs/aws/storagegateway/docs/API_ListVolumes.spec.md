---
id: "@specs/aws/storagegateway/docs/API_ListVolumes"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListVolumes"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# ListVolumes

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_ListVolumes
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListVolumes
<a name="API_ListVolumes"></a>

Lists the iSCSI stored volumes of a gateway. Results are sorted by volume ARN. The response includes only the volume ARNs. If you want additional volume information, use the [DescribeStorediSCSIVolumes](API_DescribeStorediSCSIVolumes.md) or the [DescribeCachediSCSIVolumes](API_DescribeCachediSCSIVolumes.md) API.

The operation supports pagination. By default, the operation returns a maximum of up to 100 volumes. You can optionally specify the `Limit` field in the body to limit the number of volumes in the response. If the number of volumes returned in the response is truncated, the response includes a Marker field. You can use this Marker value in your subsequent request to retrieve the next set of volumes. This operation is only supported in the cached volume and stored volume gateway types.

## Request Syntax
<a name="API_ListVolumes_RequestSyntax"></a>

```
{
   "GatewayARN": "{{string}}",
   "Limit": {{number}},
   "Marker": "{{string}}"
}
```

## Request Parameters
<a name="API_ListVolumes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [GatewayARN](#API_ListVolumes_RequestSyntax) **   <a name="StorageGateway-ListVolumes-request-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: No

 ** [Limit](#API_ListVolumes_RequestSyntax) **   <a name="StorageGateway-ListVolumes-request-Limit"></a>
Specifies that the list of volumes returned be limited to the specified number of items.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

 ** [Marker](#API_ListVolumes_RequestSyntax) **   <a name="StorageGateway-ListVolumes-request-Marker"></a>
A string that indicates the position at which to begin the returned list of volumes. Obtain the marker from the response of a previous List iSCSI Volumes request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.  
Required: No

## Response Syntax
<a name="API_ListVolumes_ResponseSyntax"></a>

```
{
   "GatewayARN": "string",
   "Marker": "string",
   "VolumeInfos": [ 
      { 
         "GatewayARN": "string",
         "GatewayId": "string",
         "VolumeARN": "string",
         "VolumeAttachmentStatus": "string",
         "VolumeId": "string",
         "VolumeSizeInBytes": number,
         "VolumeType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListVolumes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GatewayARN](#API_ListVolumes_ResponseSyntax) **   <a name="StorageGateway-ListVolumes-response-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.

 ** [Marker](#API_ListVolumes_ResponseSyntax) **   <a name="StorageGateway-ListVolumes-response-Marker"></a>
Use the marker in your next request to continue pagination of iSCSI volumes. If there are no more volumes to list, this field does not appear in the response body.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.

 ** [VolumeInfos](#API_ListVolumes_ResponseSyntax) **   <a name="StorageGateway-ListVolumes-response-VolumeInfos"></a>
An array of [VolumeInfo](API_VolumeInfo.md) objects, where each object describes an iSCSI volume. If no volumes are defined for the gateway, then `VolumeInfos` is an empty array "[]".  
Type: Array of [VolumeInfo](API_VolumeInfo.md) objects

## Errors
<a name="API_ListVolumes_Errors"></a>

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
<a name="API_ListVolumes_Examples"></a>

### Example request
<a name="API_ListVolumes_Example_1"></a>

The ListVolumes request in this example does not specify a `limit` or `marker` field in the response body. If the number of volumes in the gateway is greater than 100, the response returns first 100.

#### Sample Request
<a name="API_ListVolumes_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: storagegateway.us-east-2.amazonaws.com
x-amz-Date: 20120425T120000Z
Authorization: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Content-type: application/x-amz-json-1.1
x-amz-target: StorageGateway_20130630.ListVolumes

{
    "GatewayARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B"
}
```

#### Sample Response
<a name="API_ListVolumes_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Date: Wed, 25 Apr 2012 12:00:02 GMT
Content-type: application/x-amz-json-1.1
Content-length: 346

{
    "GatewayARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B",
    "VolumeInfos": [
        {
            "GatewayARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B",
            "GatewayId": "sgw-12A3456B",
            "VolumeARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB",
            "VolumeId": "vol-1122AABB",
            "VolumeSizeInBytes": "107374182400",
            "VolumeType": "STORED"
        },
        {
            "GatewayARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-13B4567C",
            "GatewayId": "sgw-gw-13B4567C",
            "VolumeARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-13B4567C/volume/vol-3344CCDD",
            "VolumeId": "vol-1122AABB",
            "VolumeSizeInBytes": "107374182400",
            "VolumeType": "STORED"
        }
    ]
```

## See Also
<a name="API_ListVolumes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/ListVolumes) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/ListVolumes) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/ListVolumes) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/ListVolumes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/ListVolumes) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/ListVolumes) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/ListVolumes) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/ListVolumes) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/ListVolumes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/ListVolumes) 