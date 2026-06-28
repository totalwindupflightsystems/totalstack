---
id: "@specs/aws/storagegateway/docs/API_DeleteSnapshotSchedule"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteSnapshotSchedule"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# DeleteSnapshotSchedule

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_DeleteSnapshotSchedule
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteSnapshotSchedule
<a name="API_DeleteSnapshotSchedule"></a>

Deletes a snapshot of a volume.

You can take snapshots of your gateway volumes on a scheduled or ad hoc basis. This API action enables you to delete a snapshot schedule for a volume. For more information, see [Backing up your volumes](https://docs.aws.amazon.com/storagegateway/latest/userguide/backing-up-volumes.html). In the `DeleteSnapshotSchedule` request, you identify the volume by providing its Amazon Resource Name (ARN). This operation is only supported for cached volume gateway types.

**Note**  
To list or delete a snapshot, you must use the Amazon EC2 API. For more information, go to [DescribeSnapshots](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSnapshots.html) in the *Amazon Elastic Compute Cloud API Reference*.

## Request Syntax
<a name="API_DeleteSnapshotSchedule_RequestSyntax"></a>

```
{
   "VolumeARN": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteSnapshotSchedule_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [VolumeARN](#API_DeleteSnapshotSchedule_RequestSyntax) **   <a name="StorageGateway-DeleteSnapshotSchedule-request-VolumeARN"></a>
The volume which snapshot schedule to delete.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Pattern: `arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):storagegateway:[a-z\-0-9]+:[0-9]+:gateway\/(.+)\/volume\/vol-(\S+)`   
Required: Yes

## Response Syntax
<a name="API_DeleteSnapshotSchedule_ResponseSyntax"></a>

```
{
   "VolumeARN": "string"
}
```

## Response Elements
<a name="API_DeleteSnapshotSchedule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [VolumeARN](#API_DeleteSnapshotSchedule_ResponseSyntax) **   <a name="StorageGateway-DeleteSnapshotSchedule-response-VolumeARN"></a>
The volume which snapshot schedule was deleted.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Pattern: `arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):storagegateway:[a-z\-0-9]+:[0-9]+:gateway\/(.+)\/volume\/vol-(\S+)` 

## Errors
<a name="API_DeleteSnapshotSchedule_Errors"></a>

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
<a name="API_DeleteSnapshotSchedule_Examples"></a>

### Example request
<a name="API_DeleteSnapshotSchedule_Example_1"></a>

The following example shows a request that deletes a snapshot schedule.

#### Sample Request
<a name="API_DeleteSnapshotSchedule_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: storagegateway.us-east-2.amazonaws.com
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20120425/us-east-2/storagegateway/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=9cd5a3584d1d67d57e61f120f35102d6b3649066abdd4bf4bbcf05bd9f2f8fe2
x-amz-date: 20120912T120000Z
x-amz-target: StorageGateway_20130630.DeleteSnapshotSchedule

{
    "VolumeARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB"
}
```

#### Sample Response
<a name="API_DeleteSnapshotSchedule_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: gur28r2rqlgb8vvs0mq17hlgij1q8glle1qeu3kpgg6f0kstauu0
Date: Wed, 12 Sep 2012 12:00:02 GMT
Content-Type: application/x-amz-json-1.1
Content-length: 137

{
    "VolumeARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB"
}
```

## See Also
<a name="API_DeleteSnapshotSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/DeleteSnapshotSchedule) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/DeleteSnapshotSchedule) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/DeleteSnapshotSchedule) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/DeleteSnapshotSchedule) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/DeleteSnapshotSchedule) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/DeleteSnapshotSchedule) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/DeleteSnapshotSchedule) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/DeleteSnapshotSchedule) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/DeleteSnapshotSchedule) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/DeleteSnapshotSchedule) 