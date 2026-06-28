---
id: "@specs/aws/storagegateway/docs/API_UpdateGatewaySoftwareNow"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateGatewaySoftwareNow"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# UpdateGatewaySoftwareNow

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_UpdateGatewaySoftwareNow
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateGatewaySoftwareNow
<a name="API_UpdateGatewaySoftwareNow"></a>

Updates the gateway virtual machine (VM) software. The request immediately triggers the software update.

**Note**  
When you make this request, you get a `200 OK` success response immediately. However, it might take some time for the update to complete. You can call [DescribeGatewayInformation](API_DescribeGatewayInformation.md) to verify the gateway is in the `STATE_RUNNING` state.

**Important**  
A software update forces a system restart of your gateway. You can minimize the chance of any disruption to your applications by increasing your iSCSI Initiators' timeouts. For more information about increasing iSCSI Initiator timeouts for Windows and Linux, see [Customizing your Windows iSCSI settings](https://docs.aws.amazon.com/storagegateway/latest/userguide/ConfiguringiSCSIClientInitiatorWindowsClient.html#CustomizeWindowsiSCSISettings) and [Customizing your Linux iSCSI settings](https://docs.aws.amazon.com/storagegateway/latest/userguide/ConfiguringiSCSIClientInitiatorRedHatClient.html#CustomizeLinuxiSCSISettings), respectively.

## Request Syntax
<a name="API_UpdateGatewaySoftwareNow_RequestSyntax"></a>

```
{
   "GatewayARN": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateGatewaySoftwareNow_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [GatewayARN](#API_UpdateGatewaySoftwareNow_RequestSyntax) **   <a name="StorageGateway-UpdateGatewaySoftwareNow-request-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

## Response Syntax
<a name="API_UpdateGatewaySoftwareNow_ResponseSyntax"></a>

```
{
   "GatewayARN": "string"
}
```

## Response Elements
<a name="API_UpdateGatewaySoftwareNow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GatewayARN](#API_UpdateGatewaySoftwareNow_ResponseSyntax) **   <a name="StorageGateway-UpdateGatewaySoftwareNow-response-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.

## Errors
<a name="API_UpdateGatewaySoftwareNow_Errors"></a>

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
<a name="API_UpdateGatewaySoftwareNow_Examples"></a>

### Initiate a gateway VM update
<a name="API_UpdateGatewaySoftwareNow_Example_1"></a>

The following example shows a request that initiates a gateway VM update.

#### Sample Request
<a name="API_UpdateGatewaySoftwareNow_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: storagegateway.us-east-2.amazonaws.com
x-amz-Date: 20120425T120000Z
Authorization: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Content-type: application/x-amz-json-1.1
x-amz-target: StorageGateway_20130630.UpdateGatewaySoftwareNow

{
    "GatewayARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B"
}
```

#### Sample Response
<a name="API_UpdateGatewaySoftwareNow_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Date: Wed, 25 Apr 2012 12:00:02 GMT
Content-type: application/x-amz-json-1.1
Content-length: 80

{
    "GatewayARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B"
}
```

## See Also
<a name="API_UpdateGatewaySoftwareNow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/UpdateGatewaySoftwareNow) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/UpdateGatewaySoftwareNow) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/UpdateGatewaySoftwareNow) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/UpdateGatewaySoftwareNow) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/UpdateGatewaySoftwareNow) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/UpdateGatewaySoftwareNow) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/UpdateGatewaySoftwareNow) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/UpdateGatewaySoftwareNow) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/UpdateGatewaySoftwareNow) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/UpdateGatewaySoftwareNow) 