---
id: "@specs/aws/codepipeline/docs/API_CreatePipeline"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreatePipeline"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# CreatePipeline

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_CreatePipeline
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreatePipeline
<a name="API_CreatePipeline"></a>

Creates a pipeline.

**Note**  
In the pipeline structure, you must include either `artifactStore` or `artifactStores` in your pipeline, but you cannot use both. If you create a cross-region action in your pipeline, you must use `artifactStores`.

## Request Syntax
<a name="API_CreatePipeline_RequestSyntax"></a>

```
{
   "pipeline": { 
      "artifactStore": { 
         "encryptionKey": { 
            "id": "{{string}}",
            "type": "{{string}}"
         },
         "location": "{{string}}",
         "type": "{{string}}"
      },
      "artifactStores": { 
         "{{string}}" : { 
            "encryptionKey": { 
               "id": "{{string}}",
               "type": "{{string}}"
            },
            "location": "{{string}}",
            "type": "{{string}}"
         }
      },
      "executionMode": "{{string}}",
      "name": "{{string}}",
      "pipelineType": "{{string}}",
      "roleArn": "{{string}}",
      "stages": [ 
         { 
            "actions": [ 
               { 
                  "actionTypeId": { 
                     "category": "{{string}}",
                     "owner": "{{string}}",
                     "provider": "{{string}}",
                     "version": "{{string}}"
                  },
                  "commands": [ "{{string}}" ],
                  "configuration": { 
                     "{{string}}" : "{{string}}" 
                  },
                  "environmentVariables": [ 
                     { 
                        "name": "{{string}}",
                        "type": "{{string}}",
                        "value": "{{string}}"
                     }
                  ],
                  "inputArtifacts": [ 
                     { 
                        "name": "{{string}}"
                     }
                  ],
                  "name": "{{string}}",
                  "namespace": "{{string}}",
                  "outputArtifacts": [ 
                     { 
                        "files": [ "{{string}}" ],
                        "name": "{{string}}"
                     }
                  ],
                  "outputVariables": [ "{{string}}" ],
                  "region": "{{string}}",
                  "roleArn": "{{string}}",
                  "runOrder": {{number}},
                  "timeoutInMinutes": {{number}}
               }
            ],
            "beforeEntry": { 
               "conditions": [ 
                  { 
                     "result": "{{string}}",
                     "rules": [ 
                        { 
                           "commands": [ "{{string}}" ],
                           "configuration": { 
                              "{{string}}" : "{{string}}" 
                           },
                           "inputArtifacts": [ 
                              { 
                                 "name": "{{string}}"
                              }
                           ],
                           "name": "{{string}}",
                           "region": "{{string}}",
                           "roleArn": "{{string}}",
                           "ruleTypeId": { 
                              "category": "{{string}}",
                              "owner": "{{string}}",
                              "provider": "{{string}}",
                              "version": "{{string}}"
                           },
                           "timeoutInMinutes": {{number}}
                        }
                     ]
                  }
               ]
            },
            "blockers": [ 
               { 
                  "name": "{{string}}",
                  "type": "{{string}}"
               }
            ],
            "name": "{{string}}",
            "onFailure": { 
               "conditions": [ 
                  { 
                     "result": "{{string}}",
                     "rules": [ 
                        { 
                           "commands": [ "{{string}}" ],
                           "configuration": { 
                              "{{string}}" : "{{string}}" 
                           },
                           "inputArtifacts": [ 
                              { 
                                 "name": "{{string}}"
                              }
                           ],
                           "name": "{{string}}",
                           "region": "{{string}}",
                           "roleArn": "{{string}}",
                           "ruleTypeId": { 
                              "category": "{{string}}",
                              "owner": "{{string}}",
                              "provider": "{{string}}",
                              "version": "{{string}}"
                           },
                           "timeoutInMinutes": {{number}}
                        }
                     ]
                  }
               ],
               "result": "{{string}}",
               "retryConfiguration": { 
                  "retryMode": "{{string}}"
               }
            },
            "onSuccess": { 
               "conditions": [ 
                  { 
                     "result": "{{string}}",
                     "rules": [ 
                        { 
                           "commands": [ "{{string}}" ],
                           "configuration": { 
                              "{{string}}" : "{{string}}" 
                           },
                           "inputArtifacts": [ 
                              { 
                                 "name": "{{string}}"
                              }
                           ],
                           "name": "{{string}}",
                           "region": "{{string}}",
                           "roleArn": "{{string}}",
                           "ruleTypeId": { 
                              "category": "{{string}}",
                              "owner": "{{string}}",
                              "provider": "{{string}}",
                              "version": "{{string}}"
                           },
                           "timeoutInMinutes": {{number}}
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
                        "excludes": [ "{{string}}" ],
                        "includes": [ "{{string}}" ]
                     },
                     "events": [ "{{string}}" ],
                     "filePaths": { 
                        "excludes": [ "{{string}}" ],
                        "includes": [ "{{string}}" ]
                     }
                  }
               ],
               "push": [ 
                  { 
                     "branches": { 
                        "excludes": [ "{{string}}" ],
                        "includes": [ "{{string}}" ]
                     },
                     "filePaths": { 
                        "excludes": [ "{{string}}" ],
                        "includes": [ "{{string}}" ]
                     },
                     "tags": { 
                        "excludes": [ "{{string}}" ],
                        "includes": [ "{{string}}" ]
                     }
                  }
               ],
               "sourceActionName": "{{string}}"
            },
            "providerType": "{{string}}"
         }
      ],
      "variables": [ 
         { 
            "defaultValue": "{{string}}",
            "description": "{{string}}",
            "name": "{{string}}"
         }
      ],
      "version": {{number}}
   },
   "tags": [ 
      { 
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreatePipeline_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [pipeline](#API_CreatePipeline_RequestSyntax) **   <a name="CodePipeline-CreatePipeline-request-pipeline"></a>
Represents the structure of actions and stages to be performed in the pipeline.   
Type: [PipelineDeclaration](API_PipelineDeclaration.md) object  
Required: Yes

 ** [tags](#API_CreatePipeline_RequestSyntax) **   <a name="CodePipeline-CreatePipeline-request-tags"></a>
The tags for the pipeline.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## Response Syntax
<a name="API_CreatePipeline_ResponseSyntax"></a>

```
{
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
   },
   "tags": [ 
      { 
         "key": "string",
         "value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_CreatePipeline_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [pipeline](#API_CreatePipeline_ResponseSyntax) **   <a name="CodePipeline-CreatePipeline-response-pipeline"></a>
Represents the structure of actions and stages to be performed in the pipeline.   
Type: [PipelineDeclaration](API_PipelineDeclaration.md) object

 ** [tags](#API_CreatePipeline_ResponseSyntax) **   <a name="CodePipeline-CreatePipeline-response-tags"></a>
Specifies the tags applied to the pipeline.  
Type: Array of [Tag](API_Tag.md) objects

## Errors
<a name="API_CreatePipeline_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **   
Unable to modify the tag due to a simultaneous update request.  
HTTP Status Code: 400

 ** InvalidActionDeclarationException **   
The action declaration was specified in an invalid format.  
HTTP Status Code: 400

 ** InvalidBlockerDeclarationException **   
Reserved for future use.  
HTTP Status Code: 400

 ** InvalidStageDeclarationException **   
The stage declaration was specified in an invalid format.  
HTTP Status Code: 400

 ** InvalidStructureException **   
The structure was specified in an invalid format.  
HTTP Status Code: 400

 ** InvalidTagsException **   
The specified resource tags are invalid.  
HTTP Status Code: 400

 ** LimitExceededException **   
The number of pipelines associated with the AWS account has exceeded the limit allowed for the account.  
HTTP Status Code: 400

 ** PipelineNameInUseException **   
The specified pipeline name is already in use.  
HTTP Status Code: 400

 ** TooManyTagsException **   
The tags limit for a resource has been exceeded.  
HTTP Status Code: 400

 ** ValidationException **   
The validation was specified in an invalid format.  
HTTP Status Code: 400

## Examples
<a name="API_CreatePipeline_Examples"></a>

### Example
<a name="API_CreatePipeline_Example_1"></a>

This example illustrates one usage of CreatePipeline.

#### Sample Request
<a name="API_CreatePipeline_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codepipeline.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 923
X-Amz-Target: CodePipeline_20150709.CreatePipeline
X-Amz-Date: 20160707T175936Z
User-Agent: aws-cli/1.7.38 Python/2.7.9 Windows/7
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20160707/us-east-1/codepipeline/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
  "pipeline": {
    "roleArn": "arn:aws:iam::111111111111:role/AWS-CodePipeline-Service",
    "stages": [
      {
        "name": "Source",
        "actions": [
          {
            "inputArtifacts": [],
            "name": "Source",
            "actionTypeId": {
              "category": "Source",
              "owner": "AWS",
              "version": "1",
              "provider": "S3"
            },
            "outputArtifacts": [
              {
                "name": "MyApp"
              }
            ],
            "configuration": {
              "S3Bucket": "amzn-s3-demo-bucket",
              "S3ObjectKey": "aws-codepipeline-s3-aws-codedeploy_linux.zip"
            },
            "runOrder": 1
          }
        ]
      },
      {
        "name": "Staging",
        "actions": [
          {
            "inputArtifacts": [
              {
                "name": "MyApp"
              }
            ],
            "name": "CodePipelineDemoFleet",
            "actionTypeId": {
              "category": "Deploy",
              "owner": "AWS",
              "version": "1",
              "provider": "CodeDeploy"
            },
            "outputArtifacts": [],
            "configuration": {
              "ApplicationName": "CodePipelineDemoApplication",
              "DeploymentGroupName": "CodePipelineDemoFleet"
            },
            "runOrder": 1
          }
        ]
      }
    ],
    "artifactStore": {
      "type": "S3",
      "location": "amzn-s3-demo-bucket"
    },
    "name": "MySecondPipeline",
    "version": 1
  }
}
```

#### Sample Response
<a name="API_CreatePipeline_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 620484b7-88cb-11e5-b497-75c49EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 907

{
  "pipeline": {
    "artifactStore": {
      "location": "amzn-s3-demo-bucket",
      "type": "S3"
    },
    "name": "MySecondPipeline",
    "roleArn": "arn:aws:iam::111111111111:role/AWS-CodePipeline-Service",
    "stages": [
      {
        "actions": [
          {
            "actionTypeId": {
              "__type": "ActionTypeId",
              "category": "Source",
              "owner": "AWS",
              "provider": "S3",
              "version": "1"
            },
            "configuration": {
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
        ],
        "name": "Source"
      },
      {
        "actions": [
          {
            "actionTypeId": {
              "__type": "ActionTypeId",
              "category": "Deploy",
              "owner": "AWS",
              "provider": "CodeDeploy",
              "version": "1"
            },
            "configuration": {
              "ApplicationName": "CodePipelineDemoApplication",
              "DeploymentGroupName": "CodePipelineDemoFleet"
            },
            "inputArtifacts": [
              {
                "name": "MyApp"
              }
            ],
            "name": "CodePipelineDemoFleet",
            "outputArtifacts": [],
            "runOrder": 1
          }
        ],
        "name": "Staging"
      }
    ],
    "version": 1
  }
}
```

## See Also
<a name="API_CreatePipeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codepipeline-2015-07-09/CreatePipeline) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codepipeline-2015-07-09/CreatePipeline) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/CreatePipeline) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codepipeline-2015-07-09/CreatePipeline) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/CreatePipeline) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codepipeline-2015-07-09/CreatePipeline) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codepipeline-2015-07-09/CreatePipeline) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codepipeline-2015-07-09/CreatePipeline) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codepipeline-2015-07-09/CreatePipeline) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/CreatePipeline) 