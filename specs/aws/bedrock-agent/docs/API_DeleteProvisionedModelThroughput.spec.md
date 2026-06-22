---
id: "@specs/aws/bedrock-agent/docs/API_DeleteProvisionedModelThroughput"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteProvisionedModelThroughput"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# DeleteProvisionedModelThroughput

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_DeleteProvisionedModelThroughput
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteProvisionedModelThroughput
<a name="API_DeleteProvisionedModelThroughput"></a>

Deletes a Provisioned Throughput. You can't delete a Provisioned Throughput before the commitment term is over. For more information, see [Provisioned Throughput](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html) in the [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html).

## Request Syntax
<a name="API_DeleteProvisionedModelThroughput_RequestSyntax"></a>

```
DELETE /provisioned-model-throughput/{{provisionedModelId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteProvisionedModelThroughput_RequestParameters"></a>

The request uses the following URI parameters.

 ** [provisionedModelId](#API_DeleteProvisionedModelThroughput_RequestSyntax) **   <a name="bedrock-DeleteProvisionedModelThroughput-request-uri-provisionedModelId"></a>
The Amazon Resource Name (ARN) or ID of the Provisioned Throughput.  
Pattern: `((([0-9a-zA-Z][_-]?)+)|(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:provisioned-model/[a-z0-9]{12}))`   
Required: Yes

## Request Body
<a name="API_DeleteProvisionedModelThroughput_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteProvisionedModelThroughput_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteProvisionedModelThroughput_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteProvisionedModelThroughput_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions.  
HTTP Status Code: 403

 ** ConflictException **   
Error occurred because of a conflict while performing an operation.  
HTTP Status Code: 400

 ** InternalServerException **   
An internal server error occurred. Retry your request.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.  
HTTP Status Code: 404

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.  
HTTP Status Code: 400

## See Also
<a name="API_DeleteProvisionedModelThroughput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/DeleteProvisionedModelThroughput) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/DeleteProvisionedModelThroughput) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/DeleteProvisionedModelThroughput) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/DeleteProvisionedModelThroughput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/DeleteProvisionedModelThroughput) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/DeleteProvisionedModelThroughput) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/DeleteProvisionedModelThroughput) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/DeleteProvisionedModelThroughput) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/DeleteProvisionedModelThroughput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/DeleteProvisionedModelThroughput) 