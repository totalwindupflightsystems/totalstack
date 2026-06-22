---
id: "@specs/aws/batch/docs/API_DescribeJobs"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeJobs"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# DescribeJobs

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_DescribeJobs
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeJobs
<a name="API_DescribeJobs"></a>

Describes a list of AWS Batch jobs.

## Request Syntax
<a name="API_DescribeJobs_RequestSyntax"></a>

```
POST /v1/describejobs HTTP/1.1
Content-type: application/json

{
   "jobs": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_DescribeJobs_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeJobs_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [jobs](#API_DescribeJobs_RequestSyntax) **   <a name="Batch-DescribeJobs-request-jobs"></a>
A list of up to 100 job IDs.  
Type: Array of strings  
Required: Yes

## Response Syntax
<a name="API_DescribeJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "jobs": [ 
      { 
         "arrayProperties": { 
            "index": number,
            "size": number,
            "statusSummary": { 
               "string" : number 
            },
            "statusSummaryLastUpdatedAt": number
         },
         "attempts": [ 
            { 
               "container": { 
                  "containerInstanceArn": "string",
                  "exitCode": number,
                  "logStreamName": "string",
                  "networkInterfaces": [ 
                     { 
                        "attachmentId": "string",
                        "ipv6Address": "string",
                        "privateIpv4Address": "string"
                     }
                  ],
                  "reason": "string",
                  "taskArn": "string"
               },
               "startedAt": number,
               "statusReason": "string",
               "stoppedAt": number,
               "taskProperties": [ 
                  { 
                     "containerInstanceArn": "string",
                     "containers": [ 
                        { 
                           "exitCode": number,
                           "logStreamName": "string",
                           "name": "string",
                           "networkInterfaces": [ 
                              { 
                                 "attachmentId": "string",
                                 "ipv6Address": "string",
                                 "privateIpv4Address": "string"
                              }
                           ],
                           "reason": "string"
                        }
                     ],
                     "taskArn": "string"
                  }
               ]
            }
         ],
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
            "containerInstanceArn": "string",
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
            "exitCode": number,
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
            "logStreamName": "string",
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
            "networkInterfaces": [ 
               { 
                  "attachmentId": "string",
                  "ipv6Address": "string",
                  "privateIpv4Address": "string"
               }
            ],
            "privileged": boolean,
            "readonlyRootFilesystem": boolean,
            "reason": "string",
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
            "taskArn": "string",
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
         "createdAt": number,
         "dependsOn": [ 
            { 
               "jobId": "string",
               "type": "string"
            }
         ],
         "ecsProperties": { 
            "taskProperties": [ 
               { 
                  "containerInstanceArn": "string",
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
                        "exitCode": number,
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
                        "logStreamName": "string",
                        "mountPoints": [ 
                           { 
                              "containerPath": "string",
                              "readOnly": boolean,
                              "sourceVolume": "string"
                           }
                        ],
                        "name": "string",
                        "networkInterfaces": [ 
                           { 
                              "attachmentId": "string",
                              "ipv6Address": "string",
                              "privateIpv4Address": "string"
                           }
                        ],
                        "privileged": boolean,
                        "readonlyRootFilesystem": boolean,
                        "reason": "string",
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
                  "taskArn": "string",
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
         "eksAttempts": [ 
            { 
               "containers": [ 
                  { 
                     "containerID": "string",
                     "exitCode": number,
                     "name": "string",
                     "reason": "string"
                  }
               ],
               "eksClusterArn": "string",
               "initContainers": [ 
                  { 
                     "containerID": "string",
                     "exitCode": number,
                     "name": "string",
                     "reason": "string"
                  }
               ],
               "nodeName": "string",
               "podName": "string",
               "podNamespace": "string",
               "startedAt": number,
               "statusReason": "string",
               "stoppedAt": number
            }
         ],
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
                     "exitCode": number,
                     "image": "string",
                     "imagePullPolicy": "string",
                     "name": "string",
                     "reason": "string",
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
                     "exitCode": number,
                     "image": "string",
                     "imagePullPolicy": "string",
                     "name": "string",
                     "reason": "string",
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
               "nodeName": "string",
               "podName": "string",
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
         "isCancelled": boolean,
         "isTerminated": boolean,
         "jobArn": "string",
         "jobDefinition": "string",
         "jobId": "string",
         "jobName": "string",
         "jobQueue": "string",
         "nodeDetails": { 
            "isMainNode": boolean,
            "nodeIndex": number
         },
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
         "schedulingPriority": number,
         "shareIdentifier": "string",
         "startedAt": number,
         "status": "string",
         "statusReason": "string",
         "stoppedAt": number,
         "tags": { 
            "string" : "string" 
         },
         "timeout": { 
            "attemptDurationSeconds": number
         }
      }
   ]
}
```

## Response Elements
<a name="API_DescribeJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobs](#API_DescribeJobs_ResponseSyntax) **   <a name="Batch-DescribeJobs-response-jobs"></a>
The list of jobs.  
Type: Array of [JobDetail](API_JobDetail.md) objects

## Errors
<a name="API_DescribeJobs_Errors"></a>

 ** ClientException **   
These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.  
HTTP Status Code: 400

 ** ServerException **   
These errors are usually caused by a server issue.  
HTTP Status Code: 500

## Examples
<a name="API_DescribeJobs_Examples"></a>

In the following example or examples, the Authorization header contents (` [authorization-params] `) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_DescribeJobs_Example_1"></a>

This example describes a job with the specified job ID.

#### Sample Request
<a name="API_DescribeJobs_Example_1_Request"></a>

```
POST /v1/describejobs HTTP/1.1
Host: batch.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: [content-length]
Authorization: [authorization-params]
X-Amz-Date: 20170327T151323Z
User-Agent: aws-cli/1.11.22 Python/2.7.12 Darwin/16.1.0 botocore/1.4.79

{
  "jobs": [
    "0668da57-1bcc-478b-bc14-5d4f1c1cef48"
  ]
}
```

#### Sample Response
<a name="API_DescribeJobs_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Mon, 27 Mar 2017 15:13:13 GMT
Content-Type: application/json
Content-Length: [content-length]
Connection: keep-alive
x-amzn-RequestId: [request-id]
X-Amzn-Trace-Id: [trace-id]
X-Cache: Miss from cloudfront
Via: 1.1 8a78b675adb2cce925860f2fe4383e71.cloudfront.net (CloudFront)
X-Amz-Cf-Id: TaW8k7yrDyXHgEU2udEEOAbliIY1iPmQr4LpN80ULdqyVGR6qP0q4Q==

{
  "jobs": [
    {
      "jobName": "EchoAttemptNumber",
      "jobId": "0668da57-1bcc-478b-bc14-5d4f1c1cef48",
      "jobQueue": "arn:aws:batch:us-east-1:123456789012:job-queue/HighPriority",
      "status": "FAILED",
      "attempts": [
        {
          "container": {
            "containerInstanceArn": "arn:aws:ecs:us-east-1:123456789012:container-instance/90bfe527-119c-494a-b8fe-f5999c66d214",
            "taskArn": "arn:aws:ecs:us-east-1:123456789012:task/af37d830-6978-4a2b-b796-e890e9b477b3",
            "exitCode": 1
          },
          "startedAt": 1490627002951,
          "stoppedAt": 1490627003065,
          "statusReason": "Essential container in task exited"
        },
        {
          "container": {
            "containerInstanceArn": "arn:aws:ecs:us-east-1:123456789012:container-instance/90bfe527-119c-494a-b8fe-f5999c66d214",
            "taskArn": "arn:aws:ecs:us-east-1:123456789012:task/3dfd4d0e-a177-4798-9c13-21b7148217bc",
            "exitCode": 2
          },
          "startedAt": 1490627019948,
          "stoppedAt": 1490627020059,
          "statusReason": "Essential container in task exited"
        },
        {
          "container": {
            "containerInstanceArn": "arn:aws:ecs:us-east-1:123456789012:container-instance/90bfe527-119c-494a-b8fe-f5999c66d214",
            "taskArn": "arn:aws:ecs:us-east-1:123456789012:task/22857040-182c-4af3-85f5-bb2c71edd282",
            "exitCode": 3
          },
          "startedAt": 1490627034798,
          "stoppedAt": 1490627034949,
          "statusReason": "Essential container in task exited"
        }
      ],
      "statusReason": "Essential container in task exited",
      "createdAt": 1490626709525,
      "retryStrategy": {
        "attempts": 3
      },
      "startedAt": 1490627034798,
      "stoppedAt": 1490627034949,
      "dependsOn": [],
      "jobDefinition": "arn:aws:batch:us-east-1:123456789012:job-definition/EchoAttemptNumber:1",
      "parameters": {},
      "container": {
        "image": "amazonlinux",
        "vcpus": 1,
        "memory": 2,
        "command": [
          "/bin/bash",
          "-c",
          "exit $AWS_BATCH_JOB_ATTEMPT"
        ],
        "volumes": [],
        "environment": [],
        "mountPoints": [],
        "ulimits": [],
        "exitCode": 3,
        "containerInstanceArn": "arn:aws:ecs:us-east-1:123456789012:container-instance/90bfe527-119c-494a-b8fe-f5999c66d214",
        "taskArn": "arn:aws:ecs:us-east-1:123456789012:task/22857040-182c-4af3-85f5-bb2c71edd282"
      }
    }
  ]
}
```

## See Also
<a name="API_DescribeJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/batch-2016-08-10/DescribeJobs) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/batch-2016-08-10/DescribeJobs) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/DescribeJobs) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/batch-2016-08-10/DescribeJobs) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/DescribeJobs) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/batch-2016-08-10/DescribeJobs) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/batch-2016-08-10/DescribeJobs) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/batch-2016-08-10/DescribeJobs) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/DescribeJobs) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/DescribeJobs) 