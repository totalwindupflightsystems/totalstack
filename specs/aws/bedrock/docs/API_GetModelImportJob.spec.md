---
id: "@specs/aws/bedrock/docs/API_GetModelImportJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetModelImportJob"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# GetModelImportJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_GetModelImportJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetModelImportJob
<a name="API_GetModelImportJob"></a>

Retrieves the properties associated with import model job, including the status of the job. For more information, see [Import a customized model](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html) in the [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html).

## Request Syntax
<a name="API_GetModelImportJob_RequestSyntax"></a>

```
GET /model-import-jobs/{{jobIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetModelImportJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [jobIdentifier](#API_GetModelImportJob_RequestSyntax) **   <a name="bedrock-GetModelImportJob-request-uri-jobIdentifier"></a>
The identifier of the import job.  
Length Constraints: Minimum length of 0. Maximum length of 1011.  
Pattern: `(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:model-import-job/[a-z0-9]{12})|([a-zA-Z0-9](-*[a-zA-Z0-9\+\-\.])*)`   
Required: Yes

## Request Body
<a name="API_GetModelImportJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetModelImportJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "creationTime": "string",
   "endTime": "string",
   "failureMessage": "string",
   "importedModelArn": "string",
   "importedModelKmsKeyArn": "string",
   "importedModelName": "string",
   "jobArn": "string",
   "jobName": "string",
   "lastModifiedTime": "string",
   "modelDataSource": { ... },
   "roleArn": "string",
   "status": "string",
   "vpcConfig": { 
      "securityGroupIds": [ "string" ],
      "subnetIds": [ "string" ]
   }
}
```

## Response Elements
<a name="API_GetModelImportJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationTime](#API_GetModelImportJob_ResponseSyntax) **   <a name="bedrock-GetModelImportJob-response-creationTime"></a>
The time the resource was created.  
Type: Timestamp

 ** [endTime](#API_GetModelImportJob_ResponseSyntax) **   <a name="bedrock-GetModelImportJob-response-endTime"></a>
Time that the resource transitioned to terminal state.  
Type: Timestamp

 ** [failureMessage](#API_GetModelImportJob_ResponseSyntax) **   <a name="bedrock-GetModelImportJob-response-failureMessage"></a>
Information about why the import job failed.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [importedModelArn](#API_GetModelImportJob_ResponseSyntax) **   <a name="bedrock-GetModelImportJob-response-importedModelArn"></a>
The Amazon Resource Name (ARN) of the imported model.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:imported-model/[a-z0-9]{12}` 

 ** [importedModelKmsKeyArn](#API_GetModelImportJob_ResponseSyntax) **   <a name="bedrock-GetModelImportJob-response-importedModelKmsKeyArn"></a>
The imported model is encrypted at rest using this key.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}` 

 ** [importedModelName](#API_GetModelImportJob_ResponseSyntax) **   <a name="bedrock-GetModelImportJob-response-importedModelName"></a>
The name of the imported model.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `([0-9a-zA-Z][_-]?)+` 

 ** [jobArn](#API_GetModelImportJob_ResponseSyntax) **   <a name="bedrock-GetModelImportJob-response-jobArn"></a>
The Amazon Resource Name (ARN) of the import job.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:model-import-job/[a-z0-9]{12}` 

 ** [jobName](#API_GetModelImportJob_ResponseSyntax) **   <a name="bedrock-GetModelImportJob-response-jobName"></a>
The name of the import job.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9\+\-\.])*` 

 ** [lastModifiedTime](#API_GetModelImportJob_ResponseSyntax) **   <a name="bedrock-GetModelImportJob-response-lastModifiedTime"></a>
Time the resource was last modified.  
Type: Timestamp

 ** [modelDataSource](#API_GetModelImportJob_ResponseSyntax) **   <a name="bedrock-GetModelImportJob-response-modelDataSource"></a>
The data source for the imported model.  
Type: [ModelDataSource](API_ModelDataSource.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [roleArn](#API_GetModelImportJob_ResponseSyntax) **   <a name="bedrock-GetModelImportJob-response-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role associated with this job.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+` 

 ** [status](#API_GetModelImportJob_ResponseSyntax) **   <a name="bedrock-GetModelImportJob-response-status"></a>
The status of the job. A successful job transitions from in-progress to completed when the imported model is ready to use. If the job failed, the failure message contains information about why the job failed.  
Type: String  
Valid Values: `InProgress | Completed | Failed` 

 ** [vpcConfig](#API_GetModelImportJob_ResponseSyntax) **   <a name="bedrock-GetModelImportJob-response-vpcConfig"></a>
The Virtual Private Cloud (VPC) configuration of the import model job.  
Type: [VpcConfig](API_VpcConfig.md) object

## Errors
<a name="API_GetModelImportJob_Errors"></a>

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

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.  
HTTP Status Code: 400

## Examples
<a name="API_GetModelImportJob_Examples"></a>

### Get model import job
<a name="API_GetModelImportJob_Example_1"></a>

Gets the properties of a model import job.

```
GET /model-import-jobs/{jobIdentifier} HTTP/1.1
Content-type: application/json
```

### Example response
<a name="API_GetModelImportJob_Example_2"></a>

Response for the above request.

```
HTTP/1.1 200
Content-type: application/json

{
    "jobArn": "arn:aws:bedrock:us-east-1:111122223333:model-import-job/yggb47n4xlml",
    "jobName": "MyImportedModelJobName",
    "importedModelName": "ImportedModelName",
    "roleArn": "arn:aws:iam::111122223333:role/Role_Name",
    "modelDataSource": {
        "s3DataSource": {
            "s3Uri": "S3://amzn-s3-demo-bucket/key-name"
        }
    },
    "status": "InProgress",
    "creationTime": "2024-08-13T23:38:42.457Z",
    "lastModifiedTime": "2024-08-13T23:39:25.158Z"
}
```

## See Also
<a name="API_GetModelImportJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/GetModelImportJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/GetModelImportJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GetModelImportJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/GetModelImportJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GetModelImportJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/GetModelImportJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/GetModelImportJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/GetModelImportJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/GetModelImportJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GetModelImportJob) 