---
id: "@specs/aws/codepipeline/docs/API_GetThirdPartyJobDetails"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetThirdPartyJobDetails"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# GetThirdPartyJobDetails

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_GetThirdPartyJobDetails
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetThirdPartyJobDetails
<a name="API_GetThirdPartyJobDetails"></a>

Requests the details of a job for a third party action. Used for partner actions only.

**Important**  
When this API is called, CodePipeline returns temporary credentials for the S3 bucket used to store artifacts for the pipeline, if the action requires access to that S3 bucket for input or output artifacts. This API also returns any secret values defined for the action.

## Request Syntax
<a name="API_GetThirdPartyJobDetails_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "jobId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetThirdPartyJobDetails_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_GetThirdPartyJobDetails_RequestSyntax) **   <a name="CodePipeline-GetThirdPartyJobDetails-request-clientToken"></a>
The clientToken portion of the clientId and clientToken pair used to verify that the calling entity is allowed access to the job and its details.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: Yes

 ** [jobId](#API_GetThirdPartyJobDetails_RequestSyntax) **   <a name="CodePipeline-GetThirdPartyJobDetails-request-jobId"></a>
The unique system-generated ID used for identifying the job.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Required: Yes

## Response Syntax
<a name="API_GetThirdPartyJobDetails_ResponseSyntax"></a>

```
{
   "jobDetails": { 
      "data": { 
         "actionConfiguration": { 
            "configuration": { 
               "string" : "string" 
            }
         },
         "actionTypeId": { 
            "category": "string",
            "owner": "string",
            "provider": "string",
            "version": "string"
         },
         "artifactCredentials": { 
            "accessKeyId": "string",
            "secretAccessKey": "string",
            "sessionToken": "string"
         },
         "continuationToken": "string",
         "encryptionKey": { 
            "id": "string",
            "type": "string"
         },
         "inputArtifacts": [ 
            { 
               "location": { 
                  "s3Location": { 
                     "bucketName": "string",
                     "objectKey": "string"
                  },
                  "type": "string"
               },
               "name": "string",
               "revision": "string"
            }
         ],
         "outputArtifacts": [ 
            { 
               "location": { 
                  "s3Location": { 
                     "bucketName": "string",
                     "objectKey": "string"
                  },
                  "type": "string"
               },
               "name": "string",
               "revision": "string"
            }
         ],
         "pipelineContext": { 
            "action": { 
               "actionExecutionId": "string",
               "name": "string"
            },
            "pipelineArn": "string",
            "pipelineExecutionId": "string",
            "pipelineName": "string",
            "stage": { 
               "name": "string"
            }
         }
      },
      "id": "string",
      "nonce": "string"
   }
}
```

## Response Elements
<a name="API_GetThirdPartyJobDetails_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobDetails](#API_GetThirdPartyJobDetails_ResponseSyntax) **   <a name="CodePipeline-GetThirdPartyJobDetails-response-jobDetails"></a>
The details of the job, including any protected values defined for the job.  
Type: [ThirdPartyJobDetails](API_ThirdPartyJobDetails.md) object

## Errors
<a name="API_GetThirdPartyJobDetails_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidClientTokenException **   
The client token was specified in an invalid format  
HTTP Status Code: 400

 ** InvalidJobException **   
The job was specified in an invalid format or cannot be found.  
HTTP Status Code: 400

 ** JobNotFoundException **   
The job was specified in an invalid format or cannot be found.  
HTTP Status Code: 400

 ** ValidationException **   
The validation was specified in an invalid format.  
HTTP Status Code: 400

## See Also
<a name="API_GetThirdPartyJobDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codepipeline-2015-07-09/GetThirdPartyJobDetails) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codepipeline-2015-07-09/GetThirdPartyJobDetails) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/GetThirdPartyJobDetails) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codepipeline-2015-07-09/GetThirdPartyJobDetails) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/GetThirdPartyJobDetails) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codepipeline-2015-07-09/GetThirdPartyJobDetails) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codepipeline-2015-07-09/GetThirdPartyJobDetails) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codepipeline-2015-07-09/GetThirdPartyJobDetails) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codepipeline-2015-07-09/GetThirdPartyJobDetails) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/GetThirdPartyJobDetails) 