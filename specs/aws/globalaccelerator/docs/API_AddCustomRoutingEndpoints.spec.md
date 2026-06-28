---
id: "@specs/aws/globalaccelerator/docs/API_AddCustomRoutingEndpoints"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AddCustomRoutingEndpoints"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# AddCustomRoutingEndpoints

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_AddCustomRoutingEndpoints
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AddCustomRoutingEndpoints
<a name="API_AddCustomRoutingEndpoints"></a>

Associate a virtual private cloud (VPC) subnet endpoint with your custom routing accelerator.

The listener port range must be large enough to support the number of IP addresses that can be specified in your subnet. The number of ports required is: subnet size times the number of ports per destination EC2 instances. For example, a subnet defined as /24 requires a listener port range of at least 255 ports. 

Note: You must have enough remaining listener ports available to map to the subnet ports, or the call will fail with a LimitExceededException.

By default, all destinations in a subnet in a custom routing accelerator cannot receive traffic. To enable all destinations to receive traffic, or to specify individual port mappings that can receive traffic, see the [ AllowCustomRoutingTraffic](https://docs.aws.amazon.com/global-accelerator/latest/api/API_AllowCustomRoutingTraffic.html) operation.

## Request Syntax
<a name="API_AddCustomRoutingEndpoints_RequestSyntax"></a>

```
{
   "EndpointConfigurations": [ 
      { 
         "AttachmentArn": "{{string}}",
         "EndpointId": "{{string}}"
      }
   ],
   "EndpointGroupArn": "{{string}}"
}
```

## Request Parameters
<a name="API_AddCustomRoutingEndpoints_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EndpointConfigurations](#API_AddCustomRoutingEndpoints_RequestSyntax) **   <a name="globalaccelerator-AddCustomRoutingEndpoints-request-EndpointConfigurations"></a>
The list of endpoint objects to add to a custom routing accelerator.  
Type: Array of [CustomRoutingEndpointConfiguration](API_CustomRoutingEndpointConfiguration.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 20 items.  
Required: Yes

 ** [EndpointGroupArn](#API_AddCustomRoutingEndpoints_RequestSyntax) **   <a name="globalaccelerator-AddCustomRoutingEndpoints-request-EndpointGroupArn"></a>
The Amazon Resource Name (ARN) of the endpoint group for the custom routing endpoint.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

## Response Syntax
<a name="API_AddCustomRoutingEndpoints_ResponseSyntax"></a>

```
{
   "EndpointDescriptions": [ 
      { 
         "EndpointId": "string"
      }
   ],
   "EndpointGroupArn": "string"
}
```

## Response Elements
<a name="API_AddCustomRoutingEndpoints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EndpointDescriptions](#API_AddCustomRoutingEndpoints_ResponseSyntax) **   <a name="globalaccelerator-AddCustomRoutingEndpoints-response-EndpointDescriptions"></a>
The endpoint objects added to the custom routing accelerator.  
Type: Array of [CustomRoutingEndpointDescription](API_CustomRoutingEndpointDescription.md) objects

 ** [EndpointGroupArn](#API_AddCustomRoutingEndpoints_ResponseSyntax) **   <a name="globalaccelerator-AddCustomRoutingEndpoints-response-EndpointGroupArn"></a>
The Amazon Resource Name (ARN) of the endpoint group for the custom routing endpoint.  
Type: String  
Length Constraints: Maximum length of 255.

## Errors
<a name="API_AddCustomRoutingEndpoints_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have access permission.  
HTTP Status Code: 400

 ** ConflictException **   
You can't use both of those options.  
HTTP Status Code: 400

 ** EndpointAlreadyExistsException **   
The endpoint that you specified doesn't exist.  
HTTP Status Code: 400

 ** EndpointGroupNotFoundException **   
The endpoint group that you specified doesn't exist.  
HTTP Status Code: 400

 ** InternalServiceErrorException **   
There was an internal error for AWS Global Accelerator.  
HTTP Status Code: 400

 ** InvalidArgumentException **   
An argument that you specified is invalid.  
HTTP Status Code: 400

 ** LimitExceededException **   
Processing your request would cause you to exceed an AWS Global Accelerator limit.  
HTTP Status Code: 400

## See Also
<a name="API_AddCustomRoutingEndpoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/globalaccelerator-2018-08-08/AddCustomRoutingEndpoints) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/globalaccelerator-2018-08-08/AddCustomRoutingEndpoints) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/AddCustomRoutingEndpoints) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/globalaccelerator-2018-08-08/AddCustomRoutingEndpoints) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/AddCustomRoutingEndpoints) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/globalaccelerator-2018-08-08/AddCustomRoutingEndpoints) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/globalaccelerator-2018-08-08/AddCustomRoutingEndpoints) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/globalaccelerator-2018-08-08/AddCustomRoutingEndpoints) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/globalaccelerator-2018-08-08/AddCustomRoutingEndpoints) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/AddCustomRoutingEndpoints) 