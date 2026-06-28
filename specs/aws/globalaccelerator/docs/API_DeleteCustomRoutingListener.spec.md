---
id: "@specs/aws/globalaccelerator/docs/API_DeleteCustomRoutingListener"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteCustomRoutingListener"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# DeleteCustomRoutingListener

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_DeleteCustomRoutingListener
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteCustomRoutingListener
<a name="API_DeleteCustomRoutingListener"></a>

Delete a listener for a custom routing accelerator.

## Request Syntax
<a name="API_DeleteCustomRoutingListener_RequestSyntax"></a>

```
{
   "ListenerArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteCustomRoutingListener_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ListenerArn](#API_DeleteCustomRoutingListener_RequestSyntax) **   <a name="globalaccelerator-DeleteCustomRoutingListener-request-ListenerArn"></a>
The Amazon Resource Name (ARN) of the listener to delete.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

## Response Elements
<a name="API_DeleteCustomRoutingListener_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteCustomRoutingListener_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AssociatedEndpointGroupFoundException **   
The listener that you specified has an endpoint group associated with it. You must remove all dependent resources from a listener before you can delete it.  
HTTP Status Code: 400

 ** InternalServiceErrorException **   
There was an internal error for AWS Global Accelerator.  
HTTP Status Code: 400

 ** InvalidArgumentException **   
An argument that you specified is invalid.  
HTTP Status Code: 400

 ** ListenerNotFoundException **   
The listener that you specified doesn't exist.  
HTTP Status Code: 400

## See Also
<a name="API_DeleteCustomRoutingListener_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/globalaccelerator-2018-08-08/DeleteCustomRoutingListener) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/globalaccelerator-2018-08-08/DeleteCustomRoutingListener) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/DeleteCustomRoutingListener) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/globalaccelerator-2018-08-08/DeleteCustomRoutingListener) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/DeleteCustomRoutingListener) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/globalaccelerator-2018-08-08/DeleteCustomRoutingListener) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/globalaccelerator-2018-08-08/DeleteCustomRoutingListener) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/globalaccelerator-2018-08-08/DeleteCustomRoutingListener) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/globalaccelerator-2018-08-08/DeleteCustomRoutingListener) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/DeleteCustomRoutingListener) 