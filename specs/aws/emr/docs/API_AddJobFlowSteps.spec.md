---
id: "@specs/aws/emr/docs/API_AddJobFlowSteps"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AddJobFlowSteps"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# AddJobFlowSteps

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_AddJobFlowSteps
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AddJobFlowSteps
<a name="API_AddJobFlowSteps"></a>

AddJobFlowSteps adds new steps to a running cluster. A maximum of 256 steps are allowed in each job flow.

If your cluster is long-running (such as a Hive data warehouse) or complex, you may require more than 256 steps to process your data. You can bypass the 256-step limitation in various ways, including using SSH to connect to the master node and submitting queries directly to the software running on the master node, such as Hive and Hadoop.

A step specifies the location of a JAR file stored either on the master node of the cluster or in Amazon S3. Each step is performed by the main function of the main class of the JAR file. The main class can be specified either in the manifest of the JAR or by using the MainFunction parameter of the step.

Amazon EMR executes each step in the order listed. For a step to be considered complete, the main function must exit with a zero exit code and all Hadoop jobs started while the step was running must have completed and run successfully.

You can only add steps to a cluster that is in one of the following states: STARTING, BOOTSTRAPPING, RUNNING, or WAITING.

**Note**  
The string values passed into `HadoopJarStep` object cannot exceed a total of 10240 characters.

## Request Syntax
<a name="API_AddJobFlowSteps_RequestSyntax"></a>

```
{
   "ExecutionRoleArn": "{{string}}",
   "JobFlowId": "{{string}}",
   "Steps": [ 
      { 
         "ActionOnFailure": "{{string}}",
         "HadoopJarStep": { 
            "Args": [ "{{string}}" ],
            "Jar": "{{string}}",
            "MainClass": "{{string}}",
            "Properties": [ 
               { 
                  "Key": "{{string}}",
                  "Value": "{{string}}"
               }
            ]
         },
         "Name": "{{string}}",
         "StepMonitoringConfiguration": { 
            "S3MonitoringConfiguration": { 
               "EncryptionKeyArn": "{{string}}",
               "LogUri": "{{string}}"
            }
         }
      }
   ]
}
```

## Request Parameters
<a name="API_AddJobFlowSteps_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ExecutionRoleArn](#API_AddJobFlowSteps_RequestSyntax) **   <a name="EMR-AddJobFlowSteps-request-ExecutionRoleArn"></a>
The Amazon Resource Name (ARN) of the runtime role for a step on the cluster. The runtime role can be a cross-account IAM role. The runtime role ARN is a combination of account ID, role name, and role type using the following format: `arn:partition:service:region:account:resource`.   
For example, `arn:aws:IAM::1234567890:role/ReadOnly` is a correctly formatted runtime role ARN.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Required: No

 ** [JobFlowId](#API_AddJobFlowSteps_RequestSyntax) **   <a name="EMR-AddJobFlowSteps-request-JobFlowId"></a>
A string that uniquely identifies the job flow. This identifier is returned by [RunJobFlow](API_RunJobFlow.md) and can also be obtained from [ListClusters](API_ListClusters.md).   
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: Yes

 ** [Steps](#API_AddJobFlowSteps_RequestSyntax) **   <a name="EMR-AddJobFlowSteps-request-Steps"></a>
 A list of [StepConfig](API_StepConfig.md) to be executed by the job flow.   
Type: Array of [StepConfig](API_StepConfig.md) objects  
Required: Yes

## Response Syntax
<a name="API_AddJobFlowSteps_ResponseSyntax"></a>

```
{
   "StepIds": [ "string" ]
}
```

## Response Elements
<a name="API_AddJobFlowSteps_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [StepIds](#API_AddJobFlowSteps_ResponseSyntax) **   <a name="EMR-AddJobFlowSteps-response-StepIds"></a>
The identifiers of the list of steps added to the job flow.  
Type: Array of strings  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*` 

## Errors
<a name="API_AddJobFlowSteps_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **   
Indicates that an error occurred while processing the request and that the request was not completed.  
HTTP Status Code: 400

## Examples
<a name="API_AddJobFlowSteps_Examples"></a>

### Example
<a name="API_AddJobFlowSteps_Example_1"></a>

This example illustrates one usage of AddJobFlowSteps.

#### Sample Request
<a name="API_AddJobFlowSteps_Example_1_Request"></a>

```
POST / HTTP/1.1
Content-Type: application/x-amz-json-1.1
X-Amz-Target: ElasticMapReduce.AddJobFlowSteps
Content-Length: 426
User-Agent: aws-sdk-ruby/1.9.2 ruby/1.9.3 i386-mingw32
Host: us-east-1.elasticmapreduce.amazonaws.com
X-Amz-Date: 20130716T210948Z
X-Amz-Content-Sha256: 9e5ad0a93c22224947ce98eea94f766103d91b28fa82eb60d0cb8b6f9555a6b2
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20130716/us-east-1/elasticmapreduce/aws4_request, SignedHeaders=content-length;content-type;host;user-agent;x-amz-content-sha256;x-amz-date;x-amz-target, Signature=2a2393390760ae85eb74ee3a539e1d758bfdd8815a1a6d6f14d4a2fbcfdcd5b7
Accept: */*

{
    "JobFlowId": "j-3TS0OIYO4NFN",
    "Steps": [{
        "Name": "Example Jar Step",
        "ActionOnFailure": "CANCEL_AND_WAIT",
        "HadoopJarStep": {
            "Jar": "s3n:\\/\\/elasticmapreduce\\/samples\\/cloudburst\\/cloudburst.jar",
            "Args": [
                "s3n:\\/\\/elasticmapreduce\\/samples\\/cloudburst\\/input\\/s_suis.br",
                "s3n:\\/\\/elasticmapreduce\\/samples\\/cloudburst\\/input\\/100k.br",
                "s3n:\\/\\/examples-bucket\\/cloudburst\\/output",
                "36",
                "3",
                "0",
                "1",
                "240",
                "48",
                "24",
                "24",
                "128",
                "16"
            ]
        }
    }]
}
```

#### Sample Response
<a name="API_AddJobFlowSteps_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 6514261f-ee5b-11e2-9345-5332e9ab2e6d
Content-Type: application/x-amz-json-1.1
Content-Length: 0
Date: Tue, 16 Jul 2013 21:05:07 GMT

{
   "StepIds": [ 
      "s-1XXXXXXXXXXA"
   ]
}
```

## See Also
<a name="API_AddJobFlowSteps_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/AddJobFlowSteps) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/AddJobFlowSteps) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/AddJobFlowSteps) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/AddJobFlowSteps) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/AddJobFlowSteps) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/AddJobFlowSteps) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/AddJobFlowSteps) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/AddJobFlowSteps) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/AddJobFlowSteps) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/AddJobFlowSteps) 