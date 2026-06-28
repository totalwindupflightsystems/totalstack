---
id: "@specs/aws/globalaccelerator/docs/API_CreateEndpointGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateEndpointGroup"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# CreateEndpointGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_CreateEndpointGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateEndpointGroup
<a name="API_CreateEndpointGroup"></a>

Create an endpoint group for the specified listener. An endpoint group is a collection of endpoints in one AWS Region. A resource must be valid and active when you add it as an endpoint.

For more information about endpoint types and requirements for endpoints that you can add to Global Accelerator, see [ Endpoints for standard accelerators](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoints.html) in the * AWS Global Accelerator Developer Guide*.

## Request Syntax
<a name="API_CreateEndpointGroup_RequestSyntax"></a>

```
{
   "EndpointConfigurations": [ 
      { 
         "AttachmentArn": "{{string}}",
         "ClientIPPreservationEnabled": {{boolean}},
         "EndpointId": "{{string}}",
         "Weight": {{number}}
      }
   ],
   "EndpointGroupRegion": "{{string}}",
   "HealthCheckIntervalSeconds": {{number}},
   "HealthCheckPath": "{{string}}",
   "HealthCheckPort": {{number}},
   "HealthCheckProtocol": "{{string}}",
   "IdempotencyToken": "{{string}}",
   "ListenerArn": "{{string}}",
   "PortOverrides": [ 
      { 
         "EndpointPort": {{number}},
         "ListenerPort": {{number}}
      }
   ],
   "ThresholdCount": {{number}},
   "TrafficDialPercentage": {{number}}
}
```

## Request Parameters
<a name="API_CreateEndpointGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EndpointConfigurations](#API_CreateEndpointGroup_RequestSyntax) **   <a name="globalaccelerator-CreateEndpointGroup-request-EndpointConfigurations"></a>
The list of endpoint objects.  
Type: Array of [EndpointConfiguration](API_EndpointConfiguration.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 10 items.  
Required: No

 ** [EndpointGroupRegion](#API_CreateEndpointGroup_RequestSyntax) **   <a name="globalaccelerator-CreateEndpointGroup-request-EndpointGroupRegion"></a>
The AWS Region where the endpoint group is located. A listener can have only one endpoint group in a specific Region.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

 ** [HealthCheckIntervalSeconds](#API_CreateEndpointGroup_RequestSyntax) **   <a name="globalaccelerator-CreateEndpointGroup-request-HealthCheckIntervalSeconds"></a>
The time—10 seconds or 30 seconds—between each health check for an endpoint. The default value is 30.  
Type: Integer  
Valid Range: Minimum value of 10. Maximum value of 30.  
Required: No

 ** [HealthCheckPath](#API_CreateEndpointGroup_RequestSyntax) **   <a name="globalaccelerator-CreateEndpointGroup-request-HealthCheckPath"></a>
If the protocol is HTTP/S, then this specifies the path that is the destination for health check targets. The default value is slash (/).  
Type: String  
Length Constraints: Maximum length of 255.  
Pattern: `^/[-a-zA-Z0-9@:%_\\+.~#?&/=]*$`   
Required: No

 ** [HealthCheckPort](#API_CreateEndpointGroup_RequestSyntax) **   <a name="globalaccelerator-CreateEndpointGroup-request-HealthCheckPort"></a>
The port that AWS Global Accelerator uses to check the health of endpoints that are part of this endpoint group. The default port is the listener port that this endpoint group is associated with. If listener port is a list of ports, Global Accelerator uses the first port in the list.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 65535.  
Required: No

 ** [HealthCheckProtocol](#API_CreateEndpointGroup_RequestSyntax) **   <a name="globalaccelerator-CreateEndpointGroup-request-HealthCheckProtocol"></a>
The protocol that AWS Global Accelerator uses to check the health of endpoints that are part of this endpoint group. The default value is TCP.  
Type: String  
Valid Values: `TCP | HTTP | HTTPS`   
Required: No

 ** [IdempotencyToken](#API_CreateEndpointGroup_RequestSyntax) **   <a name="globalaccelerator-CreateEndpointGroup-request-IdempotencyToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency—that is, the uniqueness—of the request.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

 ** [ListenerArn](#API_CreateEndpointGroup_RequestSyntax) **   <a name="globalaccelerator-CreateEndpointGroup-request-ListenerArn"></a>
The Amazon Resource Name (ARN) of the listener.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

 ** [PortOverrides](#API_CreateEndpointGroup_RequestSyntax) **   <a name="globalaccelerator-CreateEndpointGroup-request-PortOverrides"></a>
Override specific listener ports used to route traffic to endpoints that are part of this endpoint group. For example, you can create a port override in which the listener receives user traffic on ports 80 and 443, but your accelerator routes that traffic to ports 1080 and 1443, respectively, on the endpoints.  
For more information, see [ Overriding listener ports](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoint-groups-port-override.html) in the * AWS Global Accelerator Developer Guide*.  
Type: Array of [PortOverride](API_PortOverride.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 10 items.  
Required: No

 ** [ThresholdCount](#API_CreateEndpointGroup_RequestSyntax) **   <a name="globalaccelerator-CreateEndpointGroup-request-ThresholdCount"></a>
The number of consecutive health checks required to set the state of a healthy endpoint to unhealthy, or to set an unhealthy endpoint to healthy. The default value is 3.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 10.  
Required: No

 ** [TrafficDialPercentage](#API_CreateEndpointGroup_RequestSyntax) **   <a name="globalaccelerator-CreateEndpointGroup-request-TrafficDialPercentage"></a>
The percentage of traffic to send to an AWS Region. Additional traffic is distributed to other endpoint groups for this listener.   
Use this action to increase (dial up) or decrease (dial down) traffic to a specific Region. The percentage is applied to the traffic that would otherwise have been routed to the Region based on optimal routing.  
The default value is 100.  
Type: Float  
Valid Range: Minimum value of 0. Maximum value of 100.  
Required: No

## Response Syntax
<a name="API_CreateEndpointGroup_ResponseSyntax"></a>

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
<a name="API_CreateEndpointGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EndpointGroup](#API_CreateEndpointGroup_ResponseSyntax) **   <a name="globalaccelerator-CreateEndpointGroup-response-EndpointGroup"></a>
The information about the endpoint group that was created.  
Type: [EndpointGroup](API_EndpointGroup.md) object

## Errors
<a name="API_CreateEndpointGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AcceleratorNotFoundException **   
The accelerator that you specified doesn't exist.  
HTTP Status Code: 400

 ** AccessDeniedException **   
You don't have access permission.  
HTTP Status Code: 400

 ** EndpointGroupAlreadyExistsException **   
The endpoint group that you specified already exists.  
HTTP Status Code: 400

 ** InternalServiceErrorException **   
There was an internal error for AWS Global Accelerator.  
HTTP Status Code: 400

 ** InvalidArgumentException **   
An argument that you specified is invalid.  
HTTP Status Code: 400

 ** LimitExceededException **   
Processing your request would cause you to exceed an AWS Global Accelerator limit.  
HTTP Status Code: 400

 ** ListenerNotFoundException **   
The listener that you specified doesn't exist.  
HTTP Status Code: 400

## Examples
<a name="API_CreateEndpointGroup_Examples"></a>

### Create an endpoint group
<a name="API_CreateEndpointGroup_Example_1"></a>

The following is an example of creating an endpoint group, and the response.

```
aws globalaccelerator create-endpoint-group 
           --listener-arn arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/0123vxyz 
           --endpoint-group-region us-east-1
           --port-overrides ListenerPort=443,EndpointPort=1443
           --endpoint-configurations EndpointId=i-1234567890abcdef0,Weight=128
           --region us-west-2
```

```
{
    "EndpointGroup": {
        "TrafficDialPercentage": 100.0, 
        "EndpointDescriptions": [
            {
                "Weight": 128, 
                "EndpointId": "i-1234567890abcdef0"
            }
        ],
        "PortOverrides": [
            {
                "EndpointPort": 1443,
                "ListenerPort": 443
            }
        ],
        "EndpointGroupArn": "arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/0123vxyz/endpoint-group/098765zyxwvu", 
        "EndpointGroupRegion": "us-east-1"
    }
}
```

## See Also
<a name="API_CreateEndpointGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/globalaccelerator-2018-08-08/CreateEndpointGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/globalaccelerator-2018-08-08/CreateEndpointGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/CreateEndpointGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/globalaccelerator-2018-08-08/CreateEndpointGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/CreateEndpointGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/globalaccelerator-2018-08-08/CreateEndpointGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/globalaccelerator-2018-08-08/CreateEndpointGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/globalaccelerator-2018-08-08/CreateEndpointGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/globalaccelerator-2018-08-08/CreateEndpointGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/CreateEndpointGroup) 