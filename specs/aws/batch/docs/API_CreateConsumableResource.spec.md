---
id: "@specs/aws/batch/docs/API_CreateConsumableResource"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateConsumableResource"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# CreateConsumableResource

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_CreateConsumableResource
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateConsumableResource
<a name="API_CreateConsumableResource"></a>

Creates an AWS Batch consumable resource.

## Request Syntax
<a name="API_CreateConsumableResource_RequestSyntax"></a>

```
POST /v1/createconsumableresource HTTP/1.1
Content-type: application/json

{
   "consumableResourceName": "{{string}}",
   "resourceType": "{{string}}",
   "tags": { 
      "{{string}}" : "{{string}}" 
   },
   "totalQuantity": {{number}}
}
```

## URI Request Parameters
<a name="API_CreateConsumableResource_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateConsumableResource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [consumableResourceName](#API_CreateConsumableResource_RequestSyntax) **   <a name="Batch-CreateConsumableResource-request-consumableResourceName"></a>
The name of the consumable resource. Must be unique.  
Type: String  
Required: Yes

 ** [resourceType](#API_CreateConsumableResource_RequestSyntax) **   <a name="Batch-CreateConsumableResource-request-resourceType"></a>
Indicates whether the resource is available to be re-used after a job completes. Can be one of:   
+  `REPLENISHABLE` (default)
+  `NON_REPLENISHABLE` 
Type: String  
Required: No

 ** [tags](#API_CreateConsumableResource_RequestSyntax) **   <a name="Batch-CreateConsumableResource-request-tags"></a>
The tags that you apply to the consumable resource to help you categorize and organize your resources. Each tag consists of a key and an optional value. For more information, see [Tagging your AWS Batch resources](https://docs.aws.amazon.com/batch/latest/userguide/using-tags.html).  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Maximum length of 256.  
Required: No

 ** [totalQuantity](#API_CreateConsumableResource_RequestSyntax) **   <a name="Batch-CreateConsumableResource-request-totalQuantity"></a>
The total amount of the consumable resource that is available. Must be non-negative.  
Type: Long  
Required: No

## Response Syntax
<a name="API_CreateConsumableResource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "consumableResourceArn": "string",
   "consumableResourceName": "string"
}
```

## Response Elements
<a name="API_CreateConsumableResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [consumableResourceArn](#API_CreateConsumableResource_ResponseSyntax) **   <a name="Batch-CreateConsumableResource-response-consumableResourceArn"></a>
The Amazon Resource Name (ARN) of the consumable resource.  
Type: String

 ** [consumableResourceName](#API_CreateConsumableResource_ResponseSyntax) **   <a name="Batch-CreateConsumableResource-response-consumableResourceName"></a>
The name of the consumable resource.  
Type: String

## Errors
<a name="API_CreateConsumableResource_Errors"></a>

 ** ClientException **   
These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.  
HTTP Status Code: 400

 ** ServerException **   
These errors are usually caused by a server issue.  
HTTP Status Code: 500

## See Also
<a name="API_CreateConsumableResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/batch-2016-08-10/CreateConsumableResource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/batch-2016-08-10/CreateConsumableResource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/CreateConsumableResource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/batch-2016-08-10/CreateConsumableResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/CreateConsumableResource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/batch-2016-08-10/CreateConsumableResource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/batch-2016-08-10/CreateConsumableResource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/batch-2016-08-10/CreateConsumableResource) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/CreateConsumableResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/CreateConsumableResource) 