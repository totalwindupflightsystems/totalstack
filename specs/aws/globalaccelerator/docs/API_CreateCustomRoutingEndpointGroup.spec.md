---
id: "@specs/aws/globalaccelerator/docs/API_CreateCustomRoutingEndpointGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateCustomRoutingEndpointGroup"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# CreateCustomRoutingEndpointGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_CreateCustomRoutingEndpointGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateCustomRoutingEndpointGroup
<a name="API_CreateCustomRoutingEndpointGroup"></a>

Create an endpoint group for the specified listener for a custom routing accelerator. An endpoint group is a collection of endpoints in one AWS Region. 

## Request Syntax
<a name="API_CreateCustomRoutingEndpointGroup_RequestSyntax"></a>

```
{
   "DestinationConfigurations": [ 
      { 
         "FromPort": {{number}},
         "Protocols": [ "{{string}}" ],
         "ToPort": {{number}}
      }
   ],
   "EndpointGroupRegion": "{{string}}",
   "IdempotencyToken": "{{string}}",
   "ListenerArn": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateCustomRoutingEndpointGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DestinationConfigurations](#API_CreateCustomRoutingEndpointGroup_RequestSyntax) **   <a name="globalaccelerator-CreateCustomRoutingEndpointGroup-request-DestinationConfigurations"></a>
Sets the port range and protocol for all endpoints (virtual private cloud subnets) in a custom routing endpoint group to accept client traffic on.  
Type: Array of [CustomRoutingDestinationConfiguration](API_CustomRoutingDestinationConfiguration.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 100 items.  
Required: Yes

 ** [EndpointGroupRegion](#API_CreateCustomRoutingEndpointGroup_RequestSyntax) **   <a name="globalaccelerator-CreateCustomRoutingEndpointGroup-request-EndpointGroupRegion"></a>
The AWS Region where the endpoint group is located. A listener can have only one endpoint group in a specific Region.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

 ** [IdempotencyToken](#API_CreateCustomRoutingEndpointGroup_RequestSyntax) **   <a name="globalaccelerator-CreateCustomRoutingEndpointGroup-request-IdempotencyToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency—that is, the uniqueness—of the request.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

 ** [ListenerArn](#API_CreateCustomRoutingEndpointGroup_RequestSyntax) **   <a name="globalaccelerator-CreateCustomRoutingEndpointGroup-request-ListenerArn"></a>
The Amazon Resource Name (ARN) of the listener for a custom routing endpoint.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

## Response Syntax
<a name="API_CreateCustomRoutingEndpointGroup_ResponseSyntax"></a>

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
<a name="API_CreateCustomRoutingEndpointGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EndpointGroup](#API_CreateCustomRoutingEndpointGroup_ResponseSyntax) **   <a name="globalaccelerator-CreateCustomRoutingEndpointGroup-response-EndpointGroup"></a>
The information about the endpoint group created for a custom routing accelerator.  
Type: [CustomRoutingEndpointGroup](API_CustomRoutingEndpointGroup.md) object

## Errors
<a name="API_CreateCustomRoutingEndpointGroup_Errors"></a>

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

 ** InvalidPortRangeException **   
The port numbers that you specified are not valid numbers or are not unique for this accelerator.  
HTTP Status Code: 400

 ** LimitExceededException **   
Processing your request would cause you to exceed an AWS Global Accelerator limit.  
HTTP Status Code: 400

 ** ListenerNotFoundException **   
The listener that you specified doesn't exist.  
HTTP Status Code: 400

## Examples
<a name="API_CreateCustomRoutingEndpointGroup_Examples"></a>

### Create an endpoint group for a custom routing accelerator
<a name="API_CreateCustomRoutingEndpointGroup_Example_1"></a>

The following is an example of creating an endpoint group for a custom routing accelerator, and the response.

```
aws globalaccelerator create-custom-routing-endpoint-group 
           --listener-arn arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/0123vxyz 
           --endpoint-group-region us-east-1 
           --endpoint-configurations EndpointId=i-1234567890abcdef0,Weight=128
           --region us-west-2
```

```
{
    "EndpointGroup": {
        "EndpointId": "i-1234567890abcdef0"
        "EndpointGroupArn": "arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/0123vxyz/endpoint-group/098765zyxwvu", 
        "EndpointGroupRegion": "us-east-1"
    }
}
```

## See Also
<a name="API_CreateCustomRoutingEndpointGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/globalaccelerator-2018-08-08/CreateCustomRoutingEndpointGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/globalaccelerator-2018-08-08/CreateCustomRoutingEndpointGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/CreateCustomRoutingEndpointGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/globalaccelerator-2018-08-08/CreateCustomRoutingEndpointGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/CreateCustomRoutingEndpointGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/globalaccelerator-2018-08-08/CreateCustomRoutingEndpointGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/globalaccelerator-2018-08-08/CreateCustomRoutingEndpointGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/globalaccelerator-2018-08-08/CreateCustomRoutingEndpointGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/globalaccelerator-2018-08-08/CreateCustomRoutingEndpointGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/CreateCustomRoutingEndpointGroup) 