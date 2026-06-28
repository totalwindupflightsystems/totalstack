---
id: "@specs/aws/globalaccelerator/docs/API_CreateCustomRoutingListener"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateCustomRoutingListener"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# CreateCustomRoutingListener

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_CreateCustomRoutingListener
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateCustomRoutingListener
<a name="API_CreateCustomRoutingListener"></a>

Create a listener to process inbound connections from clients to a custom routing accelerator. Connections arrive to assigned static IP addresses on the port range that you specify. 

## Request Syntax
<a name="API_CreateCustomRoutingListener_RequestSyntax"></a>

```
{
   "AcceleratorArn": "{{string}}",
   "IdempotencyToken": "{{string}}",
   "PortRanges": [ 
      { 
         "FromPort": {{number}},
         "ToPort": {{number}}
      }
   ]
}
```

## Request Parameters
<a name="API_CreateCustomRoutingListener_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AcceleratorArn](#API_CreateCustomRoutingListener_RequestSyntax) **   <a name="globalaccelerator-CreateCustomRoutingListener-request-AcceleratorArn"></a>
The Amazon Resource Name (ARN) of the accelerator for a custom routing listener.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

 ** [IdempotencyToken](#API_CreateCustomRoutingListener_RequestSyntax) **   <a name="globalaccelerator-CreateCustomRoutingListener-request-IdempotencyToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency—that is, the uniqueness—of the request.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

 ** [PortRanges](#API_CreateCustomRoutingListener_RequestSyntax) **   <a name="globalaccelerator-CreateCustomRoutingListener-request-PortRanges"></a>
The port range to support for connections from clients to your accelerator.  
Separately, you set port ranges for endpoints. For more information, see [About endpoints for custom routing accelerators](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-endpoints.html).  
Type: Array of [PortRange](API_PortRange.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Required: Yes

## Response Syntax
<a name="API_CreateCustomRoutingListener_ResponseSyntax"></a>

```
{
   "Listener": { 
      "ListenerArn": "string",
      "PortRanges": [ 
         { 
            "FromPort": number,
            "ToPort": number
         }
      ]
   }
}
```

## Response Elements
<a name="API_CreateCustomRoutingListener_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Listener](#API_CreateCustomRoutingListener_ResponseSyntax) **   <a name="globalaccelerator-CreateCustomRoutingListener-response-Listener"></a>
The listener that you've created for a custom routing accelerator.  
Type: [CustomRoutingListener](API_CustomRoutingListener.md) object

## Errors
<a name="API_CreateCustomRoutingListener_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AcceleratorNotFoundException **   
The accelerator that you specified doesn't exist.  
HTTP Status Code: 400

 ** InternalServiceErrorException **   
There was an internal error for AWS Global Accelerator.  
HTTP Status Code: 400

 ** InvalidArgumentException **   
An argument that you specified is invalid.  
HTTP Status Code: 400

 ** InvalidPortRangeException **   
The port numbers that you specified are not valid numbers or are not unique for this accelerator.  
HTTP Status Code: 400

 ** LimitExceededException **   
Processing your request would cause you to exceed an AWS Global Accelerator limit.  
HTTP Status Code: 400

## Examples
<a name="API_CreateCustomRoutingListener_Examples"></a>

### Create a listener for a custom routing accelerator
<a name="API_CreateCustomRoutingListener_Example_1"></a>

The following is an example of creating a listener for a custom routing accelerator, and the response.

```
aws --region us-west-2 globalaccelerator create-custom-routing-listener 
       --accelerator-arn arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh 
       --port-ranges FromPort=5000,ToPort=10000
```

```
{
    "Listener": {
        "PortRange": [
            "FromPort": 5000 
            "ToPort": 10000, 
        ], 
        "ListenerArn": "arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/0123vxyz"
    }
}
```

## See Also
<a name="API_CreateCustomRoutingListener_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/globalaccelerator-2018-08-08/CreateCustomRoutingListener) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/globalaccelerator-2018-08-08/CreateCustomRoutingListener) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/CreateCustomRoutingListener) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/globalaccelerator-2018-08-08/CreateCustomRoutingListener) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/CreateCustomRoutingListener) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/globalaccelerator-2018-08-08/CreateCustomRoutingListener) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/globalaccelerator-2018-08-08/CreateCustomRoutingListener) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/globalaccelerator-2018-08-08/CreateCustomRoutingListener) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/globalaccelerator-2018-08-08/CreateCustomRoutingListener) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/CreateCustomRoutingListener) 