---
id: "@specs/aws/globalaccelerator/docs/API_ListCustomRoutingPortMappingsByDestination"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListCustomRoutingPortMappingsByDestination"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# ListCustomRoutingPortMappingsByDestination

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_ListCustomRoutingPortMappingsByDestination
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListCustomRoutingPortMappingsByDestination
<a name="API_ListCustomRoutingPortMappingsByDestination"></a>

List the port mappings for a specific EC2 instance (destination) in a VPC subnet endpoint. The response is the mappings for one destination IP address. This is useful when your subnet endpoint has mappings that span multiple custom routing accelerators in your account, or for scenarios where you only want to list the port mappings for a specific destination instance.

## Request Syntax
<a name="API_ListCustomRoutingPortMappingsByDestination_RequestSyntax"></a>

```
{
   "DestinationAddress": "{{string}}",
   "EndpointId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListCustomRoutingPortMappingsByDestination_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DestinationAddress](#API_ListCustomRoutingPortMappingsByDestination_RequestSyntax) **   <a name="globalaccelerator-ListCustomRoutingPortMappingsByDestination-request-DestinationAddress"></a>
The endpoint IP address in a virtual private cloud (VPC) subnet for which you want to receive back port mappings.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

 ** [EndpointId](#API_ListCustomRoutingPortMappingsByDestination_RequestSyntax) **   <a name="globalaccelerator-ListCustomRoutingPortMappingsByDestination-request-EndpointId"></a>
The ID for the virtual private cloud (VPC) subnet.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

 ** [MaxResults](#API_ListCustomRoutingPortMappingsByDestination_RequestSyntax) **   <a name="globalaccelerator-ListCustomRoutingPortMappingsByDestination-request-MaxResults"></a>
The number of destination port mappings that you want to return with this call. The default value is 10.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 20000.  
Required: No

 ** [NextToken](#API_ListCustomRoutingPortMappingsByDestination_RequestSyntax) **   <a name="globalaccelerator-ListCustomRoutingPortMappingsByDestination-request-NextToken"></a>
The token for the next set of results. You receive this token from a previous call.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: No

## Response Syntax
<a name="API_ListCustomRoutingPortMappingsByDestination_ResponseSyntax"></a>

```
{
   "DestinationPortMappings": [ 
      { 
         "AcceleratorArn": "string",
         "AcceleratorSocketAddresses": [ 
            { 
               "IpAddress": "string",
               "Port": number
            }
         ],
         "DestinationSocketAddress": { 
            "IpAddress": "string",
            "Port": number
         },
         "DestinationTrafficState": "string",
         "EndpointGroupArn": "string",
         "EndpointGroupRegion": "string",
         "EndpointId": "string",
         "IpAddressType": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListCustomRoutingPortMappingsByDestination_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DestinationPortMappings](#API_ListCustomRoutingPortMappingsByDestination_ResponseSyntax) **   <a name="globalaccelerator-ListCustomRoutingPortMappingsByDestination-response-DestinationPortMappings"></a>
The port mappings for the endpoint IP address that you specified in the request.  
Type: Array of [DestinationPortMapping](API_DestinationPortMapping.md) objects

 ** [NextToken](#API_ListCustomRoutingPortMappingsByDestination_ResponseSyntax) **   <a name="globalaccelerator-ListCustomRoutingPortMappingsByDestination-response-NextToken"></a>
The token for the next set of results. You receive this token from a previous call.  
Type: String  
Length Constraints: Maximum length of 255.

## Errors
<a name="API_ListCustomRoutingPortMappingsByDestination_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EndpointNotFoundException **   
The endpoint that you specified doesn't exist.  
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

## Examples
<a name="API_ListCustomRoutingPortMappingsByDestination_Examples"></a>

### List the port mappings for an EC2 instance destination
<a name="API_ListCustomRoutingPortMappingsByDestination_Example_1"></a>

The following is an example of listing the port mappings for an EC2 instance destination for a custom routing accelerator.

```
aws --region us-west-2 globalaccelerator list-custom-routing-port-mappings-by-destination 
					--endpoint-id subnet-abcd123example --destination-address "198.51.100.52"
```

```
{
    "DestinationPortMappings": [
        {
            "AcceleratorArn": "arn:aws:globalaccelerator::402092451327:accelerator/24ea29b8-d750-4489-8919-3095f3c4b0a7",
                "AcceleratorSocketAddresses": [
                    {
                        "IpAddress": "192.0.2.250",
                        "Port": 65514
                    },
                    {
                        "IpAddress": "198.51.100.52",
                        "Port": 65514
                    }
                ],
                "EndpointGroupArn": "arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/0123vxyz/endpoint-group/ab88888example",
                "EndpointId": "subnet-abcd123example",
                "EndpointGroupRegion": "us-west-2",
                "DestinationSocketAddress": {
                    "IpAddress": "198.51.100.52",
                    "Port": 80
                },
                "IpAddressType": "IPv4",
                "DestinationTrafficState": "DENY"
            }
        ]
    }
```

## See Also
<a name="API_ListCustomRoutingPortMappingsByDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/globalaccelerator-2018-08-08/ListCustomRoutingPortMappingsByDestination) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/globalaccelerator-2018-08-08/ListCustomRoutingPortMappingsByDestination) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/ListCustomRoutingPortMappingsByDestination) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/globalaccelerator-2018-08-08/ListCustomRoutingPortMappingsByDestination) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/ListCustomRoutingPortMappingsByDestination) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/globalaccelerator-2018-08-08/ListCustomRoutingPortMappingsByDestination) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/globalaccelerator-2018-08-08/ListCustomRoutingPortMappingsByDestination) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/globalaccelerator-2018-08-08/ListCustomRoutingPortMappingsByDestination) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/globalaccelerator-2018-08-08/ListCustomRoutingPortMappingsByDestination) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/ListCustomRoutingPortMappingsByDestination) 