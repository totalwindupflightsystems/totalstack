---
id: "@specs/aws/fsx/docs/API_CreateBackup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateBackup"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# CreateBackup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_CreateBackup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateBackup
<a name="API_CreateBackup"></a>

Creates a backup of an existing Amazon FSx for Windows File Server file system, Amazon FSx for Lustre file system, Amazon FSx for NetApp ONTAP volume, or Amazon FSx for OpenZFS file system. We recommend creating regular backups so that you can restore a file system or volume from a backup if an issue arises with the original file system or volume.

For Amazon FSx for Lustre file systems, you can create a backup only for file systems that have the following configuration:
+ A Persistent deployment type
+ Are *not* linked to a data repository

For more information about backups, see the following:
+ For Amazon FSx for Lustre, see [Working with FSx for Lustre backups](https://docs.aws.amazon.com/fsx/latest/LustreGuide/using-backups-fsx.html).
+ For Amazon FSx for Windows, see [Working with FSx for Windows backups](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/using-backups.html).
+ For Amazon FSx for NetApp ONTAP, see [Working with FSx for NetApp ONTAP backups](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/using-backups.html).
+ For Amazon FSx for OpenZFS, see [Working with FSx for OpenZFS backups](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/using-backups.html).

If a backup with the specified client request token exists and the parameters match, this operation returns the description of the existing backup. If a backup with the specified client request token exists and the parameters don't match, this operation returns `IncompatibleParameterError`. If a backup with the specified client request token doesn't exist, `CreateBackup` does the following: 
+ Creates a new Amazon FSx backup with an assigned ID, and an initial lifecycle state of `CREATING`.
+ Returns the description of the backup.

By using the idempotent operation, you can retry a `CreateBackup` operation without the risk of creating an extra backup. This approach can be useful when an initial call fails in a way that makes it unclear whether a backup was created. If you use the same client request token and the initial call created a backup, the operation returns a successful result because all the parameters are the same.

The `CreateBackup` operation returns while the backup's lifecycle state is still `CREATING`. You can check the backup creation status by calling the [DescribeBackups](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeBackups.html) operation, which returns the backup state along with other information.

## Request Syntax
<a name="API_CreateBackup_RequestSyntax"></a>

```
{
   "ClientRequestToken": "{{string}}",
   "FileSystemId": "{{string}}",
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "VolumeId": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateBackup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_CreateBackup_RequestSyntax) **   <a name="FSx-CreateBackup-request-ClientRequestToken"></a>
(Optional) A string of up to 63 ASCII characters that Amazon FSx uses to ensure idempotent creation. This string is automatically filled on your behalf when you use the AWS Command Line Interface (AWS CLI) or an AWS SDK.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[A-za-z0-9_.-]{0,63}$`   
Required: No

 ** [FileSystemId](#API_CreateBackup_RequestSyntax) **   <a name="FSx-CreateBackup-request-FileSystemId"></a>
The ID of the file system to back up.  
Type: String  
Length Constraints: Minimum length of 11. Maximum length of 21.  
Pattern: `^(fs-[0-9a-f]{8,})$`   
Required: No

 ** [Tags](#API_CreateBackup_RequestSyntax) **   <a name="FSx-CreateBackup-request-Tags"></a>
(Optional) The tags to apply to the backup at backup creation. The key value of the `Name` tag appears in the console as the backup name. If you have set `CopyTagsToBackups` to `true`, and you specify one or more tags using the `CreateBackup` operation, no existing file system tags are copied from the file system to the backup.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 50 items.  
Required: No

 ** [VolumeId](#API_CreateBackup_RequestSyntax) **   <a name="FSx-CreateBackup-request-VolumeId"></a>
(Optional) The ID of the FSx for ONTAP volume to back up.  
Type: String  
Length Constraints: Fixed length of 23.  
Pattern: `^(fsvol-[0-9a-f]{17,})$`   
Required: No

## Response Syntax
<a name="API_CreateBackup_ResponseSyntax"></a>

```
{
   "Backup": { 
      "BackupId": "string",
      "CreationTime": number,
      "DirectoryInformation": { 
         "ActiveDirectoryId": "string",
         "DomainName": "string",
         "ResourceARN": "string"
      },
      "FailureDetails": { 
         "Message": "string"
      },
      "FileSystem": { 
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
               "TargetFileSystemValues": "FileSystem",
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
               "TargetVolumeValues": { 
                  "AdministrativeActions": [ 
                     "AdministrativeAction"
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
               },
               "TotalTransferBytes": number
            }
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
      "KmsKeyId": "string",
      "Lifecycle": "string",
      "OwnerId": "string",
      "ProgressPercent": number,
      "ResourceARN": "string",
      "ResourceType": "string",
      "SizeInBytes": number,
      "SourceBackupId": "string",
      "SourceBackupRegion": "string",
      "Tags": [ 
         { 
            "Key": "string",
            "Value": "string"
         }
      ],
      "Type": "string",
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
}
```

## Response Elements
<a name="API_CreateBackup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Backup](#API_CreateBackup_ResponseSyntax) **   <a name="FSx-CreateBackup-response-Backup"></a>
A description of the backup.  
Type: [Backup](API_Backup.md) object

## Errors
<a name="API_CreateBackup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BackupInProgress **   
Another backup is already under way. Wait for completion before initiating additional backups of this file system.    
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

 ** ServiceLimitExceeded **   
An error indicating that a particular service limit was exceeded. You can increase some service limits by contacting AWS Support.    
 ** Limit **   
Enumeration of the service limit that was exceeded.   
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** UnsupportedOperation **   
The requested operation is not supported for this resource or API.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** VolumeNotFound **   
No Amazon FSx volumes were found based upon the supplied parameters.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

## See Also
<a name="API_CreateBackup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/CreateBackup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/CreateBackup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/CreateBackup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/CreateBackup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/CreateBackup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/CreateBackup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/CreateBackup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/CreateBackup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/CreateBackup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/CreateBackup) 