---
id: "@specs/aws/batch/docs/API_DeleteConsumableResource"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteConsumableResource"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# DeleteConsumableResource

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_DeleteConsumableResource
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteConsumableResource
<a name="API_DeleteConsumableResource"></a>

Deletes the specified consumable resource.

## Request Syntax
<a name="API_DeleteConsumableResource_RequestSyntax"></a>

```
POST /v1/deleteconsumableresource HTTP/1.1
Content-type: application/json

{
   "consumableResource": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteConsumableResource_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteConsumableResource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [consumableResource](#API_DeleteConsumableResource_RequestSyntax) **   <a name="Batch-DeleteConsumableResource-request-consumableResource"></a>
The name or ARN of the consumable resource that will be deleted.  
Type: String  
Required: Yes

## Response Syntax
<a name="API_DeleteConsumableResource_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteConsumableResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteConsumableResource_Errors"></a>

 ** ClientException **   
These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.  
HTTP Status Code: 400

 ** ServerException **   
These errors are usually caused by a server issue.  
HTTP Status Code: 500

## See Also
<a name="API_DeleteConsumableResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/batch-2016-08-10/DeleteConsumableResource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/batch-2016-08-10/DeleteConsumableResource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/DeleteConsumableResource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/batch-2016-08-10/DeleteConsumableResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/DeleteConsumableResource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/batch-2016-08-10/DeleteConsumableResource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/batch-2016-08-10/DeleteConsumableResource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/batch-2016-08-10/DeleteConsumableResource) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/DeleteConsumableResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/DeleteConsumableResource) 