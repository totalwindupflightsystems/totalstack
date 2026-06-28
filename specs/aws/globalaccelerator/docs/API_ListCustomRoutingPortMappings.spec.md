---
id: "@specs/aws/globalaccelerator/docs/API_ListCustomRoutingPortMappings"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListCustomRoutingPortMappings"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# ListCustomRoutingPortMappings

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_ListCustomRoutingPortMappings
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListCustomRoutingPortMappings
<a name="API_ListCustomRoutingPortMappings"></a>

Provides a complete mapping from the public accelerator IP address and port to destination EC2 instance IP addresses and ports in the virtual public cloud (VPC) subnet endpoint for a custom routing accelerator. For each subnet endpoint that you add, Global Accelerator creates a new static port mapping for the accelerator. The port mappings don't change after Global Accelerator generates them, so you can retrieve and cache the full mapping on your servers. 

If you remove a subnet from your accelerator, Global Accelerator removes (reclaims) the port mappings. If you add a subnet to your accelerator, Global Accelerator creates new port mappings (the existing ones don't change). If you add or remove EC2 instances in your subnet, the port mappings don't change, because the mappings are created when you add the subnet to Global Accelerator.

The mappings also include a flag for each destination denoting which destination IP addresses and ports are allowed or denied traffic.

## Request Syntax
<a name="API_ListCustomRoutingPortMappings_RequestSyntax"></a>

```
{
   "AcceleratorArn": "{{string}}",
   "EndpointGroupArn": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListCustomRoutingPortMappings_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AcceleratorArn](#API_ListCustomRoutingPortMappings_RequestSyntax) **   <a name="globalaccelerator-ListCustomRoutingPortMappings-request-AcceleratorArn"></a>
The Amazon Resource Name (ARN) of the accelerator to list the custom routing port mappings for.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

 ** [EndpointGroupArn](#API_ListCustomRoutingPortMappings_RequestSyntax) **   <a name="globalaccelerator-ListCustomRoutingPortMappings-request-EndpointGroupArn"></a>
The Amazon Resource Name (ARN) of the endpoint group to list the custom routing port mappings for.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: No

 ** [MaxResults](#API_ListCustomRoutingPortMappings_RequestSyntax) **   <a name="globalaccelerator-ListCustomRoutingPortMappings-request-MaxResults"></a>
The number of destination port mappings that you want to return with this call. The default value is 10.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 20000.  
Required: No

 ** [NextToken](#API_ListCustomRoutingPortMappings_RequestSyntax) **   <a name="globalaccelerator-ListCustomRoutingPortMappings-request-NextToken"></a>
The token for the next set of results. You receive this token from a previous call.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: No

## Response Syntax
<a name="API_ListCustomRoutingPortMappings_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "PortMappings": [ 
      { 
         "AcceleratorPort": number,
         "DestinationSocketAddress": { 
            "IpAddress": "string",
            "Port": number
         },
         "DestinationTrafficState": "string",
         "EndpointGroupArn": "string",
         "EndpointId": "string",
         "Protocols": [ "string" ]
      }
   ]
}
```

## Response Elements
<a name="API_ListCustomRoutingPortMappings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListCustomRoutingPortMappings_ResponseSyntax) **   <a name="globalaccelerator-ListCustomRoutingPortMappings-response-NextToken"></a>
The token for the next set of results. You receive this token from a previous call.  
Type: String  
Length Constraints: Maximum length of 255.

 ** [PortMappings](#API_ListCustomRoutingPortMappings_ResponseSyntax) **   <a name="globalaccelerator-ListCustomRoutingPortMappings-response-PortMappings"></a>
The port mappings for a custom routing accelerator.  
Type: Array of [PortMapping](API_PortMapping.md) objects

## Errors
<a name="API_ListCustomRoutingPortMappings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AcceleratorNotFoundException **   
The accelerator that you specified doesn't exist.  
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

 ** InvalidNextTokenException **   
There isn't another item to return.  
HTTP Status Code: 400

## See Also
<a name="API_ListCustomRoutingPortMappings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/globalaccelerator-2018-08-08/ListCustomRoutingPortMappings) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/globalaccelerator-2018-08-08/ListCustomRoutingPortMappings) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/ListCustomRoutingPortMappings) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/globalaccelerator-2018-08-08/ListCustomRoutingPortMappings) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/ListCustomRoutingPortMappings) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/globalaccelerator-2018-08-08/ListCustomRoutingPortMappings) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/globalaccelerator-2018-08-08/ListCustomRoutingPortMappings) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/globalaccelerator-2018-08-08/ListCustomRoutingPortMappings) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/globalaccelerator-2018-08-08/ListCustomRoutingPortMappings) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/ListCustomRoutingPortMappings) 