---
id: "@specs/aws/bedrock-agent/docs/API_CreateModelImportJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateModelImportJob"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# CreateModelImportJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_CreateModelImportJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateModelImportJob
<a name="API_CreateModelImportJob"></a>

Creates a model import job to import model that you have customized in other environments, such as Amazon SageMaker. For more information, see [Import a customized model](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html) 

## Request Syntax
<a name="API_CreateModelImportJob_RequestSyntax"></a>

```
POST /model-import-jobs HTTP/1.1
Content-type: application/json

{
   "clientRequestToken": "{{string}}",
   "importedModelKmsKeyId": "{{string}}",
   "importedModelName": "{{string}}",
   "importedModelTags": [ 
      { 
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "jobName": "{{string}}",
   "jobTags": [ 
      { 
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "modelDataSource": { ... },
   "roleArn": "{{string}}",
   "vpcConfig": { 
      "securityGroupIds": [ "{{string}}" ],
      "subnetIds": [ "{{string}}" ]
   }
}
```

## URI Request Parameters
<a name="API_CreateModelImportJob_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateModelImportJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientRequestToken](#API_CreateModelImportJob_RequestSyntax) **   <a name="bedrock-CreateModelImportJob-request-clientRequestToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9]([-a-zA-Z0-9]{0,254}[a-zA-Z0-9])?`   
Required: No

 ** [importedModelKmsKeyId](#API_CreateModelImportJob_RequestSyntax) **   <a name="bedrock-CreateModelImportJob-request-importedModelKmsKeyId"></a>
The imported model is encrypted at rest using this key.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:kms:[a-zA-Z0-9-]*:[0-9]{12}:((key/[a-zA-Z0-9-]{36})|(alias/[a-zA-Z0-9-_/]+)))|([a-zA-Z0-9-]{36})|(alias/[a-zA-Z0-9-_/]+)`   
Required: No

 ** [importedModelName](#API_CreateModelImportJob_RequestSyntax) **   <a name="bedrock-CreateModelImportJob-request-importedModelName"></a>
The name of the imported model.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `([0-9a-zA-Z][_-]?)+`   
Required: Yes

 ** [importedModelTags](#API_CreateModelImportJob_RequestSyntax) **   <a name="bedrock-CreateModelImportJob-request-importedModelTags"></a>
Tags to attach to the imported model.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 200 items.  
Required: No

 ** [jobName](#API_CreateModelImportJob_RequestSyntax) **   <a name="bedrock-CreateModelImportJob-request-jobName"></a>
The name of the import job.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9\+\-\.])*`   
Required: Yes

 ** [jobTags](#API_CreateModelImportJob_RequestSyntax) **   <a name="bedrock-CreateModelImportJob-request-jobTags"></a>
Tags to attach to this import job.   
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 200 items.  
Required: No

 ** [modelDataSource](#API_CreateModelImportJob_RequestSyntax) **   <a name="bedrock-CreateModelImportJob-request-modelDataSource"></a>
The data source for the imported model.  
Type: [ModelDataSource](API_ModelDataSource.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** [roleArn](#API_CreateModelImportJob_RequestSyntax) **   <a name="bedrock-CreateModelImportJob-request-roleArn"></a>
The Amazon Resource Name (ARN) of the service role with the proper custom model import permissions. You can use the console to automatically create a service role with the proper permissions or create a custom service role. For more information about creating a custom service role, see [Create a service role for model import](https://docs.aws.amazon.com/bedrock/latest/userguide/model-import-iam-role.html).  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+`   
Required: Yes

 ** [vpcConfig](#API_CreateModelImportJob_RequestSyntax) **   <a name="bedrock-CreateModelImportJob-request-vpcConfig"></a>
VPC configuration parameters for the private Virtual Private Cloud (VPC) that contains the resources you are using for the import job.  
Type: [VpcConfig](API_VpcConfig.md) object  
Required: No

## Response Syntax
<a name="API_CreateModelImportJob_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "jobArn": "string"
}
```

## Response Elements
<a name="API_CreateModelImportJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [jobArn](#API_CreateModelImportJob_ResponseSyntax) **   <a name="bedrock-CreateModelImportJob-response-jobArn"></a>
The Amazon Resource Name (ARN) of the model import job.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:model-import-job/[a-z0-9]{12}` 

## Errors
<a name="API_CreateModelImportJob_Errors"></a>

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
<a name="API_CreateModelImportJob_Examples"></a>

### Create a model import job
<a name="API_CreateModelImportJob_Example_1"></a>

Creates a model import job.

```
POST /model-import-jobs/ HTTP/1.1
Content-type: application/json
{
    "importedModelName": "ImportedModelName",
    "jobName": "MyImportedModelJobName",
    "modelDataSource": {
        "s3DataSource": {
            "s3Uri": "S3://amzn-s3-demo-bucket/key-name"
        }
    },
    "roleArn": "arn:aws:iam::111122223333:role/Role_Name"
}
```

### Example response
<a name="API_CreateModelImportJob_Example_2"></a>

Response for the above request.

```
HTTP/1.1 200
Content-type: application/json

{
    "jobArn": "arn:aws:bedrock:us-east-1:111122223333:model-import-job/yggb47n4xlml"
}
```

## See Also
<a name="API_CreateModelImportJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/CreateModelImportJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/CreateModelImportJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/CreateModelImportJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/CreateModelImportJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/CreateModelImportJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/CreateModelImportJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/CreateModelImportJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/CreateModelImportJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/CreateModelImportJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/CreateModelImportJob) 