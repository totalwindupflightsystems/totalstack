---
id: "@specs/aws/storagegateway/docs/API_UpdateAutomaticTapeCreationPolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateAutomaticTapeCreationPolicy"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# UpdateAutomaticTapeCreationPolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_UpdateAutomaticTapeCreationPolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateAutomaticTapeCreationPolicy
<a name="API_UpdateAutomaticTapeCreationPolicy"></a>

Updates the automatic tape creation policy of a gateway. Use this to update the policy with a new set of automatic tape creation rules. This is only supported for tape gateways.

By default, there is no automatic tape creation policy.

**Note**  
A gateway can have only one automatic tape creation policy.

## Request Syntax
<a name="API_UpdateAutomaticTapeCreationPolicy_RequestSyntax"></a>

```
{
   "AutomaticTapeCreationRules": [ 
      { 
         "MinimumNumTapes": {{number}},
         "PoolId": "{{string}}",
         "TapeBarcodePrefix": "{{string}}",
         "TapeSizeInBytes": {{number}},
         "Worm": {{boolean}}
      }
   ],
   "GatewayARN": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateAutomaticTapeCreationPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AutomaticTapeCreationRules](#API_UpdateAutomaticTapeCreationPolicy_RequestSyntax) **   <a name="StorageGateway-UpdateAutomaticTapeCreationPolicy-request-AutomaticTapeCreationRules"></a>
An automatic tape creation policy consists of a list of automatic tape creation rules. The rules determine when and how to automatically create new tapes.  
Type: Array of [AutomaticTapeCreationRule](API_AutomaticTapeCreationRule.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Required: Yes

 ** [GatewayARN](#API_UpdateAutomaticTapeCreationPolicy_RequestSyntax) **   <a name="StorageGateway-UpdateAutomaticTapeCreationPolicy-request-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

## Response Syntax
<a name="API_UpdateAutomaticTapeCreationPolicy_ResponseSyntax"></a>

```
{
   "GatewayARN": "string"
}
```

## Response Elements
<a name="API_UpdateAutomaticTapeCreationPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GatewayARN](#API_UpdateAutomaticTapeCreationPolicy_ResponseSyntax) **   <a name="StorageGateway-UpdateAutomaticTapeCreationPolicy-response-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.

## Errors
<a name="API_UpdateAutomaticTapeCreationPolicy_Errors"></a>

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

## See Also
<a name="API_UpdateAutomaticTapeCreationPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/UpdateAutomaticTapeCreationPolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/UpdateAutomaticTapeCreationPolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/UpdateAutomaticTapeCreationPolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/UpdateAutomaticTapeCreationPolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/UpdateAutomaticTapeCreationPolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/UpdateAutomaticTapeCreationPolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/UpdateAutomaticTapeCreationPolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/UpdateAutomaticTapeCreationPolicy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/UpdateAutomaticTapeCreationPolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/UpdateAutomaticTapeCreationPolicy) 