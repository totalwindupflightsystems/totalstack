---
id: "@specs/aws/fsx/docs/API_CopyBackup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CopyBackup"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# CopyBackup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_CopyBackup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CopyBackup
<a name="API_CopyBackup"></a>

Copies an existing backup within the same AWS account to another AWS Region (cross-Region copy) or within the same AWS Region (in-Region copy). You can have up to five backup copy requests in progress to a single destination Region per account.

You can use cross-Region backup copies for cross-Region disaster recovery. You can periodically take backups and copy them to another Region so that in the event of a disaster in the primary Region, you can restore from backup and recover availability quickly in the other Region. You can make cross-Region copies only within your AWS partition. A partition is a grouping of Regions. AWS currently has three partitions: `aws` (Standard Regions), `aws-cn` (China Regions), and `aws-us-gov` (AWS GovCloud [US] Regions).

You can also use backup copies to clone your file dataset to another Region or within the same Region.

You can use the `SourceRegion` parameter to specify the AWS Region from which the backup will be copied. For example, if you make the call from the `us-west-1` Region and want to copy a backup from the `us-east-2` Region, you specify `us-east-2` in the `SourceRegion` parameter to make a cross-Region copy. If you don't specify a Region, the backup copy is created in the same Region where the request is sent from (in-Region copy).

For more information about creating backup copies, see [ Copying backups](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/using-backups.html#copy-backups) in the *Amazon FSx for Windows User Guide*, [Copying backups](https://docs.aws.amazon.com/fsx/latest/LustreGuide/using-backups-fsx.html#copy-backups) in the *Amazon FSx for Lustre User Guide*, and [Copying backups](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/using-backups.html#copy-backups) in the *Amazon FSx for OpenZFS User Guide*.

## Request Syntax
<a name="API_CopyBackup_RequestSyntax"></a>

```
{
   "ClientRequestToken": "{{string}}",
   "CopyTags": {{boolean}},
   "KmsKeyId": "{{string}}",
   "SourceBackupId": "{{string}}",
   "SourceRegion": "{{string}}",
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CopyBackup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_CopyBackup_RequestSyntax) **   <a name="FSx-CopyBackup-request-ClientRequestToken"></a>
(Optional) An idempotency token for resource creation, in a string of up to 63 ASCII characters. This token is automatically filled on your behalf when you use the AWS Command Line Interface (AWS CLI) or an AWS SDK.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[A-za-z0-9_.-]{0,63}$`   
Required: No

 ** [CopyTags](#API_CopyBackup_RequestSyntax) **   <a name="FSx-CopyBackup-request-CopyTags"></a>
A Boolean flag indicating whether tags from the source backup should be copied to the backup copy. This value defaults to `false`.  
If you set `CopyTags` to `true` and the source backup has existing tags, you can use the `Tags` parameter to create new tags, provided that the sum of the source backup tags and the new tags doesn't exceed 50. Both sets of tags are merged. If there are tag conflicts (for example, two tags with the same key but different values), the tags created with the `Tags` parameter take precedence.  
Type: Boolean  
Required: No

 ** [KmsKeyId](#API_CopyBackup_RequestSyntax) **   <a name="FSx-CopyBackup-request-KmsKeyId"></a>
Specifies the ID of the AWS Key Management Service (AWS KMS) key to use for encrypting data on Amazon FSx file systems, as follows:  
+ Amazon FSx for Lustre `PERSISTENT_1` and `PERSISTENT_2` deployment types only.

   `SCRATCH_1` and `SCRATCH_2` types are encrypted using the Amazon FSx service AWS KMS key for your account.
+ Amazon FSx for NetApp ONTAP
+ Amazon FSx for OpenZFS
+ Amazon FSx for Windows File Server
If a `KmsKeyId` isn't specified, the Amazon FSx-managed AWS KMS key for your account is used. For more information, see [Encrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html) in the * AWS Key Management Service API Reference*.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `^.{1,2048}$`   
Required: No

 ** [SourceBackupId](#API_CopyBackup_RequestSyntax) **   <a name="FSx-CopyBackup-request-SourceBackupId"></a>
The ID of the source backup. Specifies the ID of the backup that's being copied.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 128.  
Pattern: `^(backup-[0-9a-f]{8,})$`   
Required: Yes

 ** [SourceRegion](#API_CopyBackup_RequestSyntax) **   <a name="FSx-CopyBackup-request-SourceRegion"></a>
The source AWS Region of the backup. Specifies the AWS Region from which the backup is being copied. The source and destination Regions must be in the same AWS partition. If you don't specify a Region, `SourceRegion` defaults to the Region where the request is sent from (in-Region copy).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 20.  
Pattern: `^[a-z0-9-]{1,20}$`   
Required: No

 ** [Tags](#API_CopyBackup_RequestSyntax) **   <a name="FSx-CopyBackup-request-Tags"></a>
A list of `Tag` values, with a maximum of 50 elements.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 50 items.  
Required: No

## Response Syntax
<a name="API_CopyBackup_ResponseSyntax"></a>

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
<a name="API_CopyBackup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Backup](#API_CopyBackup_ResponseSyntax) **   <a name="FSx-CopyBackup-response-Backup"></a>
A backup of an Amazon FSx for Windows File Server, Amazon FSx for Lustre file system, Amazon FSx for NetApp ONTAP volume, or Amazon FSx for OpenZFS file system.  
Type: [Backup](API_Backup.md) object

## Errors
<a name="API_CopyBackup_Errors"></a>

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

 ** IncompatibleParameterError **   
The error returned when a second request is received with the same client request token but different parameters settings. A client request token should always uniquely identify a single request.    
 ** Message **   
A detailed error message.  
 ** Parameter **   
A parameter that is incompatible with the earlier request.
HTTP Status Code: 400

 ** IncompatibleRegionForMultiAZ **   
Amazon FSx doesn't support Multi-AZ Windows File Server copy backup in the destination Region, so the copied backup can't be restored.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** InternalServerError **   
A generic error indicating a server-side failure.    
 ** Message **   
A detailed error message.
HTTP Status Code: 500

 ** InvalidDestinationKmsKey **   
The AWS Key Management Service (AWS KMS) key of the destination backup is not valid.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** InvalidRegion **   
The Region provided for `SourceRegion` is not valid or is in a different AWS partition.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** InvalidSourceKmsKey **   
The AWS Key Management Service (AWS KMS) key of the source backup is not valid.    
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

 ** SourceBackupUnavailable **   
The request was rejected because the lifecycle status of the source backup isn't `AVAILABLE`.    
 ** BackupId **   
The ID of the source backup. Specifies the backup that you are copying.  
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** UnsupportedOperation **   
The requested operation is not supported for this resource or API.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

## See Also
<a name="API_CopyBackup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/CopyBackup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/CopyBackup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/CopyBackup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/CopyBackup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/CopyBackup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/CopyBackup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/CopyBackup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/CopyBackup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/CopyBackup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/CopyBackup) 