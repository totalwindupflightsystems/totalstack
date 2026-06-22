---
id: "@specs/aws/emr/docs/API_DescribeCluster"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeCluster"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# DescribeCluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_DescribeCluster
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeCluster
<a name="API_DescribeCluster"></a>

Provides cluster-level details including status, hardware and software configuration, VPC settings, and so on.

## Request Syntax
<a name="API_DescribeCluster_RequestSyntax"></a>

```
{
   "ClusterId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeCluster_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterId](#API_DescribeCluster_RequestSyntax) **   <a name="EMR-DescribeCluster-request-ClusterId"></a>
The identifier of the cluster to describe.  
Type: String  
Length Constraints: Maximum length of 256.  
Required: Yes

## Response Syntax
<a name="API_DescribeCluster_ResponseSyntax"></a>

```
{
   "Cluster": { 
      "Applications": [ 
         { 
            "AdditionalInfo": { 
               "string" : "string" 
            },
            "Args": [ "string" ],
            "Name": "string",
            "Version": "string"
         }
      ],
      "AutoScalingRole": "string",
      "AutoTerminate": boolean,
      "ClusterArn": "string",
      "Configurations": [ 
         { 
            "Classification": "string",
            "Configurations": [ 
               "Configuration"
            ],
            "Properties": { 
               "string" : "string" 
            }
         }
      ],
      "CustomAmiId": "string",
      "EbsRootVolumeIops": number,
      "EbsRootVolumeSize": number,
      "EbsRootVolumeThroughput": number,
      "Ec2InstanceAttributes": { 
         "AdditionalMasterSecurityGroups": [ "string" ],
         "AdditionalSlaveSecurityGroups": [ "string" ],
         "Ec2AvailabilityZone": "string",
         "Ec2KeyName": "string",
         "Ec2SubnetId": "string",
         "EmrManagedMasterSecurityGroup": "string",
         "EmrManagedSlaveSecurityGroup": "string",
         "IamInstanceProfile": "string",
         "RequestedEc2AvailabilityZones": [ "string" ],
         "RequestedEc2SubnetIds": [ "string" ],
         "ServiceAccessSecurityGroup": "string"
      },
      "ExtendedSupport": boolean,
      "Id": "string",
      "InstanceCollectionType": "string",
      "KerberosAttributes": { 
         "ADDomainJoinPassword": "string",
         "ADDomainJoinUser": "string",
         "CrossRealmTrustPrincipalPassword": "string",
         "KdcAdminPassword": "string",
         "Realm": "string"
      },
      "LogEncryptionKmsKeyId": "string",
      "LogUri": "string",
      "MasterPublicDnsName": "string",
      "MonitoringConfiguration": { 
         "CloudWatchLogConfiguration": { 
            "Enabled": boolean,
            "EncryptionKeyArn": "string",
            "LogGroupName": "string",
            "LogStreamNamePrefix": "string",
            "LogTypes": { 
               "string" : [ "string" ]
            }
         },
         "S3LoggingConfiguration": { 
            "LogTypeUploadPolicy": { 
               "string" : "string" 
            }
         }
      },
      "Name": "string",
      "NormalizedInstanceHours": number,
      "OSReleaseLabel": "string",
      "OutpostArn": "string",
      "PlacementGroups": [ 
         { 
            "InstanceRole": "string",
            "PlacementStrategy": "string"
         }
      ],
      "ReleaseLabel": "string",
      "RepoUpgradeOnBoot": "string",
      "RequestedAmiVersion": "string",
      "RunningAmiVersion": "string",
      "ScaleDownBehavior": "string",
      "SecurityConfiguration": "string",
      "ServiceRole": "string",
      "Status": { 
         "ErrorDetails": [ 
            { 
               "ErrorCode": "string",
               "ErrorData": [ 
                  { 
                     "string" : "string" 
                  }
               ],
               "ErrorMessage": "string"
            }
         ],
         "State": "string",
         "StateChangeReason": { 
            "Code": "string",
            "Message": "string"
         },
         "Timeline": { 
            "CreationDateTime": number,
            "EndDateTime": number,
            "ReadyDateTime": number
         }
      },
      "StepConcurrencyLevel": number,
      "Tags": [ 
         { 
            "Key": "string",
            "Value": "string"
         }
      ],
      "TerminationProtected": boolean,
      "UnhealthyNodeReplacement": boolean,
      "VisibleToAllUsers": boolean
   }
}
```

## Response Elements
<a name="API_DescribeCluster_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Cluster](#API_DescribeCluster_ResponseSyntax) **   <a name="EMR-DescribeCluster-response-Cluster"></a>
This output contains the details for the requested cluster.  
Type: [Cluster](API_Cluster.md) object

## Errors
<a name="API_DescribeCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **   
This exception occurs when there is an internal failure in the Amazon EMR service.    
 ** Message **   
The message associated with the exception.
HTTP Status Code: 500

 ** InvalidRequestException **   
This exception occurs when there is something wrong with user input.    
 ** ErrorCode **   
The error code associated with the exception.  
 ** Message **   
The message associated with the exception.
HTTP Status Code: 400

## See Also
<a name="API_DescribeCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/DescribeCluster) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/DescribeCluster) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/DescribeCluster) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/DescribeCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/DescribeCluster) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/DescribeCluster) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/DescribeCluster) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/DescribeCluster) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/DescribeCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/DescribeCluster) 