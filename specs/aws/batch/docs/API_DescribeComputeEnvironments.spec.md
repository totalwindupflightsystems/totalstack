---
id: "@specs/aws/batch/docs/API_DescribeComputeEnvironments"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeComputeEnvironments"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# DescribeComputeEnvironments

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_DescribeComputeEnvironments
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeComputeEnvironments
<a name="API_DescribeComputeEnvironments"></a>

Describes one or more of your compute environments.

If you're using an unmanaged compute environment, you can use the `DescribeComputeEnvironment` operation to determine the `ecsClusterArn` that you launch your Amazon ECS container instances into.

## Request Syntax
<a name="API_DescribeComputeEnvironments_RequestSyntax"></a>

```
POST /v1/describecomputeenvironments HTTP/1.1
Content-type: application/json

{
   "computeEnvironments": [ "{{string}}" ],
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DescribeComputeEnvironments_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeComputeEnvironments_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [computeEnvironments](#API_DescribeComputeEnvironments_RequestSyntax) **   <a name="Batch-DescribeComputeEnvironments-request-computeEnvironments"></a>
A list of up to 100 compute environment names or full Amazon Resource Name (ARN) entries.  
Type: Array of strings  
Required: No

 ** [maxResults](#API_DescribeComputeEnvironments_RequestSyntax) **   <a name="Batch-DescribeComputeEnvironments-request-maxResults"></a>
The maximum number of cluster results returned by `DescribeComputeEnvironments` in paginated output. When this parameter is used, `DescribeComputeEnvironments` only returns `maxResults` results in a single page along with a `nextToken` response element. The remaining results of the initial request can be seen by sending another `DescribeComputeEnvironments` request with the returned `nextToken` value. This value can be between 1 and 100. If this parameter isn't used, then `DescribeComputeEnvironments` returns up to 100 results and a `nextToken` value if applicable.  
Type: Integer  
Required: No

 ** [nextToken](#API_DescribeComputeEnvironments_RequestSyntax) **   <a name="Batch-DescribeComputeEnvironments-request-nextToken"></a>
The `nextToken` value returned from a previous paginated `DescribeComputeEnvironments` request where `maxResults` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the `nextToken` value. This value is `null` when there are no more results to return.  
Treat this token as an opaque identifier that's only used to retrieve the next items in a list and not for other programmatic purposes.
Type: String  
Required: No

## Response Syntax
<a name="API_DescribeComputeEnvironments_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "computeEnvironments": [ 
      { 
         "computeEnvironmentArn": "string",
         "computeEnvironmentName": "string",
         "computeResources": { 
            "allocationStrategy": "string",
            "bidPercentage": number,
            "desiredvCpus": number,
            "ec2Configuration": [ 
               { 
                  "batchImageStatus": "string",
                  "imageIdOverride": "string",
                  "imageKubernetesVersion": "string",
                  "imageType": "string"
               }
            ],
            "ec2KeyPair": "string",
            "imageId": "string",
            "instanceRole": "string",
            "instanceTypes": [ "string" ],
            "launchTemplate": { 
               "launchTemplateId": "string",
               "launchTemplateName": "string",
               "overrides": [ 
                  { 
                     "launchTemplateId": "string",
                     "launchTemplateName": "string",
                     "targetInstanceTypes": [ "string" ],
                     "userdataType": "string",
                     "version": "string"
                  }
               ],
               "userdataType": "string",
               "version": "string"
            },
            "maxvCpus": number,
            "minvCpus": number,
            "placementGroup": "string",
            "scalingPolicy": { 
               "minScaleDownDelayMinutes": number
            },
            "securityGroupIds": [ "string" ],
            "spotIamFleetRole": "string",
            "subnets": [ "string" ],
            "tags": { 
               "string" : "string" 
            },
            "type": "string"
         },
         "containerOrchestrationType": "string",
         "context": "string",
         "ecsClusterArn": "string",
         "eksConfiguration": { 
            "eksClusterArn": "string",
            "kubernetesNamespace": "string"
         },
         "serviceRole": "string",
         "state": "string",
         "status": "string",
         "statusReason": "string",
         "tags": { 
            "string" : "string" 
         },
         "type": "string",
         "unmanagedvCpus": number,
         "updatePolicy": { 
            "jobExecutionTimeoutMinutes": number,
            "terminateJobsOnUpdate": boolean
         },
         "uuid": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeComputeEnvironments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [computeEnvironments](#API_DescribeComputeEnvironments_ResponseSyntax) **   <a name="Batch-DescribeComputeEnvironments-response-computeEnvironments"></a>
The list of compute environments.  
Type: Array of [ComputeEnvironmentDetail](API_ComputeEnvironmentDetail.md) objects

 ** [nextToken](#API_DescribeComputeEnvironments_ResponseSyntax) **   <a name="Batch-DescribeComputeEnvironments-response-nextToken"></a>
The `nextToken` value to include in a future `DescribeComputeEnvironments` request. When the results of a `DescribeComputeEnvironments` request exceed `maxResults`, this value can be used to retrieve the next page of results. This value is `null` when there are no more results to return.  
Type: String

## Errors
<a name="API_DescribeComputeEnvironments_Errors"></a>

 ** ClientException **   
These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.  
HTTP Status Code: 400

 ** ServerException **   
These errors are usually caused by a server issue.  
HTTP Status Code: 500

## Examples
<a name="API_DescribeComputeEnvironments_Examples"></a>

In the following example or examples, the Authorization header contents (` [authorization-params] `) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_DescribeComputeEnvironments_Example_1"></a>

This example describes the `P3OnDemand` compute environment.

#### Sample Request
<a name="API_DescribeComputeEnvironments_Example_1_Request"></a>

```
POST /v1/describecomputeenvironments HTTP/1.1
Host: batch.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: [content-length]
Authorization: AUTHPARAMS
X-Amz-Date: 20161128T193355Z
User-Agent: aws-cli/1.11.21 Python/2.7.12 Darwin/16.1.0 botocore/1.4.78

{
  "computeEnvironments": [
    "P3OnDemand"
  ]
}
```

#### Sample Response
<a name="API_DescribeComputeEnvironments_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: [content-length]
Connection: keep-alive
Date: Mon, 28 Nov 2016 19:33:56 GMT
x-amzn-RequestId: [request-id]
X-Amzn-Trace-Id: [trace-id]
X-Cache: Miss from cloudfront
Via: 1.1 56908f89e8d17ba579c0607313114955.cloudfront.net (CloudFront)
X-Amz-Cf-Id: FbgslaatWhj_yGhfkSCTPpPtjiuVuFOBns-kK5EsaasYQC5p2FnpiQ==

{
  "computeEnvironments": [{
    "computeEnvironmentName": "P3OnDemand",
    "computeEnvironmentArn": "arn:aws:batch:us-east-1:123456789012:compute-environment/P3OnDemand",
    "ecsClusterArn": "arn:aws:ecs:us-east-1:123456789012:cluster/P3OnDemand_Batch_2c06f29d-d1fe-3a49-879d-42394c86effc",
    "type": "MANAGED",
    "state": "ENABLED",
    "status": "VALID",
    "statusReason": "ComputeEnvironment Healthy",
    "computeResources": {
      "type": "EC2",
      "minvCpus": 0,
      "maxvCpus": 128,
      "desiredvCpus": 48,
      "instanceTypes": ["p3"],
      "subnets": ["subnet-220c0e0a", "subnet-1a95556d", "subnet-978f6dce"],
      "securityGroupIds": ["sg-cf5093b2"],
      "ec2KeyPair": "id_rsa",
      "instanceRole": "ecsInstanceRole",
      "tags": {
        "Name": "Batch Instance - P3OnDemand",
        "Department": "Management"
      }
    },
    "serviceRole": "arn:aws:iam::123456789012:role/AWSBatchServiceRole"
  }]
}
```

## See Also
<a name="API_DescribeComputeEnvironments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/batch-2016-08-10/DescribeComputeEnvironments) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/batch-2016-08-10/DescribeComputeEnvironments) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/DescribeComputeEnvironments) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/batch-2016-08-10/DescribeComputeEnvironments) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/DescribeComputeEnvironments) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/batch-2016-08-10/DescribeComputeEnvironments) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/batch-2016-08-10/DescribeComputeEnvironments) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/batch-2016-08-10/DescribeComputeEnvironments) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/DescribeComputeEnvironments) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/DescribeComputeEnvironments) 