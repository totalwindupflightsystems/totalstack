---
id: "@specs/aws/emr/docs/API_AddInstanceGroups"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AddInstanceGroups"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# AddInstanceGroups

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_AddInstanceGroups
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AddInstanceGroups
<a name="API_AddInstanceGroups"></a>

Adds one or more instance groups to a running cluster.

## Request Syntax
<a name="API_AddInstanceGroups_RequestSyntax"></a>

```
{
   "InstanceGroups": [ 
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
         "BidPrice": "{{string}}",
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
         "InstanceCount": {{number}},
         "InstanceRole": "{{string}}",
         "InstanceType": "{{string}}",
         "Market": "{{string}}",
         "Name": "{{string}}"
      }
   ],
   "JobFlowId": "{{string}}"
}
```

## Request Parameters
<a name="API_AddInstanceGroups_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [InstanceGroups](#API_AddInstanceGroups_RequestSyntax) **   <a name="EMR-AddInstanceGroups-request-InstanceGroups"></a>
Instance groups to add.  
Type: Array of [InstanceGroupConfig](API_InstanceGroupConfig.md) objects  
Required: Yes

 ** [JobFlowId](#API_AddInstanceGroups_RequestSyntax) **   <a name="EMR-AddInstanceGroups-request-JobFlowId"></a>
Job flow in which to add the instance groups.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: Yes

## Response Syntax
<a name="API_AddInstanceGroups_ResponseSyntax"></a>

```
{
   "ClusterArn": "string",
   "InstanceGroupIds": [ "string" ],
   "JobFlowId": "string"
}
```

## Response Elements
<a name="API_AddInstanceGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ClusterArn](#API_AddInstanceGroups_ResponseSyntax) **   <a name="EMR-AddInstanceGroups-response-ClusterArn"></a>
The Amazon Resource Name of the cluster.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [InstanceGroupIds](#API_AddInstanceGroups_ResponseSyntax) **   <a name="EMR-AddInstanceGroups-response-InstanceGroupIds"></a>
Instance group IDs of the newly created instance groups.  
Type: Array of strings  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*` 

 ** [JobFlowId](#API_AddInstanceGroups_ResponseSyntax) **   <a name="EMR-AddInstanceGroups-response-JobFlowId"></a>
The job flow ID in which the instance groups are added.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*` 

## Errors
<a name="API_AddInstanceGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **   
Indicates that an error occurred while processing the request and that the request was not completed.  
HTTP Status Code: 400

## Examples
<a name="API_AddInstanceGroups_Examples"></a>

### Example
<a name="API_AddInstanceGroups_Example_1"></a>

This example illustrates one usage of AddInstanceGroups.

#### Sample Request
<a name="API_AddInstanceGroups_Example_1_Request"></a>

```
POST / HTTP/1.1
Content-Type: application/x-amz-json-1.1
X-Amz-Target: ElasticMapReduce.AddInstanceGroups
Content-Length: 168
User-Agent: aws-sdk-ruby/1.9.2 ruby/1.9.3 i386-mingw32
Host: us-east-1.elasticmapreduce.amazonaws.com
X-Amz-Date: 20130715T223346Z
X-Amz-Content-Sha256: ac5a7193b1283898dd822a4b16ca36963879bb010d2dbe57198439973ab2a7d3
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20130715/us-east-1/elasticmapreduce/aws4_request, SignedHeaders=content-length;content-type;host;user-agent;x-amz-content-sha256;x-amz-date;x-amz-target, Signature=4c5e7eb762ea45f292a5cd1a1cc56ed60009e19a9dba3d6e5e4e67e96d43af11
Accept: */*


{
    "JobFlowId": "j-3U7TSX5GZFD8Y",
    "InstanceGroups": [{
        "Name": "Task Instance Group",
        "InstanceRole": "TASK",
        "InstanceCount": 2,
        "InstanceType": "m1.small",
        "Market": "ON_DEMAND"
    }]
}
```

#### Sample Response
<a name="API_AddInstanceGroups_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 9da5a349-ed9e-11e2-90db-69a5154aeb8d
Content-Type: application/x-amz-json-1.1
Content-Length: 71
Date: Mon, 15 Jul 2013 22:33:47 GMT

{
    "InstanceGroupIds": ["ig-294A6A2KWT4WB"],
    "JobFlowId": "j-3U7TSX5GZFD8Y"
}
```

## See Also
<a name="API_AddInstanceGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/AddInstanceGroups) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/AddInstanceGroups) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/AddInstanceGroups) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/AddInstanceGroups) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/AddInstanceGroups) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/AddInstanceGroups) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/AddInstanceGroups) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/AddInstanceGroups) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/AddInstanceGroups) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/AddInstanceGroups) 