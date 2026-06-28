---
id: "@specs/aws/fsx/docs/API_DescribeBackups"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeBackups"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# DescribeBackups

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_DescribeBackups
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeBackups
<a name="API_DescribeBackups"></a>

Returns the description of a specific Amazon FSx backup, if a `BackupIds` value is provided for that backup. Otherwise, it returns all backups owned by your AWS account in the AWS Region of the endpoint that you're calling.

When retrieving all backups, you can optionally specify the `MaxResults` parameter to limit the number of backups in a response. If more backups remain, Amazon FSx returns a `NextToken` value in the response. In this case, send a later request with the `NextToken` request parameter set to the value of the `NextToken` value from the last response.

This operation is used in an iterative process to retrieve a list of your backups. `DescribeBackups` is called first without a `NextToken` value. Then the operation continues to be called with the `NextToken` parameter set to the value of the last `NextToken` value until a response has no `NextToken` value.

When using this operation, keep the following in mind:
+ The operation might return fewer than the `MaxResults` value of backup descriptions while still including a `NextToken` value.
+ The order of the backups returned in the response of one `DescribeBackups` call and the order of the backups returned across the responses of a multi-call iteration is unspecified.

## Request Syntax
<a name="API_DescribeBackups_RequestSyntax"></a>

```
{
   "BackupIds": [ "{{string}}" ],
   "Filters": [ 
      { 
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeBackups_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [BackupIds](#API_DescribeBackups_RequestSyntax) **   <a name="FSx-DescribeBackups-request-BackupIds"></a>
The IDs of the backups that you want to retrieve. This parameter value overrides any filters. If any IDs aren't found, a `BackupNotFound` error occurs.  
Type: Array of strings  
Array Members: Maximum number of 50 items.  
Length Constraints: Minimum length of 12. Maximum length of 128.  
Pattern: `^(backup-[0-9a-f]{8,})$`   
Required: No

 ** [Filters](#API_DescribeBackups_RequestSyntax) **   <a name="FSx-DescribeBackups-request-Filters"></a>
The filters structure. The supported names are `file-system-id`, `backup-type`, `file-system-type`, and `volume-id`.  
Type: Array of [Filter](API_Filter.md) objects  
Array Members: Maximum number of 10 items.  
Required: No

 ** [MaxResults](#API_DescribeBackups_RequestSyntax) **   <a name="FSx-DescribeBackups-request-MaxResults"></a>
Maximum number of backups to return in the response. This parameter value must be greater than 0. The number of items that Amazon FSx returns is the minimum of the `MaxResults` parameter specified in the request and the service's internal maximum number of items per page.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 2147483647.  
Required: No

 ** [NextToken](#API_DescribeBackups_RequestSyntax) **   <a name="FSx-DescribeBackups-request-NextToken"></a>
An opaque pagination token returned from a previous `DescribeBackups` operation. If a token is present, the operation continues the list from where the returning call left off.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$`   
Required: No

## Response Syntax
<a name="API_DescribeBackups_ResponseSyntax"></a>

```
{
   "Backups": [ 
      { 
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
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeBackups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Backups](#API_DescribeBackups_ResponseSyntax) **   <a name="FSx-DescribeBackups-response-Backups"></a>
An array of backups.  
Type: Array of [Backup](API_Backup.md) objects  
Array Members: Maximum number of 50 items.

 ** [NextToken](#API_DescribeBackups_ResponseSyntax) **   <a name="FSx-DescribeBackups-response-NextToken"></a>
A `NextToken` value is present if there are more backups than returned in the response. You can use the `NextToken` value in the subsequent request to fetch the backups.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$` 

## Errors
<a name="API_DescribeBackups_Errors"></a>

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

 ** InternalServerError **   
A generic error indicating a server-side failure.    
 ** Message **   
A detailed error message.
HTTP Status Code: 500

 ** VolumeNotFound **   
No Amazon FSx volumes were found based upon the supplied parameters.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

## See Also
<a name="API_DescribeBackups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/DescribeBackups) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/DescribeBackups) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/DescribeBackups) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/DescribeBackups) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/DescribeBackups) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/DescribeBackups) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/DescribeBackups) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/DescribeBackups) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/DescribeBackups) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/DescribeBackups) 