---
id: "@specs/aws/globalaccelerator/docs/API_RemoveCustomRoutingEndpoints"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RemoveCustomRoutingEndpoints"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# RemoveCustomRoutingEndpoints

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_RemoveCustomRoutingEndpoints
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RemoveCustomRoutingEndpoints
<a name="API_RemoveCustomRoutingEndpoints"></a>

Remove endpoints from a custom routing accelerator.

## Request Syntax
<a name="API_RemoveCustomRoutingEndpoints_RequestSyntax"></a>

```
{
   "EndpointGroupArn": "{{string}}",
   "EndpointIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_RemoveCustomRoutingEndpoints_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EndpointGroupArn](#API_RemoveCustomRoutingEndpoints_RequestSyntax) **   <a name="globalaccelerator-RemoveCustomRoutingEndpoints-request-EndpointGroupArn"></a>
The Amazon Resource Name (ARN) of the endpoint group to remove endpoints from.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

 ** [EndpointIds](#API_RemoveCustomRoutingEndpoints_RequestSyntax) **   <a name="globalaccelerator-RemoveCustomRoutingEndpoints-request-EndpointIds"></a>
The IDs for the endpoints. For custom routing accelerators, endpoint IDs are the virtual private cloud (VPC) subnet IDs.   
Type: Array of strings  
Length Constraints: Maximum length of 255.  
Required: Yes

## Response Elements
<a name="API_RemoveCustomRoutingEndpoints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_RemoveCustomRoutingEndpoints_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have access permission.  
HTTP Status Code: 400

 ** ConflictException **   
You can't use both of those options.  
HTTP Status Code: 400

 ** EndpointGroupNotFoundException **   
The endpoint group that you specified doesn't exist.  
HTTP Status Code: 400

 ** EndpointNotFoundException **   
The endpoint that you specified doesn't exist.  
HTTP Status Code: 400

 ** InternalServiceErrorException **   
There was an internal error for AWS Global Accelerator.  
HTTP Status Code: 400

 ** InvalidArgumentException **   
An argument that you specified is invalid.  
HTTP Status Code: 400

## See Also
<a name="API_RemoveCustomRoutingEndpoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/globalaccelerator-2018-08-08/RemoveCustomRoutingEndpoints) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/globalaccelerator-2018-08-08/RemoveCustomRoutingEndpoints) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/RemoveCustomRoutingEndpoints) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/globalaccelerator-2018-08-08/RemoveCustomRoutingEndpoints) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/RemoveCustomRoutingEndpoints) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/globalaccelerator-2018-08-08/RemoveCustomRoutingEndpoints) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/globalaccelerator-2018-08-08/RemoveCustomRoutingEndpoints) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/globalaccelerator-2018-08-08/RemoveCustomRoutingEndpoints) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/globalaccelerator-2018-08-08/RemoveCustomRoutingEndpoints) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/RemoveCustomRoutingEndpoints) 