---
id: "@specs/aws/globalaccelerator/docs/API_PortOverride"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PortOverride"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# PortOverride

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_PortOverride
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PortOverride
<a name="API_PortOverride"></a>

Override specific listener ports used to route traffic to endpoints that are part of an endpoint group. For example, you can create a port override in which the listener receives user traffic on ports 80 and 443, but your accelerator routes that traffic to ports 1080 and 1443, respectively, on the endpoints.

For more information, see [ Overriding listener ports](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoint-groups-port-override.html) in the * AWS Global Accelerator Developer Guide*.

## Contents
<a name="API_PortOverride_Contents"></a>

 ** EndpointPort **   <a name="globalaccelerator-Type-PortOverride-EndpointPort"></a>
The endpoint port that you want a listener port to be mapped to. This is the port on the endpoint, such as the Application Load Balancer or Amazon EC2 instance.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 65535.  
Required: No

 ** ListenerPort **   <a name="globalaccelerator-Type-PortOverride-ListenerPort"></a>
The listener port that you want to map to a specific endpoint port. This is the port that user traffic arrives to the Global Accelerator on.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 65535.  
Required: No

## See Also
<a name="API_PortOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/PortOverride) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/PortOverride) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/PortOverride) 