---
id: "@specs/aws/globalaccelerator/docs/API_EndpointConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EndpointConfiguration"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# EndpointConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_EndpointConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EndpointConfiguration
<a name="API_EndpointConfiguration"></a>

A complex type for endpoints. A resource must be valid and active when you add it as an endpoint.

## Contents
<a name="API_EndpointConfiguration_Contents"></a>

 ** AttachmentArn **   <a name="globalaccelerator-Type-EndpointConfiguration-AttachmentArn"></a>
The Amazon Resource Name (ARN) of the cross-account attachment that specifies the endpoints (resources) that can be added to accelerators and principals that have permission to add the endpoints.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: No

 ** ClientIPPreservationEnabled **   <a name="globalaccelerator-Type-EndpointConfiguration-ClientIPPreservationEnabled"></a>
Indicates whether client IP address preservation is enabled for an endpoint. The value is true or false. The default value is true for Application Load Balancer endpoints.   
If the value is set to true, the client's IP address is preserved in the `X-Forwarded-For` request header as traffic travels to applications on the endpoint fronted by the accelerator.  
Client IP address preservation is supported, in specific AWS Regions, for endpoints that are Application Load Balancers, Amazon EC2 instances, and Network Load Balancers with security groups. IMPORTANT: You cannot use client IP address preservation with Network Load Balancers with TLS listeners.  
For more information, see [ Preserve client IP addresses in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/preserve-client-ip-address.html) in the * AWS Global Accelerator Developer Guide*.  
Type: Boolean  
Required: No

 ** EndpointId **   <a name="globalaccelerator-Type-EndpointConfiguration-EndpointId"></a>
An ID for the endpoint. If the endpoint is a Network Load Balancer or Application Load Balancer, this is the Amazon Resource Name (ARN) of the resource. If the endpoint is an Elastic IP address, this is the Elastic IP address allocation ID. For Amazon EC2 instances, this is the EC2 instance ID. A resource must be valid and active when you add it as an endpoint.  
For cross-account endpoints, this must be the ARN of the resource.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: No

 ** Weight **   <a name="globalaccelerator-Type-EndpointConfiguration-Weight"></a>
The weight associated with the endpoint. When you add weights to endpoints, you configure AWS Global Accelerator to route traffic based on proportions that you specify. For example, you might specify endpoint weights of 4, 5, 5, and 6 (sum=20). The result is that 4/20 of your traffic, on average, is routed to the first endpoint, 5/20 is routed both to the second and third endpoints, and 6/20 is routed to the last endpoint. For more information, see [Endpoint weights](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoints-endpoint-weights.html) in the * AWS Global Accelerator Developer Guide*.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 255.  
Required: No

## See Also
<a name="API_EndpointConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/EndpointConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/EndpointConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/EndpointConfiguration) 