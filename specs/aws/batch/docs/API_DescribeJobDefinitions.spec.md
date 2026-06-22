---
id: "@specs/aws/batch/docs/API_DescribeJobDefinitions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeJobDefinitions"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# DescribeJobDefinitions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_DescribeJobDefinitions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeJobDefinitions
<a name="API_DescribeJobDefinitions"></a>

Describes a list of job definitions. You can specify a `status` (such as `ACTIVE`) to only return job definitions that match that status.

## Request Syntax
<a name="API_DescribeJobDefinitions_RequestSyntax"></a>

```
POST /v1/describejobdefinitions HTTP/1.1
Content-type: application/json

{
   "jobDefinitionName": "{{string}}",
   "jobDefinitions": [ "{{string}}" ],
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "status": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DescribeJobDefinitions_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeJobDefinitions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [jobDefinitionName](#API_DescribeJobDefinitions_RequestSyntax) **   <a name="Batch-DescribeJobDefinitions-request-jobDefinitionName"></a>
The name of the job definition to describe.  
Type: String  
Required: No

 ** [jobDefinitions](#API_DescribeJobDefinitions_RequestSyntax) **   <a name="Batch-DescribeJobDefinitions-request-jobDefinitions"></a>
A list of up to 100 job definitions. Each entry in the list can either be an ARN in the format `arn:aws:batch:${Region}:${Account}:job-definition/${JobDefinitionName}:${Revision}` or a short version using the form `${JobDefinitionName}:${Revision}`. This parameter can't be used with other parameters.  
Type: Array of strings  
Required: No

 ** [maxResults](#API_DescribeJobDefinitions_RequestSyntax) **   <a name="Batch-DescribeJobDefinitions-request-maxResults"></a>
The maximum number of results returned by `DescribeJobDefinitions` in paginated output. When this parameter is used, `DescribeJobDefinitions` only returns `maxResults` results in a single page and a `nextToken` response element. The remaining results of the initial request can be seen by sending another `DescribeJobDefinitions` request with the returned `nextToken` value. This value can be between 1 and 100. If this parameter isn't used, then `DescribeJobDefinitions` returns up to 100 results and a `nextToken` value if applicable.  
Type: Integer  
Required: No

 ** [nextToken](#API_DescribeJobDefinitions_RequestSyntax) **   <a name="Batch-DescribeJobDefinitions-request-nextToken"></a>
The `nextToken` value returned from a previous paginated `DescribeJobDefinitions` request where `maxResults` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the `nextToken` value. This value is `null` when there are no more results to return.  
Treat this token as an opaque identifier that's only used to retrieve the next items in a list and not for other programmatic purposes.
Type: String  
Required: No

 ** [status](#API_DescribeJobDefinitions_RequestSyntax) **   <a name="Batch-DescribeJobDefinitions-request-status"></a>
The status used to filter job definitions.  
Type: String  
Required: No

## Response Syntax
<a name="API_DescribeJobDefinitions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "jobDefinitions": [ 
      { 
         "consumableResourceProperties": { 
            "consumableResourceList": [ 
               { 
                  "consumableResource": "string",
                  "quantity": number
               }
            ]
         },
         "containerOrchestrationType": "string",
         "containerProperties": { 
            "command": [ "string" ],
            "enableExecuteCommand": boolean,
            "environment": [ 
               { 
                  "name": "string",
                  "value": "string"
               }
            ],
            "ephemeralStorage": { 
               "sizeInGiB": number
            },
            "executionRoleArn": "string",
            "fargatePlatformConfiguration": { 
               "platformVersion": "string"
            },
            "image": "string",
            "instanceType": "string",
            "jobRoleArn": "string",
            "linuxParameters": { 
               "devices": [ 
                  { 
                     "containerPath": "string",
                     "hostPath": "string",
                     "permissions": [ "string" ]
                  }
               ],
               "initProcessEnabled": boolean,
               "maxSwap": number,
               "sharedMemorySize": number,
               "swappiness": number,
               "tmpfs": [ 
                  { 
                     "containerPath": "string",
                     "mountOptions": [ "string" ],
                     "size": number
                  }
               ]
            },
            "logConfiguration": { 
               "logDriver": "string",
               "options": { 
                  "string" : "string" 
               },
               "secretOptions": [ 
                  { 
                     "name": "string",
                     "valueFrom": "string"
                  }
               ]
            },
            "memory": number,
            "mountPoints": [ 
               { 
                  "containerPath": "string",
                  "readOnly": boolean,
                  "sourceVolume": "string"
               }
            ],
            "networkConfiguration": { 
               "assignPublicIp": "string"
            },
            "privileged": boolean,
            "readonlyRootFilesystem": boolean,
            "repositoryCredentials": { 
               "credentialsParameter": "string"
            },
            "resourceRequirements": [ 
               { 
                  "type": "string",
                  "value": "string"
               }
            ],
            "runtimePlatform": { 
               "cpuArchitecture": "string",
               "operatingSystemFamily": "string"
            },
            "secrets": [ 
               { 
                  "name": "string",
                  "valueFrom": "string"
               }
            ],
            "ulimits": [ 
               { 
                  "hardLimit": number,
                  "name": "string",
                  "softLimit": number
               }
            ],
            "user": "string",
            "vcpus": number,
            "volumes": [ 
               { 
                  "efsVolumeConfiguration": { 
                     "authorizationConfig": { 
                        "accessPointId": "string",
                        "iam": "string"
                     },
                     "fileSystemId": "string",
                     "rootDirectory": "string",
                     "transitEncryption": "string",
                     "transitEncryptionPort": number
                  },
                  "host": { 
                     "sourcePath": "string"
                  },
                  "name": "string",
                  "s3filesVolumeConfiguration": { 
                     "accessPointArn": "string",
                     "fileSystemArn": "string",
                     "rootDirectory": "string",
                     "transitEncryptionPort": number
                  }
               }
            ]
         },
         "ecsProperties": { 
            "taskProperties": [ 
               { 
                  "containers": [ 
                     { 
                        "command": [ "string" ],
                        "dependsOn": [ 
                           { 
                              "condition": "string",
                              "containerName": "string"
                           }
                        ],
                        "environment": [ 
                           { 
                              "name": "string",
                              "value": "string"
                           }
                        ],
                        "essential": boolean,
                        "firelensConfiguration": { 
                           "options": { 
                              "string" : "string" 
                           },
                           "type": "string"
                        },
                        "image": "string",
                        "linuxParameters": { 
                           "devices": [ 
                              { 
                                 "containerPath": "string",
                                 "hostPath": "string",
                                 "permissions": [ "string" ]
                              }
                           ],
                           "initProcessEnabled": boolean,
                           "maxSwap": number,
                           "sharedMemorySize": number,
                           "swappiness": number,
                           "tmpfs": [ 
                              { 
                                 "containerPath": "string",
                                 "mountOptions": [ "string" ],
                                 "size": number
                              }
                           ]
                        },
                        "logConfiguration": { 
                           "logDriver": "string",
                           "options": { 
                              "string" : "string" 
                           },
                           "secretOptions": [ 
                              { 
                                 "name": "string",
                                 "valueFrom": "string"
                              }
                           ]
                        },
                        "mountPoints": [ 
                           { 
                              "containerPath": "string",
                              "readOnly": boolean,
                              "sourceVolume": "string"
                           }
                        ],
                        "name": "string",
                        "privileged": boolean,
                        "readonlyRootFilesystem": boolean,
                        "repositoryCredentials": { 
                           "credentialsParameter": "string"
                        },
                        "resourceRequirements": [ 
                           { 
                              "type": "string",
                              "value": "string"
                           }
                        ],
                        "secrets": [ 
                           { 
                              "name": "string",
                              "valueFrom": "string"
                           }
                        ],
                        "startTimeout": number,
                        "stopTimeout": number,
                        "ulimits": [ 
                           { 
                              "hardLimit": number,
                              "name": "string",
                              "softLimit": number
                           }
                        ],
                        "user": "string"
                     }
                  ],
                  "enableExecuteCommand": boolean,
                  "ephemeralStorage": { 
                     "sizeInGiB": number
                  },
                  "executionRoleArn": "string",
                  "ipcMode": "string",
                  "networkConfiguration": { 
                     "assignPublicIp": "string"
                  },
                  "pidMode": "string",
                  "platformVersion": "string",
                  "runtimePlatform": { 
                     "cpuArchitecture": "string",
                     "operatingSystemFamily": "string"
                  },
                  "taskRoleArn": "string",
                  "volumes": [ 
                     { 
                        "efsVolumeConfiguration": { 
                           "authorizationConfig": { 
                              "accessPointId": "string",
                              "iam": "string"
                           },
                           "fileSystemId": "string",
                           "rootDirectory": "string",
                           "transitEncryption": "string",
                           "transitEncryptionPort": number
                        },
                        "host": { 
                           "sourcePath": "string"
                        },
                        "name": "string",
                        "s3filesVolumeConfiguration": { 
                           "accessPointArn": "string",
                           "fileSystemArn": "string",
                           "rootDirectory": "string",
                           "transitEncryptionPort": number
                        }
                     }
                  ]
               }
            ]
         },
         "eksProperties": { 
            "podProperties": { 
               "containers": [ 
                  { 
                     "args": [ "string" ],
                     "command": [ "string" ],
                     "env": [ 
                        { 
                           "name": "string",
                           "value": "string"
                        }
                     ],
                     "image": "string",
                     "imagePullPolicy": "string",
                     "name": "string",
                     "resources": { 
                        "limits": { 
                           "string" : "string" 
                        },
                        "requests": { 
                           "string" : "string" 
                        }
                     },
                     "securityContext": { 
                        "allowPrivilegeEscalation": boolean,
                        "privileged": boolean,
                        "readOnlyRootFilesystem": boolean,
                        "runAsGroup": number,
                        "runAsNonRoot": boolean,
                        "runAsUser": number
                     },
                     "volumeMounts": [ 
                        { 
                           "mountPath": "string",
                           "name": "string",
                           "readOnly": boolean,
                           "subPath": "string"
                        }
                     ]
                  }
               ],
               "dnsPolicy": "string",
               "hostNetwork": boolean,
               "imagePullSecrets": [ 
                  { 
                     "name": "string"
                  }
               ],
               "initContainers": [ 
                  { 
                     "args": [ "string" ],
                     "command": [ "string" ],
                     "env": [ 
                        { 
                           "name": "string",
                           "value": "string"
                        }
                     ],
                     "image": "string",
                     "imagePullPolicy": "string",
                     "name": "string",
                     "resources": { 
                        "limits": { 
                           "string" : "string" 
                        },
                        "requests": { 
                           "string" : "string" 
                        }
                     },
                     "securityContext": { 
                        "allowPrivilegeEscalation": boolean,
                        "privileged": boolean,
                        "readOnlyRootFilesystem": boolean,
                        "runAsGroup": number,
                        "runAsNonRoot": boolean,
                        "runAsUser": number
                     },
                     "volumeMounts": [ 
                        { 
                           "mountPath": "string",
                           "name": "string",
                           "readOnly": boolean,
                           "subPath": "string"
                        }
                     ]
                  }
               ],
               "metadata": { 
                  "annotations": { 
                     "string" : "string" 
                  },
                  "labels": { 
                     "string" : "string" 
                  },
                  "namespace": "string"
               },
               "serviceAccountName": "string",
               "shareProcessNamespace": boolean,
               "volumes": [ 
                  { 
                     "emptyDir": { 
                        "medium": "string",
                        "sizeLimit": "string"
                     },
                     "hostPath": { 
                        "path": "string"
                     },
                     "name": "string",
                     "persistentVolumeClaim": { 
                        "claimName": "string",
                        "readOnly": boolean
                     },
                     "secret": { 
                        "optional": boolean,
                        "secretName": "string"
                     }
                  }
               ]
            }
         },
         "jobDefinitionArn": "string",
         "jobDefinitionName": "string",
         "nodeProperties": { 
            "mainNode": number,
            "nodeRangeProperties": [ 
               { 
                  "consumableResourceProperties": { 
                     "consumableResourceList": [ 
                        { 
                           "consumableResource": "string",
                           "quantity": number
                        }
                     ]
                  },
                  "container": { 
                     "command": [ "string" ],
                     "enableExecuteCommand": boolean,
                     "environment": [ 
                        { 
                           "name": "string",
                           "value": "string"
                        }
                     ],
                     "ephemeralStorage": { 
                        "sizeInGiB": number
                     },
                     "executionRoleArn": "string",
                     "fargatePlatformConfiguration": { 
                        "platformVersion": "string"
                     },
                     "image": "string",
                     "instanceType": "string",
                     "jobRoleArn": "string",
                     "linuxParameters": { 
                        "devices": [ 
                           { 
                              "containerPath": "string",
                              "hostPath": "string",
                              "permissions": [ "string" ]
                           }
                        ],
                        "initProcessEnabled": boolean,
                        "maxSwap": number,
                        "sharedMemorySize": number,
                        "swappiness": number,
                        "tmpfs": [ 
                           { 
                              "containerPath": "string",
                              "mountOptions": [ "string" ],
                              "size": number
                           }
                        ]
                     },
                     "logConfiguration": { 
                        "logDriver": "string",
                        "options": { 
                           "string" : "string" 
                        },
                        "secretOptions": [ 
                           { 
                              "name": "string",
                              "valueFrom": "string"
                           }
                        ]
                     },
                     "memory": number,
                     "mountPoints": [ 
                        { 
                           "containerPath": "string",
                           "readOnly": boolean,
                           "sourceVolume": "string"
                        }
                     ],
                     "networkConfiguration": { 
                        "assignPublicIp": "string"
                     },
                     "privileged": boolean,
                     "readonlyRootFilesystem": boolean,
                     "repositoryCredentials": { 
                        "credentialsParameter": "string"
                     },
                     "resourceRequirements": [ 
                        { 
                           "type": "string",
                           "value": "string"
                        }
                     ],
                     "runtimePlatform": { 
                        "cpuArchitecture": "string",
                        "operatingSystemFamily": "string"
                     },
                     "secrets": [ 
                        { 
                           "name": "string",
                           "valueFrom": "string"
                        }
                     ],
                     "ulimits": [ 
                        { 
                           "hardLimit": number,
                           "name": "string",
                           "softLimit": number
                        }
                     ],
                     "user": "string",
                     "vcpus": number,
                     "volumes": [ 
                        { 
                           "efsVolumeConfiguration": { 
                              "authorizationConfig": { 
                                 "accessPointId": "string",
                                 "iam": "string"
                              },
                              "fileSystemId": "string",
                              "rootDirectory": "string",
                              "transitEncryption": "string",
                              "transitEncryptionPort": number
                           },
                           "host": { 
                              "sourcePath": "string"
                           },
                           "name": "string",
                           "s3filesVolumeConfiguration": { 
                              "accessPointArn": "string",
                              "fileSystemArn": "string",
                              "rootDirectory": "string",
                              "transitEncryptionPort": number
                           }
                        }
                     ]
                  },
                  "ecsProperties": { 
                     "taskProperties": [ 
                        { 
                           "containers": [ 
                              { 
                                 "command": [ "string" ],
                                 "dependsOn": [ 
                                    { 
                                       "condition": "string",
                                       "containerName": "string"
                                    }
                                 ],
                                 "environment": [ 
                                    { 
                                       "name": "string",
                                       "value": "string"
                                    }
                                 ],
                                 "essential": boolean,
                                 "firelensConfiguration": { 
                                    "options": { 
                                       "string" : "string" 
                                    },
                                    "type": "string"
                                 },
                                 "image": "string",
                                 "linuxParameters": { 
                                    "devices": [ 
                                       { 
                                          "containerPath": "string",
                                          "hostPath": "string",
                                          "permissions": [ "string" ]
                                       }
                                    ],
                                    "initProcessEnabled": boolean,
                                    "maxSwap": number,
                                    "sharedMemorySize": number,
                                    "swappiness": number,
                                    "tmpfs": [ 
                                       { 
                                          "containerPath": "string",
                                          "mountOptions": [ "string" ],
                                          "size": number
                                       }
                                    ]
                                 },
                                 "logConfiguration": { 
                                    "logDriver": "string",
                                    "options": { 
                                       "string" : "string" 
                                    },
                                    "secretOptions": [ 
                                       { 
                                          "name": "string",
                                          "valueFrom": "string"
                                       }
                                    ]
                                 },
                                 "mountPoints": [ 
                                    { 
                                       "containerPath": "string",
                                       "readOnly": boolean,
                                       "sourceVolume": "string"
                                    }
                                 ],
                                 "name": "string",
                                 "privileged": boolean,
                                 "readonlyRootFilesystem": boolean,
                                 "repositoryCredentials": { 
                                    "credentialsParameter": "string"
                                 },
                                 "resourceRequirements": [ 
                                    { 
                                       "type": "string",
                                       "value": "string"
                                    }
                                 ],
                                 "secrets": [ 
                                    { 
                                       "name": "string",
                                       "valueFrom": "string"
                                    }
                                 ],
                                 "startTimeout": number,
                                 "stopTimeout": number,
                                 "ulimits": [ 
                                    { 
                                       "hardLimit": number,
                                       "name": "string",
                                       "softLimit": number
                                    }
                                 ],
                                 "user": "string"
                              }
                           ],
                           "enableExecuteCommand": boolean,
                           "ephemeralStorage": { 
                              "sizeInGiB": number
                           },
                           "executionRoleArn": "string",
                           "ipcMode": "string",
                           "networkConfiguration": { 
                              "assignPublicIp": "string"
                           },
                           "pidMode": "string",
                           "platformVersion": "string",
                           "runtimePlatform": { 
                              "cpuArchitecture": "string",
                              "operatingSystemFamily": "string"
                           },
                           "taskRoleArn": "string",
                           "volumes": [ 
                              { 
                                 "efsVolumeConfiguration": { 
                                    "authorizationConfig": { 
                                       "accessPointId": "string",
                                       "iam": "string"
                                    },
                                    "fileSystemId": "string",
                                    "rootDirectory": "string",
                                    "transitEncryption": "string",
                                    "transitEncryptionPort": number
                                 },
                                 "host": { 
                                    "sourcePath": "string"
                                 },
                                 "name": "string",
                                 "s3filesVolumeConfiguration": { 
                                    "accessPointArn": "string",
                                    "fileSystemArn": "string",
                                    "rootDirectory": "string",
                                    "transitEncryptionPort": number
                                 }
                              }
                           ]
                        }
                     ]
                  },
                  "eksProperties": { 
                     "podProperties": { 
                        "containers": [ 
                           { 
                              "args": [ "string" ],
                              "command": [ "string" ],
                              "env": [ 
                                 { 
                                    "name": "string",
                                    "value": "string"
                                 }
                              ],
                              "image": "string",
                              "imagePullPolicy": "string",
                              "name": "string",
                              "resources": { 
                                 "limits": { 
                                    "string" : "string" 
                                 },
                                 "requests": { 
                                    "string" : "string" 
                                 }
                              },
                              "securityContext": { 
                                 "allowPrivilegeEscalation": boolean,
                                 "privileged": boolean,
                                 "readOnlyRootFilesystem": boolean,
                                 "runAsGroup": number,
                                 "runAsNonRoot": boolean,
                                 "runAsUser": number
                              },
                              "volumeMounts": [ 
                                 { 
                                    "mountPath": "string",
                                    "name": "string",
                                    "readOnly": boolean,
                                    "subPath": "string"
                                 }
                              ]
                           }
                        ],
                        "dnsPolicy": "string",
                        "hostNetwork": boolean,
                        "imagePullSecrets": [ 
                           { 
                              "name": "string"
                           }
                        ],
                        "initContainers": [ 
                           { 
                              "args": [ "string" ],
                              "command": [ "string" ],
                              "env": [ 
                                 { 
                                    "name": "string",
                                    "value": "string"
                                 }
                              ],
                              "image": "string",
                              "imagePullPolicy": "string",
                              "name": "string",
                              "resources": { 
                                 "limits": { 
                                    "string" : "string" 
                                 },
                                 "requests": { 
                                    "string" : "string" 
                                 }
                              },
                              "securityContext": { 
                                 "allowPrivilegeEscalation": boolean,
                                 "privileged": boolean,
                                 "readOnlyRootFilesystem": boolean,
                                 "runAsGroup": number,
                                 "runAsNonRoot": boolean,
                                 "runAsUser": number
                              },
                              "volumeMounts": [ 
                                 { 
                                    "mountPath": "string",
                                    "name": "string",
                                    "readOnly": boolean,
                                    "subPath": "string"
                                 }
                              ]
                           }
                        ],
                        "metadata": { 
                           "annotations": { 
                              "string" : "string" 
                           },
                           "labels": { 
                              "string" : "string" 
                           },
                           "namespace": "string"
                        },
                        "serviceAccountName": "string",
                        "shareProcessNamespace": boolean,
                        "volumes": [ 
                           { 
                              "emptyDir": { 
                                 "medium": "string",
                                 "sizeLimit": "string"
                              },
                              "hostPath": { 
                                 "path": "string"
                              },
                              "name": "string",
                              "persistentVolumeClaim": { 
                                 "claimName": "string",
                                 "readOnly": boolean
                              },
                              "secret": { 
                                 "optional": boolean,
                                 "secretName": "string"
                              }
                           }
                        ]
                     }
                  },
                  "instanceTypes": [ "string" ],
                  "targetNodes": "string"
               }
            ],
            "numNodes": number
         },
         "parameters": { 
            "string" : "string" 
         },
         "platformCapabilities": [ "string" ],
         "propagateTags": boolean,
         "retryStrategy": { 
            "attempts": number,
            "evaluateOnExit": [ 
               { 
                  "action": "string",
                  "onExitCode": "string",
                  "onReason": "string",
                  "onStatusReason": "string"
               }
            ]
         },
         "revision": number,
         "schedulingPriority": number,
         "status": "string",
         "tags": { 
            "string" : "string" 
         },
         "timeout": { 
            "attemptDurationSeconds": number
         },
         "type": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeJobDefinitions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobDefinitions](#API_DescribeJobDefinitions_ResponseSyntax) **   <a name="Batch-DescribeJobDefinitions-response-jobDefinitions"></a>
The list of job definitions.  
Type: Array of [JobDefinition](API_JobDefinition.md) objects

 ** [nextToken](#API_DescribeJobDefinitions_ResponseSyntax) **   <a name="Batch-DescribeJobDefinitions-response-nextToken"></a>
The `nextToken` value to include in a future `DescribeJobDefinitions` request. When the results of a `DescribeJobDefinitions` request exceed `maxResults`, this value can be used to retrieve the next page of results. This value is `null` when there are no more results to return.  
Type: String

## Errors
<a name="API_DescribeJobDefinitions_Errors"></a>

 ** ClientException **   
These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.  
HTTP Status Code: 400

 ** ServerException **   
These errors are usually caused by a server issue.  
HTTP Status Code: 500

## Examples
<a name="API_DescribeJobDefinitions_Examples"></a>

In the following example or examples, the Authorization header contents (` [authorization-params] `) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_DescribeJobDefinitions_Example_1"></a>

This example describes all of your active job definitions.

#### Sample Request
<a name="API_DescribeJobDefinitions_Example_1_Request"></a>

```
POST /v1/describejobdefinitions HTTP/1.1
Host: batch.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: [content-length]
Authorization: [authorization-params]
X-Amz-Date: 20161128T221855Z
User-Agent: aws-cli/1.11.21 Python/2.7.12 Darwin/16.1.0 botocore/1.4.78

{
  "status": "ACTIVE"
}
```

#### Sample Response
<a name="API_DescribeJobDefinitions_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: [content-length]
Connection: keep-alive
Date: Mon, 28 Nov 2016 22:18:55 GMT
x-amzn-RequestId: [request-id]
X-Amzn-Trace-Id: [trace-id]
X-Cache: Miss from cloudfront
Via: 1.1 688936cc730f240888e6a59a81892a3d.cloudfront.net (CloudFront)
X-Amz-Cf-Id: hd-CAMqfaCJt-1oH7tBu9j5c-IhLQuMjFHFPck6F0MMt5CBea8mQBQ==

{
  "jobDefinitions": [{
    "jobDefinitionName": "sleep60",
    "jobDefinitionArn": "arn:aws:batch:us-east-1:123456789012:job-definition/sleep60:1",
    "revision": 1,
    "status": "ACTIVE",
    "type": "container",
    "containerProperties": {
      "image": "busybox",
      "vcpus": 1,
      "memory": 128,
      "command": ["sleep", "60"],
      "volumes": [],
      "environment": [],
      "mountPoints": [],
      "ulimits": []
    }
  }]
}
```

## See Also
<a name="API_DescribeJobDefinitions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/batch-2016-08-10/DescribeJobDefinitions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/batch-2016-08-10/DescribeJobDefinitions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/DescribeJobDefinitions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/batch-2016-08-10/DescribeJobDefinitions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/DescribeJobDefinitions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/batch-2016-08-10/DescribeJobDefinitions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/batch-2016-08-10/DescribeJobDefinitions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/batch-2016-08-10/DescribeJobDefinitions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/DescribeJobDefinitions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/DescribeJobDefinitions) 