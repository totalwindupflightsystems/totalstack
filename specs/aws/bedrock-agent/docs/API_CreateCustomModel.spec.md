---
id: "@specs/aws/bedrock-agent/docs/API_CreateCustomModel"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateCustomModel"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# CreateCustomModel

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_CreateCustomModel
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateCustomModel
<a name="API_CreateCustomModel"></a>

Creates a new custom model in Amazon Bedrock. After the model is active, you can use it for inference.

You can provide the model data source in one of the following ways:
+  `customModelDataSource` — Specify a SageMaker AI model package ARN. Amazon Bedrock resolves the model package to retrieve the model artifacts. This is the preferred method for new SageMaker AI training outputs.
+  `modelSourceConfig` — Specify an Amazon S3 URI pointing to the Amazon-managed Amazon S3 bucket containing your model artifacts.

To use the model for inference, you must purchase Provisioned Throughput for it. You can't use On-demand inference with these custom models. For more information about Provisioned Throughput, see [Provisioned Throughput](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html).

The model appears in `ListCustomModels` with a `customizationType` of `imported`. To track the status of the new model, you use the `GetCustomModel` API operation. The model can be in the following states:
+  `Creating` - Initial state during validation and registration
+  `Active` - Model is ready for use in inference
+  `Failed` - Creation process encountered an error

 **Related APIs** 
+  [GetCustomModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetCustomModel.html) 
+  [ListCustomModels](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListCustomModels.html) 
+  [DeleteCustomModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_DeleteCustomModel.html) 

## Request Syntax
<a name="API_CreateCustomModel_RequestSyntax"></a>

```
POST /custom-models/create-custom-model HTTP/1.1
Content-type: application/json

{
   "clientRequestToken": "{{string}}",
   "customModelDataSource": { ... },
   "modelKmsKeyArn": "{{string}}",
   "modelName": "{{string}}",
   "modelSourceConfig": { ... },
   "modelTags": [ 
      { 
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "roleArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateCustomModel_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateCustomModel_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientRequestToken](#API_CreateCustomModel_RequestSyntax) **   <a name="bedrock-CreateCustomModel-request-clientRequestToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9]([-a-zA-Z0-9]{0,254}[a-zA-Z0-9])?`   
Required: No

 ** [customModelDataSource](#API_CreateCustomModel_RequestSyntax) **   <a name="bedrock-CreateCustomModel-request-customModelDataSource"></a>
The data source for the custom model. Use this field to specify a SageMaker AI model package ARN as the source for your custom model. Amazon Bedrock resolves the model package to retrieve the model artifacts.  
You can specify either `customModelDataSource` or `modelSourceConfig`, but not both.  
Type: [CustomModelDataSource](API_CustomModelDataSource.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** [modelKmsKeyArn](#API_CreateCustomModel_RequestSyntax) **   <a name="bedrock-CreateCustomModel-request-modelKmsKeyArn"></a>
The Amazon Resource Name (ARN) of the customer managed AWS KMS key to encrypt the custom model. If you don't provide a AWS KMS key, Amazon Bedrock uses an AWS-managed AWS KMS key to encrypt the model.   
If you provide a customer managed AWS KMS key, your Amazon Bedrock service role must have permissions to use it. For more information see [Encryption of imported models](https://docs.aws.amazon.com/bedrock/latest/userguide/encryption-import-model.html).   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`   
Required: No

 ** [modelName](#API_CreateCustomModel_RequestSyntax) **   <a name="bedrock-CreateCustomModel-request-modelName"></a>
A unique name for the custom model.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `([0-9a-zA-Z][_-]?){1,63}`   
Required: Yes

 ** [modelSourceConfig](#API_CreateCustomModel_RequestSyntax) **   <a name="bedrock-CreateCustomModel-request-modelSourceConfig"></a>
The data source for the model. The Amazon S3 URI in the model source must be for the Amazon-managed Amazon S3 bucket containing your model artifacts.  
Type: [ModelDataSource](API_ModelDataSource.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** [modelTags](#API_CreateCustomModel_RequestSyntax) **   <a name="bedrock-CreateCustomModel-request-modelTags"></a>
A list of key-value pairs to associate with the custom model resource. You can use these tags to organize and identify your resources.  
For more information, see [Tagging resources](https://docs.aws.amazon.com/bedrock/latest/userguide/tagging.html) in the [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html).  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 200 items.  
Required: No

 ** [roleArn](#API_CreateCustomModel_RequestSyntax) **   <a name="bedrock-CreateCustomModel-request-roleArn"></a>
The Amazon Resource Name (ARN) of an IAM service role that Amazon Bedrock assumes to perform tasks on your behalf. This role must have permissions to access the Amazon S3 bucket containing your model artifacts and the AWS KMS key (if specified). For more information, see [Setting up an IAM service role for importing models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-import-iam-role.html) in the Amazon Bedrock User Guide.  
This field is required when you use `modelSourceConfig` with an Amazon S3 data source. It is not required when you use `customModelDataSource` with a model package ARN, because Amazon Bedrock uses its own credentials to access the model artifacts.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+`   
Required: No

## Response Syntax
<a name="API_CreateCustomModel_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "modelArn": "string"
}
```

## Response Elements
<a name="API_CreateCustomModel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [modelArn](#API_CreateCustomModel_ResponseSyntax) **   <a name="bedrock-CreateCustomModel-response-modelArn"></a>
The Amazon Resource Name (ARN) of the new custom model.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:(([0-9]{12}:custom-model/((imported)|([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}))(([:][a-z0-9-]{1,63}){0,2})?/[a-z0-9]{12})|(:foundation-model/[a-z0-9-]{1,63}[.]{1}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}))` 

## Errors
<a name="API_CreateCustomModel_Errors"></a>

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

 ** ServiceQuotaExceededException **   
The number of requests exceeds the service quota. Resubmit your request later.  
HTTP Status Code: 400

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** TooManyTagsException **   
The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request.     
 ** resourceName **   
The name of the resource with too many tags.
HTTP Status Code: 400

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.  
HTTP Status Code: 400

## Examples
<a name="API_CreateCustomModel_Examples"></a>

### Example request using a model package ARN
<a name="API_CreateCustomModel_Example_1"></a>

This example illustrates one usage of CreateCustomModel.

```
POST /custom-models/create-custom-model HTTP/1.1
Content-type: application/json
 
{
    "modelName": "my-custom-nova-model",
    "customModelDataSource": {
        "modelPackageArnDataSource": {
            "modelPackageArn": "arn:aws:sagemaker:us-east-1:123456789012:model-package/my-model-package/1"
        }
    },
    "modelKmsKeyArn": "arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012",
    "clientRequestToken": "unique-request-token-123",
    "modelTags": [
        {
            "key": "Environment",
            "value": "Production"
        },
        {
            "key": "Project",
            "value": "CustomNova"
        }
    ]
}
```

### Example request using an S3 data source
<a name="API_CreateCustomModel_Example_2"></a>

This example illustrates one usage of CreateCustomModel.

```
POST /custom-models/create-custom-model HTTP/1.1
Content-type: application/json

{
    "modelName": "my-custom-nova-model",
    "modelSourceConfig": {
        "s3Uri": "s3://amzn-s3-demo-bucket/"
    },
    "roleArn": "arn:aws:iam::123456789012:role/BedrockCustomModelRole",
    "modelKmsKeyArn": "arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012",
    "clientRequestToken": "unique-request-token-123",
    "modelTags": [
        {
            "key": "Environment",
            "value": "Production"
        },
        {
            "key": "Project",
            "value": "CustomNova"
        }
    ]
}
```

## See Also
<a name="API_CreateCustomModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/CreateCustomModel) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/CreateCustomModel) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/CreateCustomModel) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/CreateCustomModel) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/CreateCustomModel) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/CreateCustomModel) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/CreateCustomModel) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/CreateCustomModel) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/CreateCustomModel) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/CreateCustomModel) 