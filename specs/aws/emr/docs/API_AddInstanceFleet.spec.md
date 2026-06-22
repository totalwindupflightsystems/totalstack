---
id: "@specs/aws/emr/docs/API_AddInstanceFleet"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AddInstanceFleet"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# AddInstanceFleet

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_AddInstanceFleet
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AddInstanceFleet
<a name="API_AddInstanceFleet"></a>

Adds an instance fleet to a running cluster.

**Note**  
The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x.

## Request Syntax
<a name="API_AddInstanceFleet_RequestSyntax"></a>

```
{
   "ClusterId": "{{string}}",
   "InstanceFleet": { 
      "Context": "{{string}}",
      "InstanceFleetType": "{{string}}",
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
      "LaunchSpecifications": { 
         "OnDemandSpecification": { 
            "AllocationStrategy": "{{string}}",
            "CapacityReservationOptions": { 
               "CapacityReservationPreference": "{{string}}",
               "CapacityReservationResourceGroupArn": "{{string}}",
               "UsageStrategy": "{{string}}"
            }
         },
         "SpotSpecification": { 
            "AllocationStrategy": "{{string}}",
            "BlockDurationMinutes": {{number}},
            "TimeoutAction": "{{string}}",
            "TimeoutDurationMinutes": {{number}}
         }
      },
      "Name": "{{string}}",
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
<a name="API_AddInstanceFleet_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterId](#API_AddInstanceFleet_RequestSyntax) **   <a name="EMR-AddInstanceFleet-request-ClusterId"></a>
The unique identifier of the cluster.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: Yes

 ** [InstanceFleet](#API_AddInstanceFleet_RequestSyntax) **   <a name="EMR-AddInstanceFleet-request-InstanceFleet"></a>
Specifies the configuration of the instance fleet.  
Type: [InstanceFleetConfig](API_InstanceFleetConfig.md) object  
Required: Yes

## Response Syntax
<a name="API_AddInstanceFleet_ResponseSyntax"></a>

```
{
   "ClusterArn": "string",
   "ClusterId": "string",
   "InstanceFleetId": "string"
}
```

## Response Elements
<a name="API_AddInstanceFleet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ClusterArn](#API_AddInstanceFleet_ResponseSyntax) **   <a name="EMR-AddInstanceFleet-response-ClusterArn"></a>
The Amazon Resource Name of the cluster.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [ClusterId](#API_AddInstanceFleet_ResponseSyntax) **   <a name="EMR-AddInstanceFleet-response-ClusterId"></a>
The unique identifier of the cluster.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*` 

 ** [InstanceFleetId](#API_AddInstanceFleet_ResponseSyntax) **   <a name="EMR-AddInstanceFleet-response-InstanceFleetId"></a>
The unique identifier of the instance fleet.  
Type: String  
Length Constraints: Maximum length of 256.

## Errors
<a name="API_AddInstanceFleet_Errors"></a>

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
<a name="API_AddInstanceFleet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/AddInstanceFleet) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/AddInstanceFleet) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/AddInstanceFleet) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/AddInstanceFleet) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/AddInstanceFleet) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/AddInstanceFleet) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/AddInstanceFleet) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/AddInstanceFleet) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/AddInstanceFleet) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/AddInstanceFleet) 