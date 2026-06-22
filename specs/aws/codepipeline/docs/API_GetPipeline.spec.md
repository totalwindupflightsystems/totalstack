---
id: "@specs/aws/codepipeline/docs/API_GetPipeline"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetPipeline"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# GetPipeline

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_GetPipeline
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetPipeline
<a name="API_GetPipeline"></a>

Returns the metadata, structure, stages, and actions of a pipeline. Can be used to return the entire structure of a pipeline in JSON format, which can then be modified and used to update the pipeline structure with [UpdatePipeline](API_UpdatePipeline.md).

## Request Syntax
<a name="API_GetPipeline_RequestSyntax"></a>

```
{
   "name": "{{string}}",
   "version": {{number}}
}
```

## Request Parameters
<a name="API_GetPipeline_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [name](#API_GetPipeline_RequestSyntax) **   <a name="CodePipeline-GetPipeline-request-name"></a>
The name of the pipeline for which you want to get information. Pipeline names must be unique in an AWS account.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9.@\-_]+`   
Required: Yes

 ** [version](#API_GetPipeline_RequestSyntax) **   <a name="CodePipeline-GetPipeline-request-version"></a>
The version number of the pipeline. If you do not specify a version, defaults to the current version.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

## Response Syntax
<a name="API_GetPipeline_ResponseSyntax"></a>

```
{
   "metadata": { 
      "created": number,
      "pipelineArn": "string",
      "pollingDisabledAt": number,
      "updated": number
   },
   "pipeline": { 
      "artifactStore": { 
         "encryptionKey": { 
            "id": "string",
            "type": "string"
         },
         "location": "string",
         "type": "string"
      },
      "artifactStores": { 
         "string" : { 
            "encryptionKey": { 
               "id": "string",
               "type": "string"
            },
            "location": "string",
            "type": "string"
         }
      },
      "executionMode": "string",
      "name": "string",
      "pipelineType": "string",
      "roleArn": "string",
      "stages": [ 
         { 
            "actions": [ 
               { 
                  "actionTypeId": { 
                     "category": "string",
                     "owner": "string",
                     "provider": "string",
                     "version": "string"
                  },
                  "commands": [ "string" ],
                  "configuration": { 
                     "string" : "string" 
                  },
                  "environmentVariables": [ 
                     { 
                        "name": "string",
                        "type": "string",
                        "value": "string"
                     }
                  ],
                  "inputArtifacts": [ 
                     { 
                        "name": "string"
                     }
                  ],
                  "name": "string",
                  "namespace": "string",
                  "outputArtifacts": [ 
                     { 
                        "files": [ "string" ],
                        "name": "string"
                     }
                  ],
                  "outputVariables": [ "string" ],
                  "region": "string",
                  "roleArn": "string",
                  "runOrder": number,
                  "timeoutInMinutes": number
               }
            ],
            "beforeEntry": { 
               "conditions": [ 
                  { 
                     "result": "string",
                     "rules": [ 
                        { 
                           "commands": [ "string" ],
                           "configuration": { 
                              "string" : "string" 
                           },
                           "inputArtifacts": [ 
                              { 
                                 "name": "string"
                              }
                           ],
                           "name": "string",
                           "region": "string",
                           "roleArn": "string",
                           "ruleTypeId": { 
                              "category": "string",
                              "owner": "string",
                              "provider": "string",
                              "version": "string"
                           },
                           "timeoutInMinutes": number
                        }
                     ]
                  }
               ]
            },
            "blockers": [ 
               { 
                  "name": "string",
                  "type": "string"
               }
            ],
            "name": "string",
            "onFailure": { 
               "conditions": [ 
                  { 
                     "result": "string",
                     "rules": [ 
                        { 
                           "commands": [ "string" ],
                           "configuration": { 
                              "string" : "string" 
                           },
                           "inputArtifacts": [ 
                              { 
                                 "name": "string"
                              }
                           ],
                           "name": "string",
                           "region": "string",
                           "roleArn": "string",
                           "ruleTypeId": { 
                              "category": "string",
                              "owner": "string",
                              "provider": "string",
                              "version": "string"
                           },
                           "timeoutInMinutes": number
                        }
                     ]
                  }
               ],
               "result": "string",
               "retryConfiguration": { 
                  "retryMode": "string"
               }
            },
            "onSuccess": { 
               "conditions": [ 
                  { 
                     "result": "string",
                     "rules": [ 
                        { 
                           "commands": [ "string" ],
                           "configuration": { 
                              "string" : "string" 
                           },
                           "inputArtifacts": [ 
                              { 
                                 "name": "string"
                              }
                           ],
                           "name": "string",
                           "region": "string",
                           "roleArn": "string",
                           "ruleTypeId": { 
                              "category": "string",
                              "owner": "string",
                              "provider": "string",
                              "version": "string"
                           },
                           "timeoutInMinutes": number
                        }
                     ]
                  }
               ]
            }
         }
      ],
      "triggers": [ 
         { 
            "gitConfiguration": { 
               "pullRequest": [ 
                  { 
                     "branches": { 
                        "excludes": [ "string" ],
                        "includes": [ "string" ]
                     },
                     "events": [ "string" ],
                     "filePaths": { 
                        "excludes": [ "string" ],
                        "includes": [ "string" ]
                     }
                  }
               ],
               "push": [ 
                  { 
                     "branches": { 
                        "excludes": [ "string" ],
                        "includes": [ "string" ]
                     },
                     "filePaths": { 
                        "excludes": [ "string" ],
                        "includes": [ "string" ]
                     },
                     "tags": { 
                        "excludes": [ "string" ],
                        "includes": [ "string" ]
                     }
                  }
               ],
               "sourceActionName": "string"
            },
            "providerType": "string"
         }
      ],
      "variables": [ 
         { 
            "defaultValue": "string",
            "description": "string",
            "name": "string"
         }
      ],
      "version": number
   }
}
```

## Response Elements
<a name="API_GetPipeline_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [metadata](#API_GetPipeline_ResponseSyntax) **   <a name="CodePipeline-GetPipeline-response-metadata"></a>
Represents the pipeline metadata information returned as part of the output of a `GetPipeline` action.  
Type: [PipelineMetadata](API_PipelineMetadata.md) object

 ** [pipeline](#API_GetPipeline_ResponseSyntax) **   <a name="CodePipeline-GetPipeline-response-pipeline"></a>
Represents the structure of actions and stages to be performed in the pipeline.   
Type: [PipelineDeclaration](API_PipelineDeclaration.md) object

## Errors
<a name="API_GetPipeline_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** PipelineNotFoundException **   
The pipeline was specified in an invalid format or cannot be found.  
HTTP Status Code: 400

 ** PipelineVersionNotFoundException **   
The pipeline version was specified in an invalid format or cannot be found.  
HTTP Status Code: 400

 ** ValidationException **   
The validation was specified in an invalid format.  
HTTP Status Code: 400

## Examples
<a name="API_GetPipeline_Examples"></a>

### Example
<a name="API_GetPipeline_Example_1"></a>

This example illustrates one usage of GetPipeline.

#### Sample Request
<a name="API_GetPipeline_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codepipeline.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 27
X-Amz-Target: CodePipeline_20150709.GetPipeline
X-Amz-Date: 20160707T171559Z
User-Agent: aws-cli/1.7.38 Python/2.7.9 Windows/7
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20160707/us-east-1/codepipeline/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
  "name": "MyFirstPipeline"
}
```

#### Sample Response
<a name="API_GetPipeline_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 620484b7-88cb-11e5-b497-75c49EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 898

{
    "pipeline": {
        "roleArn": "arn:aws:iam::11111EXAMPLE:role/AWS-CodePipeline-Service",
        "stages": [
            {
                "name": "Source",
                "actions": [
                    {
                        "actionTypeId": {
                            "category": "Source",
                            "owner": "AWS",
                            "provider": "S3",
                            "version": "1"
                        },
                        "configuration": {
                            "PollForSourceChanges": "true",
                            "S3Bucket": "amzn-s3-demo-bucket",
                            "S3ObjectKey": "aws-codepipeline-s3-aws-codedeploy_linux.zip"
                        },
                        "inputArtifacts": [],
                        "name": "Source",
                        "outputArtifacts": [
                            {
                                "name": "MyApp"
                            }
                        ],
                        "runOrder": 1
                    }
                ]
            },
            {
                "name": "Build",
                "actions": [
                    {
                        "actionTypeId": {
                            "category": "Build",
                            "owner": "AWS",
                            "provider": "CodeBuild",
                            "version": "1"
                        },
                        "configuration": {
                            "ProjectName": "BuildProject"
                        },
                        "inputArtifacts": [
                            {
                                "name": "MyApp"
                            }
                        ],
                        "name": "CodeBuild",
                        "outputArtifacts": [
                            {
                                "name": "MyAppBuild"
                            }
                        ],
                        "runOrder": 1
                    }
                ]
            }
        ],
        "artifactStore": {
            "type": "S3",
            "location": "codepipeline-us-east-2-250656481468"
        },
        "name": "MyFirstPipeline",
        "version": 1
    },
    "metadata": {
        "pipelineArn": "arn:aws:codepipeline:us-east-2:80398EXAMPLE:MyFirstPipeline",
        "updated": 1501626591.112,
        "created": 1501626591.112
    }
}
```

## See Also
<a name="API_GetPipeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codepipeline-2015-07-09/GetPipeline) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codepipeline-2015-07-09/GetPipeline) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/GetPipeline) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codepipeline-2015-07-09/GetPipeline) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/GetPipeline) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codepipeline-2015-07-09/GetPipeline) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codepipeline-2015-07-09/GetPipeline) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codepipeline-2015-07-09/GetPipeline) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codepipeline-2015-07-09/GetPipeline) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/GetPipeline) 