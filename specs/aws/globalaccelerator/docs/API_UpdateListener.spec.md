---
id: "@specs/aws/globalaccelerator/docs/API_UpdateListener"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateListener"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# UpdateListener

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_UpdateListener
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateListener
<a name="API_UpdateListener"></a>

Update a listener. 

## Request Syntax
<a name="API_UpdateListener_RequestSyntax"></a>

```
{
   "ClientAffinity": "{{string}}",
   "ListenerArn": "{{string}}",
   "PortRanges": [ 
      { 
         "FromPort": {{number}},
         "ToPort": {{number}}
      }
   ],
   "Protocol": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateListener_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientAffinity](#API_UpdateListener_RequestSyntax) **   <a name="globalaccelerator-UpdateListener-request-ClientAffinity"></a>
Client affinity lets you direct all requests from a user to the same endpoint, if you have stateful applications, regardless of the port and protocol of the client request. Client affinity gives you control over whether to always route each client to the same specific endpoint.  
 AWS Global Accelerator uses a consistent-flow hashing algorithm to choose the optimal endpoint for a connection. If client affinity is `NONE`, Global Accelerator uses the "five-tuple" (5-tuple) properties—source IP address, source port, destination IP address, destination port, and protocol—to select the hash value, and then chooses the best endpoint. However, with this setting, if someone uses different ports to connect to Global Accelerator, their connections might not be always routed to the same endpoint because the hash value changes.   
If you want a given client to always be routed to the same endpoint, set client affinity to `SOURCE_IP` instead. When you use the `SOURCE_IP` setting, Global Accelerator uses the "two-tuple" (2-tuple) properties— source (client) IP address and destination IP address—to select the hash value.  
The default value is `NONE`.  
Type: String  
Valid Values: `NONE | SOURCE_IP`   
Required: No

 ** [ListenerArn](#API_UpdateListener_RequestSyntax) **   <a name="globalaccelerator-UpdateListener-request-ListenerArn"></a>
The Amazon Resource Name (ARN) of the listener to update.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

 ** [PortRanges](#API_UpdateListener_RequestSyntax) **   <a name="globalaccelerator-UpdateListener-request-PortRanges"></a>
The updated list of port ranges for the connections from clients to the accelerator.  
Type: Array of [PortRange](API_PortRange.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Required: No

 ** [Protocol](#API_UpdateListener_RequestSyntax) **   <a name="globalaccelerator-UpdateListener-request-Protocol"></a>
The updated protocol for the connections from clients to the accelerator.  
Type: String  
Valid Values: `TCP | UDP`   
Required: No

## Response Syntax
<a name="API_UpdateListener_ResponseSyntax"></a>

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
<a name="API_UpdateListener_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Listener](#API_UpdateListener_ResponseSyntax) **   <a name="globalaccelerator-UpdateListener-response-Listener"></a>
Information for the updated listener.  
Type: [Listener](API_Listener.md) object

## Errors
<a name="API_UpdateListener_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** ListenerNotFoundException **   
The listener that you specified doesn't exist.  
HTTP Status Code: 400

## Examples
<a name="API_UpdateListener_Examples"></a>

### Update a listener
<a name="API_UpdateListener_Example_1"></a>

The following is an example of updating the port range for a listener, and the response.

```
aws globalaccelerator update-listener
    --listener-arn arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/0123vxyz 
    --port-ranges FromPort=100,ToPort=100
```

```
{
    "Listener": {
        "ListenerArn": "arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/0123vxyz
        "PortRanges": [
            {
                "FromPort": 100,
                "ToPort": 100
            }
        ],
        "Protocol": "TCP",
        "ClientAffinity": "NONE"
    }
}
```

## See Also
<a name="API_UpdateListener_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/globalaccelerator-2018-08-08/UpdateListener) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/globalaccelerator-2018-08-08/UpdateListener) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/UpdateListener) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/globalaccelerator-2018-08-08/UpdateListener) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/UpdateListener) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/globalaccelerator-2018-08-08/UpdateListener) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/globalaccelerator-2018-08-08/UpdateListener) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/globalaccelerator-2018-08-08/UpdateListener) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/globalaccelerator-2018-08-08/UpdateListener) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/UpdateListener) 