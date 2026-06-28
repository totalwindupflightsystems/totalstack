---
id: "@specs/aws/fsx/docs/API_CreateFileSystemFromBackup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateFileSystemFromBackup"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# CreateFileSystemFromBackup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_CreateFileSystemFromBackup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateFileSystemFromBackup
<a name="API_CreateFileSystemFromBackup"></a>

Creates a new Amazon FSx for Lustre, Amazon FSx for Windows File Server, or Amazon FSx for OpenZFS file system from an existing Amazon FSx backup.

If a file system with the specified client request token exists and the parameters match, this operation returns the description of the file system. If a file system with the specified client request token exists but the parameters don't match, this call returns `IncompatibleParameterError`. If a file system with the specified client request token doesn't exist, this operation does the following:
+ Creates a new Amazon FSx file system from backup with an assigned ID, and an initial lifecycle state of `CREATING`.
+ Returns the description of the file system.

Parameters like the Active Directory, default share name, automatic backup, and backup settings default to the parameters of the file system that was backed up, unless overridden. You can explicitly supply other settings.

By using the idempotent operation, you can retry a `CreateFileSystemFromBackup` call without the risk of creating an extra file system. This approach can be useful when an initial call fails in a way that makes it unclear whether a file system was created. Examples are if a transport level timeout occurred, or your connection was reset. If you use the same client request token and the initial call created a file system, the client receives a success message as long as the parameters are the same.

**Note**  
The `CreateFileSystemFromBackup` call returns while the file system's lifecycle state is still `CREATING`. You can check the file-system creation status by calling the [ DescribeFileSystems](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeFileSystems.html) operation, which returns the file system state along with other information.

## Request Syntax
<a name="API_CreateFileSystemFromBackup_RequestSyntax"></a>

```
{
   "BackupId": "{{string}}",
   "ClientRequestToken": "{{string}}",
   "FileSystemTypeVersion": "{{string}}",
   "KmsKeyId": "{{string}}",
   "LustreConfiguration": { 
      "AutoImportPolicy": "{{string}}",
      "AutomaticBackupRetentionDays": {{number}},
      "CopyTagsToBackups": {{boolean}},
      "DailyAutomaticBackupStartTime": "{{string}}",
      "DataCompressionType": "{{string}}",
      "DataReadCacheConfiguration": { 
         "SizeGiB": {{number}},
         "SizingMode": "{{string}}"
      },
      "DeploymentType": "{{string}}",
      "DriveCacheType": "{{string}}",
      "EfaEnabled": {{boolean}},
      "ExportPath": "{{string}}",
      "ImportedFileChunkSize": {{number}},
      "ImportPath": "{{string}}",
      "LogConfiguration": { 
         "Destination": "{{string}}",
         "Level": "{{string}}"
      },
      "MetadataConfiguration": { 
         "Iops": {{number}},
         "Mode": "{{string}}"
      },
      "PerUnitStorageThroughput": {{number}},
      "RootSquashConfiguration": { 
         "NoSquashNids": [ "{{string}}" ],
         "RootSquash": "{{string}}"
      },
      "ThroughputCapacity": {{number}},
      "WeeklyMaintenanceStartTime": "{{string}}"
   },
   "NetworkType": "{{string}}",
   "OpenZFSConfiguration": { 
      "AutomaticBackupRetentionDays": {{number}},
      "CopyTagsToBackups": {{boolean}},
      "CopyTagsToVolumes": {{boolean}},
      "DailyAutomaticBackupStartTime": "{{string}}",
      "DeploymentType": "{{string}}",
      "DiskIopsConfiguration": { 
         "Iops": {{number}},
         "Mode": "{{string}}"
      },
      "EndpointIpAddressRange": "{{string}}",
      "EndpointIpv6AddressRange": "{{string}}",
      "PreferredSubnetId": "{{string}}",
      "ReadCacheConfiguration": { 
         "SizeGiB": {{number}},
         "SizingMode": "{{string}}"
      },
      "RootVolumeConfiguration": { 
         "CopyTagsToSnapshots": {{boolean}},
         "DataCompressionType": "{{string}}",
         "NfsExports": [ 
            { 
               "ClientConfigurations": [ 
                  { 
                     "Clients": "{{string}}",
                     "Options": [ "{{string}}" ]
                  }
               ]
            }
         ],
         "ReadOnly": {{boolean}},
         "RecordSizeKiB": {{number}},
         "UserAndGroupQuotas": [ 
            { 
               "Id": {{number}},
               "StorageCapacityQuotaGiB": {{number}},
               "Type": "{{string}}"
            }
         ]
      },
      "RouteTableIds": [ "{{string}}" ],
      "ThroughputCapacity": {{number}},
      "WeeklyMaintenanceStartTime": "{{string}}"
   },
   "SecurityGroupIds": [ "{{string}}" ],
   "StorageCapacity": {{number}},
   "StorageType": "{{string}}",
   "SubnetIds": [ "{{string}}" ],
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "WindowsConfiguration": { 
      "ActiveDirectoryId": "{{string}}",
      "Aliases": [ "{{string}}" ],
      "AuditLogConfiguration": { 
         "AuditLogDestination": "{{string}}",
         "FileAccessAuditLogLevel": "{{string}}",
         "FileShareAccessAuditLogLevel": "{{string}}"
      },
      "AutomaticBackupRetentionDays": {{number}},
      "CopyTagsToBackups": {{boolean}},
      "DailyAutomaticBackupStartTime": "{{string}}",
      "DeploymentType": "{{string}}",
      "DiskIopsConfiguration": { 
         "Iops": {{number}},
         "Mode": "{{string}}"
      },
      "FsrmConfiguration": { 
         "EventLogDestination": "{{string}}",
         "FsrmServiceEnabled": {{boolean}}
      },
      "PreferredSubnetId": "{{string}}",
      "SelfManagedActiveDirectoryConfiguration": { 
         "DnsIps": [ "{{string}}" ],
         "DomainJoinServiceAccountSecret": "{{string}}",
         "DomainName": "{{string}}",
         "FileSystemAdministratorsGroup": "{{string}}",
         "OrganizationalUnitDistinguishedName": "{{string}}",
         "Password": "{{string}}",
         "UserName": "{{string}}"
      },
      "ThroughputCapacity": {{number}},
      "WeeklyMaintenanceStartTime": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateFileSystemFromBackup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [BackupId](#API_CreateFileSystemFromBackup_RequestSyntax) **   <a name="FSx-CreateFileSystemFromBackup-request-BackupId"></a>
The ID of the source backup. Specifies the backup that you are copying.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 128.  
Pattern: `^(backup-[0-9a-f]{8,})$`   
Required: Yes

 ** [ClientRequestToken](#API_CreateFileSystemFromBackup_RequestSyntax) **   <a name="FSx-CreateFileSystemFromBackup-request-ClientRequestToken"></a>
A string of up to 63 ASCII characters that Amazon FSx uses to ensure idempotent creation. This string is automatically filled on your behalf when you use the AWS Command Line Interface (AWS CLI) or an AWS SDK.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[A-za-z0-9_.-]{0,63}$`   
Required: No

 ** [FileSystemTypeVersion](#API_CreateFileSystemFromBackup_RequestSyntax) **   <a name="FSx-CreateFileSystemFromBackup-request-FileSystemTypeVersion"></a>
Sets the version for the Amazon FSx for Lustre file system that you're creating from a backup. Valid values are `2.10`, `2.12`, and `2.15`.  
You can enter a Lustre version that is newer than the backup's `FileSystemTypeVersion` setting. If you don't enter a newer Lustre version, it defaults to the backup's setting.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 20.  
Pattern: `^[0-9](.[0-9]*)*$`   
Required: No

 ** [KmsKeyId](#API_CreateFileSystemFromBackup_RequestSyntax) **   <a name="FSx-CreateFileSystemFromBackup-request-KmsKeyId"></a>
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

 ** [LustreConfiguration](#API_CreateFileSystemFromBackup_RequestSyntax) **   <a name="FSx-CreateFileSystemFromBackup-request-LustreConfiguration"></a>
The Lustre configuration for the file system being created.  
The following parameters are not supported for file systems with a data repository association created with [CreateDataRepositoryAssociation](API_CreateDataRepositoryAssociation.md).  
+  `AutoImportPolicy` 
+  `ExportPath` 
+  `ImportedFileChunkSize` 
+  `ImportPath` 
Type: [CreateFileSystemLustreConfiguration](API_CreateFileSystemLustreConfiguration.md) object  
Required: No

 ** [NetworkType](#API_CreateFileSystemFromBackup_RequestSyntax) **   <a name="FSx-CreateFileSystemFromBackup-request-NetworkType"></a>
Sets the network type for the Amazon FSx for OpenZFS file system that you're creating from a backup.  
Type: String  
Valid Values: `IPV4 | DUAL`   
Required: No

 ** [OpenZFSConfiguration](#API_CreateFileSystemFromBackup_RequestSyntax) **   <a name="FSx-CreateFileSystemFromBackup-request-OpenZFSConfiguration"></a>
The OpenZFS configuration for the file system that's being created.   
Type: [CreateFileSystemOpenZFSConfiguration](API_CreateFileSystemOpenZFSConfiguration.md) object  
Required: No

 ** [SecurityGroupIds](#API_CreateFileSystemFromBackup_RequestSyntax) **   <a name="FSx-CreateFileSystemFromBackup-request-SecurityGroupIds"></a>
A list of IDs for the security groups that apply to the specified network interfaces created for file system access. These security groups apply to all network interfaces. This value isn't returned in later `DescribeFileSystem` requests.  
Type: Array of strings  
Array Members: Maximum number of 50 items.  
Length Constraints: Minimum length of 11. Maximum length of 20.  
Pattern: `^(sg-[0-9a-f]{8,})$`   
Required: No

 ** [StorageCapacity](#API_CreateFileSystemFromBackup_RequestSyntax) **   <a name="FSx-CreateFileSystemFromBackup-request-StorageCapacity"></a>
Sets the storage capacity of the OpenZFS file system that you're creating from a backup, in gibibytes (GiB). Valid values are from 64 GiB up to 524,288 GiB (512 TiB). However, the value that you specify must be equal to or greater than the backup's storage capacity value. If you don't use the `StorageCapacity` parameter, the default is the backup's `StorageCapacity` value.  
If used to create a file system other than OpenZFS, you must provide a value that matches the backup's `StorageCapacity` value. If you provide any other value, Amazon FSx responds with an HTTP status code 400 Bad Request.   
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 2147483647.  
Required: No

 ** [StorageType](#API_CreateFileSystemFromBackup_RequestSyntax) **   <a name="FSx-CreateFileSystemFromBackup-request-StorageType"></a>
Sets the storage type for the Windows, OpenZFS, or Lustre file system that you're creating from a backup. Valid values are `SSD`, `HDD`, and `INTELLIGENT_TIERING`.  
+ Set to `SSD` to use solid state drive storage. SSD is supported on all Windows and OpenZFS deployment types.
+ Set to `HDD` to use hard disk drive storage. HDD is supported on `SINGLE_AZ_2` and `MULTI_AZ_1` FSx for Windows File Server file system deployment types.
+ Set to `INTELLIGENT_TIERING` to use fully elastic, intelligently-tiered storage. Intelligent-Tiering is only available for OpenZFS file systems with the Multi-AZ deployment type and for Lustre file systems with the Persistent\_2 deployment type.
 The default value is `SSD`.   
HDD and SSD storage types have different minimum storage capacity requirements. A restored file system's storage capacity is tied to the file system that was backed up. You can create a file system that uses HDD storage from a backup of a file system that used SSD storage if the original SSD file system had a storage capacity of at least 2000 GiB.
Type: String  
Valid Values: `SSD | HDD | INTELLIGENT_TIERING`   
Required: No

 ** [SubnetIds](#API_CreateFileSystemFromBackup_RequestSyntax) **   <a name="FSx-CreateFileSystemFromBackup-request-SubnetIds"></a>
Specifies the IDs of the subnets that the file system will be accessible from. For Windows `MULTI_AZ_1` file system deployment types, provide exactly two subnet IDs, one for the preferred file server and one for the standby file server. You specify one of these subnets as the preferred subnet using the `WindowsConfiguration > PreferredSubnetID` property.  
Windows `SINGLE_AZ_1` and `SINGLE_AZ_2` file system deployment types, Lustre file systems, and OpenZFS file systems provide exactly one subnet ID. The file server is launched in that subnet's Availability Zone.  
Type: Array of strings  
Array Members: Maximum number of 50 items.  
Length Constraints: Minimum length of 15. Maximum length of 24.  
Pattern: `^(subnet-[0-9a-f]{8,})$`   
Required: Yes

 ** [Tags](#API_CreateFileSystemFromBackup_RequestSyntax) **   <a name="FSx-CreateFileSystemFromBackup-request-Tags"></a>
The tags to be applied to the file system at file system creation. The key value of the `Name` tag appears in the console as the file system name.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 50 items.  
Required: No

 ** [WindowsConfiguration](#API_CreateFileSystemFromBackup_RequestSyntax) **   <a name="FSx-CreateFileSystemFromBackup-request-WindowsConfiguration"></a>
The configuration for this Microsoft Windows file system.  
Type: [CreateFileSystemWindowsConfiguration](API_CreateFileSystemWindowsConfiguration.md) object  
Required: No

## Response Syntax
<a name="API_CreateFileSystemFromBackup_ResponseSyntax"></a>

```
{
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
   }
}
```

## Response Elements
<a name="API_CreateFileSystemFromBackup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FileSystem](#API_CreateFileSystemFromBackup_ResponseSyntax) **   <a name="FSx-CreateFileSystemFromBackup-response-FileSystem"></a>
A description of the file system.  
Type: [FileSystem](API_FileSystem.md) object

## Errors
<a name="API_CreateFileSystemFromBackup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ActiveDirectoryError **   
An Active Directory error.    
 ** ActiveDirectoryId **   
The directory ID of the directory that an error pertains to.  
 ** Message **   
A detailed error message.  
 ** Type **   
The type of Active Directory error.
HTTP Status Code: 400

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

 ** InternalServerError **   
A generic error indicating a server-side failure.    
 ** Message **   
A detailed error message.
HTTP Status Code: 500

 ** InvalidNetworkSettings **   
One or more network settings specified in the request are invalid.    
 ** InvalidRouteTableId **   
The route table ID is either invalid or not part of the VPC specified.  
 ** InvalidSecurityGroupId **   
The security group ID is either invalid or not part of the VPC specified.  
 ** InvalidSubnetId **   
The subnet ID that is either invalid or not part of the VPC specified.  
 ** Message **   
Error message explaining what's wrong with network settings.
HTTP Status Code: 400

 ** InvalidPerUnitStorageThroughput **   
An invalid value for `PerUnitStorageThroughput` was provided. Please create your file system again, using a valid value.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** MissingFileSystemConfiguration **   
A file system configuration is required for this operation.    
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

## See Also
<a name="API_CreateFileSystemFromBackup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/CreateFileSystemFromBackup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/CreateFileSystemFromBackup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/CreateFileSystemFromBackup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/CreateFileSystemFromBackup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/CreateFileSystemFromBackup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/CreateFileSystemFromBackup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/CreateFileSystemFromBackup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/CreateFileSystemFromBackup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/CreateFileSystemFromBackup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/CreateFileSystemFromBackup) 