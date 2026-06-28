---
id: "@specs/aws/globalaccelerator/docs/API_AddEndpoints"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AddEndpoints"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# AddEndpoints

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_AddEndpoints
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AddEndpoints
<a name="API_AddEndpoints"></a>

Add endpoints to an endpoint group. The `AddEndpoints` API operation is the recommended option for adding endpoints. The alternative options are to add endpoints when you create an endpoint group (with the [CreateEndpointGroup](https://docs.aws.amazon.com/global-accelerator/latest/api/API_CreateEndpointGroup.html) API) or when you update an endpoint group (with the [UpdateEndpointGroup](https://docs.aws.amazon.com/global-accelerator/latest/api/API_UpdateEndpointGroup.html) API). 

There are two advantages to using `AddEndpoints` to add endpoints in Global Accelerator:
+ It's faster, because Global Accelerator only has to resolve the new endpoints that you're adding, rather than resolving new and existing endpoints.
+ It's more convenient, because you don't need to specify the current endpoints that are already in the endpoint group, in addition to the new endpoints that you want to add.

For information about endpoint types and requirements for endpoints that you can add to Global Accelerator, see [ Endpoints for standard accelerators](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoints.html) in the * AWS Global Accelerator Developer Guide*.

## Request Syntax
<a name="API_AddEndpoints_RequestSyntax"></a>

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
   "EndpointGroupArn": "{{string}}"
}
```

## Request Parameters
<a name="API_AddEndpoints_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EndpointConfigurations](#API_AddEndpoints_RequestSyntax) **   <a name="globalaccelerator-AddEndpoints-request-EndpointConfigurations"></a>
The list of endpoint objects.  
Type: Array of [EndpointConfiguration](API_EndpointConfiguration.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 10 items.  
Required: Yes

 ** [EndpointGroupArn](#API_AddEndpoints_RequestSyntax) **   <a name="globalaccelerator-AddEndpoints-request-EndpointGroupArn"></a>
The Amazon Resource Name (ARN) of the endpoint group.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

## Response Syntax
<a name="API_AddEndpoints_ResponseSyntax"></a>

```
{
   "EndpointDescriptions": [ 
      { 
         "ClientIPPreservationEnabled": boolean,
         "EndpointId": "string",
         "HealthReason": "string",
         "HealthState": "string",
         "Weight": number
      }
   ],
   "EndpointGroupArn": "string"
}
```

## Response Elements
<a name="API_AddEndpoints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EndpointDescriptions](#API_AddEndpoints_ResponseSyntax) **   <a name="globalaccelerator-AddEndpoints-response-EndpointDescriptions"></a>
The list of endpoint objects.  
Type: Array of [EndpointDescription](API_EndpointDescription.md) objects

 ** [EndpointGroupArn](#API_AddEndpoints_ResponseSyntax) **   <a name="globalaccelerator-AddEndpoints-response-EndpointGroupArn"></a>
The Amazon Resource Name (ARN) of the endpoint group.  
Type: String  
Length Constraints: Maximum length of 255.

## Errors
<a name="API_AddEndpoints_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have access permission.  
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

 ** LimitExceededException **   
Processing your request would cause you to exceed an AWS Global Accelerator limit.  
HTTP Status Code: 400

 ** TransactionInProgressException **   
There's already a transaction in progress. Another transaction can't be processed.  
HTTP Status Code: 400

## See Also
<a name="API_AddEndpoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/globalaccelerator-2018-08-08/AddEndpoints) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/globalaccelerator-2018-08-08/AddEndpoints) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/AddEndpoints) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/globalaccelerator-2018-08-08/AddEndpoints) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/AddEndpoints) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/globalaccelerator-2018-08-08/AddEndpoints) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/globalaccelerator-2018-08-08/AddEndpoints) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/globalaccelerator-2018-08-08/AddEndpoints) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/globalaccelerator-2018-08-08/AddEndpoints) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/AddEndpoints) 