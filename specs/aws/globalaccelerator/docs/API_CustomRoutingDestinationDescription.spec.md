---
id: "@specs/aws/globalaccelerator/docs/API_CustomRoutingDestinationDescription"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CustomRoutingDestinationDescription"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# CustomRoutingDestinationDescription

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_CustomRoutingDestinationDescription
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CustomRoutingDestinationDescription
<a name="API_CustomRoutingDestinationDescription"></a>

For a custom routing accelerator, describes the port range and protocol for all endpoints (virtual private cloud subnets) in an endpoint group to accept client traffic on.

## Contents
<a name="API_CustomRoutingDestinationDescription_Contents"></a>

 ** FromPort **   <a name="globalaccelerator-Type-CustomRoutingDestinationDescription-FromPort"></a>
The first port, inclusive, in the range of ports for the endpoint group that is associated with a custom routing accelerator.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 65535.  
Required: No

 ** Protocols **   <a name="globalaccelerator-Type-CustomRoutingDestinationDescription-Protocols"></a>
The protocol for the endpoint group that is associated with a custom routing accelerator. The protocol can be either TCP or UDP.  
Type: Array of strings  
Valid Values: `TCP | UDP`   
Required: No

 ** ToPort **   <a name="globalaccelerator-Type-CustomRoutingDestinationDescription-ToPort"></a>
The last port, inclusive, in the range of ports for the endpoint group that is associated with a custom routing accelerator.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 65535.  
Required: No

## See Also
<a name="API_CustomRoutingDestinationDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/CustomRoutingDestinationDescription) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/CustomRoutingDestinationDescription) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/CustomRoutingDestinationDescription) 