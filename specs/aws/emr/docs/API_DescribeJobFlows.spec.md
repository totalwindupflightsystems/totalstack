---
id: "@specs/aws/emr/docs/API_DescribeJobFlows"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeJobFlows"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# DescribeJobFlows

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_DescribeJobFlows
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeJobFlows
<a name="API_DescribeJobFlows"></a>

This API is no longer supported and will eventually be removed. We recommend you use [ListClusters](API_ListClusters.md), [DescribeCluster](API_DescribeCluster.md), [ListSteps](API_ListSteps.md), [ListInstanceGroups](API_ListInstanceGroups.md) and [ListBootstrapActions](API_ListBootstrapActions.md) instead.

DescribeJobFlows returns a list of job flows that match all of the supplied parameters. The parameters can include a list of job flow IDs, job flow states, and restrictions on job flow creation date and time.

Regardless of supplied parameters, only job flows created within the last two months are returned.

If no parameters are supplied, then job flows matching either of the following criteria are returned:
+ Job flows created and completed in the last two weeks
+  Job flows created within the last two months that are in one of the following states: `RUNNING`, `WAITING`, `SHUTTING_DOWN`, `STARTING` 

Amazon EMR can return a maximum of 512 job flow descriptions.

## Request Syntax
<a name="API_DescribeJobFlows_RequestSyntax"></a>

```
{
   "CreatedAfter": {{number}},
   "CreatedBefore": {{number}},
   "JobFlowIds": [ "{{string}}" ],
   "JobFlowStates": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeJobFlows_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CreatedAfter](#API_DescribeJobFlows_RequestSyntax) **   <a name="EMR-DescribeJobFlows-request-CreatedAfter"></a>
Return only job flows created after this date and time.  
Type: Timestamp  
Required: No

 ** [CreatedBefore](#API_DescribeJobFlows_RequestSyntax) **   <a name="EMR-DescribeJobFlows-request-CreatedBefore"></a>
Return only job flows created before this date and time.  
Type: Timestamp  
Required: No

 ** [JobFlowIds](#API_DescribeJobFlows_RequestSyntax) **   <a name="EMR-DescribeJobFlows-request-JobFlowIds"></a>
Return only job flows whose job flow ID is contained in this list.  
Type: Array of strings  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** [JobFlowStates](#API_DescribeJobFlows_RequestSyntax) **   <a name="EMR-DescribeJobFlows-request-JobFlowStates"></a>
Return only job flows whose state is contained in this list.  
Type: Array of strings  
Valid Values: `STARTING | BOOTSTRAPPING | RUNNING | WAITING | SHUTTING_DOWN | TERMINATED | COMPLETED | FAILED`   
Required: No

## Response Syntax
<a name="API_DescribeJobFlows_ResponseSyntax"></a>

```
{
   "JobFlows": [ 
      { 
         "AmiVersion": "string",
         "AutoScalingRole": "string",
         "BootstrapActions": [ 
            { 
               "BootstrapActionConfig": { 
                  "Name": "string",
                  "ScriptBootstrapAction": { 
                     "Args": [ "string" ],
                     "Path": "string"
                  }
               }
            }
         ],
         "ExecutionStatusDetail": { 
            "CreationDateTime": number,
            "EndDateTime": number,
            "LastStateChangeReason": "string",
            "ReadyDateTime": number,
            "StartDateTime": number,
            "State": "string"
         },
         "Instances": { 
            "Ec2KeyName": "string",
            "Ec2SubnetId": "string",
            "HadoopVersion": "string",
            "InstanceCount": number,
            "InstanceGroups": [ 
               { 
                  "BidPrice": "string",
                  "CreationDateTime": number,
                  "CustomAmiId": "string",
                  "EndDateTime": number,
                  "InstanceGroupId": "string",
                  "InstanceRequestCount": number,
                  "InstanceRole": "string",
                  "InstanceRunningCount": number,
                  "InstanceType": "string",
                  "LastStateChangeReason": "string",
                  "Market": "string",
                  "Name": "string",
                  "ReadyDateTime": number,
                  "StartDateTime": number,
                  "State": "string"
               }
            ],
            "KeepJobFlowAliveWhenNoSteps": boolean,
            "MasterInstanceId": "string",
            "MasterInstanceType": "string",
            "MasterPublicDnsName": "string",
            "NormalizedInstanceHours": number,
            "Placement": { 
               "AvailabilityZone": "string",
               "AvailabilityZones": [ "string" ]
            },
            "SlaveInstanceType": "string",
            "TerminationProtected": boolean,
            "UnhealthyNodeReplacement": boolean
         },
         "JobFlowId": "string",
         "JobFlowRole": "string",
         "LogEncryptionKmsKeyId": "string",
         "LogUri": "string",
         "Name": "string",
         "ScaleDownBehavior": "string",
         "ServiceRole": "string",
         "Steps": [ 
            { 
               "ExecutionStatusDetail": { 
                  "CreationDateTime": number,
                  "EndDateTime": number,
                  "LastStateChangeReason": "string",
                  "StartDateTime": number,
                  "State": "string"
               },
               "StepConfig": { 
                  "ActionOnFailure": "string",
                  "HadoopJarStep": { 
                     "Args": [ "string" ],
                     "Jar": "string",
                     "MainClass": "string",
                     "Properties": [ 
                        { 
                           "Key": "string",
                           "Value": "string"
                        }
                     ]
                  },
                  "Name": "string",
                  "StepMonitoringConfiguration": { 
                     "S3MonitoringConfiguration": { 
                        "EncryptionKeyArn": "string",
                        "LogUri": "string"
                     }
                  }
               }
            }
         ],
         "SupportedProducts": [ "string" ],
         "VisibleToAllUsers": boolean
      }
   ]
}
```

## Response Elements
<a name="API_DescribeJobFlows_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [JobFlows](#API_DescribeJobFlows_ResponseSyntax) **   <a name="EMR-DescribeJobFlows-response-JobFlows"></a>
A list of job flows matching the parameters supplied.  
Type: Array of [JobFlowDetail](API_JobFlowDetail.md) objects

## Errors
<a name="API_DescribeJobFlows_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **   
Indicates that an error occurred while processing the request and that the request was not completed.  
HTTP Status Code: 400

## Examples
<a name="API_DescribeJobFlows_Examples"></a>

### Example
<a name="API_DescribeJobFlows_Example_1"></a>

This example illustrates one usage of DescribeJobFlows.

#### Sample Request
<a name="API_DescribeJobFlows_Example_1_Request"></a>

```
POST / HTTP/1.1
Content-Type: application/x-amz-json-1.1
X-Amz-Target: ElasticMapReduce.DescribeJobFlows
Content-Length: 62
User-Agent: aws-sdk-ruby/1.9.2 ruby/1.9.3 i386-mingw32
Host: us-east-1.elasticmapreduce.amazonaws.com
X-Amz-Date: 20130715T220330Z
X-Amz-Content-Sha256: fce83af973f96f173512aca2845c56862b946feb1de0600326f1365b658a0e39
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20130715/us-east-1/elasticmapreduce/aws4_request, SignedHeaders=content-length;content-type;host;user-agent;x-amz-content-sha256;x-amz-date;x-amz-target, Signature=29F98a6f44e05ad54fe1e8b3d1a7101ab08dc3ad348995f89c533693cee2bb3b
Accept: */*

{
    "JobFlowIds": ["j-ZKIY4CKQRX72"],
    "DescriptionType": "EXTENDED"
}
```

#### Sample Response
<a name="API_DescribeJobFlows_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 634d4142-ed9a-11e2-bbba-b56d7d016ec4
Content-Type: application/x-amz-json-1.1
Content-Length: 1624
Date: Mon, 15 Jul 2013 22:03:31 GMT

{"JobFlows": [{
    "AmiVersion": "2.3.6",
    "BootstrapActions": [],
    "ExecutionStatusDetail": {
        "CreationDateTime": 1.373923429E9,
        "EndDateTime": 1.373923995E9,
        "LastStateChangeReason": "Steps completed",
        "ReadyDateTime": 1.373923754E9,
        "StartDateTime": 1.373923754E9,
        "State": "COMPLETED"
    },
    "Instances": {
        "HadoopVersion": "1.0.3",
        "InstanceCount": 1,
        "InstanceGroups": [{
            "CreationDateTime": 1.373923429E9,
            "EndDateTime": 1.373923995E9,
            "InstanceGroupId": "ig-3SRUWV3E0NB7K",
            "InstanceRequestCount": 1,
            "InstanceRole": "MASTER",
            "InstanceRunningCount": 0,
            "InstanceType": "m1.small",
            "LastStateChangeReason": "Job flow terminated",
            "Market": "ON_DEMAND",
            "Name": "Master InstanceGroup",
            "ReadyDateTime": 1.37392375E9,
            "StartDateTime": 1.373923646E9,
            "State": "ENDED"
        }],
        "KeepJobFlowAliveWhenNoSteps": false,
        "MasterInstanceId": "i-8c4fbbef",
        "MasterInstanceType": "m1.small",
        "MasterPublicDnsName": "ec2-107-20-46-140.compute-1.amazonaws.com",
        "NormalizedInstanceHours": 1,
        "Placement": {"AvailabilityZone": "us-east-1a"},
        "TerminationProtected": false
    },
    "JobFlowId": "j-ZKIY4CKQRX72",
    "Name": "Development Job Flow",
    "Steps": [{
        "ExecutionStatusDetail": {
            "CreationDateTime": 1.373923429E9,
            "EndDateTime": 1.373923914E9,
            "StartDateTime": 1.373923754E9,
            "State": "COMPLETED"
        },
        "StepConfig": {
            "ActionOnFailure": "CANCEL_AND_WAIT",
            "HadoopJarStep": {
                "Args": [
                    "-input",
                    "s3://elasticmapreduce/samples/wordcount/input",
                    "-output",
                    "s3://examples-bucket/example-output",
                    "-mapper",
                    "s3://elasticmapreduce/samples/wordcount/wordSplitter.py",
                    "-reducer",
                    "aggregate"
                ],
                "Jar": "/home/hadoop/contrib/streaming/hadoop-streaming.jar",
                "Properties": []
            },
            "Name": "Example Streaming Step"
        }
    }],
    "SupportedProducts": []
}]}
```

## See Also
<a name="API_DescribeJobFlows_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/DescribeJobFlows) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/DescribeJobFlows) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/DescribeJobFlows) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/DescribeJobFlows) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/DescribeJobFlows) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/DescribeJobFlows) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/DescribeJobFlows) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/DescribeJobFlows) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/DescribeJobFlows) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/DescribeJobFlows) 