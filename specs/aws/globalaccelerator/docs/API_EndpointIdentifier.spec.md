---
id: "@specs/aws/globalaccelerator/docs/API_EndpointIdentifier"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EndpointIdentifier"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# EndpointIdentifier

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_EndpointIdentifier
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EndpointIdentifier
<a name="API_EndpointIdentifier"></a>

A complex type for an endpoint. Specifies information about the endpoint to remove from the endpoint group.

## Contents
<a name="API_EndpointIdentifier_Contents"></a>

 ** EndpointId **   <a name="globalaccelerator-Type-EndpointIdentifier-EndpointId"></a>
An ID for the endpoint. If the endpoint is a Network Load Balancer or Application Load Balancer, this is the Amazon Resource Name (ARN) of the resource. If the endpoint is an Elastic IP address, this is the Elastic IP address allocation ID. For Amazon EC2 instances, this is the EC2 instance ID.   
An Application Load Balancer can be either internal or internet-facing.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

 ** ClientIPPreservationEnabled **   <a name="globalaccelerator-Type-EndpointIdentifier-ClientIPPreservationEnabled"></a>
Indicates whether client IP address preservation is enabled for an endpoint. The value is true or false.   
If the value is set to true, the client's IP address is preserved in the `X-Forwarded-For` request header as traffic travels to applications on the endpoint fronted by the accelerator.  
Type: Boolean  
Required: No

## See Also
<a name="API_EndpointIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/EndpointIdentifier) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/EndpointIdentifier) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/EndpointIdentifier) 