---
id: "@specs/aws/globalaccelerator/docs/API_DeleteCustomRoutingEndpointGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteCustomRoutingEndpointGroup"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# DeleteCustomRoutingEndpointGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_DeleteCustomRoutingEndpointGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteCustomRoutingEndpointGroup
<a name="API_DeleteCustomRoutingEndpointGroup"></a>

Delete an endpoint group from a listener for a custom routing accelerator.

## Request Syntax
<a name="API_DeleteCustomRoutingEndpointGroup_RequestSyntax"></a>

```
{
   "EndpointGroupArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteCustomRoutingEndpointGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EndpointGroupArn](#API_DeleteCustomRoutingEndpointGroup_RequestSyntax) **   <a name="globalaccelerator-DeleteCustomRoutingEndpointGroup-request-EndpointGroupArn"></a>
The Amazon Resource Name (ARN) of the endpoint group to delete.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

## Response Elements
<a name="API_DeleteCustomRoutingEndpointGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteCustomRoutingEndpointGroup_Errors"></a>

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

## See Also
<a name="API_DeleteCustomRoutingEndpointGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/globalaccelerator-2018-08-08/DeleteCustomRoutingEndpointGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/globalaccelerator-2018-08-08/DeleteCustomRoutingEndpointGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/DeleteCustomRoutingEndpointGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/globalaccelerator-2018-08-08/DeleteCustomRoutingEndpointGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/DeleteCustomRoutingEndpointGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/globalaccelerator-2018-08-08/DeleteCustomRoutingEndpointGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/globalaccelerator-2018-08-08/DeleteCustomRoutingEndpointGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/globalaccelerator-2018-08-08/DeleteCustomRoutingEndpointGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/globalaccelerator-2018-08-08/DeleteCustomRoutingEndpointGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/DeleteCustomRoutingEndpointGroup) 