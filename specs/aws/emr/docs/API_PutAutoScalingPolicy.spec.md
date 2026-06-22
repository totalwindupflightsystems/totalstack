---
id: "@specs/aws/emr/docs/API_PutAutoScalingPolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PutAutoScalingPolicy"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# PutAutoScalingPolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_PutAutoScalingPolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PutAutoScalingPolicy
<a name="API_PutAutoScalingPolicy"></a>

Creates or updates an automatic scaling policy for a core instance group or task instance group in an Amazon EMR cluster. The automatic scaling policy defines how an instance group dynamically adds and terminates Amazon EC2 instances in response to the value of a CloudWatch metric.

## Request Syntax
<a name="API_PutAutoScalingPolicy_RequestSyntax"></a>

```
{
   "AutoScalingPolicy": { 
      "Constraints": { 
         "MaxCapacity": {{number}},
         "MinCapacity": {{number}}
      },
      "Rules": [ 
         { 
            "Action": { 
               "Market": "{{string}}",
               "SimpleScalingPolicyConfiguration": { 
                  "AdjustmentType": "{{string}}",
                  "CoolDown": {{number}},
                  "ScalingAdjustment": {{number}}
               }
            },
            "Description": "{{string}}",
            "Name": "{{string}}",
            "Trigger": { 
               "CloudWatchAlarmDefinition": { 
                  "ComparisonOperator": "{{string}}",
                  "Dimensions": [ 
                     { 
                        "Key": "{{string}}",
                        "Value": "{{string}}"
                     }
                  ],
                  "EvaluationPeriods": {{number}},
                  "MetricName": "{{string}}",
                  "Namespace": "{{string}}",
                  "Period": {{number}},
                  "Statistic": "{{string}}",
                  "Threshold": {{number}},
                  "Unit": "{{string}}"
               }
            }
         }
      ]
   },
   "ClusterId": "{{string}}",
   "InstanceGroupId": "{{string}}"
}
```

## Request Parameters
<a name="API_PutAutoScalingPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AutoScalingPolicy](#API_PutAutoScalingPolicy_RequestSyntax) **   <a name="EMR-PutAutoScalingPolicy-request-AutoScalingPolicy"></a>
Specifies the definition of the automatic scaling policy.  
Type: [AutoScalingPolicy](API_AutoScalingPolicy.md) object  
Required: Yes

 ** [ClusterId](#API_PutAutoScalingPolicy_RequestSyntax) **   <a name="EMR-PutAutoScalingPolicy-request-ClusterId"></a>
Specifies the ID of a cluster. The instance group to which the automatic scaling policy is applied is within this cluster.  
Type: String  
Length Constraints: Maximum length of 256.  
Required: Yes

 ** [InstanceGroupId](#API_PutAutoScalingPolicy_RequestSyntax) **   <a name="EMR-PutAutoScalingPolicy-request-InstanceGroupId"></a>
Specifies the ID of the instance group to which the automatic scaling policy is applied.  
Type: String  
Length Constraints: Maximum length of 256.  
Required: Yes

## Response Syntax
<a name="API_PutAutoScalingPolicy_ResponseSyntax"></a>

```
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
   "ClusterArn": "string",
   "ClusterId": "string",
   "InstanceGroupId": "string"
}
```

## Response Elements
<a name="API_PutAutoScalingPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AutoScalingPolicy](#API_PutAutoScalingPolicy_ResponseSyntax) **   <a name="EMR-PutAutoScalingPolicy-response-AutoScalingPolicy"></a>
The automatic scaling policy definition.  
Type: [AutoScalingPolicyDescription](API_AutoScalingPolicyDescription.md) object

 ** [ClusterArn](#API_PutAutoScalingPolicy_ResponseSyntax) **   <a name="EMR-PutAutoScalingPolicy-response-ClusterArn"></a>
The Amazon Resource Name (ARN) of the cluster.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [ClusterId](#API_PutAutoScalingPolicy_ResponseSyntax) **   <a name="EMR-PutAutoScalingPolicy-response-ClusterId"></a>
Specifies the ID of a cluster. The instance group to which the automatic scaling policy is applied is within this cluster.  
Type: String  
Length Constraints: Maximum length of 256.

 ** [InstanceGroupId](#API_PutAutoScalingPolicy_ResponseSyntax) **   <a name="EMR-PutAutoScalingPolicy-response-InstanceGroupId"></a>
Specifies the ID of the instance group to which the scaling policy is applied.  
Type: String  
Length Constraints: Maximum length of 256.

## Errors
<a name="API_PutAutoScalingPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_PutAutoScalingPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/PutAutoScalingPolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/PutAutoScalingPolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/PutAutoScalingPolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/PutAutoScalingPolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/PutAutoScalingPolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/PutAutoScalingPolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/PutAutoScalingPolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/PutAutoScalingPolicy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/PutAutoScalingPolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/PutAutoScalingPolicy) 