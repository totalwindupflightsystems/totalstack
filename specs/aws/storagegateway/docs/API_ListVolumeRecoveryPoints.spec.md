---
id: "@specs/aws/storagegateway/docs/API_ListVolumeRecoveryPoints"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListVolumeRecoveryPoints"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# ListVolumeRecoveryPoints

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_ListVolumeRecoveryPoints
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListVolumeRecoveryPoints
<a name="API_ListVolumeRecoveryPoints"></a>

Lists the recovery points for a specified gateway. This operation is only supported in the cached volume gateway type.

Each cache volume has one recovery point. A volume recovery point is a point in time at which all data of the volume is consistent and from which you can create a snapshot or clone a new cached volume from a source volume. To create a snapshot from a volume recovery point use the [CreateSnapshotFromVolumeRecoveryPoint](API_CreateSnapshotFromVolumeRecoveryPoint.md) operation.

## Request Syntax
<a name="API_ListVolumeRecoveryPoints_RequestSyntax"></a>

```
{
   "GatewayARN": "{{string}}"
}
```

## Request Parameters
<a name="API_ListVolumeRecoveryPoints_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [GatewayARN](#API_ListVolumeRecoveryPoints_RequestSyntax) **   <a name="StorageGateway-ListVolumeRecoveryPoints-request-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

## Response Syntax
<a name="API_ListVolumeRecoveryPoints_ResponseSyntax"></a>

```
{
   "GatewayARN": "string",
   "VolumeRecoveryPointInfos": [ 
      { 
         "VolumeARN": "string",
         "VolumeRecoveryPointTime": "string",
         "VolumeSizeInBytes": number,
         "VolumeUsageInBytes": number
      }
   ]
}
```

## Response Elements
<a name="API_ListVolumeRecoveryPoints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GatewayARN](#API_ListVolumeRecoveryPoints_ResponseSyntax) **   <a name="StorageGateway-ListVolumeRecoveryPoints-response-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.

 ** [VolumeRecoveryPointInfos](#API_ListVolumeRecoveryPoints_ResponseSyntax) **   <a name="StorageGateway-ListVolumeRecoveryPoints-response-VolumeRecoveryPointInfos"></a>
An array of [VolumeRecoveryPointInfo](API_VolumeRecoveryPointInfo.md) objects.  
Type: Array of [VolumeRecoveryPointInfo](API_VolumeRecoveryPointInfo.md) objects

## Errors
<a name="API_ListVolumeRecoveryPoints_Errors"></a>

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
<a name="API_ListVolumeRecoveryPoints_Examples"></a>

### Example request
<a name="API_ListVolumeRecoveryPoints_Example_1"></a>

The following example sends a `ListVolumeRecoveryPoints` request to take a snapshot of the specified example volume.

#### Sample Request
<a name="API_ListVolumeRecoveryPoints_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: storagegateway.us-east-2.amazonaws.com
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20120425/us-east-2/storagegateway/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=9cd5a3584d1d67d57e61f120f35102d6b3649066abdd4bf4bbcf05bd9f2f8fe2
x-amz-date: 20120912T120000Z
x-amz-target: StorageGateway_20130630.ListVolumeRecoveryPoints

{
    "GatewayARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B"
}
```

#### Sample Response
<a name="API_ListVolumeRecoveryPoints_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: gur28r2rqlgb8vvs0mq17hlgij1q8glle1qeu3kpgg6f0kstauu0
Date: Wed, 12 Sep 2012 12:00:02 GMT
Content-Type: application/x-amz-json-1.1
Content-length: 137

{
    "GatewayARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B",
    "VolumeRecoveryPointInfos": [
        {
            "VolumeARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB",
            "VolumeRecoveryPointTime": "2012-09-04T21:08:44.627Z",
            "VolumeSizeInBytes": "536870912000"
        }
    ]
}
```

## See Also
<a name="API_ListVolumeRecoveryPoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/ListVolumeRecoveryPoints) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/ListVolumeRecoveryPoints) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/ListVolumeRecoveryPoints) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/ListVolumeRecoveryPoints) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/ListVolumeRecoveryPoints) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/ListVolumeRecoveryPoints) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/ListVolumeRecoveryPoints) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/ListVolumeRecoveryPoints) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/ListVolumeRecoveryPoints) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/ListVolumeRecoveryPoints) 