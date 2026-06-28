---
id: "@specs/aws/fsx/docs/API_CreateVolumeFromBackup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateVolumeFromBackup"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# CreateVolumeFromBackup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_CreateVolumeFromBackup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateVolumeFromBackup
<a name="API_CreateVolumeFromBackup"></a>

Creates a new Amazon FSx for NetApp ONTAP volume from an existing Amazon FSx volume backup.

## Request Syntax
<a name="API_CreateVolumeFromBackup_RequestSyntax"></a>

```
{
   "BackupId": "{{string}}",
   "ClientRequestToken": "{{string}}",
   "Name": "{{string}}",
   "OntapConfiguration": { 
      "AggregateConfiguration": { 
         "Aggregates": [ "{{string}}" ],
         "ConstituentsPerAggregate": {{number}}
      },
      "CopyTagsToBackups": {{boolean}},
      "JunctionPath": "{{string}}",
      "OntapVolumeType": "{{string}}",
      "SecurityStyle": "{{string}}",
      "SizeInBytes": {{number}},
      "SizeInMegabytes": {{number}},
      "SnaplockConfiguration": { 
         "AuditLogVolume": {{boolean}},
         "AutocommitPeriod": { 
            "Type": "{{string}}",
            "Value": {{number}}
         },
         "PrivilegedDelete": "{{string}}",
         "RetentionPeriod": { 
            "DefaultRetention": { 
               "Type": "{{string}}",
               "Value": {{number}}
            },
            "MaximumRetention": { 
               "Type": "{{string}}",
               "Value": {{number}}
            },
            "MinimumRetention": { 
               "Type": "{{string}}",
               "Value": {{number}}
            }
         },
         "SnaplockType": "{{string}}",
         "VolumeAppendModeEnabled": {{boolean}}
      },
      "SnapshotPolicy": "{{string}}",
      "StorageEfficiencyEnabled": {{boolean}},
      "StorageVirtualMachineId": "{{string}}",
      "TieringPolicy": { 
         "CoolingPeriod": {{number}},
         "Name": "{{string}}"
      },
      "VolumeStyle": "{{string}}"
   },
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateVolumeFromBackup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [BackupId](#API_CreateVolumeFromBackup_RequestSyntax) **   <a name="FSx-CreateVolumeFromBackup-request-BackupId"></a>
The ID of the source backup. Specifies the backup that you are copying.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 128.  
Pattern: `^(backup-[0-9a-f]{8,})$`   
Required: Yes

 ** [ClientRequestToken](#API_CreateVolumeFromBackup_RequestSyntax) **   <a name="FSx-CreateVolumeFromBackup-request-ClientRequestToken"></a>
(Optional) An idempotency token for resource creation, in a string of up to 63 ASCII characters. This token is automatically filled on your behalf when you use the AWS Command Line Interface (AWS CLI) or an AWS SDK.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[A-za-z0-9_.-]{0,63}$`   
Required: No

 ** [Name](#API_CreateVolumeFromBackup_RequestSyntax) **   <a name="FSx-CreateVolumeFromBackup-request-Name"></a>
The name of the new volume you're creating.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 203.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,203}$`   
Required: Yes

 ** [OntapConfiguration](#API_CreateVolumeFromBackup_RequestSyntax) **   <a name="FSx-CreateVolumeFromBackup-request-OntapConfiguration"></a>
Specifies the configuration of the ONTAP volume that you are creating.  
Type: [CreateOntapVolumeConfiguration](API_CreateOntapVolumeConfiguration.md) object  
Required: No

 ** [Tags](#API_CreateVolumeFromBackup_RequestSyntax) **   <a name="FSx-CreateVolumeFromBackup-request-Tags"></a>
A list of `Tag` values, with a maximum of 50 elements.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 50 items.  
Required: No

## Response Syntax
<a name="API_CreateVolumeFromBackup_ResponseSyntax"></a>

```
{
   "Volume": { 
      "AdministrativeActions": [ 
         { 
            "AdministrativeActionType": "string",
            "FailureDetails": { 
               "Message": "string"
            },
            "Message": "string",
            "ProgressPercent": number,
            "RemainingTransferBytes": number,
            "RequestTime": number,
            "Status": "string",
            "TargetFileSystemValues": { 
               "AdministrativeActions": [ 
                  "AdministrativeAction"
               ],
               "CreationTime": number,
               "DNSName": "string",
               "FailureDetails": { 
                  "Message": "string"
               },
               "FileSystemId": "string",
               "FileSystemType": "string",
               "FileSystemTypeVersion": "string",
               "KmsKeyId": "string",
               "Lifecycle": "string",
               "LustreConfiguration": { 
                  "AutomaticBackupRetentionDays": number,
                  "CopyTagsToBackups": boolean,
                  "DailyAutomaticBackupStartTime": "string",
                  "DataCompressionType": "string",
                  "DataReadCacheConfiguration": { 
                     "SizeGiB": number,
                     "SizingMode": "string"
                  },
                  "DataRepositoryConfiguration": { 
                     "AutoImportPolicy": "string",
                     "ExportPath": "string",
                     "FailureDetails": { 
                        "Message": "string"
                     },
                     "ImportedFileChunkSize": number,
                     "ImportPath": "string",
                     "Lifecycle": "string"
                  },
                  "DeploymentType": "string",
                  "DriveCacheType": "string",
                  "EfaEnabled": boolean,
                  "LogConfiguration": { 
                     "Destination": "string",
                     "Level": "string"
                  },
                  "MetadataConfiguration": { 
                     "Iops": number,
                     "Mode": "string"
                  },
                  "MountName": "string",
                  "PerUnitStorageThroughput": number,
                  "RootSquashConfiguration": { 
                     "NoSquashNids": [ "string" ],
                     "RootSquash": "string"
                  },
                  "ThroughputCapacity": number,
                  "WeeklyMaintenanceStartTime": "string"
               },
               "NetworkInterfaceIds": [ "string" ],
               "NetworkType": "string",
               "OntapConfiguration": { 
                  "AutomaticBackupRetentionDays": number,
                  "DailyAutomaticBackupStartTime": "string",
                  "DeploymentType": "string",
                  "DiskIopsConfiguration": { 
                     "Iops": number,
                     "Mode": "string"
                  },
                  "EndpointIpAddressRange": "string",
                  "EndpointIpv6AddressRange": "string",
                  "Endpoints": { 
                     "Intercluster": { 
                        "DNSName": "string",
                        "IpAddresses": [ "string" ],
                        "Ipv6Addresses": [ "string" ]
                     },
                     "Management": { 
                        "DNSName": "string",
                        "IpAddresses": [ "string" ],
                        "Ipv6Addresses": [ "string" ]
                     }
                  },
                  "FsxAdminPassword": "string",
                  "HAPairs": number,
                  "PreferredSubnetId": "string",
                  "RouteTableIds": [ "string" ],
                  "ThroughputCapacity": number,
                  "ThroughputCapacityPerHAPair": number,
                  "WeeklyMaintenanceStartTime": "string"
               },
               "OpenZFSConfiguration": { 
                  "AutomaticBackupRetentionDays": number,
                  "CopyTagsToBackups": boolean,
                  "CopyTagsToVolumes": boolean,
                  "DailyAutomaticBackupStartTime": "string",
                  "DeploymentType": "string",
                  "DiskIopsConfiguration": { 
                     "Iops": number,
                     "Mode": "string"
                  },
                  "EndpointIpAddress": "string",
                  "EndpointIpAddressRange": "string",
                  "EndpointIpv6Address": "string",
                  "EndpointIpv6AddressRange": "string",
                  "PreferredSubnetId": "string",
                  "ReadCacheConfiguration": { 
                     "SizeGiB": number,
                     "SizingMode": "string"
                  },
                  "RootVolumeId": "string",
                  "RouteTableIds": [ "string" ],
                  "ThroughputCapacity": number,
                  "WeeklyMaintenanceStartTime": "string"
               },
               "OwnerId": "string",
               "ResourceARN": "string",
               "StorageCapacity": number,
               "StorageType": "string",
               "SubnetIds": [ "string" ],
               "Tags": [ 
                  { 
                     "Key": "string",
                     "Value": "string"
                  }
               ],
               "VpcId": "string",
               "WindowsConfiguration": { 
                  "ActiveDirectoryId": "string",
                  "Aliases": [ 
                     { 
                        "Lifecycle": "string",
                        "Name": "string"
                     }
                  ],
                  "AuditLogConfiguration": { 
                     "AuditLogDestination": "string",
                     "FileAccessAuditLogLevel": "string",
                     "FileShareAccessAuditLogLevel": "string"
                  },
                  "AutomaticBackupRetentionDays": number,
                  "CopyTagsToBackups": boolean,
                  "DailyAutomaticBackupStartTime": "string",
                  "DeploymentType": "string",
                  "DiskIopsConfiguration": { 
                     "Iops": number,
                     "Mode": "string"
                  },
                  "FsrmConfiguration": { 
                     "EventLogDestination": "string",
                     "FsrmServiceEnabled": boolean
                  },
                  "MaintenanceOperationsInProgress": [ "string" ],
                  "PreferredFileServerIp": "string",
                  "PreferredFileServerIpv6": "string",
                  "PreferredSubnetId": "string",
                  "RemoteAdministrationEndpoint": "string",
                  "SelfManagedActiveDirectoryConfiguration": { 
                     "DnsIps": [ "string" ],
                     "DomainJoinServiceAccountSecret": "string",
                     "DomainName": "string",
                     "FileSystemAdministratorsGroup": "string",
                     "OrganizationalUnitDistinguishedName": "string",
                     "UserName": "string"
                  },
                  "ThroughputCapacity": number,
                  "WeeklyMaintenanceStartTime": "string"
               }
            },
            "TargetSnapshotValues": { 
               "AdministrativeActions": [ 
                  "AdministrativeAction"
               ],
               "CreationTime": number,
               "Lifecycle": "string",
               "LifecycleTransitionReason": { 
                  "Message": "string"
               },
               "Name": "string",
               "ResourceARN": "string",
               "SnapshotId": "string",
               "Tags": [ 
                  { 
                     "Key": "string",
                     "Value": "string"
                  }
               ],
               "VolumeId": "string"
            },
            "TargetVolumeValues": "Volume",
            "TotalTransferBytes": number
         }
      ],
      "CreationTime": number,
      "FileSystemId": "string",
      "Lifecycle": "string",
      "LifecycleTransitionReason": { 
         "Message": "string"
      },
      "Name": "string",
      "OntapConfiguration": { 
         "AggregateConfiguration": { 
            "Aggregates": [ "string" ],
            "TotalConstituents": number
         },
         "CopyTagsToBackups": boolean,
         "FlexCacheEndpointType": "string",
         "JunctionPath": "string",
         "OntapVolumeType": "string",
         "SecurityStyle": "string",
         "SizeInBytes": number,
         "SizeInMegabytes": number,
         "SnaplockConfiguration": { 
            "AuditLogVolume": boolean,
            "AutocommitPeriod": { 
               "Type": "string",
               "Value": number
            },
            "PrivilegedDelete": "string",
            "RetentionPeriod": { 
               "DefaultRetention": { 
                  "Type": "string",
                  "Value": number
               },
               "MaximumRetention": { 
                  "Type": "string",
                  "Value": number
               },
               "MinimumRetention": { 
                  "Type": "string",
                  "Value": number
               }
            },
            "SnaplockType": "string",
            "VolumeAppendModeEnabled": boolean
         },
         "SnapshotPolicy": "string",
         "StorageEfficiencyEnabled": boolean,
         "StorageVirtualMachineId": "string",
         "StorageVirtualMachineRoot": boolean,
         "TieringPolicy": { 
            "CoolingPeriod": number,
            "Name": "string"
         },
         "UUID": "string",
         "VolumeStyle": "string"
      },
      "OpenZFSConfiguration": { 
         "CopyStrategy": "string",
         "CopyTagsToSnapshots": boolean,
         "DataCompressionType": "string",
         "DeleteClonedVolumes": boolean,
         "DeleteIntermediateData": boolean,
         "DeleteIntermediateSnaphots": boolean,
         "DestinationSnapshot": "string",
         "NfsExports": [ 
            { 
               "ClientConfigurations": [ 
                  { 
                     "Clients": "string",
                     "Options": [ "string" ]
                  }
               ]
            }
         ],
         "OriginSnapshot": { 
            "CopyStrategy": "string",
            "SnapshotARN": "string"
         },
         "ParentVolumeId": "string",
         "ReadOnly": boolean,
         "RecordSizeKiB": number,
         "RestoreToSnapshot": "string",
         "SourceSnapshotARN": "string",
         "StorageCapacityQuotaGiB": number,
         "StorageCapacityReservationGiB": number,
         "UserAndGroupQuotas": [ 
            { 
               "Id": number,
               "StorageCapacityQuotaGiB": number,
               "Type": "string"
            }
         ],
         "VolumePath": "string"
      },
      "ResourceARN": "string",
      "Tags": [ 
         { 
            "Key": "string",
            "Value": "string"
         }
      ],
      "VolumeId": "string",
      "VolumeType": "string"
   }
}
```

## Response Elements
<a name="API_CreateVolumeFromBackup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Volume](#API_CreateVolumeFromBackup_ResponseSyntax) **   <a name="FSx-CreateVolumeFromBackup-response-Volume"></a>
Returned after a successful `CreateVolumeFromBackup` API operation, describing the volume just created.  
Type: [Volume](API_Volume.md) object

## Errors
<a name="API_CreateVolumeFromBackup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BackupNotFound **   
No Amazon FSx backups were found based upon the supplied parameters.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** BadRequest **   
A generic error indicating a failure with a client request.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** FileSystemNotFound **   
No Amazon FSx file systems were found based upon supplied parameters.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** IncompatibleParameterError **   
The error returned when a second request is received with the same client request token but different parameters settings. A client request token should always uniquely identify a single request.    
 ** Message **   
A detailed error message.  
 ** Parameter **   
A parameter that is incompatible with the earlier request.
HTTP Status Code: 400

 ** InternalServerError **   
A generic error indicating a server-side failure.    
 ** Message **   
A detailed error message.
HTTP Status Code: 500

 ** MissingVolumeConfiguration **   
A volume configuration is required for this operation.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** ServiceLimitExceeded **   
An error indicating that a particular service limit was exceeded. You can increase some service limits by contacting AWS Support.    
 ** Limit **   
Enumeration of the service limit that was exceeded.   
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** StorageVirtualMachineNotFound **   
No FSx for ONTAP SVMs were found based upon the supplied parameters.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

## See Also
<a name="API_CreateVolumeFromBackup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/CreateVolumeFromBackup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/CreateVolumeFromBackup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/CreateVolumeFromBackup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/CreateVolumeFromBackup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/CreateVolumeFromBackup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/CreateVolumeFromBackup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/CreateVolumeFromBackup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/CreateVolumeFromBackup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/CreateVolumeFromBackup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/CreateVolumeFromBackup) 