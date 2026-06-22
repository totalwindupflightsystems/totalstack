---
id: "@specs/aws/codepipeline/docs/API_PollForJobs"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PollForJobs"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# PollForJobs

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_PollForJobs
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PollForJobs
<a name="API_PollForJobs"></a>

Returns information about any jobs for CodePipeline to act on. `PollForJobs` is valid only for action types with "Custom" in the owner field. If the action type contains `AWS` or `ThirdParty` in the owner field, the `PollForJobs` action returns an error.

**Important**  
When this API is called, CodePipeline returns temporary credentials for the S3 bucket used to store artifacts for the pipeline, if the action requires access to that S3 bucket for input or output artifacts. This API also returns any secret values defined for the action.

## Request Syntax
<a name="API_PollForJobs_RequestSyntax"></a>

```
{
   "actionTypeId": { 
      "category": "{{string}}",
      "owner": "{{string}}",
      "provider": "{{string}}",
      "version": "{{string}}"
   },
   "maxBatchSize": {{number}},
   "queryParam": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## Request Parameters
<a name="API_PollForJobs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [actionTypeId](#API_PollForJobs_RequestSyntax) **   <a name="CodePipeline-PollForJobs-request-actionTypeId"></a>
Represents information about an action type.  
Type: [ActionTypeId](API_ActionTypeId.md) object  
Required: Yes

 ** [maxBatchSize](#API_PollForJobs_RequestSyntax) **   <a name="CodePipeline-PollForJobs-request-maxBatchSize"></a>
The maximum number of jobs to return in a poll for jobs call.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

 ** [queryParam](#API_PollForJobs_RequestSyntax) **   <a name="CodePipeline-PollForJobs-request-queryParam"></a>
A map of property names and values. For an action type with no queryable properties, this value must be null or an empty map. For an action type with a queryable property, you must supply that property as a key in the map. Only jobs whose action configuration matches the mapped value are returned.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 1 item.  
Key Length Constraints: Minimum length of 1. Maximum length of 50.  
Value Length Constraints: Minimum length of 1. Maximum length of 50.  
Value Pattern: `[a-zA-Z0-9_-]+`   
Required: No

## Response Syntax
<a name="API_PollForJobs_ResponseSyntax"></a>

```
{
   "jobs": [ 
      { 
         "accountId": "string",
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
   ]
}
```

## Response Elements
<a name="API_PollForJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobs](#API_PollForJobs_ResponseSyntax) **   <a name="CodePipeline-PollForJobs-response-jobs"></a>
Information about the jobs to take action on.  
Type: Array of [Job](API_Job.md) objects

## Errors
<a name="API_PollForJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ActionTypeNotFoundException **   
The specified action type cannot be found.  
HTTP Status Code: 400

 ** ValidationException **   
The validation was specified in an invalid format.  
HTTP Status Code: 400

## Examples
<a name="API_PollForJobs_Examples"></a>

### Example
<a name="API_PollForJobs_Example_1"></a>

This example illustrates one usage of PollForJobs.

#### Sample Request
<a name="API_PollForJobs_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codepipeline.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 173
X-Amz-Target: CodePipeline_20150709.PollForJobs
X-Amz-Date: 20151030T230047Z
User-Agent: aws-cli/1.7.38 Python/2.7.9 Windows/7
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20151030/us-east-1/codepipeline/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
  "actionTypeId": {
    "category": "Test",
    "owner": "Custom",
    "version": "1",
    "provider": "JenkinsProviderName"
  },
  "maxBatchSize": 5,
  "queryParam": {
    "ProjectName": "JenkinsTestProject"
  }
}
```

#### Sample Response
<a name="API_PollForJobs_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 620484b7-88cb-11e5-b497-75c49EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 1830

{
  "jobs": [
    {
      "accountId": "111111111111",
      "data": {
        "actionConfiguration": {
          "__type": "ActionConfiguration",
          "configuration": {
            "ProjectName": "JenkinsTestProject"
          }
        },
        "actionTypeId": {
          "__type": "ActionTypeId",
          "category": "Test",
          "owner": "Custom",
          "provider": "JenkinsProviderName",
          "version": "1"
        },
        "artifactCredentials": {
          "__type": "AWSSessionCredentials",
          "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
          "secretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
          "sessionToken": "fICCQD6m7oRw0uXOjANBgkqhkiG9w0BAQUFADCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wHhcNMTEwNDI1MjA0NTIxWhcNMTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMaK0dn+a4GmWIWJ21uUSfwfEvySWtC2XADZ4nB+BLYgVIk60CpiwsZ3G93vUEIO3IyNoH/f0wYK8m9TrDHudUZg3qX4waLG5M43q7Wgc/MbQITxOUSQv7c7ugFFDzQGBzZswY6786m86gpEIbb3OhjZnzcvQAaRHhdlQWIMm2nrAgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAtCu4nUhVVxYUntneD9+h8Mg9q6q+auNKyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0FkbFFBjvSfpJIlJ00zbhNYS5f6GuoEDmFJl0ZxBHjJnyp378OD8uTs7fLvjx79LjSTbNYiytVbZPQUQ5Yaxu2jXnimvw3rrszlaEXAMPLE="
        },
        "inputArtifacts": [
          {
            "__type": "Artifact",
            "location": {
              "s3Location": {
                "bucketName": "amzn-s3-demo-bucket",
                "objectKey": "MySecondPipeline/MyAppBuild/EXAMPLE"
              },
              "type": "S3"
            },
            "name": "MyAppBuild"
          }
        ],
        "outputArtifacts": [],
        "pipelineContext": {
          "__type": "PipelineContext",
          "action": {
            "name": "JenkinsTestAction"
          },
          "pipelineName": "MySecondPipeline",
          "stage": {
            "name": "Testing"
          }
        }
      },
      "id": "ef66c259-64f9-EXAMPLE",
      "nonce": "3"
    }
  ]
}
```

## See Also
<a name="API_PollForJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codepipeline-2015-07-09/PollForJobs) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codepipeline-2015-07-09/PollForJobs) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/PollForJobs) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codepipeline-2015-07-09/PollForJobs) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/PollForJobs) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codepipeline-2015-07-09/PollForJobs) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codepipeline-2015-07-09/PollForJobs) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codepipeline-2015-07-09/PollForJobs) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codepipeline-2015-07-09/PollForJobs) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/PollForJobs) 