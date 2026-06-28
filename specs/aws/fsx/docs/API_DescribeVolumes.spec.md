---
id: "@specs/aws/fsx/docs/API_DescribeVolumes"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeVolumes"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# DescribeVolumes

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_DescribeVolumes
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeVolumes
<a name="API_DescribeVolumes"></a>

Describes one or more Amazon FSx for NetApp ONTAP or Amazon FSx for OpenZFS volumes.

## Request Syntax
<a name="API_DescribeVolumes_RequestSyntax"></a>

```
{
   "Filters": [ 
      { 
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "VolumeIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeVolumes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeVolumes_RequestSyntax) **   <a name="FSx-DescribeVolumes-request-Filters"></a>
Enter a filter `Name` and `Values` pair to view a select set of volumes.  
Type: Array of [VolumeFilter](API_VolumeFilter.md) objects  
Array Members: Maximum number of 2 items.  
Required: No

 ** [MaxResults](#API_DescribeVolumes_RequestSyntax) **   <a name="FSx-DescribeVolumes-request-MaxResults"></a>
The maximum number of resources to return in the response. This value must be an integer greater than zero.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 2147483647.  
Required: No

 ** [NextToken](#API_DescribeVolumes_RequestSyntax) **   <a name="FSx-DescribeVolumes-request-NextToken"></a>
(Optional) Opaque pagination token returned from a previous operation (String). If present, this token indicates from what point you can continue processing the request, where the previous `NextToken` value left off.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$`   
Required: No

 ** [VolumeIds](#API_DescribeVolumes_RequestSyntax) **   <a name="FSx-DescribeVolumes-request-VolumeIds"></a>
The IDs of the volumes whose descriptions you want to retrieve.  
Type: Array of strings  
Array Members: Maximum number of 50 items.  
Length Constraints: Fixed length of 23.  
Pattern: `^(fsvol-[0-9a-f]{17,})$`   
Required: No

## Response Syntax
<a name="API_DescribeVolumes_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Volumes": [ 
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
   ]
}
```

## Response Elements
<a name="API_DescribeVolumes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeVolumes_ResponseSyntax) **   <a name="FSx-DescribeVolumes-response-NextToken"></a>
(Optional) Opaque pagination token returned from a previous operation (String). If present, this token indicates from what point you can continue processing the request, where the previous `NextToken` value left off.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$` 

 ** [Volumes](#API_DescribeVolumes_ResponseSyntax) **   <a name="FSx-DescribeVolumes-response-Volumes"></a>
Returned after a successful `DescribeVolumes` operation, describing each volume.  
Type: Array of [Volume](API_Volume.md) objects  
Array Members: Maximum number of 50 items.

## Errors
<a name="API_DescribeVolumes_Errors"></a>

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

 ** VolumeNotFound **   
No Amazon FSx volumes were found based upon the supplied parameters.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

## See Also
<a name="API_DescribeVolumes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/DescribeVolumes) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/DescribeVolumes) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/DescribeVolumes) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/DescribeVolumes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/DescribeVolumes) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/DescribeVolumes) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/DescribeVolumes) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/DescribeVolumes) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/DescribeVolumes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/DescribeVolumes) 