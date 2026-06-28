---
id: "@specs/aws/storagegateway/docs/API_UpdateSnapshotSchedule"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateSnapshotSchedule"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# UpdateSnapshotSchedule

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_UpdateSnapshotSchedule
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateSnapshotSchedule
<a name="API_UpdateSnapshotSchedule"></a>

Updates a snapshot schedule configured for a gateway volume. This operation is only supported in the cached volume and stored volume gateway types.

The default snapshot schedule for volume is once every 24 hours, starting at the creation time of the volume. You can use this API to change the snapshot schedule configured for the volume.

In the request you must identify the gateway volume whose snapshot schedule you want to update, and the schedule information, including when you want the snapshot to begin on a day and the frequency (in hours) of snapshots.

## Request Syntax
<a name="API_UpdateSnapshotSchedule_RequestSyntax"></a>

```
{
   "Description": "{{string}}",
   "RecurrenceInHours": {{number}},
   "StartAt": {{number}},
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
<a name="API_UpdateSnapshotSchedule_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateSnapshotSchedule_RequestSyntax) **   <a name="StorageGateway-UpdateSnapshotSchedule-request-Description"></a>
Optional description of the snapshot that overwrites the existing description.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

 ** [RecurrenceInHours](#API_UpdateSnapshotSchedule_RequestSyntax) **   <a name="StorageGateway-UpdateSnapshotSchedule-request-RecurrenceInHours"></a>
Frequency of snapshots. Specify the number of hours between snapshots.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 24.  
Required: Yes

 ** [StartAt](#API_UpdateSnapshotSchedule_RequestSyntax) **   <a name="StorageGateway-UpdateSnapshotSchedule-request-StartAt"></a>
The hour of the day at which the snapshot schedule begins represented as *hh*, where *hh* is the hour (0 to 23). The hour of the day is in the time zone of the gateway.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 23.  
Required: Yes

 ** [Tags](#API_UpdateSnapshotSchedule_RequestSyntax) **   <a name="StorageGateway-UpdateSnapshotSchedule-request-Tags"></a>
A list of up to 50 tags that can be assigned to a snapshot. Each tag is a key-value pair.  
Valid characters for key and value are letters, spaces, and numbers representable in UTF-8 format, and the following special characters: \+ - = . \_ : / @. The maximum length of a tag's key is 128 characters, and the maximum length for a tag's value is 256.
Type: Array of [Tag](API_Tag.md) objects  
Required: No

 ** [VolumeARN](#API_UpdateSnapshotSchedule_RequestSyntax) **   <a name="StorageGateway-UpdateSnapshotSchedule-request-VolumeARN"></a>
The Amazon Resource Name (ARN) of the volume. Use the [ListVolumes](API_ListVolumes.md) operation to return a list of gateway volumes.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Pattern: `arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):storagegateway:[a-z\-0-9]+:[0-9]+:gateway\/(.+)\/volume\/vol-(\S+)`   
Required: Yes

## Response Syntax
<a name="API_UpdateSnapshotSchedule_ResponseSyntax"></a>

```
{
   "VolumeARN": "string"
}
```

## Response Elements
<a name="API_UpdateSnapshotSchedule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [VolumeARN](#API_UpdateSnapshotSchedule_ResponseSyntax) **   <a name="StorageGateway-UpdateSnapshotSchedule-response-VolumeARN"></a>
The Amazon Resource Name (ARN) of the volume. Use the [ListVolumes](API_ListVolumes.md) operation to return a list of gateway volumes.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Pattern: `arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):storagegateway:[a-z\-0-9]+:[0-9]+:gateway\/(.+)\/volume\/vol-(\S+)` 

## Errors
<a name="API_UpdateSnapshotSchedule_Errors"></a>

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
<a name="API_UpdateSnapshotSchedule_Examples"></a>

### Example request
<a name="API_UpdateSnapshotSchedule_Example_1"></a>

The following example shows a request that updates a snapshot schedule.

#### Sample Request
<a name="API_UpdateSnapshotSchedule_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: storagegateway.us-east-2.amazonaws.com
x-amz-Date: 20120425T120000Z
Authorization: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Content-type: application/x-amz-json-1.1
x-amz-target: StorageGateway_20130630.UpdateSnapshotSchedule

{
    "VolumeARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB",
    "StartAt": "0",
    "RecurrenceInHours": "1",
    "Description": "hourly snapshot"
}
```

#### Sample Response
<a name="API_UpdateSnapshotSchedule_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Date: Wed, 25 Apr 2012 12:00:02 GMT
Content-type: application/x-amz-json-1.1
Content-length: 99

{
    "VolumeARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB"
}
```

## See Also
<a name="API_UpdateSnapshotSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/UpdateSnapshotSchedule) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/UpdateSnapshotSchedule) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/UpdateSnapshotSchedule) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/UpdateSnapshotSchedule) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/UpdateSnapshotSchedule) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/UpdateSnapshotSchedule) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/UpdateSnapshotSchedule) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/UpdateSnapshotSchedule) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/UpdateSnapshotSchedule) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/UpdateSnapshotSchedule) 