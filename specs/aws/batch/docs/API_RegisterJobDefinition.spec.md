---
id: "@specs/aws/batch/docs/API_RegisterJobDefinition"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RegisterJobDefinition"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# RegisterJobDefinition

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_RegisterJobDefinition
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RegisterJobDefinition
<a name="API_RegisterJobDefinition"></a>

Registers an AWS Batch job definition.

## Request Syntax
<a name="API_RegisterJobDefinition_RequestSyntax"></a>

```
POST /v1/registerjobdefinition HTTP/1.1
Content-type: application/json

{
   "consumableResourceProperties": { 
      "consumableResourceList": [ 
         { 
            "consumableResource": "{{string}}",
            "quantity": {{number}}
         }
      ]
   },
   "containerProperties": { 
      "command": [ "{{string}}" ],
      "enableExecuteCommand": {{boolean}},
      "environment": [ 
         { 
            "name": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "ephemeralStorage": { 
         "sizeInGiB": {{number}}
      },
      "executionRoleArn": "{{string}}",
      "fargatePlatformConfiguration": { 
         "platformVersion": "{{string}}"
      },
      "image": "{{string}}",
      "instanceType": "{{string}}",
      "jobRoleArn": "{{string}}",
      "linuxParameters": { 
         "devices": [ 
            { 
               "containerPath": "{{string}}",
               "hostPath": "{{string}}",
               "permissions": [ "{{string}}" ]
            }
         ],
         "initProcessEnabled": {{boolean}},
         "maxSwap": {{number}},
         "sharedMemorySize": {{number}},
         "swappiness": {{number}},
         "tmpfs": [ 
            { 
               "containerPath": "{{string}}",
               "mountOptions": [ "{{string}}" ],
               "size": {{number}}
            }
         ]
      },
      "logConfiguration": { 
         "logDriver": "{{string}}",
         "options": { 
            "{{string}}" : "{{string}}" 
         },
         "secretOptions": [ 
            { 
               "name": "{{string}}",
               "valueFrom": "{{string}}"
            }
         ]
      },
      "memory": {{number}},
      "mountPoints": [ 
         { 
            "containerPath": "{{string}}",
            "readOnly": {{boolean}},
            "sourceVolume": "{{string}}"
         }
      ],
      "networkConfiguration": { 
         "assignPublicIp": "{{string}}"
      },
      "privileged": {{boolean}},
      "readonlyRootFilesystem": {{boolean}},
      "repositoryCredentials": { 
         "credentialsParameter": "{{string}}"
      },
      "resourceRequirements": [ 
         { 
            "type": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "runtimePlatform": { 
         "cpuArchitecture": "{{string}}",
         "operatingSystemFamily": "{{string}}"
      },
      "secrets": [ 
         { 
            "name": "{{string}}",
            "valueFrom": "{{string}}"
         }
      ],
      "ulimits": [ 
         { 
            "hardLimit": {{number}},
            "name": "{{string}}",
            "softLimit": {{number}}
         }
      ],
      "user": "{{string}}",
      "vcpus": {{number}},
      "volumes": [ 
         { 
            "efsVolumeConfiguration": { 
               "authorizationConfig": { 
                  "accessPointId": "{{string}}",
                  "iam": "{{string}}"
               },
               "fileSystemId": "{{string}}",
               "rootDirectory": "{{string}}",
               "transitEncryption": "{{string}}",
               "transitEncryptionPort": {{number}}
            },
            "host": { 
               "sourcePath": "{{string}}"
            },
            "name": "{{string}}",
            "s3filesVolumeConfiguration": { 
               "accessPointArn": "{{string}}",
               "fileSystemArn": "{{string}}",
               "rootDirectory": "{{string}}",
               "transitEncryptionPort": {{number}}
            }
         }
      ]
   },
   "ecsProperties": { 
      "taskProperties": [ 
         { 
            "containers": [ 
               { 
                  "command": [ "{{string}}" ],
                  "dependsOn": [ 
                     { 
                        "condition": "{{string}}",
                        "containerName": "{{string}}"
                     }
                  ],
                  "environment": [ 
                     { 
                        "name": "{{string}}",
                        "value": "{{string}}"
                     }
                  ],
                  "essential": {{boolean}},
                  "firelensConfiguration": { 
                     "options": { 
                        "{{string}}" : "{{string}}" 
                     },
                     "type": "{{string}}"
                  },
                  "image": "{{string}}",
                  "linuxParameters": { 
                     "devices": [ 
                        { 
                           "containerPath": "{{string}}",
                           "hostPath": "{{string}}",
                           "permissions": [ "{{string}}" ]
                        }
                     ],
                     "initProcessEnabled": {{boolean}},
                     "maxSwap": {{number}},
                     "sharedMemorySize": {{number}},
                     "swappiness": {{number}},
                     "tmpfs": [ 
                        { 
                           "containerPath": "{{string}}",
                           "mountOptions": [ "{{string}}" ],
                           "size": {{number}}
                        }
                     ]
                  },
                  "logConfiguration": { 
                     "logDriver": "{{string}}",
                     "options": { 
                        "{{string}}" : "{{string}}" 
                     },
                     "secretOptions": [ 
                        { 
                           "name": "{{string}}",
                           "valueFrom": "{{string}}"
                        }
                     ]
                  },
                  "mountPoints": [ 
                     { 
                        "containerPath": "{{string}}",
                        "readOnly": {{boolean}},
                        "sourceVolume": "{{string}}"
                     }
                  ],
                  "name": "{{string}}",
                  "privileged": {{boolean}},
                  "readonlyRootFilesystem": {{boolean}},
                  "repositoryCredentials": { 
                     "credentialsParameter": "{{string}}"
                  },
                  "resourceRequirements": [ 
                     { 
                        "type": "{{string}}",
                        "value": "{{string}}"
                     }
                  ],
                  "secrets": [ 
                     { 
                        "name": "{{string}}",
                        "valueFrom": "{{string}}"
                     }
                  ],
                  "startTimeout": {{number}},
                  "stopTimeout": {{number}},
                  "ulimits": [ 
                     { 
                        "hardLimit": {{number}},
                        "name": "{{string}}",
                        "softLimit": {{number}}
                     }
                  ],
                  "user": "{{string}}"
               }
            ],
            "enableExecuteCommand": {{boolean}},
            "ephemeralStorage": { 
               "sizeInGiB": {{number}}
            },
            "executionRoleArn": "{{string}}",
            "ipcMode": "{{string}}",
            "networkConfiguration": { 
               "assignPublicIp": "{{string}}"
            },
            "pidMode": "{{string}}",
            "platformVersion": "{{string}}",
            "runtimePlatform": { 
               "cpuArchitecture": "{{string}}",
               "operatingSystemFamily": "{{string}}"
            },
            "taskRoleArn": "{{string}}",
            "volumes": [ 
               { 
                  "efsVolumeConfiguration": { 
                     "authorizationConfig": { 
                        "accessPointId": "{{string}}",
                        "iam": "{{string}}"
                     },
                     "fileSystemId": "{{string}}",
                     "rootDirectory": "{{string}}",
                     "transitEncryption": "{{string}}",
                     "transitEncryptionPort": {{number}}
                  },
                  "host": { 
                     "sourcePath": "{{string}}"
                  },
                  "name": "{{string}}",
                  "s3filesVolumeConfiguration": { 
                     "accessPointArn": "{{string}}",
                     "fileSystemArn": "{{string}}",
                     "rootDirectory": "{{string}}",
                     "transitEncryptionPort": {{number}}
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
               "args": [ "{{string}}" ],
               "command": [ "{{string}}" ],
               "env": [ 
                  { 
                     "name": "{{string}}",
                     "value": "{{string}}"
                  }
               ],
               "image": "{{string}}",
               "imagePullPolicy": "{{string}}",
               "name": "{{string}}",
               "resources": { 
                  "limits": { 
                     "{{string}}" : "{{string}}" 
                  },
                  "requests": { 
                     "{{string}}" : "{{string}}" 
                  }
               },
               "securityContext": { 
                  "allowPrivilegeEscalation": {{boolean}},
                  "privileged": {{boolean}},
                  "readOnlyRootFilesystem": {{boolean}},
                  "runAsGroup": {{number}},
                  "runAsNonRoot": {{boolean}},
                  "runAsUser": {{number}}
               },
               "volumeMounts": [ 
                  { 
                     "mountPath": "{{string}}",
                     "name": "{{string}}",
                     "readOnly": {{boolean}},
                     "subPath": "{{string}}"
                  }
               ]
            }
         ],
         "dnsPolicy": "{{string}}",
         "hostNetwork": {{boolean}},
         "imagePullSecrets": [ 
            { 
               "name": "{{string}}"
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
               "imagePullPolicy": "{{string}}",
               "name": "{{string}}",
               "resources": { 
                  "limits": { 
                     "{{string}}" : "{{string}}" 
                  },
                  "requests": { 
                     "{{string}}" : "{{string}}" 
                  }
               },
               "securityContext": { 
                  "allowPrivilegeEscalation": {{boolean}},
                  "privileged": {{boolean}},
                  "readOnlyRootFilesystem": {{boolean}},
                  "runAsGroup": {{number}},
                  "runAsNonRoot": {{boolean}},
                  "runAsUser": {{number}}
               },
               "volumeMounts": [ 
                  { 
                     "mountPath": "{{string}}",
                     "name": "{{string}}",
                     "readOnly": {{boolean}},
                     "subPath": "{{string}}"
                  }
               ]
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
         },
         "serviceAccountName": "{{string}}",
         "shareProcessNamespace": {{boolean}},
         "volumes": [ 
            { 
               "emptyDir": { 
                  "medium": "{{string}}",
                  "sizeLimit": "{{string}}"
               },
               "hostPath": { 
                  "path": "{{string}}"
               },
               "name": "{{string}}",
               "persistentVolumeClaim": { 
                  "claimName": "{{string}}",
                  "readOnly": {{boolean}}
               },
               "secret": { 
                  "optional": {{boolean}},
                  "secretName": "{{string}}"
               }
            }
         ]
      }
   },
   "jobDefinitionName": "{{string}}",
   "nodeProperties": { 
      "mainNode": {{number}},
      "nodeRangeProperties": [ 
         { 
            "consumableResourceProperties": { 
               "consumableResourceList": [ 
                  { 
                     "consumableResource": "{{string}}",
                     "quantity": {{number}}
                  }
               ]
            },
            "container": { 
               "command": [ "{{string}}" ],
               "enableExecuteCommand": {{boolean}},
               "environment": [ 
                  { 
                     "name": "{{string}}",
                     "value": "{{string}}"
                  }
               ],
               "ephemeralStorage": { 
                  "sizeInGiB": {{number}}
               },
               "executionRoleArn": "{{string}}",
               "fargatePlatformConfiguration": { 
                  "platformVersion": "{{string}}"
               },
               "image": "{{string}}",
               "instanceType": "{{string}}",
               "jobRoleArn": "{{string}}",
               "linuxParameters": { 
                  "devices": [ 
                     { 
                        "containerPath": "{{string}}",
                        "hostPath": "{{string}}",
                        "permissions": [ "{{string}}" ]
                     }
                  ],
                  "initProcessEnabled": {{boolean}},
                  "maxSwap": {{number}},
                  "sharedMemorySize": {{number}},
                  "swappiness": {{number}},
                  "tmpfs": [ 
                     { 
                        "containerPath": "{{string}}",
                        "mountOptions": [ "{{string}}" ],
                        "size": {{number}}
                     }
                  ]
               },
               "logConfiguration": { 
                  "logDriver": "{{string}}",
                  "options": { 
                     "{{string}}" : "{{string}}" 
                  },
                  "secretOptions": [ 
                     { 
                        "name": "{{string}}",
                        "valueFrom": "{{string}}"
                     }
                  ]
               },
               "memory": {{number}},
               "mountPoints": [ 
                  { 
                     "containerPath": "{{string}}",
                     "readOnly": {{boolean}},
                     "sourceVolume": "{{string}}"
                  }
               ],
               "networkConfiguration": { 
                  "assignPublicIp": "{{string}}"
               },
               "privileged": {{boolean}},
               "readonlyRootFilesystem": {{boolean}},
               "repositoryCredentials": { 
                  "credentialsParameter": "{{string}}"
               },
               "resourceRequirements": [ 
                  { 
                     "type": "{{string}}",
                     "value": "{{string}}"
                  }
               ],
               "runtimePlatform": { 
                  "cpuArchitecture": "{{string}}",
                  "operatingSystemFamily": "{{string}}"
               },
               "secrets": [ 
                  { 
                     "name": "{{string}}",
                     "valueFrom": "{{string}}"
                  }
               ],
               "ulimits": [ 
                  { 
                     "hardLimit": {{number}},
                     "name": "{{string}}",
                     "softLimit": {{number}}
                  }
               ],
               "user": "{{string}}",
               "vcpus": {{number}},
               "volumes": [ 
                  { 
                     "efsVolumeConfiguration": { 
                        "authorizationConfig": { 
                           "accessPointId": "{{string}}",
                           "iam": "{{string}}"
                        },
                        "fileSystemId": "{{string}}",
                        "rootDirectory": "{{string}}",
                        "transitEncryption": "{{string}}",
                        "transitEncryptionPort": {{number}}
                     },
                     "host": { 
                        "sourcePath": "{{string}}"
                     },
                     "name": "{{string}}",
                     "s3filesVolumeConfiguration": { 
                        "accessPointArn": "{{string}}",
                        "fileSystemArn": "{{string}}",
                        "rootDirectory": "{{string}}",
                        "transitEncryptionPort": {{number}}
                     }
                  }
               ]
            },
            "ecsProperties": { 
               "taskProperties": [ 
                  { 
                     "containers": [ 
                        { 
                           "command": [ "{{string}}" ],
                           "dependsOn": [ 
                              { 
                                 "condition": "{{string}}",
                                 "containerName": "{{string}}"
                              }
                           ],
                           "environment": [ 
                              { 
                                 "name": "{{string}}",
                                 "value": "{{string}}"
                              }
                           ],
                           "essential": {{boolean}},
                           "firelensConfiguration": { 
                              "options": { 
                                 "{{string}}" : "{{string}}" 
                              },
                              "type": "{{string}}"
                           },
                           "image": "{{string}}",
                           "linuxParameters": { 
                              "devices": [ 
                                 { 
                                    "containerPath": "{{string}}",
                                    "hostPath": "{{string}}",
                                    "permissions": [ "{{string}}" ]
                                 }
                              ],
                              "initProcessEnabled": {{boolean}},
                              "maxSwap": {{number}},
                              "sharedMemorySize": {{number}},
                              "swappiness": {{number}},
                              "tmpfs": [ 
                                 { 
                                    "containerPath": "{{string}}",
                                    "mountOptions": [ "{{string}}" ],
                                    "size": {{number}}
                                 }
                              ]
                           },
                           "logConfiguration": { 
                              "logDriver": "{{string}}",
                              "options": { 
                                 "{{string}}" : "{{string}}" 
                              },
                              "secretOptions": [ 
                                 { 
                                    "name": "{{string}}",
                                    "valueFrom": "{{string}}"
                                 }
                              ]
                           },
                           "mountPoints": [ 
                              { 
                                 "containerPath": "{{string}}",
                                 "readOnly": {{boolean}},
                                 "sourceVolume": "{{string}}"
                              }
                           ],
                           "name": "{{string}}",
                           "privileged": {{boolean}},
                           "readonlyRootFilesystem": {{boolean}},
                           "repositoryCredentials": { 
                              "credentialsParameter": "{{string}}"
                           },
                           "resourceRequirements": [ 
                              { 
                                 "type": "{{string}}",
                                 "value": "{{string}}"
                              }
                           ],
                           "secrets": [ 
                              { 
                                 "name": "{{string}}",
                                 "valueFrom": "{{string}}"
                              }
                           ],
                           "startTimeout": {{number}},
                           "stopTimeout": {{number}},
                           "ulimits": [ 
                              { 
                                 "hardLimit": {{number}},
                                 "name": "{{string}}",
                                 "softLimit": {{number}}
                              }
                           ],
                           "user": "{{string}}"
                        }
                     ],
                     "enableExecuteCommand": {{boolean}},
                     "ephemeralStorage": { 
                        "sizeInGiB": {{number}}
                     },
                     "executionRoleArn": "{{string}}",
                     "ipcMode": "{{string}}",
                     "networkConfiguration": { 
                        "assignPublicIp": "{{string}}"
                     },
                     "pidMode": "{{string}}",
                     "platformVersion": "{{string}}",
                     "runtimePlatform": { 
                        "cpuArchitecture": "{{string}}",
                        "operatingSystemFamily": "{{string}}"
                     },
                     "taskRoleArn": "{{string}}",
                     "volumes": [ 
                        { 
                           "efsVolumeConfiguration": { 
                              "authorizationConfig": { 
                                 "accessPointId": "{{string}}",
                                 "iam": "{{string}}"
                              },
                              "fileSystemId": "{{string}}",
                              "rootDirectory": "{{string}}",
                              "transitEncryption": "{{string}}",
                              "transitEncryptionPort": {{number}}
                           },
                           "host": { 
                              "sourcePath": "{{string}}"
                           },
                           "name": "{{string}}",
                           "s3filesVolumeConfiguration": { 
                              "accessPointArn": "{{string}}",
                              "fileSystemArn": "{{string}}",
                              "rootDirectory": "{{string}}",
                              "transitEncryptionPort": {{number}}
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
                        "args": [ "{{string}}" ],
                        "command": [ "{{string}}" ],
                        "env": [ 
                           { 
                              "name": "{{string}}",
                              "value": "{{string}}"
                           }
                        ],
                        "image": "{{string}}",
                        "imagePullPolicy": "{{string}}",
                        "name": "{{string}}",
                        "resources": { 
                           "limits": { 
                              "{{string}}" : "{{string}}" 
                           },
                           "requests": { 
                              "{{string}}" : "{{string}}" 
                           }
                        },
                        "securityContext": { 
                           "allowPrivilegeEscalation": {{boolean}},
                           "privileged": {{boolean}},
                           "readOnlyRootFilesystem": {{boolean}},
                           "runAsGroup": {{number}},
                           "runAsNonRoot": {{boolean}},
                           "runAsUser": {{number}}
                        },
                        "volumeMounts": [ 
                           { 
                              "mountPath": "{{string}}",
                              "name": "{{string}}",
                              "readOnly": {{boolean}},
                              "subPath": "{{string}}"
                           }
                        ]
                     }
                  ],
                  "dnsPolicy": "{{string}}",
                  "hostNetwork": {{boolean}},
                  "imagePullSecrets": [ 
                     { 
                        "name": "{{string}}"
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
                        "imagePullPolicy": "{{string}}",
                        "name": "{{string}}",
                        "resources": { 
                           "limits": { 
                              "{{string}}" : "{{string}}" 
                           },
                           "requests": { 
                              "{{string}}" : "{{string}}" 
                           }
                        },
                        "securityContext": { 
                           "allowPrivilegeEscalation": {{boolean}},
                           "privileged": {{boolean}},
                           "readOnlyRootFilesystem": {{boolean}},
                           "runAsGroup": {{number}},
                           "runAsNonRoot": {{boolean}},
                           "runAsUser": {{number}}
                        },
                        "volumeMounts": [ 
                           { 
                              "mountPath": "{{string}}",
                              "name": "{{string}}",
                              "readOnly": {{boolean}},
                              "subPath": "{{string}}"
                           }
                        ]
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
                  },
                  "serviceAccountName": "{{string}}",
                  "shareProcessNamespace": {{boolean}},
                  "volumes": [ 
                     { 
                        "emptyDir": { 
                           "medium": "{{string}}",
                           "sizeLimit": "{{string}}"
                        },
                        "hostPath": { 
                           "path": "{{string}}"
                        },
                        "name": "{{string}}",
                        "persistentVolumeClaim": { 
                           "claimName": "{{string}}",
                           "readOnly": {{boolean}}
                        },
                        "secret": { 
                           "optional": {{boolean}},
                           "secretName": "{{string}}"
                        }
                     }
                  ]
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
   "platformCapabilities": [ "{{string}}" ],
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
   "schedulingPriority": {{number}},
   "tags": { 
      "{{string}}" : "{{string}}" 
   },
   "timeout": { 
      "attemptDurationSeconds": {{number}}
   },
   "type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_RegisterJobDefinition_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_RegisterJobDefinition_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [consumableResourceProperties](#API_RegisterJobDefinition_RequestSyntax) **   <a name="Batch-RegisterJobDefinition-request-consumableResourceProperties"></a>
Contains a list of consumable resources required by the job.  
Type: [ConsumableResourceProperties](API_ConsumableResourceProperties.md) object  
Required: No

 ** [containerProperties](#API_RegisterJobDefinition_RequestSyntax) **   <a name="Batch-RegisterJobDefinition-request-containerProperties"></a>
An object with properties specific to Amazon ECS-based single-node container-based jobs. If the job definition's `type` parameter is `container`, then you must specify either `containerProperties` or `nodeProperties`. This must not be specified for Amazon EKS-based job definitions.  
If the job runs on Fargate resources, then you must not specify `nodeProperties`; use only `containerProperties`.
Type: [ContainerProperties](API_ContainerProperties.md) object  
Required: No

 ** [ecsProperties](#API_RegisterJobDefinition_RequestSyntax) **   <a name="Batch-RegisterJobDefinition-request-ecsProperties"></a>
An object with properties that are specific to Amazon ECS-based jobs. This must not be specified for Amazon EKS-based job definitions.  
Type: [EcsProperties](API_EcsProperties.md) object  
Required: No

 ** [eksProperties](#API_RegisterJobDefinition_RequestSyntax) **   <a name="Batch-RegisterJobDefinition-request-eksProperties"></a>
An object with properties that are specific to Amazon EKS-based jobs. This must not be specified for Amazon ECS based job definitions.  
Type: [EksProperties](API_EksProperties.md) object  
Required: No

 ** [jobDefinitionName](#API_RegisterJobDefinition_RequestSyntax) **   <a name="Batch-RegisterJobDefinition-request-jobDefinitionName"></a>
The name of the job definition to register. It can be up to 128 letters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (\_).  
Type: String  
Required: Yes

 ** [nodeProperties](#API_RegisterJobDefinition_RequestSyntax) **   <a name="Batch-RegisterJobDefinition-request-nodeProperties"></a>
An object with properties specific to multi-node parallel jobs. If you specify node properties for a job, it becomes a multi-node parallel job. For more information, see [Multi-node Parallel Jobs](https://docs.aws.amazon.com/batch/latest/userguide/multi-node-parallel-jobs.html) in the * AWS Batch User Guide*.  
If the job runs on Fargate resources, then you must not specify `nodeProperties`; use `containerProperties` instead.
If the job runs on Amazon EKS resources, then you must not specify `nodeProperties`.
Type: [NodeProperties](API_NodeProperties.md) object  
Required: No

 ** [parameters](#API_RegisterJobDefinition_RequestSyntax) **   <a name="Batch-RegisterJobDefinition-request-parameters"></a>
Default parameter substitution placeholders to set in the job definition. Parameters are specified as a key-value pair mapping. Parameters in a `SubmitJob` request override any corresponding parameter defaults from the job definition.  
Type: String to string map  
Required: No

 ** [platformCapabilities](#API_RegisterJobDefinition_RequestSyntax) **   <a name="Batch-RegisterJobDefinition-request-platformCapabilities"></a>
The platform capabilities required by the job definition. If no value is specified, it defaults to `EC2`. To run the job on Fargate resources, specify `FARGATE`.  
If the job runs on Amazon EKS resources, then you must not specify `platformCapabilities`.
Type: Array of strings  
Valid Values: `EC2 | FARGATE`   
Required: No

 ** [propagateTags](#API_RegisterJobDefinition_RequestSyntax) **   <a name="Batch-RegisterJobDefinition-request-propagateTags"></a>
Specifies whether to propagate the tags from the job or job definition to the corresponding Amazon ECS task. If no value is specified, the tags are not propagated. Tags can only be propagated to the tasks during task creation. For tags with the same name, job tags are given priority over job definitions tags. If the total number of combined tags from the job and job definition is over 50, the job is moved to the `FAILED` state.  
If the job runs on Amazon EKS resources, then you must not specify `propagateTags`.
Type: Boolean  
Required: No

 ** [retryStrategy](#API_RegisterJobDefinition_RequestSyntax) **   <a name="Batch-RegisterJobDefinition-request-retryStrategy"></a>
The retry strategy to use for failed jobs that are submitted with this job definition. Any retry strategy that's specified during a [SubmitJob](API_SubmitJob.md) operation overrides the retry strategy defined here. If a job is terminated due to a timeout, it isn't retried.  
Type: [RetryStrategy](API_RetryStrategy.md) object  
Required: No

 ** [schedulingPriority](#API_RegisterJobDefinition_RequestSyntax) **   <a name="Batch-RegisterJobDefinition-request-schedulingPriority"></a>
The scheduling priority for jobs that are submitted with this job definition. This only affects jobs in job queues with a fair-share policy. Jobs with a higher scheduling priority are scheduled before jobs with a lower scheduling priority.  
The minimum supported value is 0 and the maximum supported value is 9999.  
Type: Integer  
Required: No

 ** [tags](#API_RegisterJobDefinition_RequestSyntax) **   <a name="Batch-RegisterJobDefinition-request-tags"></a>
The tags that you apply to the job definition to help you categorize and organize your resources. Each tag consists of a key and an optional value. For more information, see [Tagging AWS Resources](https://docs.aws.amazon.com/batch/latest/userguide/using-tags.html) in * AWS Batch User Guide*.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Maximum length of 256.  
Required: No

 ** [timeout](#API_RegisterJobDefinition_RequestSyntax) **   <a name="Batch-RegisterJobDefinition-request-timeout"></a>
The timeout configuration for jobs that are submitted with this job definition, after which AWS Batch terminates your jobs if they have not finished. If a job is terminated due to a timeout, it isn't retried. The minimum value for the timeout is 60 seconds. Any timeout configuration that's specified during a [SubmitJob](API_SubmitJob.md) operation overrides the timeout configuration defined here. For more information, see [Job Timeouts](https://docs.aws.amazon.com/batch/latest/userguide/job_timeouts.html) in the * AWS Batch User Guide*.  
Type: [JobTimeout](API_JobTimeout.md) object  
Required: No

 ** [type](#API_RegisterJobDefinition_RequestSyntax) **   <a name="Batch-RegisterJobDefinition-request-type"></a>
The type of job definition. For more information about multi-node parallel jobs, see [Creating a multi-node parallel job definition](https://docs.aws.amazon.com/batch/latest/userguide/multi-node-job-def.html) in the * AWS Batch User Guide*.  
+ If the value is `container`, then one of the following is required: `containerProperties`, `ecsProperties`, or `eksProperties`.
+ If the value is `multinode`, then `nodeProperties` is required.
If the job is run on Fargate resources, then `multinode` isn't supported.
Type: String  
Valid Values: `container | multinode`   
Required: Yes

## Response Syntax
<a name="API_RegisterJobDefinition_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "jobDefinitionArn": "string",
   "jobDefinitionName": "string",
   "revision": number
}
```

## Response Elements
<a name="API_RegisterJobDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobDefinitionArn](#API_RegisterJobDefinition_ResponseSyntax) **   <a name="Batch-RegisterJobDefinition-response-jobDefinitionArn"></a>
The Amazon Resource Name (ARN) of the job definition.  
Type: String

 ** [jobDefinitionName](#API_RegisterJobDefinition_ResponseSyntax) **   <a name="Batch-RegisterJobDefinition-response-jobDefinitionName"></a>
The name of the job definition.  
Type: String

 ** [revision](#API_RegisterJobDefinition_ResponseSyntax) **   <a name="Batch-RegisterJobDefinition-response-revision"></a>
The revision of the job definition.  
Type: Integer

## Errors
<a name="API_RegisterJobDefinition_Errors"></a>

 ** ClientException **   
These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.  
HTTP Status Code: 400

 ** ServerException **   
These errors are usually caused by a server issue.  
HTTP Status Code: 500

## Examples
<a name="API_RegisterJobDefinition_Examples"></a>

In the following example or examples, the Authorization header contents (` [authorization-params] `) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_RegisterJobDefinition_Example_1"></a>

This example registers a job definition for a simple container job.

#### Sample Request
<a name="API_RegisterJobDefinition_Example_1_Request"></a>

```
POST /v1/registerjobdefinition HTTP/1.1
Host: batch.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: [content-length]
Authorization: [authorization-params]
X-Amz-Date: 20201128T215526Z
User-Agent: aws-cli/1.11.21 Python/2.7.12 Darwin/16.1.0 botocore/1.4.78

{
  "containerProperties": {
    "image": "busybox",
    "command": [
      "sleep",
      "10"
    ],
    "resourceRequirements": [
      {
        "type": "MEMORY",
        "value": "128"
      },
      {
        "type": "VCPU",
        "value": "1"
      }
    ]
  },
  "type": "container",
  "jobDefinitionName": "sleep10"
}
```

#### Sample Response
<a name="API_RegisterJobDefinition_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: [content-length]
Connection: keep-alive
Date: Mon, 28 Nov 2020 21:55:27 GMT
x-amzn-RequestId: [request-id]
X-Amzn-Trace-Id: [trace-id]
X-Cache: Miss from cloudfront
Via: 1.1 7a06af51e583997d8673ab89482dd45a.cloudfront.net (CloudFront)
X-Amz-Cf-Id: Y14HPNWWcKgm1U0wJPfLBzLDvrMSdyuHo4GMi0oQwI0ukruLpi0nFw==

{
  "jobDefinitionName": "sleep10",
  "jobDefinitionArn": "arn:aws:batch:us-east-1:123456789012:job-definition/sleep10:1",
  "revision": 1
}
```

### Example
<a name="API_RegisterJobDefinition_Example_2"></a>

This example registers a job definition for a simple container job with retries.

#### Sample Request
<a name="API_RegisterJobDefinition_Example_2_Request"></a>

```
POST /v1/registerjobdefinition HTTP/1.1
Host: batch.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: [content-length]
Authorization: [authorization-params]
X-Amz-Date: 20170327T145208Z
User-Agent: aws-cli/1.11.66 Python/2.7.10 Darwin/16.4.0 botocore/1.5.29

{
  "containerProperties": {
    "mountPoints": [],
    "image": "amazonlinux",
    "environment": [],
    "command": [
      "/bin/bash",
      "-c",
      "exit $AWS_BATCH_JOB_ATTEMPT"
    ],
    "volumes": [],
    "resourceRequirements": [
      {
        "type": "MEMORY",
        "value": "8"
      },
      {
        "type": "VCPU",
        "value": "1"
      }
    ],
    "ulimits": []
  },
  "retryStrategy": {
    "attempts": 3
  },
  "jobDefinitionName": "EchoAttemptNumber",
  "parameters": {},
  "type": "container"
}
```

#### Sample Response
<a name="API_RegisterJobDefinition_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Date: Mon, 27 Mar 2017 14:51:58 GMT
Content-Type: application/json
Content-Length: [content-length]
Connection: keep-alive
x-amzn-RequestId: [request-id]
X-Amzn-Trace-Id: [trace-id]
X-Cache: Miss from cloudfront
Via: 1.1 861b49a34b383ce3ac4ea8b7117b8953.cloudfront.net (CloudFront)
X-Amz-Cf-Id: l3zCxHtlIx4c1-RN2vkqIlpSbU9tsZNxfMSg6oIf700wg1BX0V5f_A==

{
  "jobDefinitionName": "EchoAttemptNumber",
  "jobDefinitionArn": "arn:aws:batch:us-east-1:123456789012:job-definition/EchoAttemptNumber:1",
  "revision": 1
}
```

## See Also
<a name="API_RegisterJobDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/batch-2016-08-10/RegisterJobDefinition) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/batch-2016-08-10/RegisterJobDefinition) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/RegisterJobDefinition) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/batch-2016-08-10/RegisterJobDefinition) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/RegisterJobDefinition) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/batch-2016-08-10/RegisterJobDefinition) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/batch-2016-08-10/RegisterJobDefinition) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/batch-2016-08-10/RegisterJobDefinition) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/RegisterJobDefinition) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/RegisterJobDefinition) 