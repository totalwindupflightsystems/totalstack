---
id: "@specs/aws/globalaccelerator/docs/API_EndpointGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EndpointGroup"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# EndpointGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_EndpointGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EndpointGroup
<a name="API_EndpointGroup"></a>

A complex type for the endpoint group. An AWS Region can have only one endpoint group for a specific listener. 

## Contents
<a name="API_EndpointGroup_Contents"></a>

 ** EndpointDescriptions **   <a name="globalaccelerator-Type-EndpointGroup-EndpointDescriptions"></a>
The list of endpoint objects.  
Type: Array of [EndpointDescription](API_EndpointDescription.md) objects  
Required: No

 ** EndpointGroupArn **   <a name="globalaccelerator-Type-EndpointGroup-EndpointGroupArn"></a>
The Amazon Resource Name (ARN) of the endpoint group.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: No

 ** EndpointGroupRegion **   <a name="globalaccelerator-Type-EndpointGroup-EndpointGroupRegion"></a>
The AWS Region where the endpoint group is located.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: No

 ** HealthCheckIntervalSeconds **   <a name="globalaccelerator-Type-EndpointGroup-HealthCheckIntervalSeconds"></a>
The time—10 seconds or 30 seconds—between health checks for each endpoint. The default value is 30.  
Type: Integer  
Valid Range: Minimum value of 10. Maximum value of 30.  
Required: No

 ** HealthCheckPath **   <a name="globalaccelerator-Type-EndpointGroup-HealthCheckPath"></a>
If the protocol is HTTP/S, then this value provides the ping path that Global Accelerator uses for the destination on the endpoints for health checks. The default is slash (/).  
Type: String  
Length Constraints: Maximum length of 255.  
Pattern: `^/[-a-zA-Z0-9@:%_\\+.~#?&/=]*$`   
Required: No

 ** HealthCheckPort **   <a name="globalaccelerator-Type-EndpointGroup-HealthCheckPort"></a>
The port that Global Accelerator uses to perform health checks on endpoints that are part of this endpoint group.   
The default port is the port for the listener that this endpoint group is associated with. If the listener port is a list, Global Accelerator uses the first specified port in the list of ports.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 65535.  
Required: No

 ** HealthCheckProtocol **   <a name="globalaccelerator-Type-EndpointGroup-HealthCheckProtocol"></a>
The protocol that Global Accelerator uses to perform health checks on endpoints that are part of this endpoint group. The default value is TCP.  
Type: String  
Valid Values: `TCP | HTTP | HTTPS`   
Required: No

 ** PortOverrides **   <a name="globalaccelerator-Type-EndpointGroup-PortOverrides"></a>
Allows you to override the destination ports used to route traffic to an endpoint. Using a port override lets you map a list of external destination ports (that your users send traffic to) to a list of internal destination ports that you want an application endpoint to receive traffic on.   
Type: Array of [PortOverride](API_PortOverride.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 10 items.  
Required: No

 ** ThresholdCount **   <a name="globalaccelerator-Type-EndpointGroup-ThresholdCount"></a>
The number of consecutive health checks required to set the state of a healthy endpoint to unhealthy, or to set an unhealthy endpoint to healthy. The default value is 3.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 10.  
Required: No

 ** TrafficDialPercentage **   <a name="globalaccelerator-Type-EndpointGroup-TrafficDialPercentage"></a>
The percentage of traffic to send to an AWS Region. Additional traffic is distributed to other endpoint groups for this listener.   
Use this action to increase (dial up) or decrease (dial down) traffic to a specific Region. The percentage is applied to the traffic that would otherwise have been routed to the Region based on optimal routing.  
The default value is 100.  
Type: Float  
Valid Range: Minimum value of 0. Maximum value of 100.  
Required: No

## See Also
<a name="API_EndpointGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/EndpointGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/EndpointGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/EndpointGroup) 