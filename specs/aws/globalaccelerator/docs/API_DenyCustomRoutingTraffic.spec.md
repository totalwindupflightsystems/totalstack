---
id: "@specs/aws/globalaccelerator/docs/API_DenyCustomRoutingTraffic"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DenyCustomRoutingTraffic"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# DenyCustomRoutingTraffic

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_DenyCustomRoutingTraffic
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DenyCustomRoutingTraffic
<a name="API_DenyCustomRoutingTraffic"></a>

Specify the Amazon EC2 instance (destination) IP addresses and ports for a VPC subnet endpoint that cannot receive traffic for a custom routing accelerator. You can deny traffic to all destinations in the VPC endpoint, or deny traffic to a specified list of destination IP addresses and ports. Note that you cannot specify IP addresses or ports outside of the range that you configured for the endpoint group.

After you make changes, you can verify that the updates are complete by checking the status of your accelerator: the status changes from IN\_PROGRESS to DEPLOYED.

## Request Syntax
<a name="API_DenyCustomRoutingTraffic_RequestSyntax"></a>

```
{
   "DenyAllTrafficToEndpoint": {{boolean}},
   "DestinationAddresses": [ "{{string}}" ],
   "DestinationPorts": [ {{number}} ],
   "EndpointGroupArn": "{{string}}",
   "EndpointId": "{{string}}"
}
```

## Request Parameters
<a name="API_DenyCustomRoutingTraffic_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DenyAllTrafficToEndpoint](#API_DenyCustomRoutingTraffic_RequestSyntax) **   <a name="globalaccelerator-DenyCustomRoutingTraffic-request-DenyAllTrafficToEndpoint"></a>
Indicates whether all destination IP addresses and ports for a specified VPC subnet endpoint *cannot* receive traffic from a custom routing accelerator. The value is TRUE or FALSE.   
When set to TRUE, *no* destinations in the custom routing VPC subnet can receive traffic. Note that you cannot specify destination IP addresses and ports when the value is set to TRUE.  
When set to FALSE (or not specified), you *must* specify a list of destination IP addresses that cannot receive traffic. A list of ports is optional. If you don't specify a list of ports, the ports that can accept traffic is the same as the ports configured for the endpoint group.  
The default value is FALSE.  
Type: Boolean  
Required: No

 ** [DestinationAddresses](#API_DenyCustomRoutingTraffic_RequestSyntax) **   <a name="globalaccelerator-DenyCustomRoutingTraffic-request-DestinationAddresses"></a>
A list of specific Amazon EC2 instance IP addresses (destination addresses) in a subnet that you want to prevent from receiving traffic. The IP addresses must be a subset of the IP addresses allowed for the VPC subnet associated with the endpoint group.  
Type: Array of strings  
Array Members: Maximum number of 100 items.  
Length Constraints: Maximum length of 45.  
Required: No

 ** [DestinationPorts](#API_DenyCustomRoutingTraffic_RequestSyntax) **   <a name="globalaccelerator-DenyCustomRoutingTraffic-request-DestinationPorts"></a>
A list of specific Amazon EC2 instance ports (destination ports) in a subnet endpoint that you want to prevent from receiving traffic.  
Type: Array of integers  
Array Members: Maximum number of 100 items.  
Valid Range: Minimum value of 1. Maximum value of 65535.  
Required: No

 ** [EndpointGroupArn](#API_DenyCustomRoutingTraffic_RequestSyntax) **   <a name="globalaccelerator-DenyCustomRoutingTraffic-request-EndpointGroupArn"></a>
The Amazon Resource Name (ARN) of the endpoint group.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

 ** [EndpointId](#API_DenyCustomRoutingTraffic_RequestSyntax) **   <a name="globalaccelerator-DenyCustomRoutingTraffic-request-EndpointId"></a>
An ID for the endpoint. For custom routing accelerators, this is the virtual private cloud (VPC) subnet ID.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

## Response Elements
<a name="API_DenyCustomRoutingTraffic_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DenyCustomRoutingTraffic_Errors"></a>

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
<a name="API_DenyCustomRoutingTraffic_Examples"></a>

### Deny traffic to specific destination instances
<a name="API_DenyCustomRoutingTraffic_Example_1"></a>

The following is an example for specifying specific instances in a subnet endpoint that cannot receive traffic for a custom routing accelerator.

```
aws --region us-west-2 globalaccelerator deny-custom-routing-traffic --endpoint-group-arn 
					arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/0123vxyz/endpoint-group/ab88888example
					--endpoint-id subnet-abcd123example --destination-addresses "198.51.100.52" "198.51.100.53" --destination-ports "80"
```

## See Also
<a name="API_DenyCustomRoutingTraffic_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/globalaccelerator-2018-08-08/DenyCustomRoutingTraffic) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/globalaccelerator-2018-08-08/DenyCustomRoutingTraffic) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/DenyCustomRoutingTraffic) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/globalaccelerator-2018-08-08/DenyCustomRoutingTraffic) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/DenyCustomRoutingTraffic) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/globalaccelerator-2018-08-08/DenyCustomRoutingTraffic) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/globalaccelerator-2018-08-08/DenyCustomRoutingTraffic) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/globalaccelerator-2018-08-08/DenyCustomRoutingTraffic) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/globalaccelerator-2018-08-08/DenyCustomRoutingTraffic) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/DenyCustomRoutingTraffic) 