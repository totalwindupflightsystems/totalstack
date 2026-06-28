---
id: "@specs/aws/globalaccelerator/docs/API_CustomRoutingDestinationConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CustomRoutingDestinationConfiguration"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# CustomRoutingDestinationConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_CustomRoutingDestinationConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CustomRoutingDestinationConfiguration
<a name="API_CustomRoutingDestinationConfiguration"></a>

For a custom routing accelerator, sets the port range and protocol for all endpoints (virtual private cloud subnets) in an endpoint group to accept client traffic on.

## Contents
<a name="API_CustomRoutingDestinationConfiguration_Contents"></a>

 ** FromPort **   <a name="globalaccelerator-Type-CustomRoutingDestinationConfiguration-FromPort"></a>
The first port, inclusive, in the range of ports for the endpoint group that is associated with a custom routing accelerator.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 65535.  
Required: Yes

 ** Protocols **   <a name="globalaccelerator-Type-CustomRoutingDestinationConfiguration-Protocols"></a>
The protocol for the endpoint group that is associated with a custom routing accelerator. The protocol can be either TCP or UDP.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 2 items.  
Valid Values: `TCP | UDP`   
Required: Yes

 ** ToPort **   <a name="globalaccelerator-Type-CustomRoutingDestinationConfiguration-ToPort"></a>
The last port, inclusive, in the range of ports for the endpoint group that is associated with a custom routing accelerator.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 65535.  
Required: Yes

## See Also
<a name="API_CustomRoutingDestinationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/CustomRoutingDestinationConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/CustomRoutingDestinationConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/CustomRoutingDestinationConfiguration) 