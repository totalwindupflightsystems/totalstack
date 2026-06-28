---
id: "@specs/aws/fsx/docs/API_CopySnapshotAndUpdateVolume"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CopySnapshotAndUpdateVolume"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# CopySnapshotAndUpdateVolume

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_CopySnapshotAndUpdateVolume
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CopySnapshotAndUpdateVolume
<a name="API_CopySnapshotAndUpdateVolume"></a>

Updates an existing volume by using a snapshot from another Amazon FSx for OpenZFS file system. For more information, see [on-demand data replication](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/on-demand-replication.html) in the Amazon FSx for OpenZFS User Guide.

## Request Syntax
<a name="API_CopySnapshotAndUpdateVolume_RequestSyntax"></a>

```
{
   "ClientRequestToken": "{{string}}",
   "CopyStrategy": "{{string}}",
   "Options": [ "{{string}}" ],
   "SourceSnapshotARN": "{{string}}",
   "VolumeId": "{{string}}"
}
```

## Request Parameters
<a name="API_CopySnapshotAndUpdateVolume_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_CopySnapshotAndUpdateVolume_RequestSyntax) **   <a name="FSx-CopySnapshotAndUpdateVolume-request-ClientRequestToken"></a>
(Optional) An idempotency token for resource creation, in a string of up to 63 ASCII characters. This token is automatically filled on your behalf when you use the AWS Command Line Interface (AWS CLI) or an AWS SDK.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[A-za-z0-9_.-]{0,63}$`   
Required: No

 ** [CopyStrategy](#API_CopySnapshotAndUpdateVolume_RequestSyntax) **   <a name="FSx-CopySnapshotAndUpdateVolume-request-CopyStrategy"></a>
Specifies the strategy to use when copying data from a snapshot to the volume.   
+  `FULL_COPY` - Copies all data from the snapshot to the volume. 
+  `INCREMENTAL_COPY` - Copies only the snapshot data that's changed since the previous replication.
 `CLONE` isn't a valid copy strategy option for the `CopySnapshotAndUpdateVolume` operation.
Type: String  
Valid Values: `CLONE | FULL_COPY | INCREMENTAL_COPY`   
Required: No

 ** [Options](#API_CopySnapshotAndUpdateVolume_RequestSyntax) **   <a name="FSx-CopySnapshotAndUpdateVolume-request-Options"></a>
Confirms that you want to delete data on the destination volume that wasn’t there during the previous snapshot replication.  
Your replication will fail if you don’t include an option for a specific type of data and that data is on your destination. For example, if you don’t include `DELETE_INTERMEDIATE_SNAPSHOTS` and there are intermediate snapshots on the destination, you can’t copy the snapshot.  
+  `DELETE_INTERMEDIATE_SNAPSHOTS` - Deletes snapshots on the destination volume that aren’t on the source volume.
+  `DELETE_CLONED_VOLUMES` - Deletes snapshot clones on the destination volume that aren't on the source volume.
+  `DELETE_INTERMEDIATE_DATA` - Overwrites snapshots on the destination volume that don’t match the source snapshot that you’re copying.
Type: Array of strings  
Valid Values: `DELETE_INTERMEDIATE_SNAPSHOTS | DELETE_CLONED_VOLUMES | DELETE_INTERMEDIATE_DATA`   
Required: No

 ** [SourceSnapshotARN](#API_CopySnapshotAndUpdateVolume_RequestSyntax) **   <a name="FSx-CopySnapshotAndUpdateVolume-request-SourceSnapshotARN"></a>
The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify AWS resources. We require an ARN when you need to specify a resource unambiguously across all of AWS. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.  
Type: String  
Length Constraints: Minimum length of 8. Maximum length of 512.  
Pattern: `^arn:(?=[^:]+:fsx:[^:]+:\d{12}:)((|(?=[a-z0-9-.]{1,63})(?!\d{1,3}(\.\d{1,3}){3})(?![^:]*-{2})(?![^:]*-\.)(?![^:]*\.-)[a-z0-9].*(?<!-)):){4}(?!/).{0,1024}$`   
Required: Yes

 ** [VolumeId](#API_CopySnapshotAndUpdateVolume_RequestSyntax) **   <a name="FSx-CopySnapshotAndUpdateVolume-request-VolumeId"></a>
Specifies the ID of the volume that you are copying the snapshot to.  
Type: String  
Length Constraints: Fixed length of 23.  
Pattern: `^(fsvol-[0-9a-f]{17,})$`   
Required: Yes

## Response Syntax
<a name="API_CopySnapshotAndUpdateVolume_ResponseSyntax"></a>

```
{
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
   "Lifecycle": "string",
   "VolumeId": "string"
}
```

## Response Elements
<a name="API_CopySnapshotAndUpdateVolume_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AdministrativeActions](#API_CopySnapshotAndUpdateVolume_ResponseSyntax) **   <a name="FSx-CopySnapshotAndUpdateVolume-response-AdministrativeActions"></a>
A list of administrative actions for the file system that are in process or waiting to be processed. Administrative actions describe changes to the Amazon FSx system.  
Type: Array of [AdministrativeAction](API_AdministrativeAction.md) objects  
Array Members: Maximum number of 50 items.

 ** [Lifecycle](#API_CopySnapshotAndUpdateVolume_ResponseSyntax) **   <a name="FSx-CopySnapshotAndUpdateVolume-response-Lifecycle"></a>
The lifecycle state of the destination volume.   
Type: String  
Valid Values: `CREATING | CREATED | DELETING | FAILED | MISCONFIGURED | PENDING | AVAILABLE` 

 ** [VolumeId](#API_CopySnapshotAndUpdateVolume_ResponseSyntax) **   <a name="FSx-CopySnapshotAndUpdateVolume-response-VolumeId"></a>
The ID of the volume that you copied the snapshot to.  
Type: String  
Length Constraints: Fixed length of 23.  
Pattern: `^(fsvol-[0-9a-f]{17,})$` 

## Errors
<a name="API_CopySnapshotAndUpdateVolume_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** ServiceLimitExceeded **   
An error indicating that a particular service limit was exceeded. You can increase some service limits by contacting AWS Support.    
 ** Limit **   
Enumeration of the service limit that was exceeded.   
 ** Message **   
A detailed error message.
HTTP Status Code: 400

## See Also
<a name="API_CopySnapshotAndUpdateVolume_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/CopySnapshotAndUpdateVolume) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/CopySnapshotAndUpdateVolume) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/CopySnapshotAndUpdateVolume) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/CopySnapshotAndUpdateVolume) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/CopySnapshotAndUpdateVolume) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/CopySnapshotAndUpdateVolume) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/CopySnapshotAndUpdateVolume) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/CopySnapshotAndUpdateVolume) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/CopySnapshotAndUpdateVolume) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/CopySnapshotAndUpdateVolume) 