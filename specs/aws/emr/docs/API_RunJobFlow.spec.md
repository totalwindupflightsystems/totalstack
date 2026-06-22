---
id: "@specs/aws/emr/docs/API_RunJobFlow"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RunJobFlow"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# RunJobFlow

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_RunJobFlow
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RunJobFlow
<a name="API_RunJobFlow"></a>

RunJobFlow creates and starts running a new cluster (job flow). The cluster runs the steps specified. After the steps complete, the cluster stops and the HDFS partition is lost. To prevent loss of data, configure the last step of the job flow to store results in Amazon S3. If the [JobFlowInstancesConfig](API_JobFlowInstancesConfig.md) `KeepJobFlowAliveWhenNoSteps` parameter is set to `TRUE`, the cluster transitions to the WAITING state rather than shutting down after the steps have completed. 

For additional protection, you can set the [JobFlowInstancesConfig](API_JobFlowInstancesConfig.md) `TerminationProtected` parameter to `TRUE` to lock the cluster and prevent it from being terminated by API call, user intervention, or in the event of a job flow error.

A maximum of 256 steps are allowed in each job flow.

If your cluster is long-running (such as a Hive data warehouse) or complex, you may require more than 256 steps to process your data. You can bypass the 256-step limitation in various ways, including using the SSH shell to connect to the master node and submitting queries directly to the software running on the master node, such as Hive and Hadoop.

For long-running clusters, we recommend that you periodically store your results.

**Note**  
The instance fleets configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions. The RunJobFlow request can contain InstanceFleets parameters or InstanceGroups parameters, but not both.

## Request Syntax
<a name="API_RunJobFlow_RequestSyntax"></a>

```
{
   "AdditionalInfo": "{{string}}",
   "AmiVersion": "{{string}}",
   "Applications": [ 
      { 
         "AdditionalInfo": { 
            "{{string}}" : "{{string}}" 
         },
         "Args": [ "{{string}}" ],
         "Name": "{{string}}",
         "Version": "{{string}}"
      }
   ],
   "AutoScalingRole": "{{string}}",
   "AutoTerminationPolicy": { 
      "IdleTimeout": {{number}}
   },
   "BootstrapActions": [ 
      { 
         "Name": "{{string}}",
         "ScriptBootstrapAction": { 
            "Args": [ "{{string}}" ],
            "Path": "{{string}}"
         }
      }
   ],
   "Configurations": [ 
      { 
         "Classification": "{{string}}",
         "Configurations": [ 
            "Configuration"
         ],
         "Properties": { 
            "{{string}}" : "{{string}}" 
         }
      }
   ],
   "CustomAmiId": "{{string}}",
   "EbsRootVolumeIops": {{number}},
   "EbsRootVolumeSize": {{number}},
   "EbsRootVolumeThroughput": {{number}},
   "ExtendedSupport": {{boolean}},
   "Instances": { 
      "AdditionalMasterSecurityGroups": [ "{{string}}" ],
      "AdditionalSlaveSecurityGroups": [ "{{string}}" ],
      "Ec2KeyName": "{{string}}",
      "Ec2SubnetId": "{{string}}",
      "Ec2SubnetIds": [ "{{string}}" ],
      "EmrManagedMasterSecurityGroup": "{{string}}",
      "EmrManagedSlaveSecurityGroup": "{{string}}",
      "HadoopVersion": "{{string}}",
      "InstanceCount": {{number}},
      "InstanceFleets": [ 
         { 
            "Context": "{{string}}",
            "InstanceFleetType": "{{string}}",
            "InstanceTypeConfigs": [ 
               { 
                  "BidPrice": "{{string}}",
                  "BidPriceAsPercentageOfOnDemandPrice": {{number}},
                  "Configurations": [ 
                     { 
                        "Classification": "{{string}}",
                        "Configurations": [ 
                           "Configuration"
                        ],
                        "Properties": { 
                           "{{string}}" : "{{string}}" 
                        }
                     }
                  ],
                  "CustomAmiId": "{{string}}",
                  "EbsConfiguration": { 
                     "EbsBlockDeviceConfigs": [ 
                        { 
                           "VolumeSpecification": { 
                              "Iops": {{number}},
                              "SizeInGB": {{number}},
                              "Throughput": {{number}},
                              "VolumeType": "{{string}}"
                           },
                           "VolumesPerInstance": {{number}}
                        }
                     ],
                     "EbsOptimized": {{boolean}}
                  },
                  "InstanceType": "{{string}}",
                  "Priority": {{number}},
                  "WeightedCapacity": {{number}}
               }
            ],
            "LaunchSpecifications": { 
               "OnDemandSpecification": { 
                  "AllocationStrategy": "{{string}}",
                  "CapacityReservationOptions": { 
                     "CapacityReservationPreference": "{{string}}",
                     "CapacityReservationResourceGroupArn": "{{string}}",
                     "UsageStrategy": "{{string}}"
                  }
               },
               "SpotSpecification": { 
                  "AllocationStrategy": "{{string}}",
                  "BlockDurationMinutes": {{number}},
                  "TimeoutAction": "{{string}}",
                  "TimeoutDurationMinutes": {{number}}
               }
            },
            "Name": "{{string}}",
            "ResizeSpecifications": { 
               "OnDemandResizeSpecification": { 
                  "AllocationStrategy": "{{string}}",
                  "CapacityReservationOptions": { 
                     "CapacityReservationPreference": "{{string}}",
                     "CapacityReservationResourceGroupArn": "{{string}}",
                     "UsageStrategy": "{{string}}"
                  },
                  "TimeoutDurationMinutes": {{number}}
               },
               "SpotResizeSpecification": { 
                  "AllocationStrategy": "{{string}}",
                  "TimeoutDurationMinutes": {{number}}
               }
            },
            "TargetOnDemandCapacity": {{number}},
            "TargetSpotCapacity": {{number}}
         }
      ],
      "InstanceGroups": [ 
         { 
            "AutoScalingPolicy": { 
               "Constraints": { 
                  "MaxCapacity": {{number}},
                  "MinCapacity": {{number}}
               },
               "Rules": [ 
                  { 
                     "Action": { 
                        "Market": "{{string}}",
                        "SimpleScalingPolicyConfiguration": { 
                           "AdjustmentType": "{{string}}",
                           "CoolDown": {{number}},
                           "ScalingAdjustment": {{number}}
                        }
                     },
                     "Description": "{{string}}",
                     "Name": "{{string}}",
                     "Trigger": { 
                        "CloudWatchAlarmDefinition": { 
                           "ComparisonOperator": "{{string}}",
                           "Dimensions": [ 
                              { 
                                 "Key": "{{string}}",
                                 "Value": "{{string}}"
                              }
                           ],
                           "EvaluationPeriods": {{number}},
                           "MetricName": "{{string}}",
                           "Namespace": "{{string}}",
                           "Period": {{number}},
                           "Statistic": "{{string}}",
                           "Threshold": {{number}},
                           "Unit": "{{string}}"
                        }
                     }
                  }
               ]
            },
            "BidPrice": "{{string}}",
            "Configurations": [ 
               { 
                  "Classification": "{{string}}",
                  "Configurations": [ 
                     "Configuration"
                  ],
                  "Properties": { 
                     "{{string}}" : "{{string}}" 
                  }
               }
            ],
            "CustomAmiId": "{{string}}",
            "EbsConfiguration": { 
               "EbsBlockDeviceConfigs": [ 
                  { 
                     "VolumeSpecification": { 
                        "Iops": {{number}},
                        "SizeInGB": {{number}},
                        "Throughput": {{number}},
                        "VolumeType": "{{string}}"
                     },
                     "VolumesPerInstance": {{number}}
                  }
               ],
               "EbsOptimized": {{boolean}}
            },
            "InstanceCount": {{number}},
            "InstanceRole": "{{string}}",
            "InstanceType": "{{string}}",
            "Market": "{{string}}",
            "Name": "{{string}}"
         }
      ],
      "KeepJobFlowAliveWhenNoSteps": {{boolean}},
      "MasterInstanceType": "{{string}}",
      "Placement": { 
         "AvailabilityZone": "{{string}}",
         "AvailabilityZones": [ "{{string}}" ]
      },
      "ServiceAccessSecurityGroup": "{{string}}",
      "SlaveInstanceType": "{{string}}",
      "TerminationProtected": {{boolean}},
      "UnhealthyNodeReplacement": {{boolean}}
   },
   "JobFlowRole": "{{string}}",
   "KerberosAttributes": { 
      "ADDomainJoinPassword": "{{string}}",
      "ADDomainJoinUser": "{{string}}",
      "CrossRealmTrustPrincipalPassword": "{{string}}",
      "KdcAdminPassword": "{{string}}",
      "Realm": "{{string}}"
   },
   "LogEncryptionKmsKeyId": "{{string}}",
   "LogUri": "{{string}}",
   "ManagedScalingPolicy": { 
      "ComputeLimits": { 
         "MaximumCapacityUnits": {{number}},
         "MaximumCoreCapacityUnits": {{number}},
         "MaximumOnDemandCapacityUnits": {{number}},
         "MinimumCapacityUnits": {{number}},
         "UnitType": "{{string}}"
      },
      "ScalingStrategy": "{{string}}",
      "UtilizationPerformanceIndex": {{number}}
   },
   "MonitoringConfiguration": { 
      "CloudWatchLogConfiguration": { 
         "Enabled": {{boolean}},
         "EncryptionKeyArn": "{{string}}",
         "LogGroupName": "{{string}}",
         "LogStreamNamePrefix": "{{string}}",
         "LogTypes": { 
            "{{string}}" : [ "{{string}}" ]
         }
      },
      "S3LoggingConfiguration": { 
         "LogTypeUploadPolicy": { 
            "{{string}}" : "{{string}}" 
         }
      }
   },
   "Name": "{{string}}",
   "NewSupportedProducts": [ 
      { 
         "Args": [ "{{string}}" ],
         "Name": "{{string}}"
      }
   ],
   "OSReleaseLabel": "{{string}}",
   "PlacementGroupConfigs": [ 
      { 
         "InstanceRole": "{{string}}",
         "PlacementStrategy": "{{string}}"
      }
   ],
   "ReleaseLabel": "{{string}}",
   "RepoUpgradeOnBoot": "{{string}}",
   "ScaleDownBehavior": "{{string}}",
   "SecurityConfiguration": "{{string}}",
   "ServiceRole": "{{string}}",
   "StepConcurrencyLevel": {{number}},
   "StepExecutionRoleArn": "{{string}}",
   "Steps": [ 
      { 
         "ActionOnFailure": "{{string}}",
         "HadoopJarStep": { 
            "Args": [ "{{string}}" ],
            "Jar": "{{string}}",
            "MainClass": "{{string}}",
            "Properties": [ 
               { 
                  "Key": "{{string}}",
                  "Value": "{{string}}"
               }
            ]
         },
         "Name": "{{string}}",
         "StepMonitoringConfiguration": { 
            "S3MonitoringConfiguration": { 
               "EncryptionKeyArn": "{{string}}",
               "LogUri": "{{string}}"
            }
         }
      }
   ],
   "SupportedProducts": [ "{{string}}" ],
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "VisibleToAllUsers": {{boolean}}
}
```

## Request Parameters
<a name="API_RunJobFlow_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AdditionalInfo](#API_RunJobFlow_RequestSyntax) **   <a name="EMR-RunJobFlow-request-AdditionalInfo"></a>
A JSON string for selecting additional features.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** [AmiVersion](#API_RunJobFlow_RequestSyntax) **   <a name="EMR-RunJobFlow-request-AmiVersion"></a>
Applies only to Amazon EMR AMI versions 3.x and 2.x. For Amazon EMR releases 4.0 and later, `ReleaseLabel` is used. To specify a custom AMI, use `CustomAmiID`.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** [Applications](#API_RunJobFlow_RequestSyntax) **   <a name="EMR-RunJobFlow-request-Applications"></a>
Applies to Amazon EMR releases 4.0 and later. A case-insensitive list of applications for Amazon EMR to install and configure when launching the cluster. For a list of applications available for each Amazon EMR release version, see the [Amazon EMRRelease Guide](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/).  
Type: Array of [Application](API_Application.md) objects  
Required: No

 ** [AutoScalingRole](#API_RunJobFlow_RequestSyntax) **   <a name="EMR-RunJobFlow-request-AutoScalingRole"></a>
An IAM role for automatic scaling policies. The default role is `EMR_AutoScaling_DefaultRole`. The IAM role provides permissions that the automatic scaling feature requires to launch and terminate Amazon EC2 instances in an instance group.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** [AutoTerminationPolicy](#API_RunJobFlow_RequestSyntax) **   <a name="EMR-RunJobFlow-request-AutoTerminationPolicy"></a>
An auto-termination policy for an Amazon EMR cluster. An auto-termination policy defines the amount of idle time in seconds after which a cluster automatically terminates. For alternative cluster termination options, see [Control cluster termination](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-termination.html).  
Type: [AutoTerminationPolicy](API_AutoTerminationPolicy.md) object  
Required: No

 ** [BootstrapActions](#API_RunJobFlow_RequestSyntax) **   <a name="EMR-RunJobFlow-request-BootstrapActions"></a>
A list of bootstrap actions to run before Hadoop starts on the cluster nodes.  
Type: Array of [BootstrapActionConfig](API_BootstrapActionConfig.md) objects  
Required: No

 ** [Configurations](#API_RunJobFlow_RequestSyntax) **   <a name="EMR-RunJobFlow-request-Configurations"></a>
For Amazon EMR releases 4.0 and later. The list of configurations supplied for the Amazon EMR cluster that you are creating.  
Type: Array of [Configuration](API_Configuration.md) objects  
Required: No

 ** [CustomAmiId](#API_RunJobFlow_RequestSyntax) **   <a name="EMR-RunJobFlow-request-CustomAmiId"></a>
Available only in Amazon EMR releases 5.7.0 and later. The ID of a custom Amazon EBS-backed Linux AMI. If specified, Amazon EMR uses this AMI when it launches cluster Amazon EC2 instances. For more information about custom AMIs in Amazon EMR, see [Using a Custom AMI](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-custom-ami.html) in the *Amazon EMR Management Guide*. If omitted, the cluster uses the base Linux AMI for the `ReleaseLabel` specified. For Amazon EMR releases 2.x and 3.x, use `AmiVersion` instead.  
For information about creating a custom AMI, see [Creating an Amazon EBS-Backed Linux AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-an-ami-ebs.html) in the *Amazon Elastic Compute Cloud User Guide for Linux Instances*. For information about finding an AMI ID, see [Finding a Linux AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/finding-an-ami.html).   
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** [EbsRootVolumeIops](#API_RunJobFlow_RequestSyntax) **   <a name="EMR-RunJobFlow-request-EbsRootVolumeIops"></a>
The IOPS, of the Amazon EBS root device volume of the Linux AMI that is used for each Amazon EC2 instance. Available in Amazon EMR releases 6.15.0 and later.  
Type: Integer  
Required: No

 ** [EbsRootVolumeSize](#API_RunJobFlow_RequestSyntax) **   <a name="EMR-RunJobFlow-request-EbsRootVolumeSize"></a>
The size, in GiB, of the Amazon EBS root device volume of the Linux AMI that is used for each Amazon EC2 instance. Available in Amazon EMR releases 4.x and later.  
Type: Integer  
Required: No

 ** [EbsRootVolumeThroughput](#API_RunJobFlow_RequestSyntax) **   <a name="EMR-RunJobFlow-request-EbsRootVolumeThroughput"></a>
The throughput, in MiB/s, of the Amazon EBS root device volume of the Linux AMI that is used for each Amazon EC2 instance. Available in Amazon EMR releases 6.15.0 and later.  
Type: Integer  
Required: No

 ** [ExtendedSupport](#API_RunJobFlow_RequestSyntax) **   <a name="EMR-RunJobFlow-request-ExtendedSupport"></a>
Reserved.  
Type: Boolean  
Required: No

 ** [Instances](#API_RunJobFlow_RequestSyntax) **   <a name="EMR-RunJobFlow-request-Instances"></a>
A specification of the number and type of Amazon EC2 instances.  
Type: [JobFlowInstancesConfig](API_JobFlowInstancesConfig.md) object  
Required: Yes

 ** [JobFlowRole](#API_RunJobFlow_RequestSyntax) **   <a name="EMR-RunJobFlow-request-JobFlowRole"></a>
Also called instance profile and Amazon EC2 role. An IAM role for an Amazon EMR cluster. The Amazon EC2 instances of the cluster assume this role. The default role is `EMR_EC2_DefaultRole`. In order to use the default role, you must have already created it using the AWS CLI or console.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** [KerberosAttributes](#API_RunJobFlow_RequestSyntax) **   <a name="EMR-RunJobFlow-request-KerberosAttributes"></a>
Attributes for Kerberos configuration when Kerberos authentication is enabled using a security configuration. For more information see [Use Kerberos Authentication](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-kerberos.html) in the *Amazon EMR Management Guide*.  
Type: [KerberosAttributes](API_KerberosAttributes.md) object  
Required: No

 ** [LogEncryptionKmsKeyId](#API_RunJobFlow_RequestSyntax) **   <a name="EMR-RunJobFlow-request-LogEncryptionKmsKeyId"></a>
The AWS KMS key used for encrypting log files. If a value is not provided, the logs remain encrypted by AES-256. This attribute is only available with Amazon EMR releases 5.30.0 and later, excluding Amazon EMR 6.0.0.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** [LogUri](#API_RunJobFlow_RequestSyntax) **   <a name="EMR-RunJobFlow-request-LogUri"></a>
The location in Amazon S3 to write the log files of the job flow. If a value is not provided, logs are not created.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** [ManagedScalingPolicy](#API_RunJobFlow_RequestSyntax) **   <a name="EMR-RunJobFlow-request-ManagedScalingPolicy"></a>
 The specified managed scaling policy for an Amazon EMR cluster.   
Type: [ManagedScalingPolicy](API_ManagedScalingPolicy.md) object  
Required: No

 ** [MonitoringConfiguration](#API_RunJobFlow_RequestSyntax) **   <a name="EMR-RunJobFlow-request-MonitoringConfiguration"></a>
Contains CloudWatch log configuration metadata and settings.  
Type: [MonitoringConfiguration](API_MonitoringConfiguration.md) object  
Required: No

 ** [Name](#API_RunJobFlow_RequestSyntax) **   <a name="EMR-RunJobFlow-request-Name"></a>
The name of the job flow.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: Yes

 ** [NewSupportedProducts](#API_RunJobFlow_RequestSyntax) **   <a name="EMR-RunJobFlow-request-NewSupportedProducts"></a>
For Amazon EMR releases 3.x and 2.x. For Amazon EMR releases 4.x and later, use Applications.
A list of strings that indicates third-party software to use with the job flow that accepts a user argument list. Amazon EMR accepts and forwards the argument list to the corresponding installation script as bootstrap action arguments. For more information, see "Launch a Job Flow on the MapR Distribution for Hadoop" in the [Amazon EMR Developer Guide](https://docs.aws.amazon.com/emr/latest/DeveloperGuide/emr-dg.pdf). Supported values are:  
+ "mapr-m3" - launch the cluster using MapR M3 Edition.
+ "mapr-m5" - launch the cluster using MapR M5 Edition.
+ "mapr" with the user arguments specifying "--edition,m3" or "--edition,m5" - launch the job flow using MapR M3 or M5 Edition respectively.
+ "mapr-m7" - launch the cluster using MapR M7 Edition.
+ "hunk" - launch the cluster with the Hunk Big Data Analytics Platform.
+ "hue"- launch the cluster with Hue installed.
+ "spark" - launch the cluster with Apache Spark installed.
+ "ganglia" - launch the cluster with the Ganglia Monitoring System installed.
Type: Array of [SupportedProductConfig](API_SupportedProductConfig.md) objects  
Required: No

 ** [OSReleaseLabel](#API_RunJobFlow_RequestSyntax) **   <a name="EMR-RunJobFlow-request-OSReleaseLabel"></a>
Specifies a particular Amazon Linux release for all nodes in a cluster launch RunJobFlow request. If a release is not specified, Amazon EMR uses the latest validated Amazon Linux release for cluster launch.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** [PlacementGroupConfigs](#API_RunJobFlow_RequestSyntax) **   <a name="EMR-RunJobFlow-request-PlacementGroupConfigs"></a>
The specified placement group configuration for an Amazon EMR cluster.  
Type: Array of [PlacementGroupConfig](API_PlacementGroupConfig.md) objects  
Required: No

 ** [ReleaseLabel](#API_RunJobFlow_RequestSyntax) **   <a name="EMR-RunJobFlow-request-ReleaseLabel"></a>
The Amazon EMR release label, which determines the version of open-source application packages installed on the cluster. Release labels are in the form `emr-x.x.x`, where x.x.x is an Amazon EMR release version such as `emr-5.14.0`. For more information about Amazon EMR release versions and included application versions and features, see [https://docs.aws.amazon.com/emr/latest/ReleaseGuide/](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/). The release label applies only to Amazon EMR releases version 4.0 and later. Earlier versions use `AmiVersion`.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** [RepoUpgradeOnBoot](#API_RunJobFlow_RequestSyntax) **   <a name="EMR-RunJobFlow-request-RepoUpgradeOnBoot"></a>
Applies only when `CustomAmiID` is used. Specifies which updates from the Amazon Linux AMI package repositories to apply automatically when the instance boots using the AMI. If omitted, the default is `SECURITY`, which indicates that only security updates are applied. If `NONE` is specified, no updates are applied, and all updates must be applied manually.  
Type: String  
Valid Values: `SECURITY | NONE`   
Required: No

 ** [ScaleDownBehavior](#API_RunJobFlow_RequestSyntax) **   <a name="EMR-RunJobFlow-request-ScaleDownBehavior"></a>
Specifies the way that individual Amazon EC2 instances terminate when an automatic scale-in activity occurs or an instance group is resized. `TERMINATE_AT_INSTANCE_HOUR` indicates that Amazon EMR terminates nodes at the instance-hour boundary, regardless of when the request to terminate the instance was submitted. This option is only available with Amazon EMR 5.1.0 and later and is the default for clusters created using that version. `TERMINATE_AT_TASK_COMPLETION` indicates that Amazon EMR adds nodes to a deny list and drains tasks from nodes before terminating the Amazon EC2 instances, regardless of the instance-hour boundary. With either behavior, Amazon EMR removes the least active nodes first and blocks instance termination if it could lead to HDFS corruption. `TERMINATE_AT_TASK_COMPLETION` available only in Amazon EMR releases 4.1.0 and later, and is the default for releases of Amazon EMR earlier than 5.1.0.  
Type: String  
Valid Values: `TERMINATE_AT_INSTANCE_HOUR | TERMINATE_AT_TASK_COMPLETION`   
Required: No

 ** [SecurityConfiguration](#API_RunJobFlow_RequestSyntax) **   <a name="EMR-RunJobFlow-request-SecurityConfiguration"></a>
The name of a security configuration to apply to the cluster.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** [ServiceRole](#API_RunJobFlow_RequestSyntax) **   <a name="EMR-RunJobFlow-request-ServiceRole"></a>
The IAM role that Amazon EMR assumes in order to access AWS resources on your behalf. If you've created a custom service role path, you must specify it for the service role when you launch your cluster.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** [StepConcurrencyLevel](#API_RunJobFlow_RequestSyntax) **   <a name="EMR-RunJobFlow-request-StepConcurrencyLevel"></a>
Specifies the number of steps that can be executed concurrently. The default value is `1`. The maximum value is `256`.  
Type: Integer  
Required: No

 ** [StepExecutionRoleArn](#API_RunJobFlow_RequestSyntax) **   <a name="EMR-RunJobFlow-request-StepExecutionRoleArn"></a>
The Amazon Resource Name (ARN) of the runtime role for steps specified in the RunJobFlow request. The runtime role can be a cross-account IAM role. The runtime role ARN is a combination of account ID, role name, and role type using the following format: `arn:partition:iam::account-id:role/role-name`.  
For example, `arn:aws:iam::1234567890:role/ReadOnly` is a correctly formatted runtime role ARN.  
This parameter applies only to steps included in the `Steps` parameter of this RunJobFlow request. It does not apply to steps added later to the cluster.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Required: No

 ** [Steps](#API_RunJobFlow_RequestSyntax) **   <a name="EMR-RunJobFlow-request-Steps"></a>
A list of steps to run.  
Type: Array of [StepConfig](API_StepConfig.md) objects  
Required: No

 ** [SupportedProducts](#API_RunJobFlow_RequestSyntax) **   <a name="EMR-RunJobFlow-request-SupportedProducts"></a>
For Amazon EMR releases 3.x and 2.x. For Amazon EMR releases 4.x and later, use Applications.
A list of strings that indicates third-party software to use. For more information, see the [Amazon EMR Developer Guide](https://docs.aws.amazon.com/emr/latest/DeveloperGuide/emr-dg.pdf). Currently supported values are:  
+ "mapr-m3" - launch the job flow using MapR M3 Edition.
+ "mapr-m5" - launch the job flow using MapR M5 Edition.
Type: Array of strings  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** [Tags](#API_RunJobFlow_RequestSyntax) **   <a name="EMR-RunJobFlow-request-Tags"></a>
A list of tags to associate with a cluster and propagate to Amazon EC2 instances.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

 ** [VisibleToAllUsers](#API_RunJobFlow_RequestSyntax) **   <a name="EMR-RunJobFlow-request-VisibleToAllUsers"></a>
The VisibleToAllUsers parameter is no longer supported. By default, the value is set to `true`. Setting it to `false` now has no effect.
Set this value to `true` so that IAM principals in the AWS account associated with the cluster can perform Amazon EMR actions on the cluster that their IAM policies allow. This value defaults to `true` for clusters created using the Amazon EMR API or the AWS CLI [create-cluster](https://docs.aws.amazon.com/cli/latest/reference/emr/create-cluster.html) command.  
When set to `false`, only the IAM principal that created the cluster and the AWS account root user can perform Amazon EMR actions for the cluster, regardless of the IAM permissions policies attached to other IAM principals. For more information, see [Understanding the Amazon EMR cluster VisibleToAllUsers setting](https://docs.aws.amazon.com/emr/latest/ManagementGuide/security_IAM_emr-with-IAM.html#security_set_visible_to_all_users) in the *Amazon EMR Management Guide*.  
Type: Boolean  
Required: No

## Response Syntax
<a name="API_RunJobFlow_ResponseSyntax"></a>

```
{
   "ClusterArn": "string",
   "JobFlowId": "string"
}
```

## Response Elements
<a name="API_RunJobFlow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ClusterArn](#API_RunJobFlow_ResponseSyntax) **   <a name="EMR-RunJobFlow-response-ClusterArn"></a>
The Amazon Resource Name (ARN) of the cluster.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [JobFlowId](#API_RunJobFlow_ResponseSyntax) **   <a name="EMR-RunJobFlow-response-JobFlowId"></a>
A unique identifier for the job flow.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*` 

## Errors
<a name="API_RunJobFlow_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **   
Indicates that an error occurred while processing the request and that the request was not completed.  
HTTP Status Code: 400

## Examples
<a name="API_RunJobFlow_Examples"></a>

### Example 1
<a name="API_RunJobFlow_Example_1"></a>

This example illustrates one usage of RunJobFlow.

#### Sample Request
<a name="API_RunJobFlow_Example_1_Request"></a>

```
POST / HTTP/1.1
Content-Type: application/x-amz-json-1.1
X-Amz-Target: ElasticMapReduce.RunJobFlow
Content-Length: 734
User-Agent: aws-sdk-ruby/1.9.2 ruby/1.9.3 i386-mingw32
Host: us-east-1.elasticmapreduce.amazonaws.com
X-Amz-Date: 20130715T210803Z
X-Amz-Content-Sha256: 8676d21986e4628a89fb1232a1344063778d4ffc23d10be02b437e0d53a24db3
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20130715/us-east-1/elasticmapreduce/aws4_request, SignedHeaders=content-length;content-type;host;user-agent;x-amz-content-sha256;x-amz-date;x-amz-target, Signature=71f79725c4dbe77c0e842718485f0b37fe6df69e1153c80f7748ebd9617ca2f3
Accept: */*


{
    "Name": "Development Job Flow",
    "Instances": {
        "KeepJobFlowAliveWhenNoSteps": "false",
        "TerminationProtected": "false",
        "InstanceGroups": [{
            "Name": "Master Instance Group",
            "InstanceRole": "MASTER",
            "InstanceCount": 1,
            "InstanceType": "m1.small",
            "Market": "ON_DEMAND"
        }]
    },
    "Steps": [{
        "Name": "Example Streaming Step",
        "ActionOnFailure": "CANCEL_AND_WAIT",
        "HadoopJarStep": {
            "Jar": "/home/hadoop/contrib/streaming/hadoop-streaming.jar",
            "Args": [
                "-input",
                "s3://elasticmapreduce/samples/wordcount/input",
                "-output",
                "s3://examples-bucket/example-output",
                "-mapper",
                "s3://elasticmapreduce/samples/wordcount/wordSplitter.py",
                "-reducer",
                "aggregate"
            ]
        }
    }],
    "BootstrapActions": [],
    "NewSupportedProduct": [],
    "AmiVersion": "3.8.0"
}
```

#### Sample Response
<a name="API_RunJobFlow_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: a4406d6b-ed92-11e2-9787-192218ecb460
Content-Type: application/x-amz-json-1.1
Content-Length: 31
Date: Mon, 15 Jul 2013 21:08:05 GMT

{"JobFlowId": "j-ZKIY4CKQRX72"}
```

## See Also
<a name="API_RunJobFlow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/RunJobFlow) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/RunJobFlow) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/RunJobFlow) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/RunJobFlow) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/RunJobFlow) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/RunJobFlow) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/RunJobFlow) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/RunJobFlow) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/RunJobFlow) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/RunJobFlow) 