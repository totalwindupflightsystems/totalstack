---
id: "@specs/aws/storagegateway/docs/API_DeleteAutomaticTapeCreationPolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteAutomaticTapeCreationPolicy"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# DeleteAutomaticTapeCreationPolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_DeleteAutomaticTapeCreationPolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteAutomaticTapeCreationPolicy
<a name="API_DeleteAutomaticTapeCreationPolicy"></a>

Deletes the automatic tape creation policy of a gateway. If you delete this policy, new virtual tapes must be created manually. Use the Amazon Resource Name (ARN) of the gateway in your request to remove the policy.

## Request Syntax
<a name="API_DeleteAutomaticTapeCreationPolicy_RequestSyntax"></a>

```
{
   "GatewayARN": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteAutomaticTapeCreationPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [GatewayARN](#API_DeleteAutomaticTapeCreationPolicy_RequestSyntax) **   <a name="StorageGateway-DeleteAutomaticTapeCreationPolicy-request-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

## Response Syntax
<a name="API_DeleteAutomaticTapeCreationPolicy_ResponseSyntax"></a>

```
{
   "GatewayARN": "string"
}
```

## Response Elements
<a name="API_DeleteAutomaticTapeCreationPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GatewayARN](#API_DeleteAutomaticTapeCreationPolicy_ResponseSyntax) **   <a name="StorageGateway-DeleteAutomaticTapeCreationPolicy-response-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.

## Errors
<a name="API_DeleteAutomaticTapeCreationPolicy_Errors"></a>

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
<a name="API_DeleteAutomaticTapeCreationPolicy_Examples"></a>

### Example request
<a name="API_DeleteAutomaticTapeCreationPolicy_Example_1"></a>

The following example shows a request that deletes the automatic tape creation policy of the gateway.

#### Sample Request
<a name="API_DeleteAutomaticTapeCreationPolicy_Example_1_Request"></a>

```
{
    "GatewayARN": "arn:aws:storagegateway:us-east-1:346332347513:gateway/sgw-tan"
}
```

#### Sample Response
<a name="API_DeleteAutomaticTapeCreationPolicy_Example_1_Response"></a>

```
{
    "GatewayARN": "arn:aws:storagegateway:us-east-1:346332347513:gateway/sgw-tan"
}
```

## See Also
<a name="API_DeleteAutomaticTapeCreationPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/DeleteAutomaticTapeCreationPolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/DeleteAutomaticTapeCreationPolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/DeleteAutomaticTapeCreationPolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/DeleteAutomaticTapeCreationPolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/DeleteAutomaticTapeCreationPolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/DeleteAutomaticTapeCreationPolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/DeleteAutomaticTapeCreationPolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/DeleteAutomaticTapeCreationPolicy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/DeleteAutomaticTapeCreationPolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/DeleteAutomaticTapeCreationPolicy) 