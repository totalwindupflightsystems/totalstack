---
id: "@specs/aws/storagegateway/docs/API_ActivateGateway"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ActivateGateway"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# ActivateGateway

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_ActivateGateway
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ActivateGateway
<a name="API_ActivateGateway"></a>

Activates the gateway you previously deployed on your host. In the activation process, you specify information such as the AWS Region that you want to use for storing snapshots or tapes, the time zone for scheduled snapshots the gateway snapshot schedule window, an activation key, and a name for your gateway. The activation process also associates your gateway with your account. For more information, see [UpdateGatewayInformation](API_UpdateGatewayInformation.md).

**Note**  
You must turn on the gateway VM before you can activate your gateway.

## Request Syntax
<a name="API_ActivateGateway_RequestSyntax"></a>

```
{
   "ActivationKey": "{{string}}",
   "GatewayName": "{{string}}",
   "GatewayRegion": "{{string}}",
   "GatewayTimezone": "{{string}}",
   "GatewayType": "{{string}}",
   "MediumChangerType": "{{string}}",
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "TapeDriveType": "{{string}}"
}
```

## Request Parameters
<a name="API_ActivateGateway_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ActivationKey](#API_ActivateGateway_RequestSyntax) **   <a name="StorageGateway-ActivateGateway-request-ActivationKey"></a>
Your gateway activation key. You can obtain the activation key by sending an HTTP GET request with redirects enabled to the gateway IP address (port 80). The redirect URL returned in the response provides you the activation key for your gateway in the query string parameter `activationKey`. It may also include other activation-related parameters, however, these are merely defaults -- the arguments you pass to the `ActivateGateway` API call determine the actual configuration of your gateway.  
For more information, see [Getting activation key](https://docs.aws.amazon.com/storagegateway/latest/userguide/get-activation-key.html) in the *Storage Gateway User Guide*.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 50.  
Required: Yes

 ** [GatewayName](#API_ActivateGateway_RequestSyntax) **   <a name="StorageGateway-ActivateGateway-request-GatewayName"></a>
The name you configured for your gateway.  
Type: String  
Length Constraints: Minimum length of 2. Maximum length of 255.  
Pattern: `^[ -\.0-\[\]-~]*[!-\.0-\[\]-~][ -\.0-\[\]-~]*$`   
Required: Yes

 ** [GatewayRegion](#API_ActivateGateway_RequestSyntax) **   <a name="StorageGateway-ActivateGateway-request-GatewayRegion"></a>
A value that indicates the AWS Region where you want to store your data. The gateway AWS Region specified must be the same AWS Region as the AWS Region in your `Host` header in the request. For more information about available AWS Regions and endpoints for Storage Gateway, see [ Storage Gateway endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/sg.html) in the * AWS General Reference*.  
Valid Values: See [ Storage Gateway endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/sg.html) in the * AWS General Reference*.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 25.  
Required: Yes

 ** [GatewayTimezone](#API_ActivateGateway_RequestSyntax) **   <a name="StorageGateway-ActivateGateway-request-GatewayTimezone"></a>
A value that indicates the time zone you want to set for the gateway. The time zone is of the format "GMT", "GMT-hr:mm", or "GMT\+hr:mm". For example, GMT indicates Greenwich Mean Time without any offset. GMT-4:00 indicates the time is 4 hours behind GMT. GMT\+2:00 indicates the time is 2 hours ahead of GMT. The time zone is used, for example, for scheduling snapshots and your gateway's maintenance schedule.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 10.  
Required: Yes

 ** [GatewayType](#API_ActivateGateway_RequestSyntax) **   <a name="StorageGateway-ActivateGateway-request-GatewayType"></a>
A value that defines the type of gateway to activate. The type specified is critical to all later functions of the gateway and cannot be changed after activation. The default value is `CACHED`.  
Amazon FSx File Gateway is no longer available to new customers. Existing customers of FSx File Gateway can continue to use the service normally. For capabilities similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/).
Valid Values: `STORED` \| `CACHED` \| `VTL` \| `FILE_S3` \| `FILE_FSX_SMB`   
Type: String  
Length Constraints: Minimum length of 2. Maximum length of 20.  
Required: No

 ** [MediumChangerType](#API_ActivateGateway_RequestSyntax) **   <a name="StorageGateway-ActivateGateway-request-MediumChangerType"></a>
The value that indicates the type of medium changer to use for tape gateway. This field is optional.  
Valid Values: `STK-L700` \| `AWS-Gateway-VTL` \| `IBM-03584L32-0402`   
Type: String  
Length Constraints: Minimum length of 2. Maximum length of 50.  
Required: No

 ** [Tags](#API_ActivateGateway_RequestSyntax) **   <a name="StorageGateway-ActivateGateway-request-Tags"></a>
A list of up to 50 tags that you can assign to the gateway. Each tag is a key-value pair.  
Valid characters for key and value are letters, spaces, and numbers that can be represented in UTF-8 format, and the following special characters: \+ - = . \_ : / @. The maximum length of a tag's key is 128 characters, and the maximum length for a tag's value is 256 characters.
Type: Array of [Tag](API_Tag.md) objects  
Required: No

 ** [TapeDriveType](#API_ActivateGateway_RequestSyntax) **   <a name="StorageGateway-ActivateGateway-request-TapeDriveType"></a>
The value that indicates the type of tape drive to use for tape gateway. This field is optional.  
Valid Values: `IBM-ULT3580-TD5`   
Type: String  
Length Constraints: Minimum length of 2. Maximum length of 50.  
Required: No

## Response Syntax
<a name="API_ActivateGateway_ResponseSyntax"></a>

```
{
   "GatewayARN": "string"
}
```

## Response Elements
<a name="API_ActivateGateway_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GatewayARN](#API_ActivateGateway_ResponseSyntax) **   <a name="StorageGateway-ActivateGateway-response-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.

## Errors
<a name="API_ActivateGateway_Errors"></a>

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
<a name="API_ActivateGateway_Examples"></a>

### Activate a gateway
<a name="API_ActivateGateway_Example_1"></a>

The following example shows a request that activates a gateway.

#### Sample Request
<a name="API_ActivateGateway_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: storagegateway.us-east-2.amazonaws.com
x-amz-Date: 20120425T120000Z
Authorization: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Content-type: application/x-amz-json-1.1
x-amz-target: StorageGateway_20130630.ActivateGateway

{
   "ActivationKey": "29AV1-3OFV9-VVIUB-NKT0I-LRO6V",
   "GatewayName": "mygateway",
   "GatewayTimezone": "GMT-12:00",
   "GatewayRegion": "us-east-2",
   "GatewayType": "STORED",
}
```

#### Sample Response
<a name="API_ActivateGateway_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Date: Wed, 25 Apr 2012 12:00:02 GMT
Content-type: application/x-amz-json-1.1
Content-length: 80

{
    "GatewayARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-11A2222B"
}
```

## See Also
<a name="API_ActivateGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/ActivateGateway) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/ActivateGateway) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/ActivateGateway) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/ActivateGateway) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/ActivateGateway) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/ActivateGateway) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/ActivateGateway) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/ActivateGateway) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/ActivateGateway) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/ActivateGateway) 