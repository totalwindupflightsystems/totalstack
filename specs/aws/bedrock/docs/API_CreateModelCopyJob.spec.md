---
id: "@specs/aws/bedrock/docs/API_CreateModelCopyJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateModelCopyJob"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# CreateModelCopyJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_CreateModelCopyJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateModelCopyJob
<a name="API_CreateModelCopyJob"></a>

Copies a model to another region so that it can be used there. For more information, see [Copy models to be used in other regions](https://docs.aws.amazon.com/bedrock/latest/userguide/copy-model.html) in the [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html).

## Request Syntax
<a name="API_CreateModelCopyJob_RequestSyntax"></a>

```
POST /model-copy-jobs HTTP/1.1
Content-type: application/json

{
   "clientRequestToken": "{{string}}",
   "modelKmsKeyId": "{{string}}",
   "sourceModelArn": "{{string}}",
   "targetModelName": "{{string}}",
   "targetModelTags": [ 
      { 
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateModelCopyJob_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateModelCopyJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientRequestToken](#API_CreateModelCopyJob_RequestSyntax) **   <a name="bedrock-CreateModelCopyJob-request-clientRequestToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9]([-a-zA-Z0-9]{0,254}[a-zA-Z0-9])?`   
Required: No

 ** [modelKmsKeyId](#API_CreateModelCopyJob_RequestSyntax) **   <a name="bedrock-CreateModelCopyJob-request-modelKmsKeyId"></a>
The ARN of the AWS KMS key that you use to encrypt the model copy.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:kms:[a-zA-Z0-9-]*:[0-9]{12}:((key/[a-zA-Z0-9-]{36})|(alias/[a-zA-Z0-9-_/]+)))|([a-zA-Z0-9-]{36})|(alias/[a-zA-Z0-9-_/]+)`   
Required: No

 ** [sourceModelArn](#API_CreateModelCopyJob_RequestSyntax) **   <a name="bedrock-CreateModelCopyJob-request-sourceModelArn"></a>
The Amazon Resource Name (ARN) of the model to be copied.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:(([0-9]{12}:custom-model/((imported)|([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}))(([:][a-z0-9-]{1,63}){0,2})?/[a-z0-9]{12})|(:foundation-model/[a-z0-9-]{1,63}[.]{1}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}))`   
Required: Yes

 ** [targetModelName](#API_CreateModelCopyJob_RequestSyntax) **   <a name="bedrock-CreateModelCopyJob-request-targetModelName"></a>
A name for the copied model.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `([0-9a-zA-Z][_-]?){1,63}`   
Required: Yes

 ** [targetModelTags](#API_CreateModelCopyJob_RequestSyntax) **   <a name="bedrock-CreateModelCopyJob-request-targetModelTags"></a>
Tags to associate with the target model. For more information, see [Tag resources](https://docs.aws.amazon.com/bedrock/latest/userguide/tagging.html) in the [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html).  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 200 items.  
Required: No

## Response Syntax
<a name="API_CreateModelCopyJob_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "jobArn": "string"
}
```

## Response Elements
<a name="API_CreateModelCopyJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [jobArn](#API_CreateModelCopyJob_ResponseSyntax) **   <a name="bedrock-CreateModelCopyJob-response-jobArn"></a>
The Amazon Resource Name (ARN) of the model copy job.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:model-copy-job/[a-z0-9]{12}` 

## Errors
<a name="API_CreateModelCopyJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions.  
HTTP Status Code: 403

 ** InternalServerException **   
An internal server error occurred. Retry your request.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.  
HTTP Status Code: 404

 ** TooManyTagsException **   
The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request.     
 ** resourceName **   
The name of the resource with too many tags.
HTTP Status Code: 400

## Examples
<a name="API_CreateModelCopyJob_Examples"></a>

### Create a model copy job (CLI)
<a name="API_CreateModelCopyJob_Example_1"></a>

The following example shows how to copy a custom model from `us-west-2` into the region from which the request is made, using the AWS CLI.

```
aws bedrock create-model-copy-job --source-model-arn arn:aws:bedrock:us-west-2:123456789012:custom-model/amazon.titan-text-lite-v1:0:4k/MyCustomModel --target-model-name MyCustomModelCopy
```

## See Also
<a name="API_CreateModelCopyJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/CreateModelCopyJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/CreateModelCopyJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/CreateModelCopyJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/CreateModelCopyJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/CreateModelCopyJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/CreateModelCopyJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/CreateModelCopyJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/CreateModelCopyJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/CreateModelCopyJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/CreateModelCopyJob) 