---
id: "@specs/aws/emr/docs/API_ListInstanceFleets"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListInstanceFleets"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# ListInstanceFleets

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_ListInstanceFleets
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListInstanceFleets
<a name="API_ListInstanceFleets"></a>

Lists all available details about the instance fleets in a cluster.

**Note**  
The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions.

## Request Syntax
<a name="API_ListInstanceFleets_RequestSyntax"></a>

```
{
   "ClusterId": "{{string}}",
   "Marker": "{{string}}"
}
```

## Request Parameters
<a name="API_ListInstanceFleets_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterId](#API_ListInstanceFleets_RequestSyntax) **   <a name="EMR-ListInstanceFleets-request-ClusterId"></a>
The unique identifier of the cluster.  
Type: String  
Length Constraints: Maximum length of 256.  
Required: Yes

 ** [Marker](#API_ListInstanceFleets_RequestSyntax) **   <a name="EMR-ListInstanceFleets-request-Marker"></a>
The pagination token that indicates the next set of results to retrieve.  
Type: String  
Required: No

## Response Syntax
<a name="API_ListInstanceFleets_ResponseSyntax"></a>

```
{
   "InstanceFleets": [ 
      { 
         "Context": "string",
         "Id": "string",
         "InstanceFleetType": "string",
         "InstanceTypeSpecifications": [ 
            { 
               "BidPrice": "string",
               "BidPriceAsPercentageOfOnDemandPrice": number,
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
               "InstanceType": "string",
               "Priority": number,
               "WeightedCapacity": number
            }
         ],
         "LaunchSpecifications": { 
            "OnDemandSpecification": { 
               "AllocationStrategy": "string",
               "CapacityReservationOptions": { 
                  "CapacityReservationPreference": "string",
                  "CapacityReservationResourceGroupArn": "string",
                  "UsageStrategy": "string"
               }
            },
            "SpotSpecification": { 
               "AllocationStrategy": "string",
               "BlockDurationMinutes": number,
               "TimeoutAction": "string",
               "TimeoutDurationMinutes": number
            }
         },
         "Name": "string",
         "ProvisionedOnDemandCapacity": number,
         "ProvisionedSpotCapacity": number,
         "ResizeSpecifications": { 
            "OnDemandResizeSpecification": { 
               "AllocationStrategy": "string",
               "CapacityReservationOptions": { 
                  "CapacityReservationPreference": "string",
                  "CapacityReservationResourceGroupArn": "string",
                  "UsageStrategy": "string"
               },
               "TimeoutDurationMinutes": number
            },
            "SpotResizeSpecification": { 
               "AllocationStrategy": "string",
               "TimeoutDurationMinutes": number
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
         },
         "TargetOnDemandCapacity": number,
         "TargetSpotCapacity": number
      }
   ],
   "Marker": "string"
}
```

## Response Elements
<a name="API_ListInstanceFleets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InstanceFleets](#API_ListInstanceFleets_ResponseSyntax) **   <a name="EMR-ListInstanceFleets-response-InstanceFleets"></a>
The list of instance fleets for the cluster and given filters.  
Type: Array of [InstanceFleet](API_InstanceFleet.md) objects

 ** [Marker](#API_ListInstanceFleets_ResponseSyntax) **   <a name="EMR-ListInstanceFleets-response-Marker"></a>
The pagination token that indicates the next set of results to retrieve.  
Type: String

## Errors
<a name="API_ListInstanceFleets_Errors"></a>

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
<a name="API_ListInstanceFleets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/ListInstanceFleets) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/ListInstanceFleets) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/ListInstanceFleets) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/ListInstanceFleets) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/ListInstanceFleets) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/ListInstanceFleets) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/ListInstanceFleets) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/ListInstanceFleets) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/ListInstanceFleets) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/ListInstanceFleets) 