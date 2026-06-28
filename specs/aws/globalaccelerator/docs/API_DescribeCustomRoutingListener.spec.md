---
id: "@specs/aws/globalaccelerator/docs/API_DescribeCustomRoutingListener"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeCustomRoutingListener"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# DescribeCustomRoutingListener

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_DescribeCustomRoutingListener
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeCustomRoutingListener
<a name="API_DescribeCustomRoutingListener"></a>

The description of a listener for a custom routing accelerator.

## Request Syntax
<a name="API_DescribeCustomRoutingListener_RequestSyntax"></a>

```
{
   "ListenerArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeCustomRoutingListener_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ListenerArn](#API_DescribeCustomRoutingListener_RequestSyntax) **   <a name="globalaccelerator-DescribeCustomRoutingListener-request-ListenerArn"></a>
The Amazon Resource Name (ARN) of the listener to describe.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

## Response Syntax
<a name="API_DescribeCustomRoutingListener_ResponseSyntax"></a>

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
<a name="API_DescribeCustomRoutingListener_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Listener](#API_DescribeCustomRoutingListener_ResponseSyntax) **   <a name="globalaccelerator-DescribeCustomRoutingListener-response-Listener"></a>
The description of a listener for a custom routing accelerator.  
Type: [CustomRoutingListener](API_CustomRoutingListener.md) object

## Errors
<a name="API_DescribeCustomRoutingListener_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_DescribeCustomRoutingListener_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/globalaccelerator-2018-08-08/DescribeCustomRoutingListener) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/globalaccelerator-2018-08-08/DescribeCustomRoutingListener) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/DescribeCustomRoutingListener) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/globalaccelerator-2018-08-08/DescribeCustomRoutingListener) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/DescribeCustomRoutingListener) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/globalaccelerator-2018-08-08/DescribeCustomRoutingListener) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/globalaccelerator-2018-08-08/DescribeCustomRoutingListener) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/globalaccelerator-2018-08-08/DescribeCustomRoutingListener) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/globalaccelerator-2018-08-08/DescribeCustomRoutingListener) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/DescribeCustomRoutingListener) 