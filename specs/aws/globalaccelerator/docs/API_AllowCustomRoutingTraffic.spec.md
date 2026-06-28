---
id: "@specs/aws/globalaccelerator/docs/API_AllowCustomRoutingTraffic"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AllowCustomRoutingTraffic"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# AllowCustomRoutingTraffic

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_AllowCustomRoutingTraffic
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AllowCustomRoutingTraffic
<a name="API_AllowCustomRoutingTraffic"></a>

Specify the Amazon EC2 instance (destination) IP addresses and ports for a VPC subnet endpoint that can receive traffic for a custom routing accelerator. You can allow traffic to all destinations in the subnet endpoint, or allow traffic to a specified list of destination IP addresses and ports in the subnet. Note that you cannot specify IP addresses or ports outside of the range that you configured for the endpoint group.

After you make changes, you can verify that the updates are complete by checking the status of your accelerator: the status changes from IN\_PROGRESS to DEPLOYED.

## Request Syntax
<a name="API_AllowCustomRoutingTraffic_RequestSyntax"></a>

```
{
   "AllowAllTrafficToEndpoint": {{boolean}},
   "DestinationAddresses": [ "{{string}}" ],
   "DestinationPorts": [ {{number}} ],
   "EndpointGroupArn": "{{string}}",
   "EndpointId": "{{string}}"
}
```

## Request Parameters
<a name="API_AllowCustomRoutingTraffic_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AllowAllTrafficToEndpoint](#API_AllowCustomRoutingTraffic_RequestSyntax) **   <a name="globalaccelerator-AllowCustomRoutingTraffic-request-AllowAllTrafficToEndpoint"></a>
Indicates whether all destination IP addresses and ports for a specified VPC subnet endpoint can receive traffic from a custom routing accelerator. The value is TRUE or FALSE.   
When set to TRUE, *all* destinations in the custom routing VPC subnet can receive traffic. Note that you cannot specify destination IP addresses and ports when the value is set to TRUE.  
When set to FALSE (or not specified), you *must* specify a list of destination IP addresses that are allowed to receive traffic. A list of ports is optional. If you don't specify a list of ports, the ports that can accept traffic is the same as the ports configured for the endpoint group.  
The default value is FALSE.  
Type: Boolean  
Required: No

 ** [DestinationAddresses](#API_AllowCustomRoutingTraffic_RequestSyntax) **   <a name="globalaccelerator-AllowCustomRoutingTraffic-request-DestinationAddresses"></a>
A list of specific Amazon EC2 instance IP addresses (destination addresses) in a subnet that you want to allow to receive traffic. The IP addresses must be a subset of the IP addresses that you specified for the endpoint group.  
 `DestinationAddresses` is required if `AllowAllTrafficToEndpoint` is `FALSE` or is not specified.  
Type: Array of strings  
Array Members: Maximum number of 100 items.  
Length Constraints: Maximum length of 45.  
Required: No

 ** [DestinationPorts](#API_AllowCustomRoutingTraffic_RequestSyntax) **   <a name="globalaccelerator-AllowCustomRoutingTraffic-request-DestinationPorts"></a>
A list of specific Amazon EC2 instance ports (destination ports) that you want to allow to receive traffic.  
Type: Array of integers  
Array Members: Maximum number of 100 items.  
Valid Range: Minimum value of 1. Maximum value of 65535.  
Required: No

 ** [EndpointGroupArn](#API_AllowCustomRoutingTraffic_RequestSyntax) **   <a name="globalaccelerator-AllowCustomRoutingTraffic-request-EndpointGroupArn"></a>
The Amazon Resource Name (ARN) of the endpoint group.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

 ** [EndpointId](#API_AllowCustomRoutingTraffic_RequestSyntax) **   <a name="globalaccelerator-AllowCustomRoutingTraffic-request-EndpointId"></a>
An ID for the endpoint. For custom routing accelerators, this is the virtual private cloud (VPC) subnet ID.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

## Response Elements
<a name="API_AllowCustomRoutingTraffic_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AllowCustomRoutingTraffic_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EndpointGroupNotFoundException **   
The endpoint group that you specified doesn't exist.  
HTTP Status Code: 400

 ** InternalServiceErrorException **   
There was an internal error for AWS Global Accelerator.  
HTTP Status Code: 400

 ** InvalidArgumentException **   
An argument that you specified is invalid.  
HTTP Status Code: 400

## Examples
<a name="API_AllowCustomRoutingTraffic_Examples"></a>

### Allow destination EC2 instances to receive traffic
<a name="API_AllowCustomRoutingTraffic_Example_1"></a>

The following is an example for specifying all EC2 instances in a subnet endpoint to receive traffic for a custom routing accelerator.

```
aws --region us-west-2 globalaccelerator allow-custom-routing-traffic --endpoint-group-arn 
					arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/0123vxyz/endpoint-group/ab88888example
					--endpoint-id subnet-abcd123example --allow-all
```

## See Also
<a name="API_AllowCustomRoutingTraffic_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/globalaccelerator-2018-08-08/AllowCustomRoutingTraffic) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/globalaccelerator-2018-08-08/AllowCustomRoutingTraffic) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/AllowCustomRoutingTraffic) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/globalaccelerator-2018-08-08/AllowCustomRoutingTraffic) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/AllowCustomRoutingTraffic) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/globalaccelerator-2018-08-08/AllowCustomRoutingTraffic) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/globalaccelerator-2018-08-08/AllowCustomRoutingTraffic) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/globalaccelerator-2018-08-08/AllowCustomRoutingTraffic) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/globalaccelerator-2018-08-08/AllowCustomRoutingTraffic) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/AllowCustomRoutingTraffic) 