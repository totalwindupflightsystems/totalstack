---
id: "@specs/aws/fsx/docs/API_DescribeSnapshots"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeSnapshots"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# DescribeSnapshots

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_DescribeSnapshots
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeSnapshots
<a name="API_DescribeSnapshots"></a>

Returns the description of specific Amazon FSx for OpenZFS snapshots, if a `SnapshotIds` value is provided. Otherwise, this operation returns all snapshots owned by your AWS account in the AWS Region of the endpoint that you're calling.

When retrieving all snapshots, you can optionally specify the `MaxResults` parameter to limit the number of snapshots in a response. If more backups remain, Amazon FSx returns a `NextToken` value in the response. In this case, send a later request with the `NextToken` request parameter set to the value of `NextToken` from the last response. 

Use this operation in an iterative process to retrieve a list of your snapshots. `DescribeSnapshots` is called first without a `NextToken` value. Then the operation continues to be called with the `NextToken` parameter set to the value of the last `NextToken` value until a response has no `NextToken` value.

When using this operation, keep the following in mind:
+ The operation might return fewer than the `MaxResults` value of snapshot descriptions while still including a `NextToken` value.
+ The order of snapshots returned in the response of one `DescribeSnapshots` call and the order of backups returned across the responses of a multi-call iteration is unspecified. 

## Request Syntax
<a name="API_DescribeSnapshots_RequestSyntax"></a>

```
{
   "Filters": [ 
      { 
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "IncludeShared": {{boolean}},
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SnapshotIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeSnapshots_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeSnapshots_RequestSyntax) **   <a name="FSx-DescribeSnapshots-request-Filters"></a>
The filters structure. The supported names are `file-system-id` or `volume-id`.  
Type: Array of [SnapshotFilter](API_SnapshotFilter.md) objects  
Array Members: Maximum number of 2 items.  
Required: No

 ** [IncludeShared](#API_DescribeSnapshots_RequestSyntax) **   <a name="FSx-DescribeSnapshots-request-IncludeShared"></a>
Set to `false` (default) if you want to only see the snapshots owned by your AWS account. Set to `true` if you want to see the snapshots in your account and the ones shared with you from another account.  
Type: Boolean  
Required: No

 ** [MaxResults](#API_DescribeSnapshots_RequestSyntax) **   <a name="FSx-DescribeSnapshots-request-MaxResults"></a>
The maximum number of resources to return in the response. This value must be an integer greater than zero.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 2147483647.  
Required: No

 ** [NextToken](#API_DescribeSnapshots_RequestSyntax) **   <a name="FSx-DescribeSnapshots-request-NextToken"></a>
(Optional) Opaque pagination token returned from a previous operation (String). If present, this token indicates from what point you can continue processing the request, where the previous `NextToken` value left off.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$`   
Required: No

 ** [SnapshotIds](#API_DescribeSnapshots_RequestSyntax) **   <a name="FSx-DescribeSnapshots-request-SnapshotIds"></a>
The IDs of the snapshots that you want to retrieve. This parameter value overrides any filters. If any IDs aren't found, a `SnapshotNotFound` error occurs.  
Type: Array of strings  
Array Members: Maximum number of 50 items.  
Length Constraints: Minimum length of 11. Maximum length of 28.  
Pattern: `^((fs)?volsnap-[0-9a-f]{8,})$`   
Required: No

## Response Syntax
<a name="API_DescribeSnapshots_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Snapshots": [ 
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
               "TargetSnapshotValues": "Snapshot",
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
      }
   ]
}
```

## Response Elements
<a name="API_DescribeSnapshots_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeSnapshots_ResponseSyntax) **   <a name="FSx-DescribeSnapshots-response-NextToken"></a>
(Optional) Opaque pagination token returned from a previous operation (String). If present, this token indicates from what point you can continue processing the request, where the previous `NextToken` value left off.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$` 

 ** [Snapshots](#API_DescribeSnapshots_ResponseSyntax) **   <a name="FSx-DescribeSnapshots-response-Snapshots"></a>
An array of snapshots.  
Type: Array of [Snapshot](API_Snapshot.md) objects  
Array Members: Maximum number of 50 items.

## Errors
<a name="API_DescribeSnapshots_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequest **   
A generic error indicating a failure with a client request.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** InternalServerError **   
A generic error indicating a server-side failure.    
 ** Message **   
A detailed error message.
HTTP Status Code: 500

 ** SnapshotNotFound **   
No Amazon FSx snapshots were found based on the supplied parameters.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

## See Also
<a name="API_DescribeSnapshots_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/DescribeSnapshots) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/DescribeSnapshots) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/DescribeSnapshots) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/DescribeSnapshots) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/DescribeSnapshots) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/DescribeSnapshots) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/DescribeSnapshots) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/DescribeSnapshots) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/DescribeSnapshots) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/DescribeSnapshots) 