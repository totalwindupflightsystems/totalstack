---
id: "@specs/aws/storagegateway/docs/API_UpdateGatewayInformation"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateGatewayInformation"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# UpdateGatewayInformation

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_UpdateGatewayInformation
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateGatewayInformation
<a name="API_UpdateGatewayInformation"></a>

Updates a gateway's metadata, which includes the gateway's name, time zone, and metadata cache size. To specify which gateway to update, use the Amazon Resource Name (ARN) of the gateway in your request.

**Note**  
For gateways activated after September 2, 2015, the gateway's ARN contains the gateway ID rather than the gateway name. However, changing the name of the gateway has no effect on the gateway's ARN.

## Request Syntax
<a name="API_UpdateGatewayInformation_RequestSyntax"></a>

```
{
   "CloudWatchLogGroupARN": "{{string}}",
   "GatewayARN": "{{string}}",
   "GatewayCapacity": "{{string}}",
   "GatewayName": "{{string}}",
   "GatewayTimezone": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateGatewayInformation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CloudWatchLogGroupARN](#API_UpdateGatewayInformation_RequestSyntax) **   <a name="StorageGateway-UpdateGatewayInformation-request-CloudWatchLogGroupARN"></a>
The Amazon Resource Name (ARN) of the Amazon CloudWatch log group that you want to use to monitor and log events in the gateway.  
For more information, see [What is Amazon CloudWatch Logs?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html)   
Type: String  
Length Constraints: Maximum length of 562.  
Required: No

 ** [GatewayARN](#API_UpdateGatewayInformation_RequestSyntax) **   <a name="StorageGateway-UpdateGatewayInformation-request-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

 ** [GatewayCapacity](#API_UpdateGatewayInformation_RequestSyntax) **   <a name="StorageGateway-UpdateGatewayInformation-request-GatewayCapacity"></a>
Specifies the size of the gateway's metadata cache. This setting impacts gateway performance and hardware recommendations. For more information, see [Performance guidance for gateways with multiple file shares](https://docs.aws.amazon.com/filegateway/latest/files3/performance-multiple-file-shares.html) in the *Amazon S3 File Gateway User Guide*.  
Type: String  
Valid Values: `Small | Medium | Large`   
Required: No

 ** [GatewayName](#API_UpdateGatewayInformation_RequestSyntax) **   <a name="StorageGateway-UpdateGatewayInformation-request-GatewayName"></a>
The name you configured for your gateway.  
Type: String  
Length Constraints: Minimum length of 2. Maximum length of 255.  
Pattern: `^[ -\.0-\[\]-~]*[!-\.0-\[\]-~][ -\.0-\[\]-~]*$`   
Required: No

 ** [GatewayTimezone](#API_UpdateGatewayInformation_RequestSyntax) **   <a name="StorageGateway-UpdateGatewayInformation-request-GatewayTimezone"></a>
A value that indicates the time zone of the gateway.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 10.  
Required: No

## Response Syntax
<a name="API_UpdateGatewayInformation_ResponseSyntax"></a>

```
{
   "GatewayARN": "string",
   "GatewayName": "string"
}
```

## Response Elements
<a name="API_UpdateGatewayInformation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GatewayARN](#API_UpdateGatewayInformation_ResponseSyntax) **   <a name="StorageGateway-UpdateGatewayInformation-response-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.

 ** [GatewayName](#API_UpdateGatewayInformation_ResponseSyntax) **   <a name="StorageGateway-UpdateGatewayInformation-response-GatewayName"></a>
The name you configured for your gateway.  
Type: String

## Errors
<a name="API_UpdateGatewayInformation_Errors"></a>

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
<a name="API_UpdateGatewayInformation_Examples"></a>

### Update a gateway's name
<a name="API_UpdateGatewayInformation_Example_1"></a>

The following example shows a request that updates the name of a gateway.

#### Sample Request
<a name="API_UpdateGatewayInformation_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: storagegateway.us-east-2.amazonaws.com
x-amz-Date: 20120425T120000Z
Authorization: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Content-type: application/x-amz-json-1.1
x-amz-target: StorageGateway_20130630.GatewayInformation

{
    "GatewayARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B",
    "GatewayName": "mygateway2"
}
```

#### Sample Response
<a name="API_UpdateGatewayInformation_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Date: Wed, 25 Apr 2012 12:00:02 GMT
Content-type: application/x-amz-json-1.1
Content-length: 81

{
    "GatewayARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B"
}
```

## See Also
<a name="API_UpdateGatewayInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/UpdateGatewayInformation) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/UpdateGatewayInformation) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/UpdateGatewayInformation) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/UpdateGatewayInformation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/UpdateGatewayInformation) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/UpdateGatewayInformation) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/UpdateGatewayInformation) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/UpdateGatewayInformation) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/UpdateGatewayInformation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/UpdateGatewayInformation) 