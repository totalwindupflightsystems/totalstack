---
id: "@specs/aws/batch/docs/API_UpdateConsumableResource"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateConsumableResource"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# UpdateConsumableResource

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_UpdateConsumableResource
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateConsumableResource
<a name="API_UpdateConsumableResource"></a>

Updates a consumable resource.

## Request Syntax
<a name="API_UpdateConsumableResource_RequestSyntax"></a>

```
POST /v1/updateconsumableresource HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "consumableResource": "{{string}}",
   "operation": "{{string}}",
   "quantity": {{number}}
}
```

## URI Request Parameters
<a name="API_UpdateConsumableResource_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateConsumableResource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_UpdateConsumableResource_RequestSyntax) **   <a name="Batch-UpdateConsumableResource-request-clientToken"></a>
If this parameter is specified and two update requests with identical payloads and `clientToken`s are received, these requests are considered the same request. Both requests will succeed, but the update will only happen once. A `clientToken` is valid for 8 hours.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Required: No

 ** [consumableResource](#API_UpdateConsumableResource_RequestSyntax) **   <a name="Batch-UpdateConsumableResource-request-consumableResource"></a>
The name or ARN of the consumable resource to be updated.  
Type: String  
Required: Yes

 ** [operation](#API_UpdateConsumableResource_RequestSyntax) **   <a name="Batch-UpdateConsumableResource-request-operation"></a>
Indicates how the quantity of the consumable resource will be updated. Must be one of:  
+  `SET` 

  Sets the quantity of the resource to the value specified by the `quantity` parameter.
+  `ADD` 

  Increases the quantity of the resource by the value specified by the `quantity` parameter.
+  `REMOVE` 

  Reduces the quantity of the resource by the value specified by the `quantity` parameter.
Type: String  
Required: No

 ** [quantity](#API_UpdateConsumableResource_RequestSyntax) **   <a name="Batch-UpdateConsumableResource-request-quantity"></a>
The change in the total quantity of the consumable resource. The `operation` parameter determines whether the value specified here will be the new total quantity, or the amount by which the total quantity will be increased or reduced. Must be a non-negative value.  
Type: Long  
Required: No

## Response Syntax
<a name="API_UpdateConsumableResource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "consumableResourceArn": "string",
   "consumableResourceName": "string",
   "totalQuantity": number
}
```

## Response Elements
<a name="API_UpdateConsumableResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [consumableResourceArn](#API_UpdateConsumableResource_ResponseSyntax) **   <a name="Batch-UpdateConsumableResource-response-consumableResourceArn"></a>
The Amazon Resource Name (ARN) of the consumable resource.  
Type: String

 ** [consumableResourceName](#API_UpdateConsumableResource_ResponseSyntax) **   <a name="Batch-UpdateConsumableResource-response-consumableResourceName"></a>
The name of the consumable resource to be updated.  
Type: String

 ** [totalQuantity](#API_UpdateConsumableResource_ResponseSyntax) **   <a name="Batch-UpdateConsumableResource-response-totalQuantity"></a>
The total amount of the consumable resource that is available.  
Type: Long

## Errors
<a name="API_UpdateConsumableResource_Errors"></a>

 ** ClientException **   
These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.  
HTTP Status Code: 400

 ** ServerException **   
These errors are usually caused by a server issue.  
HTTP Status Code: 500

## See Also
<a name="API_UpdateConsumableResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/batch-2016-08-10/UpdateConsumableResource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/batch-2016-08-10/UpdateConsumableResource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/UpdateConsumableResource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/batch-2016-08-10/UpdateConsumableResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/UpdateConsumableResource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/batch-2016-08-10/UpdateConsumableResource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/batch-2016-08-10/UpdateConsumableResource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/batch-2016-08-10/UpdateConsumableResource) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/UpdateConsumableResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/UpdateConsumableResource) 