---
id: "@specs/aws/codepipeline/docs/API_GetPipelineState"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetPipelineState"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# GetPipelineState

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_GetPipelineState
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetPipelineState
<a name="API_GetPipelineState"></a>

Returns information about the state of a pipeline, including the stages and actions.

**Note**  
Values returned in the `revisionId` and `revisionUrl` fields indicate the source revision information, such as the commit ID, for the current state.

## Request Syntax
<a name="API_GetPipelineState_RequestSyntax"></a>

```
{
   "name": "{{string}}"
}
```

## Request Parameters
<a name="API_GetPipelineState_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [name](#API_GetPipelineState_RequestSyntax) **   <a name="CodePipeline-GetPipelineState-request-name"></a>
The name of the pipeline about which you want to get information.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9.@\-_]+`   
Required: Yes

## Response Syntax
<a name="API_GetPipelineState_ResponseSyntax"></a>

```
{
   "created": number,
   "pipelineName": "string",
   "pipelineVersion": number,
   "stageStates": [ 
      { 
         "actionStates": [ 
            { 
               "actionName": "string",
               "currentRevision": { 
                  "created": number,
                  "revisionChangeId": "string",
                  "revisionId": "string"
               },
               "entityUrl": "string",
               "latestExecution": { 
                  "actionExecutionId": "string",
                  "errorDetails": { 
                     "code": "string",
                     "message": "string"
                  },
                  "externalExecutionId": "string",
                  "externalExecutionUrl": "string",
                  "lastStatusChange": number,
                  "lastUpdatedBy": "string",
                  "logStreamARN": "string",
                  "percentComplete": number,
                  "status": "string",
                  "summary": "string",
                  "token": "string"
               },
               "revisionUrl": "string"
            }
         ],
         "beforeEntryConditionState": { 
            "conditionStates": [ 
               { 
                  "latestExecution": { 
                     "lastStatusChange": number,
                     "status": "string",
                     "summary": "string"
                  },
                  "ruleStates": [ 
                     { 
                        "currentRevision": { 
                           "created": number,
                           "revisionChangeId": "string",
                           "revisionId": "string"
                        },
                        "entityUrl": "string",
                        "latestExecution": { 
                           "errorDetails": { 
                              "code": "string",
                              "message": "string"
                           },
                           "externalExecutionId": "string",
                           "externalExecutionUrl": "string",
                           "lastStatusChange": number,
                           "lastUpdatedBy": "string",
                           "ruleExecutionId": "string",
                           "status": "string",
                           "summary": "string",
                           "token": "string"
                        },
                        "revisionUrl": "string",
                        "ruleName": "string"
                     }
                  ]
               }
            ],
            "latestExecution": { 
               "status": "string",
               "summary": "string"
            }
         },
         "inboundExecution": { 
            "pipelineExecutionId": "string",
            "status": "string",
            "type": "string"
         },
         "inboundExecutions": [ 
            { 
               "pipelineExecutionId": "string",
               "status": "string",
               "type": "string"
            }
         ],
         "inboundTransitionState": { 
            "disabledReason": "string",
            "enabled": boolean,
            "lastChangedAt": number,
            "lastChangedBy": "string"
         },
         "latestExecution": { 
            "pipelineExecutionId": "string",
            "status": "string",
            "type": "string"
         },
         "onFailureConditionState": { 
            "conditionStates": [ 
               { 
                  "latestExecution": { 
                     "lastStatusChange": number,
                     "status": "string",
                     "summary": "string"
                  },
                  "ruleStates": [ 
                     { 
                        "currentRevision": { 
                           "created": number,
                           "revisionChangeId": "string",
                           "revisionId": "string"
                        },
                        "entityUrl": "string",
                        "latestExecution": { 
                           "errorDetails": { 
                              "code": "string",
                              "message": "string"
                           },
                           "externalExecutionId": "string",
                           "externalExecutionUrl": "string",
                           "lastStatusChange": number,
                           "lastUpdatedBy": "string",
                           "ruleExecutionId": "string",
                           "status": "string",
                           "summary": "string",
                           "token": "string"
                        },
                        "revisionUrl": "string",
                        "ruleName": "string"
                     }
                  ]
               }
            ],
            "latestExecution": { 
               "status": "string",
               "summary": "string"
            }
         },
         "onSuccessConditionState": { 
            "conditionStates": [ 
               { 
                  "latestExecution": { 
                     "lastStatusChange": number,
                     "status": "string",
                     "summary": "string"
                  },
                  "ruleStates": [ 
                     { 
                        "currentRevision": { 
                           "created": number,
                           "revisionChangeId": "string",
                           "revisionId": "string"
                        },
                        "entityUrl": "string",
                        "latestExecution": { 
                           "errorDetails": { 
                              "code": "string",
                              "message": "string"
                           },
                           "externalExecutionId": "string",
                           "externalExecutionUrl": "string",
                           "lastStatusChange": number,
                           "lastUpdatedBy": "string",
                           "ruleExecutionId": "string",
                           "status": "string",
                           "summary": "string",
                           "token": "string"
                        },
                        "revisionUrl": "string",
                        "ruleName": "string"
                     }
                  ]
               }
            ],
            "latestExecution": { 
               "status": "string",
               "summary": "string"
            }
         },
         "retryStageMetadata": { 
            "autoStageRetryAttempt": number,
            "latestRetryTrigger": "string",
            "manualStageRetryAttempt": number
         },
         "stageName": "string"
      }
   ],
   "updated": number
}
```

## Response Elements
<a name="API_GetPipelineState_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [created](#API_GetPipelineState_ResponseSyntax) **   <a name="CodePipeline-GetPipelineState-response-created"></a>
The date and time the pipeline was created, in timestamp format.  
Type: Timestamp

 ** [pipelineName](#API_GetPipelineState_ResponseSyntax) **   <a name="CodePipeline-GetPipelineState-response-pipelineName"></a>
The name of the pipeline for which you want to get the state.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9.@\-_]+` 

 ** [pipelineVersion](#API_GetPipelineState_ResponseSyntax) **   <a name="CodePipeline-GetPipelineState-response-pipelineVersion"></a>
The version number of the pipeline.  
A newly created pipeline is always assigned a version number of `1`.
Type: Integer  
Valid Range: Minimum value of 1.

 ** [stageStates](#API_GetPipelineState_ResponseSyntax) **   <a name="CodePipeline-GetPipelineState-response-stageStates"></a>
A list of the pipeline stage output information, including stage name, state, most recent run details, whether the stage is disabled, and other data.  
Type: Array of [StageState](API_StageState.md) objects

 ** [updated](#API_GetPipelineState_ResponseSyntax) **   <a name="CodePipeline-GetPipelineState-response-updated"></a>
The date and time the pipeline was last updated, in timestamp format.  
Type: Timestamp

## Errors
<a name="API_GetPipelineState_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** PipelineNotFoundException **   
The pipeline was specified in an invalid format or cannot be found.  
HTTP Status Code: 400

 ** ValidationException **   
The validation was specified in an invalid format.  
HTTP Status Code: 400

## Examples
<a name="API_GetPipelineState_Examples"></a>

### Example
<a name="API_GetPipelineState_Example_1"></a>

This example illustrates one usage of GetPipelineState.

#### Sample Request
<a name="API_GetPipelineState_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codepipeline.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 27
X-Amz-Target: CodePipeline_20150709.GetPipelineState
X-Amz-Date: 20160707T172005Z
User-Agent: aws-cli/1.7.38 Python/2.7.9 Windows/7
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20160707/us-east-1/codepipeline/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
  "name": "MyFirstPipeline"
}
```

#### Sample Response
<a name="API_GetPipelineState_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 620484b7-88cb-11e5-b497-75c49EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 827

{
    "created": 1446137312.204,
    "pipelineName": "MyFirstPipeline",
    "pipelineVersion": 1,
    "stageStates": [
        {
            "actionStates": [
                {
                    "actionName": "Source",
                    "currentRevision": {
                        "created": 1446726163.571,
                        "revisionId": "HYGp7zmwbCPPwo234xsCEM7d6ToeAqIl"
                    },
                    "entityUrl": "https://console.aws.amazon.com/s3/home?#",
                    "latestExecution": {
                        "lastStatusChange": 1446137358.328,
                        "status": "Succeeded"
                    }
                }
            ],
            "stageName": "Source"
        },
        {
            "actionStates": [
                {
                    "actionName": "CodePipelineDemoFleet",
                    "currentRevision": {
                        "created": 1466726263.189,
                        "revisionId": "{\"bucket\":\"codepipeline-us-east-1-2770EXAMPLE\",\"key\":\"MyFirstPipeline/MyApp/QI8RTZY.zip\",\"bundleType\":\"zip\",\"version\":null,\"etag\":\"f51889bff5402b0249676e48cEXAMPLE\"}"
                    },
                    "entityUrl": "https://console.aws.amazon.com/codedeploy/home?#/applications/CodePipelineDemoApplication/deployment-groups/CodePipelineDemoFleet",
                    "latestExecution": {
                        "externalExecutionId": "d-EXAMPLE",
                        "externalExecutionUrl": "https://console.aws.amazon.com/codedeploy/home?#/deployments/d-EXAMPLE",
                        "lastStatusChange": 1446137493.131,
                        "status": "Succeeded",
                        "summary": "Deployment Succeeded"
                    }
                }
            ],
            "inboundTransitionState": {
                "enabled": true,
                "lastChangedAt": 1470779534.135,
                "lastChangedBy": "arn:aws:iam::111111111111:user/johndoe"
            },
            "stageName": "Staging"
        }
    ],
    "updated": 1446137312.204
}
```

## See Also
<a name="API_GetPipelineState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codepipeline-2015-07-09/GetPipelineState) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codepipeline-2015-07-09/GetPipelineState) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/GetPipelineState) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codepipeline-2015-07-09/GetPipelineState) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/GetPipelineState) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codepipeline-2015-07-09/GetPipelineState) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codepipeline-2015-07-09/GetPipelineState) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codepipeline-2015-07-09/GetPipelineState) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codepipeline-2015-07-09/GetPipelineState) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/GetPipelineState) 