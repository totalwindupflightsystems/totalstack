---
id: "@specs/aws/globalaccelerator/docs/API_DescribeCustomRoutingEndpointGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeCustomRoutingEndpointGroup"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# DescribeCustomRoutingEndpointGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_DescribeCustomRoutingEndpointGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeCustomRoutingEndpointGroup
<a name="API_DescribeCustomRoutingEndpointGroup"></a>

Describe an endpoint group for a custom routing accelerator. 

## Request Syntax
<a name="API_DescribeCustomRoutingEndpointGroup_RequestSyntax"></a>

```
{
   "EndpointGroupArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeCustomRoutingEndpointGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EndpointGroupArn](#API_DescribeCustomRoutingEndpointGroup_RequestSyntax) **   <a name="globalaccelerator-DescribeCustomRoutingEndpointGroup-request-EndpointGroupArn"></a>
The Amazon Resource Name (ARN) of the endpoint group to describe.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

## Response Syntax
<a name="API_DescribeCustomRoutingEndpointGroup_ResponseSyntax"></a>

```
{
   "EndpointGroup": { 
      "DestinationDescriptions": [ 
         { 
            "FromPort": number,
            "Protocols": [ "string" ],
            "ToPort": number
         }
      ],
      "EndpointDescriptions": [ 
         { 
            "EndpointId": "string"
         }
      ],
      "EndpointGroupArn": "string",
      "EndpointGroupRegion": "string"
   }
}
```

## Response Elements
<a name="API_DescribeCustomRoutingEndpointGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EndpointGroup](#API_DescribeCustomRoutingEndpointGroup_ResponseSyntax) **   <a name="globalaccelerator-DescribeCustomRoutingEndpointGroup-response-EndpointGroup"></a>
The description of an endpoint group for a custom routing accelerator.  
Type: [CustomRoutingEndpointGroup](API_CustomRoutingEndpointGroup.md) object

## Errors
<a name="API_DescribeCustomRoutingEndpointGroup_Errors"></a>

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
<a name="API_DescribeCustomRoutingEndpointGroup_Examples"></a>

### Describe an endpoint group for a custom routing accelerator
<a name="API_DescribeCustomRoutingEndpointGroup_Example_1"></a>

The following is an example for describing an endpoint group for a custom routing accelerator, and the response.

```
aws globalaccelerator describe-custom-routing-endpoint-group
    --endpoint-group-arn arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/6789vxyz-vxyz-6789-vxyz-6789lmnopqrs/endpoint-group/ab88888example
```

```
{
    "EndpointGroup": {
        "EndpointGroupArn": "arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/6789vxyz-vxyz-6789-vxyz-6789lmnopqrs/endpoint-group/4321abcd-abcd-4321-abcd-4321abcdefg", 
        "EndpointGroupRegion": "us-west-2",
        DestinationDescriptions": [
            {
                "FromPort": 80,
                "ToPort": 80,
                "Protocols": [
                    "UDP"
                ]
            }
        ],
        "EndpointDescriptions": [
            {
                "EndpointId": "subnet-1234567890abcdef0"
            }
        ]
    }
}
```

## See Also
<a name="API_DescribeCustomRoutingEndpointGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/globalaccelerator-2018-08-08/DescribeCustomRoutingEndpointGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/globalaccelerator-2018-08-08/DescribeCustomRoutingEndpointGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/DescribeCustomRoutingEndpointGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/globalaccelerator-2018-08-08/DescribeCustomRoutingEndpointGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/DescribeCustomRoutingEndpointGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/globalaccelerator-2018-08-08/DescribeCustomRoutingEndpointGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/globalaccelerator-2018-08-08/DescribeCustomRoutingEndpointGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/globalaccelerator-2018-08-08/DescribeCustomRoutingEndpointGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/globalaccelerator-2018-08-08/DescribeCustomRoutingEndpointGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/DescribeCustomRoutingEndpointGroup) 