---
id: "@specs/aws/storagegateway/docs/API_DescribeChapCredentials"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeChapCredentials"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# DescribeChapCredentials

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_DescribeChapCredentials
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeChapCredentials
<a name="API_DescribeChapCredentials"></a>

Returns an array of Challenge-Handshake Authentication Protocol (CHAP) credentials information for a specified iSCSI target, one for each target-initiator pair. This operation is supported in the volume and tape gateway types.

## Request Syntax
<a name="API_DescribeChapCredentials_RequestSyntax"></a>

```
{
   "TargetARN": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeChapCredentials_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [TargetARN](#API_DescribeChapCredentials_RequestSyntax) **   <a name="StorageGateway-DescribeChapCredentials-request-TargetARN"></a>
The Amazon Resource Name (ARN) of the iSCSI volume target. Use the [DescribeStorediSCSIVolumes](API_DescribeStorediSCSIVolumes.md) operation to return to retrieve the TargetARN for specified VolumeARN.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 800.  
Required: Yes

## Response Syntax
<a name="API_DescribeChapCredentials_ResponseSyntax"></a>

```
{
   "ChapCredentials": [ 
      { 
         "InitiatorName": "string",
         "SecretToAuthenticateInitiator": "string",
         "SecretToAuthenticateTarget": "string",
         "TargetARN": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeChapCredentials_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChapCredentials](#API_DescribeChapCredentials_ResponseSyntax) **   <a name="StorageGateway-DescribeChapCredentials-response-ChapCredentials"></a>
An array of [ChapInfo](API_ChapInfo.md) objects that represent CHAP credentials. Each object in the array contains CHAP credential information for one target-initiator pair. If no CHAP credentials are set, an empty array is returned. CHAP credential information is provided in a JSON object with the following fields:  
+  **InitiatorName**: The iSCSI initiator that connects to the target.
+  **SecretToAuthenticateInitiator**: The secret key that the initiator (for example, the Windows client) must provide to participate in mutual CHAP with the target.
+  **SecretToAuthenticateTarget**: The secret key that the target must provide to participate in mutual CHAP with the initiator (e.g. Windows client).
+  **TargetARN**: The Amazon Resource Name (ARN) of the storage volume.
Type: Array of [ChapInfo](API_ChapInfo.md) objects

## Errors
<a name="API_DescribeChapCredentials_Errors"></a>

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
<a name="API_DescribeChapCredentials_Examples"></a>

### Example request
<a name="API_DescribeChapCredentials_Example_1"></a>

The following example shows a request that returns the CHAP credentials of an iSCSI target.

#### Sample Request
<a name="API_DescribeChapCredentials_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: storagegateway.us-east-2.amazonaws.com
x-amz-Date: 20120425T120000Z
Authorization: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Content-type: application/x-amz-json-1.1
x-amz-target: StorageGateway_20130630.DescribeChapCredentials

{
    "TargetARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume"
}
```

#### Sample Response
<a name="API_DescribeChapCredentials_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Date: Wed, 25 Apr 2012 12:00:02 GMT
Content-type: application/x-amz-json-1.1
Content-length: 235

{
    "ChapCredentials": {
        "TargetARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume",
        "SecretToAuthenticateInitiator": "111111111111",
        "InitiatorName": "iqn.1991-05.com.microsoft:computername.domain.example.com",
        "SecretToAuthenticateTarget": "222222222222"
    }
}
```

## See Also
<a name="API_DescribeChapCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/DescribeChapCredentials) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/DescribeChapCredentials) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/DescribeChapCredentials) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/DescribeChapCredentials) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/DescribeChapCredentials) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/DescribeChapCredentials) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/DescribeChapCredentials) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/DescribeChapCredentials) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/DescribeChapCredentials) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/DescribeChapCredentials) 