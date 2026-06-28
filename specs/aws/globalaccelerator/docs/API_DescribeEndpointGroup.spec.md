---
id: "@specs/aws/globalaccelerator/docs/API_DescribeEndpointGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeEndpointGroup"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# DescribeEndpointGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_DescribeEndpointGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeEndpointGroup
<a name="API_DescribeEndpointGroup"></a>

Describe an endpoint group. 

## Request Syntax
<a name="API_DescribeEndpointGroup_RequestSyntax"></a>

```
{
   "EndpointGroupArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeEndpointGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EndpointGroupArn](#API_DescribeEndpointGroup_RequestSyntax) **   <a name="globalaccelerator-DescribeEndpointGroup-request-EndpointGroupArn"></a>
The Amazon Resource Name (ARN) of the endpoint group to describe.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

## Response Syntax
<a name="API_DescribeEndpointGroup_ResponseSyntax"></a>

```
{
   "EndpointGroup": { 
      "EndpointDescriptions": [ 
         { 
            "ClientIPPreservationEnabled": boolean,
            "EndpointId": "string",
            "HealthReason": "string",
            "HealthState": "string",
            "Weight": number
         }
      ],
      "EndpointGroupArn": "string",
      "EndpointGroupRegion": "string",
      "HealthCheckIntervalSeconds": number,
      "HealthCheckPath": "string",
      "HealthCheckPort": number,
      "HealthCheckProtocol": "string",
      "PortOverrides": [ 
         { 
            "EndpointPort": number,
            "ListenerPort": number
         }
      ],
      "ThresholdCount": number,
      "TrafficDialPercentage": number
   }
}
```

## Response Elements
<a name="API_DescribeEndpointGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EndpointGroup](#API_DescribeEndpointGroup_ResponseSyntax) **   <a name="globalaccelerator-DescribeEndpointGroup-response-EndpointGroup"></a>
The description of an endpoint group.  
Type: [EndpointGroup](API_EndpointGroup.md) object

## Errors
<a name="API_DescribeEndpointGroup_Errors"></a>

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
<a name="API_DescribeEndpointGroup_Examples"></a>

### Describe an endpoint group
<a name="API_DescribeEndpointGroup_Example_1"></a>

The following is an example for describing an endpoint group, and the response.

```
aws globalaccelerator describe-endpoint-group
    --endpoint-group-arn arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/6789vxyz-vxyz-6789-vxyz-6789lmnopqrs/endpoint-group/ab88888example
```

```
{
    "EndpointGroup": {
        "TrafficDialPercentage": 100.0, 
        "EndpointDescriptions": [
           {
              "Weight": 128, 
              "EndpointId": "i-1234567890abcdef0"
           },
           {
              "Weight": 128, 
              "EndpointId": "arn:aws:elasticloadbalancing:us-east-1:000123456789:loadbalancer/app/ALBTesting/alb01234567890xyz"
           },
           {
              "Weight": 128, 
              "EndpointId": "arn:aws:elasticloadbalancing:us-east-1:000123456789:loadbalancer/net/NLBTesting/alb01234567890qrs"
           }
        ], 
        "EndpointGroupArn": "arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/6789vxyz-vxyz-6789-vxyz-6789lmnopqrs/endpoint-group/4321abcd-abcd-4321-abcd-4321abcdefg", 
        "EndpointGroupRegion": "us-east-1"
    }
}
```

## See Also
<a name="API_DescribeEndpointGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/globalaccelerator-2018-08-08/DescribeEndpointGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/globalaccelerator-2018-08-08/DescribeEndpointGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/DescribeEndpointGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/globalaccelerator-2018-08-08/DescribeEndpointGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/DescribeEndpointGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/globalaccelerator-2018-08-08/DescribeEndpointGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/globalaccelerator-2018-08-08/DescribeEndpointGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/globalaccelerator-2018-08-08/DescribeEndpointGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/globalaccelerator-2018-08-08/DescribeEndpointGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/DescribeEndpointGroup) 