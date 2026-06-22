---
id: "@specs/aws/emr/docs/API_ModifyInstanceFleet"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ModifyInstanceFleet"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# ModifyInstanceFleet

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_ModifyInstanceFleet
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ModifyInstanceFleet
<a name="API_ModifyInstanceFleet"></a>

Modifies the target On-Demand and target Spot capacities for the instance fleet with the specified InstanceFleetID within the cluster specified using ClusterID. The call either succeeds or fails atomically.

**Note**  
The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions.

## Request Syntax
<a name="API_ModifyInstanceFleet_RequestSyntax"></a>

```
{
   "ClusterId": "{{string}}",
   "InstanceFleet": { 
      "Context": "{{string}}",
      "InstanceFleetId": "{{string}}",
      "InstanceTypeConfigs": [ 
         { 
            "BidPrice": "{{string}}",
            "BidPriceAsPercentageOfOnDemandPrice": {{number}},
            "Configurations": [ 
               { 
                  "Classification": "{{string}}",
                  "Configurations": [ 
                     "Configuration"
                  ],
                  "Properties": { 
                     "{{string}}" : "{{string}}" 
                  }
               }
            ],
            "CustomAmiId": "{{string}}",
            "EbsConfiguration": { 
               "EbsBlockDeviceConfigs": [ 
                  { 
                     "VolumeSpecification": { 
                        "Iops": {{number}},
                        "SizeInGB": {{number}},
                        "Throughput": {{number}},
                        "VolumeType": "{{string}}"
                     },
                     "VolumesPerInstance": {{number}}
                  }
               ],
               "EbsOptimized": {{boolean}}
            },
            "InstanceType": "{{string}}",
            "Priority": {{number}},
            "WeightedCapacity": {{number}}
         }
      ],
      "ResizeSpecifications": { 
         "OnDemandResizeSpecification": { 
            "AllocationStrategy": "{{string}}",
            "CapacityReservationOptions": { 
               "CapacityReservationPreference": "{{string}}",
               "CapacityReservationResourceGroupArn": "{{string}}",
               "UsageStrategy": "{{string}}"
            },
            "TimeoutDurationMinutes": {{number}}
         },
         "SpotResizeSpecification": { 
            "AllocationStrategy": "{{string}}",
            "TimeoutDurationMinutes": {{number}}
         }
      },
      "TargetOnDemandCapacity": {{number}},
      "TargetSpotCapacity": {{number}}
   }
}
```

## Request Parameters
<a name="API_ModifyInstanceFleet_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterId](#API_ModifyInstanceFleet_RequestSyntax) **   <a name="EMR-ModifyInstanceFleet-request-ClusterId"></a>
The unique identifier of the cluster.  
Type: String  
Length Constraints: Maximum length of 256.  
Required: Yes

 ** [InstanceFleet](#API_ModifyInstanceFleet_RequestSyntax) **   <a name="EMR-ModifyInstanceFleet-request-InstanceFleet"></a>
The configuration parameters of the instance fleet.  
Type: [InstanceFleetModifyConfig](API_InstanceFleetModifyConfig.md) object  
Required: Yes

## Response Elements
<a name="API_ModifyInstanceFleet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_ModifyInstanceFleet_Errors"></a>

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
<a name="API_ModifyInstanceFleet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/ModifyInstanceFleet) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/ModifyInstanceFleet) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/ModifyInstanceFleet) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/ModifyInstanceFleet) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/ModifyInstanceFleet) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/ModifyInstanceFleet) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/ModifyInstanceFleet) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/ModifyInstanceFleet) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/ModifyInstanceFleet) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/ModifyInstanceFleet) 