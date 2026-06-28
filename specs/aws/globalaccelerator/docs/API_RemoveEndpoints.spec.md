---
id: "@specs/aws/globalaccelerator/docs/API_RemoveEndpoints"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RemoveEndpoints"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# RemoveEndpoints

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_RemoveEndpoints
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RemoveEndpoints
<a name="API_RemoveEndpoints"></a>

Remove endpoints from an endpoint group. 

The `RemoveEndpoints` API operation is the recommended option for removing endpoints. The alternative is to remove endpoints by updating an endpoint group by using the [UpdateEndpointGroup](https://docs.aws.amazon.com/global-accelerator/latest/api/API_UpdateEndpointGroup.html) API operation. There are two advantages to using `AddEndpoints` to remove endpoints instead:
+ It's more convenient, because you only need to specify the endpoints that you want to remove. With the `UpdateEndpointGroup` API operation, you must specify all of the endpoints in the endpoint group except the ones that you want to remove from the group.
+ It's faster, because Global Accelerator doesn't need to resolve any endpoints. With the `UpdateEndpointGroup` API operation, Global Accelerator must resolve all of the endpoints that remain in the group.

## Request Syntax
<a name="API_RemoveEndpoints_RequestSyntax"></a>

```
{
   "EndpointGroupArn": "{{string}}",
   "EndpointIdentifiers": [ 
      { 
         "ClientIPPreservationEnabled": {{boolean}},
         "EndpointId": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_RemoveEndpoints_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EndpointGroupArn](#API_RemoveEndpoints_RequestSyntax) **   <a name="globalaccelerator-RemoveEndpoints-request-EndpointGroupArn"></a>
The Amazon Resource Name (ARN) of the endpoint group.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

 ** [EndpointIdentifiers](#API_RemoveEndpoints_RequestSyntax) **   <a name="globalaccelerator-RemoveEndpoints-request-EndpointIdentifiers"></a>
The identifiers of the endpoints that you want to remove.  
Type: Array of [EndpointIdentifier](API_EndpointIdentifier.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Required: Yes

## Response Elements
<a name="API_RemoveEndpoints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_RemoveEndpoints_Errors"></a>

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

 ** TransactionInProgressException **   
There's already a transaction in progress. Another transaction can't be processed.  
HTTP Status Code: 400

## See Also
<a name="API_RemoveEndpoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/globalaccelerator-2018-08-08/RemoveEndpoints) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/globalaccelerator-2018-08-08/RemoveEndpoints) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/RemoveEndpoints) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/globalaccelerator-2018-08-08/RemoveEndpoints) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/RemoveEndpoints) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/globalaccelerator-2018-08-08/RemoveEndpoints) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/globalaccelerator-2018-08-08/RemoveEndpoints) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/globalaccelerator-2018-08-08/RemoveEndpoints) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/globalaccelerator-2018-08-08/RemoveEndpoints) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/RemoveEndpoints) 