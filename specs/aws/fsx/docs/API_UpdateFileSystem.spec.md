---
id: "@specs/aws/fsx/docs/API_UpdateFileSystem"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateFileSystem"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# UpdateFileSystem

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_UpdateFileSystem
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateFileSystem
<a name="API_UpdateFileSystem"></a>

Use this operation to update the configuration of an existing Amazon FSx file system. You can update multiple properties in a single request.

For FSx for Windows File Server file systems, you can update the following properties:
+  `AuditLogConfiguration` 
+  `AutomaticBackupRetentionDays` 
+  `DailyAutomaticBackupStartTime` 
+  `DiskIopsConfiguration` 
+  `SelfManagedActiveDirectoryConfiguration` 
+  `StorageCapacity` 
+  `StorageType` 
+  `ThroughputCapacity` 
+  `WeeklyMaintenanceStartTime` 

For FSx for Lustre file systems, you can update the following properties:
+  `AutoImportPolicy` 
+  `AutomaticBackupRetentionDays` 
+  `DailyAutomaticBackupStartTime` 
+  `DataCompressionType` 
+  `FileSystemTypeVersion` 
+  `LogConfiguration` 
+  `LustreReadCacheConfiguration` 
+  `LustreRootSquashConfiguration` 
+  `MetadataConfiguration` 
+  `PerUnitStorageThroughput` 
+  `StorageCapacity` 
+  `ThroughputCapacity` 
+  `WeeklyMaintenanceStartTime` 

For FSx for ONTAP file systems, you can update the following properties:
+  `AddRouteTableIds` 
+  `AutomaticBackupRetentionDays` 
+  `DailyAutomaticBackupStartTime` 
+  `DiskIopsConfiguration` 
+  `EndpointIpv6AddressRange` 
+  `FsxAdminPassword` 
+  `HAPairs` 
+  `RemoveRouteTableIds` 
+  `StorageCapacity` 
+  `ThroughputCapacity` 
+  `ThroughputCapacityPerHAPair` 
+  `WeeklyMaintenanceStartTime` 

For FSx for OpenZFS file systems, you can update the following properties:
+  `AddRouteTableIds` 
+  `AutomaticBackupRetentionDays` 
+  `CopyTagsToBackups` 
+  `CopyTagsToVolumes` 
+  `DailyAutomaticBackupStartTime` 
+  `DiskIopsConfiguration` 
+  `EndpointIpv6AddressRange` 
+  `ReadCacheConfiguration` 
+  `RemoveRouteTableIds` 
+  `StorageCapacity` 
+  `ThroughputCapacity` 
+  `WeeklyMaintenanceStartTime` 

## Request Syntax
<a name="API_UpdateFileSystem_RequestSyntax"></a>

```
{
   "ClientRequestToken": "{{string}}",
   "FileSystemId": "{{string}}",
   "FileSystemTypeVersion": "{{string}}",
   "LustreConfiguration": { 
      "AutoImportPolicy": "{{string}}",
      "AutomaticBackupRetentionDays": {{number}},
      "DailyAutomaticBackupStartTime": "{{string}}",
      "DataCompressionType": "{{string}}",
      "DataReadCacheConfiguration": { 
         "SizeGiB": {{number}},
         "SizingMode": "{{string}}"
      },
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
   "OntapConfiguration": { 
      "AddRouteTableIds": [ "{{string}}" ],
      "AutomaticBackupRetentionDays": {{number}},
      "DailyAutomaticBackupStartTime": "{{string}}",
      "DiskIopsConfiguration": { 
         "Iops": {{number}},
         "Mode": "{{string}}"
      },
      "EndpointIpv6AddressRange": "{{string}}",
      "FsxAdminPassword": "{{string}}",
      "HAPairs": {{number}},
      "RemoveRouteTableIds": [ "{{string}}" ],
      "ThroughputCapacity": {{number}},
      "ThroughputCapacityPerHAPair": {{number}},
      "WeeklyMaintenanceStartTime": "{{string}}"
   },
   "OpenZFSConfiguration": { 
      "AddRouteTableIds": [ "{{string}}" ],
      "AutomaticBackupRetentionDays": {{number}},
      "CopyTagsToBackups": {{boolean}},
      "CopyTagsToVolumes": {{boolean}},
      "DailyAutomaticBackupStartTime": "{{string}}",
      "DiskIopsConfiguration": { 
         "Iops": {{number}},
         "Mode": "{{string}}"
      },
      "EndpointIpv6AddressRange": "{{string}}",
      "ReadCacheConfiguration": { 
         "SizeGiB": {{number}},
         "SizingMode": "{{string}}"
      },
      "RemoveRouteTableIds": [ "{{string}}" ],
      "ThroughputCapacity": {{number}},
      "WeeklyMaintenanceStartTime": "{{string}}"
   },
   "StorageCapacity": {{number}},
   "StorageType": "{{string}}",
   "WindowsConfiguration": { 
      "AuditLogConfiguration": { 
         "AuditLogDestination": "{{string}}",
         "FileAccessAuditLogLevel": "{{string}}",
         "FileShareAccessAuditLogLevel": "{{string}}"
      },
      "AutomaticBackupRetentionDays": {{number}},
      "DailyAutomaticBackupStartTime": "{{string}}",
      "DiskIopsConfiguration": { 
         "Iops": {{number}},
         "Mode": "{{string}}"
      },
      "FsrmConfiguration": { 
         "EventLogDestination": "{{string}}",
         "FsrmServiceEnabled": {{boolean}}
      },
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
<a name="API_UpdateFileSystem_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_UpdateFileSystem_RequestSyntax) **   <a name="FSx-UpdateFileSystem-request-ClientRequestToken"></a>
A string of up to 63 ASCII characters that Amazon FSx uses to ensure idempotent updates. This string is automatically filled on your behalf when you use the AWS Command Line Interface (AWS CLI) or an AWS SDK.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[A-za-z0-9_.-]{0,63}$`   
Required: No

 ** [FileSystemId](#API_UpdateFileSystem_RequestSyntax) **   <a name="FSx-UpdateFileSystem-request-FileSystemId"></a>
The ID of the file system that you are updating.  
Type: String  
Length Constraints: Minimum length of 11. Maximum length of 21.  
Pattern: `^(fs-[0-9a-f]{8,})$`   
Required: Yes

 ** [FileSystemTypeVersion](#API_UpdateFileSystem_RequestSyntax) **   <a name="FSx-UpdateFileSystem-request-FileSystemTypeVersion"></a>
The Lustre version you are updating an FSx for Lustre file system to. Valid values are `2.12` and `2.15`. The value you choose must be newer than the file system's current Lustre version.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 20.  
Pattern: `^[0-9](.[0-9]*)*$`   
Required: No

 ** [LustreConfiguration](#API_UpdateFileSystem_RequestSyntax) **   <a name="FSx-UpdateFileSystem-request-LustreConfiguration"></a>
The configuration object for Amazon FSx for Lustre file systems used in the `UpdateFileSystem` operation.  
Type: [UpdateFileSystemLustreConfiguration](API_UpdateFileSystemLustreConfiguration.md) object  
Required: No

 ** [NetworkType](#API_UpdateFileSystem_RequestSyntax) **   <a name="FSx-UpdateFileSystem-request-NetworkType"></a>
Changes the network type of an FSx for OpenZFS file system.  
Type: String  
Valid Values: `IPV4 | DUAL`   
Required: No

 ** [OntapConfiguration](#API_UpdateFileSystem_RequestSyntax) **   <a name="FSx-UpdateFileSystem-request-OntapConfiguration"></a>
The configuration updates for an Amazon FSx for NetApp ONTAP file system.  
Type: [UpdateFileSystemOntapConfiguration](API_UpdateFileSystemOntapConfiguration.md) object  
Required: No

 ** [OpenZFSConfiguration](#API_UpdateFileSystem_RequestSyntax) **   <a name="FSx-UpdateFileSystem-request-OpenZFSConfiguration"></a>
The configuration updates for an FSx for OpenZFS file system.  
Type: [UpdateFileSystemOpenZFSConfiguration](API_UpdateFileSystemOpenZFSConfiguration.md) object  
Required: No

 ** [StorageCapacity](#API_UpdateFileSystem_RequestSyntax) **   <a name="FSx-UpdateFileSystem-request-StorageCapacity"></a>
Use this parameter to increase the storage capacity of an FSx for Windows File Server, FSx for Lustre, FSx for OpenZFS, or FSx for ONTAP file system. For second-generation FSx for ONTAP file systems, you can also decrease the storage capacity. Specifies the storage capacity target value, in GiB, for the file system that you're updating.   
You can't make a storage capacity increase request if there is an existing storage capacity increase request in progress.
For Lustre file systems, the storage capacity target value can be the following:  
+ For `SCRATCH_2`, `PERSISTENT_1`, and `PERSISTENT_2 SSD` deployment types, valid values are in multiples of 2400 GiB. The value must be greater than the current storage capacity.
+ For `PERSISTENT HDD` file systems, valid values are multiples of 6000 GiB for 12-MBps throughput per TiB file systems and multiples of 1800 GiB for 40-MBps throughput per TiB file systems. The values must be greater than the current storage capacity.
+ For `SCRATCH_1` file systems, you can't increase the storage capacity.
For more information, see [Managing storage and throughput capacity](https://docs.aws.amazon.com/fsx/latest/LustreGuide/managing-storage-capacity.html) in the *FSx for Lustre User Guide*.  
For FSx for OpenZFS file systems, the storage capacity target value must be at least 10 percent greater than the current storage capacity value. For more information, see [Managing storage capacity](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/managing-storage-capacity.html) in the *FSx for OpenZFS User Guide*.  
For Windows file systems, the storage capacity target value must be at least 10 percent greater than the current storage capacity value. To increase storage capacity, the file system must have at least 16 MBps of throughput capacity. For more information, see [Managing storage capacity](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-storage-capacity.html) in the *Amazon FSxfor Windows File Server User Guide*.  
For ONTAP file systems, when increasing storage capacity, the storage capacity target value must be at least 10 percent greater than the current storage capacity value. When decreasing storage capacity on second-generation file systems, the target value must be at least 9 percent smaller than the current SSD storage capacity. For more information, see [File system storage capacity and IOPS](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/storage-capacity-and-IOPS.html) in the Amazon FSx for NetApp ONTAP User Guide.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 2147483647.  
Required: No

 ** [StorageType](#API_UpdateFileSystem_RequestSyntax) **   <a name="FSx-UpdateFileSystem-request-StorageType"></a>
Specifies the file system's storage type.  
Type: String  
Valid Values: `SSD | HDD | INTELLIGENT_TIERING`   
Required: No

 ** [WindowsConfiguration](#API_UpdateFileSystem_RequestSyntax) **   <a name="FSx-UpdateFileSystem-request-WindowsConfiguration"></a>
The configuration updates for an Amazon FSx for Windows File Server file system.  
Type: [UpdateFileSystemWindowsConfiguration](API_UpdateFileSystemWindowsConfiguration.md) object  
Required: No

## Response Syntax
<a name="API_UpdateFileSystem_ResponseSyntax"></a>

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
<a name="API_UpdateFileSystem_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FileSystem](#API_UpdateFileSystem_ResponseSyntax) **   <a name="FSx-UpdateFileSystem-response-FileSystem"></a>
A description of the file system that was updated.  
Type: [FileSystem](API_FileSystem.md) object

## Errors
<a name="API_UpdateFileSystem_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** UnsupportedOperation **   
The requested operation is not supported for this resource or API.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

## See Also
<a name="API_UpdateFileSystem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/UpdateFileSystem) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/UpdateFileSystem) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/UpdateFileSystem) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/UpdateFileSystem) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/UpdateFileSystem) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/UpdateFileSystem) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/UpdateFileSystem) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/UpdateFileSystem) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/UpdateFileSystem) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/UpdateFileSystem) 