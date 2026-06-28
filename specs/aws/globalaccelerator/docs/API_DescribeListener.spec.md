---
id: "@specs/aws/globalaccelerator/docs/API_DescribeListener"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeListener"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# DescribeListener

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_DescribeListener
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeListener
<a name="API_DescribeListener"></a>

Describe a listener. 

## Request Syntax
<a name="API_DescribeListener_RequestSyntax"></a>

```
{
   "ListenerArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeListener_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ListenerArn](#API_DescribeListener_RequestSyntax) **   <a name="globalaccelerator-DescribeListener-request-ListenerArn"></a>
The Amazon Resource Name (ARN) of the listener to describe.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

## Response Syntax
<a name="API_DescribeListener_ResponseSyntax"></a>

```
{
   "Listener": { 
      "ClientAffinity": "string",
      "ListenerArn": "string",
      "PortRanges": [ 
         { 
            "FromPort": number,
            "ToPort": number
         }
      ],
      "Protocol": "string"
   }
}
```

## Response Elements
<a name="API_DescribeListener_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Listener](#API_DescribeListener_ResponseSyntax) **   <a name="globalaccelerator-DescribeListener-response-Listener"></a>
The description of a listener.  
Type: [Listener](API_Listener.md) object

## Errors
<a name="API_DescribeListener_Errors"></a>

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

## Examples
<a name="API_DescribeListener_Examples"></a>

### Describe a listener
<a name="API_DescribeListener_Example_1"></a>

The following is an example for describing a listener, and the response.

```
aws globalaccelerator describe-listener 
         --listener-arn arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/abcdef1234
         --region us-west-2
```

```
{
    "Listener": {
        "ListenerArn": "arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/abcdef1234",
        "PortRanges": [
            {
                "FromPort": 80,
                "ToPort": 80
            }
        ],
        "Protocol": "TCP",
        "ClientAffinity": "NONE"
    }
}
```

## See Also
<a name="API_DescribeListener_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/globalaccelerator-2018-08-08/DescribeListener) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/globalaccelerator-2018-08-08/DescribeListener) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/DescribeListener) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/globalaccelerator-2018-08-08/DescribeListener) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/DescribeListener) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/globalaccelerator-2018-08-08/DescribeListener) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/globalaccelerator-2018-08-08/DescribeListener) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/globalaccelerator-2018-08-08/DescribeListener) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/globalaccelerator-2018-08-08/DescribeListener) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/DescribeListener) 