---
id: "@specs/aws/storagegateway/docs/API_ShutdownGateway"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ShutdownGateway"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# ShutdownGateway

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_ShutdownGateway
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ShutdownGateway
<a name="API_ShutdownGateway"></a>

Shuts down a Tape Gateway or Volume Gateway. To specify which gateway to shut down, use the Amazon Resource Name (ARN) of the gateway in the body of your request.

**Note**  
This API action cannot be used to shut down S3 File Gateway or FSx File Gateway.

The operation shuts down the gateway service component running in the gateway's virtual machine (VM) and not the host VM.

**Note**  
If you want to shut down the VM, it is recommended that you first shut down the gateway component in the VM to avoid unpredictable conditions.

After the gateway is shutdown, you cannot call any other API except [StartGateway](API_StartGateway.md), [DescribeGatewayInformation](API_DescribeGatewayInformation.md), and [ListGateways](API_ListGateways.md). For more information, see [ActivateGateway](API_ActivateGateway.md). Your applications cannot read from or write to the gateway's storage volumes, and there are no snapshots taken.

**Note**  
When you make a shutdown request, you will get a `200 OK` success response immediately. However, it might take some time for the gateway to shut down. You can call the [DescribeGatewayInformation](API_DescribeGatewayInformation.md) API to check the status. For more information, see [ActivateGateway](API_ActivateGateway.md).

If do not intend to use the gateway again, you must delete the gateway (using [DeleteGateway](API_DeleteGateway.md)) to no longer pay software charges associated with the gateway.

## Request Syntax
<a name="API_ShutdownGateway_RequestSyntax"></a>

```
{
   "GatewayARN": "{{string}}"
}
```

## Request Parameters
<a name="API_ShutdownGateway_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [GatewayARN](#API_ShutdownGateway_RequestSyntax) **   <a name="StorageGateway-ShutdownGateway-request-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

## Response Syntax
<a name="API_ShutdownGateway_ResponseSyntax"></a>

```
{
   "GatewayARN": "string"
}
```

## Response Elements
<a name="API_ShutdownGateway_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GatewayARN](#API_ShutdownGateway_ResponseSyntax) **   <a name="StorageGateway-ShutdownGateway-response-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.

## Errors
<a name="API_ShutdownGateway_Errors"></a>

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
<a name="API_ShutdownGateway_Examples"></a>

### Shut down a gateway
<a name="API_ShutdownGateway_Example_1"></a>

The following example shows a request that shuts down a gateway.

#### Sample Request
<a name="API_ShutdownGateway_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: storagegateway.us-east-2.amazonaws.com
x-amz-Date: 20120425T120000Z
Authorization: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Content-type: application/x-amz-json-1.1
x-amz-target: StorageGateway_20130630.ShutdownGateway

{
    "GatewayARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B"
}
```

#### Sample Response
<a name="API_ShutdownGateway_Example_1_Response"></a>

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
<a name="API_ShutdownGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/ShutdownGateway) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/ShutdownGateway) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/ShutdownGateway) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/ShutdownGateway) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/ShutdownGateway) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/ShutdownGateway) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/ShutdownGateway) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/ShutdownGateway) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/ShutdownGateway) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/ShutdownGateway) 