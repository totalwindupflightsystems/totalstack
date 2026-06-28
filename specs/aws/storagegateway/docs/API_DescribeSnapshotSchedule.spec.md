---
id: "@specs/aws/storagegateway/docs/API_DescribeSnapshotSchedule"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeSnapshotSchedule"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# DescribeSnapshotSchedule

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_DescribeSnapshotSchedule
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeSnapshotSchedule
<a name="API_DescribeSnapshotSchedule"></a>

Describes the snapshot schedule for the specified gateway volume. The snapshot schedule information includes intervals at which snapshots are automatically initiated on the volume. This operation is only supported in the cached volume and stored volume types.

## Request Syntax
<a name="API_DescribeSnapshotSchedule_RequestSyntax"></a>

```
{
   "VolumeARN": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeSnapshotSchedule_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [VolumeARN](#API_DescribeSnapshotSchedule_RequestSyntax) **   <a name="StorageGateway-DescribeSnapshotSchedule-request-VolumeARN"></a>
The Amazon Resource Name (ARN) of the volume. Use the [ListVolumes](API_ListVolumes.md) operation to return a list of gateway volumes.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Pattern: `arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):storagegateway:[a-z\-0-9]+:[0-9]+:gateway\/(.+)\/volume\/vol-(\S+)`   
Required: Yes

## Response Syntax
<a name="API_DescribeSnapshotSchedule_ResponseSyntax"></a>

```
{
   "Description": "string",
   "RecurrenceInHours": number,
   "StartAt": number,
   "Tags": [ 
      { 
         "Key": "string",
         "Value": "string"
      }
   ],
   "Timezone": "string",
   "VolumeARN": "string"
}
```

## Response Elements
<a name="API_DescribeSnapshotSchedule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Description](#API_DescribeSnapshotSchedule_ResponseSyntax) **   <a name="StorageGateway-DescribeSnapshotSchedule-response-Description"></a>
The snapshot description.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [RecurrenceInHours](#API_DescribeSnapshotSchedule_ResponseSyntax) **   <a name="StorageGateway-DescribeSnapshotSchedule-response-RecurrenceInHours"></a>
The number of hours between snapshots.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 24.

 ** [StartAt](#API_DescribeSnapshotSchedule_ResponseSyntax) **   <a name="StorageGateway-DescribeSnapshotSchedule-response-StartAt"></a>
The hour of the day at which the snapshot schedule begins represented as *hh*, where *hh* is the hour (0 to 23). The hour of the day is in the time zone of the gateway.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 23.

 ** [Tags](#API_DescribeSnapshotSchedule_ResponseSyntax) **   <a name="StorageGateway-DescribeSnapshotSchedule-response-Tags"></a>
A list of up to 50 tags assigned to the snapshot schedule, sorted alphabetically by key name. Each tag is a key-value pair. For a gateway with more than 10 tags assigned, you can view all tags using the `ListTagsForResource` API operation.  
Type: Array of [Tag](API_Tag.md) objects

 ** [Timezone](#API_DescribeSnapshotSchedule_ResponseSyntax) **   <a name="StorageGateway-DescribeSnapshotSchedule-response-Timezone"></a>
A value that indicates the time zone of the gateway.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 10.

 ** [VolumeARN](#API_DescribeSnapshotSchedule_ResponseSyntax) **   <a name="StorageGateway-DescribeSnapshotSchedule-response-VolumeARN"></a>
The Amazon Resource Name (ARN) of the volume that was specified in the request.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Pattern: `arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):storagegateway:[a-z\-0-9]+:[0-9]+:gateway\/(.+)\/volume\/vol-(\S+)` 

## Errors
<a name="API_DescribeSnapshotSchedule_Errors"></a>

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
<a name="API_DescribeSnapshotSchedule_Examples"></a>

### Example request
<a name="API_DescribeSnapshotSchedule_Example_1"></a>

The following example shows a request that retrieves the snapshot schedule for a volume.

#### Sample Request
<a name="API_DescribeSnapshotSchedule_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: storagegateway.us-east-2.amazonaws.com
x-amz-Date: 20120425T120000Z
Authorization: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Content-type: application/x-amz-json-1.1
x-amz-target: StorageGateway_20130630.DescribeSnapshotSchedule

{
    "VolumeARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB"
}
```

#### Sample Response
<a name="API_DescribeSnapshotSchedule_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Date: Wed, 25 Apr 2012 12:00:02 GMT
Content-type: application/x-amz-json-1.1
Content-length: 211

{
    "VolumeARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB",
    "StartAt": "6",
    "RecurrenceInHours": "24",
    "Description": "sgw-AABB1122:vol-AABB1122:Schedule",
    "Timezone": "GMT+7:00"
}
```

## See Also
<a name="API_DescribeSnapshotSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/DescribeSnapshotSchedule) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/DescribeSnapshotSchedule) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/DescribeSnapshotSchedule) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/DescribeSnapshotSchedule) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/DescribeSnapshotSchedule) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/DescribeSnapshotSchedule) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/DescribeSnapshotSchedule) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/DescribeSnapshotSchedule) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/DescribeSnapshotSchedule) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/DescribeSnapshotSchedule) 