---
id: "@specs/aws/storagegateway/docs/API_ListAutomaticTapeCreationPolicies"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListAutomaticTapeCreationPolicies"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# ListAutomaticTapeCreationPolicies

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_ListAutomaticTapeCreationPolicies
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListAutomaticTapeCreationPolicies
<a name="API_ListAutomaticTapeCreationPolicies"></a>

Lists the automatic tape creation policies for a gateway. If there are no automatic tape creation policies for the gateway, it returns an empty list.

This operation is only supported for tape gateways.

## Request Syntax
<a name="API_ListAutomaticTapeCreationPolicies_RequestSyntax"></a>

```
{
   "GatewayARN": "{{string}}"
}
```

## Request Parameters
<a name="API_ListAutomaticTapeCreationPolicies_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [GatewayARN](#API_ListAutomaticTapeCreationPolicies_RequestSyntax) **   <a name="StorageGateway-ListAutomaticTapeCreationPolicies-request-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: No

## Response Syntax
<a name="API_ListAutomaticTapeCreationPolicies_ResponseSyntax"></a>

```
{
   "AutomaticTapeCreationPolicyInfos": [ 
      { 
         "AutomaticTapeCreationRules": [ 
            { 
               "MinimumNumTapes": number,
               "PoolId": "string",
               "TapeBarcodePrefix": "string",
               "TapeSizeInBytes": number,
               "Worm": boolean
            }
         ],
         "GatewayARN": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListAutomaticTapeCreationPolicies_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AutomaticTapeCreationPolicyInfos](#API_ListAutomaticTapeCreationPolicies_ResponseSyntax) **   <a name="StorageGateway-ListAutomaticTapeCreationPolicies-response-AutomaticTapeCreationPolicyInfos"></a>
Gets a listing of information about the gateway's automatic tape creation policies, including the automatic tape creation rules and the gateway that is using the policies.  
Type: Array of [AutomaticTapeCreationPolicyInfo](API_AutomaticTapeCreationPolicyInfo.md) objects

## Errors
<a name="API_ListAutomaticTapeCreationPolicies_Errors"></a>

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
<a name="API_ListAutomaticTapeCreationPolicies_Examples"></a>

### List automatic tape creation policies for a tape gateway
<a name="API_ListAutomaticTapeCreationPolicies_Example_1"></a>

In the following request, you get a listing of the automatic tape creation policies for a tape gateway with the ARN of "`sgw-tan`".

#### Sample Request
<a name="API_ListAutomaticTapeCreationPolicies_Example_1_Request"></a>

```
{
    "GatewayARN": "arn:aws:storagegateway:us-east-1:346332347513:gateway/sgw-tan"
}
```

#### Sample Response
<a name="API_ListAutomaticTapeCreationPolicies_Example_1_Response"></a>

```
{
    "AutomaticTapeCreationPolicyInfos": [
        {
            "AutomaticTapeCreationRules": [
                {
                    "MinimumNumTapes": "1",
                    "PoolId": "GLACIER",
                    "TapeBarcodePrefix": "TAN",
                    "TapeSizeInBytes": "107374182400"
                }
            ],
            "GatewayARN": "arn:aws:storagegateway:us-east-1:346332347513:gateway/sgw-tan"
        }
    ]
}
```

## See Also
<a name="API_ListAutomaticTapeCreationPolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/ListAutomaticTapeCreationPolicies) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/ListAutomaticTapeCreationPolicies) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/ListAutomaticTapeCreationPolicies) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/ListAutomaticTapeCreationPolicies) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/ListAutomaticTapeCreationPolicies) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/ListAutomaticTapeCreationPolicies) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/ListAutomaticTapeCreationPolicies) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/ListAutomaticTapeCreationPolicies) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/ListAutomaticTapeCreationPolicies) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/ListAutomaticTapeCreationPolicies) 