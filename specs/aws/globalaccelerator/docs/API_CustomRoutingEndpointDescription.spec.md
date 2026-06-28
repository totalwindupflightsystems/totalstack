---
id: "@specs/aws/globalaccelerator/docs/API_CustomRoutingEndpointDescription"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CustomRoutingEndpointDescription"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# CustomRoutingEndpointDescription

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_CustomRoutingEndpointDescription
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CustomRoutingEndpointDescription
<a name="API_CustomRoutingEndpointDescription"></a>

A complex type for an endpoint for a custom routing accelerator. Each endpoint group can include one or more endpoints, which are virtual private cloud (VPC) subnets.

## Contents
<a name="API_CustomRoutingEndpointDescription_Contents"></a>

 ** EndpointId **   <a name="globalaccelerator-Type-CustomRoutingEndpointDescription-EndpointId"></a>
An ID for the endpoint. For custom routing accelerators, this is the virtual private cloud (VPC) subnet ID.   
Type: String  
Length Constraints: Maximum length of 255.  
Required: No

## See Also
<a name="API_CustomRoutingEndpointDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/CustomRoutingEndpointDescription) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/CustomRoutingEndpointDescription) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/CustomRoutingEndpointDescription) 