---
id: "@specs/aws/batch/docs/API_DescribeConsumableResource"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeConsumableResource"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# DescribeConsumableResource

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_DescribeConsumableResource
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeConsumableResource
<a name="API_DescribeConsumableResource"></a>

Returns a description of the specified consumable resource.

## Request Syntax
<a name="API_DescribeConsumableResource_RequestSyntax"></a>

```
POST /v1/describeconsumableresource HTTP/1.1
Content-type: application/json

{
   "consumableResource": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DescribeConsumableResource_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeConsumableResource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [consumableResource](#API_DescribeConsumableResource_RequestSyntax) **   <a name="Batch-DescribeConsumableResource-request-consumableResource"></a>
The name or ARN of the consumable resource whose description will be returned.  
Type: String  
Required: Yes

## Response Syntax
<a name="API_DescribeConsumableResource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "availableQuantity": number,
   "consumableResourceArn": "string",
   "consumableResourceName": "string",
   "createdAt": number,
   "inUseQuantity": number,
   "resourceType": "string",
   "tags": { 
      "string" : "string" 
   },
   "totalQuantity": number
}
```

## Response Elements
<a name="API_DescribeConsumableResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [availableQuantity](#API_DescribeConsumableResource_ResponseSyntax) **   <a name="Batch-DescribeConsumableResource-response-availableQuantity"></a>
The amount of the consumable resource that is currently available to use.  
Type: Long

 ** [consumableResourceArn](#API_DescribeConsumableResource_ResponseSyntax) **   <a name="Batch-DescribeConsumableResource-response-consumableResourceArn"></a>
The Amazon Resource Name (ARN) of the consumable resource.  
Type: String

 ** [consumableResourceName](#API_DescribeConsumableResource_ResponseSyntax) **   <a name="Batch-DescribeConsumableResource-response-consumableResourceName"></a>
The name of the consumable resource.  
Type: String

 ** [createdAt](#API_DescribeConsumableResource_ResponseSyntax) **   <a name="Batch-DescribeConsumableResource-response-createdAt"></a>
The Unix timestamp (in milliseconds) for when the consumable resource was created.  
Type: Long

 ** [inUseQuantity](#API_DescribeConsumableResource_ResponseSyntax) **   <a name="Batch-DescribeConsumableResource-response-inUseQuantity"></a>
The amount of the consumable resource that is currently in use.  
Type: Long

 ** [resourceType](#API_DescribeConsumableResource_ResponseSyntax) **   <a name="Batch-DescribeConsumableResource-response-resourceType"></a>
Indicates whether the resource is available to be re-used after a job completes. Can be one of:   
+  `REPLENISHABLE` 
+  `NON_REPLENISHABLE` 
Type: String

 ** [tags](#API_DescribeConsumableResource_ResponseSyntax) **   <a name="Batch-DescribeConsumableResource-response-tags"></a>
The tags that you apply to the consumable resource to help you categorize and organize your resources. Each tag consists of a key and an optional value. For more information, see [Tagging your AWS Batch resources](https://docs.aws.amazon.com/batch/latest/userguide/using-tags.html).  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Maximum length of 256.

 ** [totalQuantity](#API_DescribeConsumableResource_ResponseSyntax) **   <a name="Batch-DescribeConsumableResource-response-totalQuantity"></a>
The total amount of the consumable resource that is available.  
Type: Long

## Errors
<a name="API_DescribeConsumableResource_Errors"></a>

 ** ClientException **   
These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.  
HTTP Status Code: 400

 ** ServerException **   
These errors are usually caused by a server issue.  
HTTP Status Code: 500

## See Also
<a name="API_DescribeConsumableResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/batch-2016-08-10/DescribeConsumableResource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/batch-2016-08-10/DescribeConsumableResource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/DescribeConsumableResource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/batch-2016-08-10/DescribeConsumableResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/DescribeConsumableResource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/batch-2016-08-10/DescribeConsumableResource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/batch-2016-08-10/DescribeConsumableResource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/batch-2016-08-10/DescribeConsumableResource) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/DescribeConsumableResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/DescribeConsumableResource) 