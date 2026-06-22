---
id: "@specs/aws/batch/docs/API_SubmitJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SubmitJob"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# SubmitJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_SubmitJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SubmitJob
<a name="API_SubmitJob"></a>

Submits an AWS Batch job from a job definition. Parameters that are specified during [SubmitJob](#API_SubmitJob) override parameters defined in the job definition. vCPU and memory requirements that are specified in the `resourceRequirements` objects in the job definition are the exception. They can't be overridden this way using the `memory` and `vcpus` parameters. Rather, you must specify updates to job definition parameters in a `resourceRequirements` object that's included in the `containerOverrides` parameter.

**Note**  
Job queues with a scheduling policy are limited to 500 active share identifiers at a time. 

**Important**  
Jobs that run on Fargate resources can't be guaranteed to run for more than 14 days. This is because, after 14 days, Fargate resources might become unavailable and job might be terminated.

## Request Syntax
<a name="API_SubmitJob_RequestSyntax"></a>

```
POST /v1/submitjob HTTP/1.1
Content-type: application/json

{
   "arrayProperties": { 
      "size": {{number}}
   },
   "consumableResourcePropertiesOverride": { 
      "consumableResourceList": [ 
         { 
            "consumableResource": "{{string}}",
            "quantity": {{number}}
         }
      ]
   },
   "containerOverrides": { 
      "command": [ "{{string}}" ],
      "environment": [ 
         { 
            "name": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "instanceType": "{{string}}",
      "memory": {{number}},
      "resourceRequirements": [ 
         { 
            "type": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "vcpus": {{number}}
   },
   "dependsOn": [ 
      { 
         "jobId": "{{string}}",
         "type": "{{string}}"
      }
   ],
   "ecsPropertiesOverride": { 
      "taskProperties": [ 
         { 
            "containers": [ 
               { 
                  "command": [ "{{string}}" ],
                  "environment": [ 
                     { 
                        "name": "{{string}}",
                        "value": "{{string}}"
                     }
                  ],
                  "name": "{{string}}",
                  "resourceRequirements": [ 
                     { 
                        "type": "{{string}}",
                        "value": "{{string}}"
                     }
                  ]
               }
            ]
         }
      ]
   },
   "eksPropertiesOverride": { 
      "podProperties": { 
         "containers": [ 
            { 
               "args": [ "{{string}}" ],
               "command": [ "{{string}}" ],
               "env": [ 
                  { 
                     "name": "{{string}}",
                     "value": "{{string}}"
                  }
               ],
               "image": "{{string}}",
               "name": "{{string}}",
               "resources": { 
                  "limits": { 
                     "{{string}}" : "{{string}}" 
                  },
                  "requests": { 
                     "{{string}}" : "{{string}}" 
                  }
               }
            }
         ],
         "initContainers": [ 
            { 
               "args": [ "{{string}}" ],
               "command": [ "{{string}}" ],
               "env": [ 
                  { 
                     "name": "{{string}}",
                     "value": "{{string}}"
                  }
               ],
               "image": "{{string}}",
               "name": "{{string}}",
               "resources": { 
                  "limits": { 
                     "{{string}}" : "{{string}}" 
                  },
                  "requests": { 
                     "{{string}}" : "{{string}}" 
                  }
               }
            }
         ],
         "metadata": { 
            "annotations": { 
               "{{string}}" : "{{string}}" 
            },
            "labels": { 
               "{{string}}" : "{{string}}" 
            },
            "namespace": "{{string}}"
         }
      }
   },
   "jobDefinition": "{{string}}",
   "jobName": "{{string}}",
   "jobQueue": "{{string}}",
   "nodeOverrides": { 
      "nodePropertyOverrides": [ 
         { 
            "consumableResourcePropertiesOverride": { 
               "consumableResourceList": [ 
                  { 
                     "consumableResource": "{{string}}",
                     "quantity": {{number}}
                  }
               ]
            },
            "containerOverrides": { 
               "command": [ "{{string}}" ],
               "environment": [ 
                  { 
                     "name": "{{string}}",
                     "value": "{{string}}"
                  }
               ],
               "instanceType": "{{string}}",
               "memory": {{number}},
               "resourceRequirements": [ 
                  { 
                     "type": "{{string}}",
                     "value": "{{string}}"
                  }
               ],
               "vcpus": {{number}}
            },
            "ecsPropertiesOverride": { 
               "taskProperties": [ 
                  { 
                     "containers": [ 
                        { 
                           "command": [ "{{string}}" ],
                           "environment": [ 
                              { 
                                 "name": "{{string}}",
                                 "value": "{{string}}"
                              }
                           ],
                           "name": "{{string}}",
                           "resourceRequirements": [ 
                              { 
                                 "type": "{{string}}",
                                 "value": "{{string}}"
                              }
                           ]
                        }
                     ]
                  }
               ]
            },
            "eksPropertiesOverride": { 
               "podProperties": { 
                  "containers": [ 
                     { 
                        "args": [ "{{string}}" ],
                        "command": [ "{{string}}" ],
                        "env": [ 
                           { 
                              "name": "{{string}}",
                              "value": "{{string}}"
                           }
                        ],
                        "image": "{{string}}",
                        "name": "{{string}}",
                        "resources": { 
                           "limits": { 
                              "{{string}}" : "{{string}}" 
                           },
                           "requests": { 
                              "{{string}}" : "{{string}}" 
                           }
                        }
                     }
                  ],
                  "initContainers": [ 
                     { 
                        "args": [ "{{string}}" ],
                        "command": [ "{{string}}" ],
                        "env": [ 
                           { 
                              "name": "{{string}}",
                              "value": "{{string}}"
                           }
                        ],
                        "image": "{{string}}",
                        "name": "{{string}}",
                        "resources": { 
                           "limits": { 
                              "{{string}}" : "{{string}}" 
                           },
                           "requests": { 
                              "{{string}}" : "{{string}}" 
                           }
                        }
                     }
                  ],
                  "metadata": { 
                     "annotations": { 
                        "{{string}}" : "{{string}}" 
                     },
                     "labels": { 
                        "{{string}}" : "{{string}}" 
                     },
                     "namespace": "{{string}}"
                  }
               }
            },
            "instanceTypes": [ "{{string}}" ],
            "targetNodes": "{{string}}"
         }
      ],
      "numNodes": {{number}}
   },
   "parameters": { 
      "{{string}}" : "{{string}}" 
   },
   "propagateTags": {{boolean}},
   "retryStrategy": { 
      "attempts": {{number}},
      "evaluateOnExit": [ 
         { 
            "action": "{{string}}",
            "onExitCode": "{{string}}",
            "onReason": "{{string}}",
            "onStatusReason": "{{string}}"
         }
      ]
   },
   "schedulingPriorityOverride": {{number}},
   "shareIdentifier": "{{string}}",
   "tags": { 
      "{{string}}" : "{{string}}" 
   },
   "timeout": { 
      "attemptDurationSeconds": {{number}}
   }
}
```

## URI Request Parameters
<a name="API_SubmitJob_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SubmitJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [arrayProperties](#API_SubmitJob_RequestSyntax) **   <a name="Batch-SubmitJob-request-arrayProperties"></a>
The array properties for the submitted job, such as the size of the array. The array size can be between 2 and 10,000. If you specify array properties for a job, it becomes an array job. For more information, see [Array Jobs](https://docs.aws.amazon.com/batch/latest/userguide/array_jobs.html) in the * AWS Batch User Guide*.  
Type: [ArrayProperties](API_ArrayProperties.md) object  
Required: No

 ** [consumableResourcePropertiesOverride](#API_SubmitJob_RequestSyntax) **   <a name="Batch-SubmitJob-request-consumableResourcePropertiesOverride"></a>
An object that contains overrides for the consumable resources of a job.  
Type: [ConsumableResourceProperties](API_ConsumableResourceProperties.md) object  
Required: No

 ** [containerOverrides](#API_SubmitJob_RequestSyntax) **   <a name="Batch-SubmitJob-request-containerOverrides"></a>
An object with properties that override the defaults for the job definition that specify the name of a container in the specified job definition and the overrides it should receive. You can override the default command for a container, which is specified in the job definition or the Docker image, with a `command` override. You can also override existing environment variables on a container or add new environment variables to it with an `environment` override.  
Type: [ContainerOverrides](API_ContainerOverrides.md) object  
Required: No

 ** [dependsOn](#API_SubmitJob_RequestSyntax) **   <a name="Batch-SubmitJob-request-dependsOn"></a>
A list of dependencies for the job. A job can depend upon a maximum of 20 jobs. You can specify a `SEQUENTIAL` type dependency without specifying a job ID for array jobs so that each child array job completes sequentially, starting at index 0. You can also specify an `N_TO_N` type dependency with a job ID for array jobs. In that case, each index child of this job must wait for the corresponding index child of each dependency to complete before it can begin.  
Type: Array of [JobDependency](API_JobDependency.md) objects  
Required: No

 ** [ecsPropertiesOverride](#API_SubmitJob_RequestSyntax) **   <a name="Batch-SubmitJob-request-ecsPropertiesOverride"></a>
An object, with properties that override defaults for the job definition, can only be specified for jobs that are run on Amazon ECS resources.  
Type: [EcsPropertiesOverride](API_EcsPropertiesOverride.md) object  
Required: No

 ** [eksPropertiesOverride](#API_SubmitJob_RequestSyntax) **   <a name="Batch-SubmitJob-request-eksPropertiesOverride"></a>
An object, with properties that override defaults for the job definition, can only be specified for jobs that are run on Amazon EKS resources.  
Type: [EksPropertiesOverride](API_EksPropertiesOverride.md) object  
Required: No

 ** [jobDefinition](#API_SubmitJob_RequestSyntax) **   <a name="Batch-SubmitJob-request-jobDefinition"></a>
The job definition used by this job. This value can be one of `definition-name`, `definition-name:revision`, or the Amazon Resource Name (ARN) for the job definition, with or without the revision (`arn:aws:batch:region:account:job-definition/definition-name:revision `, or `arn:aws:batch:region:account:job-definition/definition-name `).  
If the revision is not specified, then the latest active revision is used.  
Type: String  
Required: Yes

 ** [jobName](#API_SubmitJob_RequestSyntax) **   <a name="Batch-SubmitJob-request-jobName"></a>
The name of the job. It can be up to 128 letters long. The first character must be alphanumeric, can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (\_).  
Type: String  
Required: Yes

 ** [jobQueue](#API_SubmitJob_RequestSyntax) **   <a name="Batch-SubmitJob-request-jobQueue"></a>
The job queue where the job is submitted. You can specify either the name or the Amazon Resource Name (ARN) of the queue.  
Type: String  
Required: Yes

 ** [nodeOverrides](#API_SubmitJob_RequestSyntax) **   <a name="Batch-SubmitJob-request-nodeOverrides"></a>
A list of node overrides in JSON format that specify the node range to target and the container overrides for that node range.  
This parameter isn't applicable to jobs that are running on Fargate resources; use `containerOverrides` instead.
Type: [NodeOverrides](API_NodeOverrides.md) object  
Required: No

 ** [parameters](#API_SubmitJob_RequestSyntax) **   <a name="Batch-SubmitJob-request-parameters"></a>
Additional parameters passed to the job that replace parameter substitution placeholders that are set in the job definition. Parameters are specified as a key and value pair mapping. Parameters in a `SubmitJob` request override any corresponding parameter defaults from the job definition.  
Type: String to string map  
Required: No

 ** [propagateTags](#API_SubmitJob_RequestSyntax) **   <a name="Batch-SubmitJob-request-propagateTags"></a>
Specifies whether to propagate the tags from the job or job definition to the corresponding Amazon ECS task. If no value is specified, the tags aren't propagated. Tags can only be propagated to the tasks during task creation. For tags with the same name, job tags are given priority over job definitions tags. If the total number of combined tags from the job and job definition is over 50, the job is moved to the `FAILED` state. When specified, this overrides the tag propagation setting in the job definition.  
Type: Boolean  
Required: No

 ** [retryStrategy](#API_SubmitJob_RequestSyntax) **   <a name="Batch-SubmitJob-request-retryStrategy"></a>
The retry strategy to use for failed jobs from this [SubmitJob](#API_SubmitJob) operation. When a retry strategy is specified here, it overrides the retry strategy defined in the job definition.  
Type: [RetryStrategy](API_RetryStrategy.md) object  
Required: No

 ** [schedulingPriorityOverride](#API_SubmitJob_RequestSyntax) **   <a name="Batch-SubmitJob-request-schedulingPriorityOverride"></a>
The scheduling priority for the job. This only affects jobs in job queues with a fair-share policy. Jobs with a higher scheduling priority are scheduled before jobs with a lower scheduling priority. This overrides any scheduling priority in the job definition and works only within a single share identifier.  
The minimum supported value is 0 and the maximum supported value is 9999.  
Type: Integer  
Required: No

 ** [shareIdentifier](#API_SubmitJob_RequestSyntax) **   <a name="Batch-SubmitJob-request-shareIdentifier"></a>
The share identifier for the job. Don't specify this parameter if the job queue doesn't have a fair-share scheduling policy. If the job queue has a fair-share scheduling policy, then this parameter must be specified.  
This string is limited to 255 alphanumeric characters, and can be followed by an asterisk (\*).  
Type: String  
Required: No

 ** [tags](#API_SubmitJob_RequestSyntax) **   <a name="Batch-SubmitJob-request-tags"></a>
The tags that you apply to the job request to help you categorize and organize your resources. Each tag consists of a key and an optional value. For more information, see [Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in * AWS General Reference*.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Maximum length of 256.  
Required: No

 ** [timeout](#API_SubmitJob_RequestSyntax) **   <a name="Batch-SubmitJob-request-timeout"></a>
The timeout configuration for this [SubmitJob](#API_SubmitJob) operation. You can specify a timeout duration after which AWS Batch terminates your jobs if they haven't finished. If a job is terminated due to a timeout, it isn't retried. The minimum value for the timeout is 60 seconds. This configuration overrides any timeout configuration specified in the job definition. For array jobs, child jobs have the same timeout configuration as the parent job. For more information, see [Job Timeouts](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/job_timeouts.html) in the *Amazon Elastic Container Service Developer Guide*.  
Type: [JobTimeout](API_JobTimeout.md) object  
Required: No

## Response Syntax
<a name="API_SubmitJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "jobArn": "string",
   "jobId": "string",
   "jobName": "string"
}
```

## Response Elements
<a name="API_SubmitJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobArn](#API_SubmitJob_ResponseSyntax) **   <a name="Batch-SubmitJob-response-jobArn"></a>
The Amazon Resource Name (ARN) for the job.  
Type: String

 ** [jobId](#API_SubmitJob_ResponseSyntax) **   <a name="Batch-SubmitJob-response-jobId"></a>
The unique identifier for the job.  
Type: String

 ** [jobName](#API_SubmitJob_ResponseSyntax) **   <a name="Batch-SubmitJob-response-jobName"></a>
The name of the job.  
Type: String

## Errors
<a name="API_SubmitJob_Errors"></a>

 ** ClientException **   
These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.  
HTTP Status Code: 400

 ** ServerException **   
These errors are usually caused by a server issue.  
HTTP Status Code: 500

## Examples
<a name="API_SubmitJob_Examples"></a>

In the following example or examples, the Authorization header contents (` [authorization-params] `) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_SubmitJob_Example_1"></a>

This example submits a simple container job called `example` to the `HighPriority` job queue.

#### Sample Request
<a name="API_SubmitJob_Example_1_Request"></a>

```
POST /v1/submitjob HTTP/1.1
Host: batch.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: [content-length]
Authorization: [authorization-params]
X-Amz-Date: 20161129T201034Z
User-Agent: aws-cli/1.11.22 Python/2.7.12 Darwin/16.1.0 botocore/1.4.79

{
  "jobName": "example",
  "jobQueue": "HighPriority",
  "jobDefinition": "sleep60"
}
```

#### Sample Response
<a name="API_SubmitJob_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: [content-length]
Connection: keep-alive
Date: Tue, 29 Nov 2016 20:10:34 GMT
x-amzn-RequestId: [request-id]
X-Amzn-Trace-Id: [trace-id]
X-Cache: Miss from cloudfront
Via: 1.1 6ba12aeff47e3e7677e084594bfce5e1.cloudfront.net (CloudFront)
X-Amz-Cf-Id: QoWCvISTvYBbaP2hAoxC8_TWTl2JN-kNASYCjCJ5HztN0e1OuzvpSA==

{
  "jobName": "example",
  "jobId": "876da822-4198-45f2-a252-6cea32512ea8"
}
```

## See Also
<a name="API_SubmitJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/batch-2016-08-10/SubmitJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/batch-2016-08-10/SubmitJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/SubmitJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/batch-2016-08-10/SubmitJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/SubmitJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/batch-2016-08-10/SubmitJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/batch-2016-08-10/SubmitJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/batch-2016-08-10/SubmitJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/SubmitJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/SubmitJob) 