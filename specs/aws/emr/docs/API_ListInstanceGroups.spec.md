---
id: "@specs/aws/emr/docs/API_ListInstanceGroups"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListInstanceGroups"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# ListInstanceGroups

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_ListInstanceGroups
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListInstanceGroups
<a name="API_ListInstanceGroups"></a>

Provides all available details about the instance groups in a cluster.

## Request Syntax
<a name="API_ListInstanceGroups_RequestSyntax"></a>

```
{
   "ClusterId": "{{string}}",
   "Marker": "{{string}}"
}
```

## Request Parameters
<a name="API_ListInstanceGroups_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterId](#API_ListInstanceGroups_RequestSyntax) **   <a name="EMR-ListInstanceGroups-request-ClusterId"></a>
The identifier of the cluster for which to list the instance groups.  
Type: String  
Length Constraints: Maximum length of 256.  
Required: Yes

 ** [Marker](#API_ListInstanceGroups_RequestSyntax) **   <a name="EMR-ListInstanceGroups-request-Marker"></a>
The pagination token that indicates the next set of results to retrieve.  
Type: String  
Required: No

## Response Syntax
<a name="API_ListInstanceGroups_ResponseSyntax"></a>

```
{
   "InstanceGroups": [ 
      { 
         "AutoScalingPolicy": { 
            "Constraints": { 
               "MaxCapacity": number,
               "MinCapacity": number
            },
            "Rules": [ 
               { 
                  "Action": { 
                     "Market": "string",
                     "SimpleScalingPolicyConfiguration": { 
                        "AdjustmentType": "string",
                        "CoolDown": number,
                        "ScalingAdjustment": number
                     }
                  },
                  "Description": "string",
                  "Name": "string",
                  "Trigger": { 
                     "CloudWatchAlarmDefinition": { 
                        "ComparisonOperator": "string",
                        "Dimensions": [ 
                           { 
                              "Key": "string",
                              "Value": "string"
                           }
                        ],
                        "EvaluationPeriods": number,
                        "MetricName": "string",
                        "Namespace": "string",
                        "Period": number,
                        "Statistic": "string",
                        "Threshold": number,
                        "Unit": "string"
                     }
                  }
               }
            ],
            "Status": { 
               "State": "string",
               "StateChangeReason": { 
                  "Code": "string",
                  "Message": "string"
               }
            }
         },
         "BidPrice": "string",
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
         "ConfigurationsVersion": number,
         "CustomAmiId": "string",
         "EbsBlockDevices": [ 
            { 
               "Device": "string",
               "VolumeSpecification": { 
                  "Iops": number,
                  "SizeInGB": number,
                  "Throughput": number,
                  "VolumeType": "string"
               }
            }
         ],
         "EbsOptimized": boolean,
         "Id": "string",
         "InstanceGroupType": "string",
         "InstanceType": "string",
         "LastSuccessfullyAppliedConfigurations": [ 
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
         "LastSuccessfullyAppliedConfigurationsVersion": number,
         "Market": "string",
         "Name": "string",
         "RequestedInstanceCount": number,
         "RunningInstanceCount": number,
         "ShrinkPolicy": { 
            "DecommissionTimeout": number,
            "InstanceResizePolicy": { 
               "InstancesToProtect": [ "string" ],
               "InstancesToTerminate": [ "string" ],
               "InstanceTerminationTimeout": number
            }
         },
         "Status": { 
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
         }
      }
   ],
   "Marker": "string"
}
```

## Response Elements
<a name="API_ListInstanceGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InstanceGroups](#API_ListInstanceGroups_ResponseSyntax) **   <a name="EMR-ListInstanceGroups-response-InstanceGroups"></a>
The list of instance groups for the cluster and given filters.  
Type: Array of [InstanceGroup](API_InstanceGroup.md) objects

 ** [Marker](#API_ListInstanceGroups_ResponseSyntax) **   <a name="EMR-ListInstanceGroups-response-Marker"></a>
The pagination token that indicates the next set of results to retrieve.  
Type: String

## Errors
<a name="API_ListInstanceGroups_Errors"></a>

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
<a name="API_ListInstanceGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/ListInstanceGroups) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/ListInstanceGroups) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/ListInstanceGroups) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/ListInstanceGroups) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/ListInstanceGroups) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/ListInstanceGroups) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/ListInstanceGroups) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/ListInstanceGroups) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/ListInstanceGroups) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/ListInstanceGroups) 