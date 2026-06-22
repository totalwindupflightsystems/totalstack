---
id: "@specs/aws/batch/docs/API_CreateComputeEnvironment"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateComputeEnvironment"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# CreateComputeEnvironment

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_CreateComputeEnvironment
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateComputeEnvironment
<a name="API_CreateComputeEnvironment"></a>

Creates an AWS Batch compute environment. You can create `MANAGED` or `UNMANAGED` compute environments. `MANAGED` compute environments can use Amazon EC2 or AWS Fargate resources. `UNMANAGED` compute environments can only use EC2 resources.

In a managed compute environment, AWS Batch manages the capacity and instance types of the compute resources within the environment. This is based on the compute resource specification that you define or the [launch template](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html) that you specify when you create the compute environment. Either, you can choose to use EC2 On-Demand Instances and EC2 Spot Instances. Or, you can use Fargate and Fargate Spot capacity in your managed compute environment. You can optionally set a maximum price so that Spot Instances only launch when the Spot Instance price is less than a specified percentage of the On-Demand price.

In an unmanaged compute environment, you can manage your own EC2 compute resources and have flexibility with how you configure your compute resources. For example, you can use custom AMIs. However, you must verify that each of your AMIs meet the Amazon ECS container instance AMI specification. For more information, see [container instance AMIs](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/container_instance_AMIs.html) in the *Amazon Elastic Container Service Developer Guide*. After you created your unmanaged compute environment, you can use the [DescribeComputeEnvironments](API_DescribeComputeEnvironments.md) operation to find the Amazon ECS cluster that's associated with it. Then, launch your container instances into that Amazon ECS cluster. For more information, see [Launching an Amazon ECS container instance](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_container_instance.html) in the *Amazon Elastic Container Service Developer Guide*.

**Note**  
 AWS Batch doesn't automatically upgrade the AMIs in a compute environment after it's created. For more information on how to update a compute environment's AMI, see [Updating compute environments](https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html) in the * AWS Batch User Guide*.

## Request Syntax
<a name="API_CreateComputeEnvironment_RequestSyntax"></a>

```
POST /v1/createcomputeenvironment HTTP/1.1
Content-type: application/json

{
   "computeEnvironmentName": "{{string}}",
   "computeResources": { 
      "allocationStrategy": "{{string}}",
      "bidPercentage": {{number}},
      "desiredvCpus": {{number}},
      "ec2Configuration": [ 
         { 
            "batchImageStatus": "{{string}}",
            "imageIdOverride": "{{string}}",
            "imageKubernetesVersion": "{{string}}",
            "imageType": "{{string}}"
         }
      ],
      "ec2KeyPair": "{{string}}",
      "imageId": "{{string}}",
      "instanceRole": "{{string}}",
      "instanceTypes": [ "{{string}}" ],
      "launchTemplate": { 
         "launchTemplateId": "{{string}}",
         "launchTemplateName": "{{string}}",
         "overrides": [ 
            { 
               "launchTemplateId": "{{string}}",
               "launchTemplateName": "{{string}}",
               "targetInstanceTypes": [ "{{string}}" ],
               "userdataType": "{{string}}",
               "version": "{{string}}"
            }
         ],
         "userdataType": "{{string}}",
         "version": "{{string}}"
      },
      "maxvCpus": {{number}},
      "minvCpus": {{number}},
      "placementGroup": "{{string}}",
      "scalingPolicy": { 
         "minScaleDownDelayMinutes": {{number}}
      },
      "securityGroupIds": [ "{{string}}" ],
      "spotIamFleetRole": "{{string}}",
      "subnets": [ "{{string}}" ],
      "tags": { 
         "{{string}}" : "{{string}}" 
      },
      "type": "{{string}}"
   },
   "context": "{{string}}",
   "eksConfiguration": { 
      "eksClusterArn": "{{string}}",
      "kubernetesNamespace": "{{string}}"
   },
   "serviceRole": "{{string}}",
   "state": "{{string}}",
   "tags": { 
      "{{string}}" : "{{string}}" 
   },
   "type": "{{string}}",
   "unmanagedvCpus": {{number}}
}
```

## URI Request Parameters
<a name="API_CreateComputeEnvironment_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateComputeEnvironment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [computeEnvironmentName](#API_CreateComputeEnvironment_RequestSyntax) **   <a name="Batch-CreateComputeEnvironment-request-computeEnvironmentName"></a>
The name for your compute environment. It can be up to 128 characters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (\_).  
Type: String  
Required: Yes

 ** [computeResources](#API_CreateComputeEnvironment_RequestSyntax) **   <a name="Batch-CreateComputeEnvironment-request-computeResources"></a>
Details about the compute resources managed by the compute environment. This parameter is required for managed compute environments. For more information, see [Compute Environments](https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html) in the * AWS Batch User Guide*.  
Type: [ComputeResource](API_ComputeResource.md) object  
Required: No

 ** [context](#API_CreateComputeEnvironment_RequestSyntax) **   <a name="Batch-CreateComputeEnvironment-request-context"></a>
Reserved.  
Type: String  
Required: No

 ** [eksConfiguration](#API_CreateComputeEnvironment_RequestSyntax) **   <a name="Batch-CreateComputeEnvironment-request-eksConfiguration"></a>
The details for the Amazon EKS cluster that supports the compute environment.  
To create a compute environment that uses EKS resources, the caller must have permissions to call `eks:DescribeCluster`.
Type: [EksConfiguration](API_EksConfiguration.md) object  
Required: No

 ** [serviceRole](#API_CreateComputeEnvironment_RequestSyntax) **   <a name="Batch-CreateComputeEnvironment-request-serviceRole"></a>
The full Amazon Resource Name (ARN) of the IAM role that allows AWS Batch to make calls to other AWS services on your behalf. For more information, see [AWS Batch service IAM role](https://docs.aws.amazon.com/batch/latest/userguide/service_IAM_role.html) in the * AWS Batch User Guide*.  
If your account already created the AWS Batch service-linked role, that role is used by default for your compute environment unless you specify a different role here. If the AWS Batch service-linked role doesn't exist in your account, and no role is specified here, the service attempts to create the AWS Batch service-linked role in your account.  
This automatic service-linked role creation only applies to `MANAGED` compute environments. For `UNMANAGED` compute environments, you must explicitly specify a `serviceRole`.
If your specified role has a path other than `/`, then you must specify either the full role ARN (recommended) or prefix the role name with the path. For example, if a role with the name `bar` has a path of `/foo/`, specify `/foo/bar` as the role name. For more information, see [Friendly names and paths](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-friendly-names) in the *IAM User Guide*.  
Depending on how you created your AWS Batch service role, its ARN might contain the `service-role` path prefix. When you only specify the name of the service role, AWS Batch assumes that your ARN doesn't use the `service-role` path prefix. Because of this, we recommend that you specify the full ARN of your service role when you create compute environments.
Type: String  
Required: No

 ** [state](#API_CreateComputeEnvironment_RequestSyntax) **   <a name="Batch-CreateComputeEnvironment-request-state"></a>
The state of the compute environment. A compute environment must be created in the `ENABLED` state.  
If the state is `ENABLED`, then the compute environment accepts jobs from a queue and can scale out automatically based on queues.  
If the state is `ENABLED`, then the AWS Batch scheduler can attempt to place jobs from an associated job queue on the compute resources within the environment. If the compute environment is managed, then it can scale its instances out or in automatically, based on the job queue demand.  
If the state is `DISABLED`, then the AWS Batch scheduler doesn't attempt to place jobs within the environment. Jobs in a `STARTING` or `RUNNING` state continue to progress normally. Managed compute environments in the `DISABLED` state don't scale out.   
Compute environments in a `DISABLED` state may continue to incur billing charges, for example, if they have running instances due to jobs that are still executing or a non-zero `minvCpus` setting. To prevent additional charges, disable and delete the compute environment.
When an instance is idle, the instance scales down to the `minvCpus` value. However, the instance size doesn't change. For example, consider a `c5.8xlarge` instance with a `minvCpus` value of `4` and a `desiredvCpus` value of `36`. This instance doesn't scale down to a `c5.large` instance.  
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: No

 ** [tags](#API_CreateComputeEnvironment_RequestSyntax) **   <a name="Batch-CreateComputeEnvironment-request-tags"></a>
The tags that you apply to the compute environment to help you categorize and organize your resources. Each tag consists of a key and an optional value. For more information, see [Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in * AWS General Reference*.  
These tags can be updated or removed using the [TagResource](https://docs.aws.amazon.com/batch/latest/APIReference/API_TagResource.html) and [UntagResource](https://docs.aws.amazon.com/batch/latest/APIReference/API_UntagResource.html) API operations. These tags don't propagate to the underlying compute resources.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Maximum length of 256.  
Required: No

 ** [type](#API_CreateComputeEnvironment_RequestSyntax) **   <a name="Batch-CreateComputeEnvironment-request-type"></a>
The type of the compute environment: `MANAGED` or `UNMANAGED`. For more information, see [Compute Environments](https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html) in the * AWS Batch User Guide*.  
Type: String  
Valid Values: `MANAGED | UNMANAGED`   
Required: Yes

 ** [unmanagedvCpus](#API_CreateComputeEnvironment_RequestSyntax) **   <a name="Batch-CreateComputeEnvironment-request-unmanagedvCpus"></a>
The maximum number of vCPUs for an unmanaged compute environment. This parameter is only used for fair-share scheduling to reserve vCPU capacity for new share identifiers. If this parameter isn't provided for a fair-share job queue, no vCPU capacity is reserved.  
This parameter is only supported when the `type` parameter is set to `UNMANAGED`.
Type: Integer  
Required: No

## Response Syntax
<a name="API_CreateComputeEnvironment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "computeEnvironmentArn": "string",
   "computeEnvironmentName": "string"
}
```

## Response Elements
<a name="API_CreateComputeEnvironment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [computeEnvironmentArn](#API_CreateComputeEnvironment_ResponseSyntax) **   <a name="Batch-CreateComputeEnvironment-response-computeEnvironmentArn"></a>
The Amazon Resource Name (ARN) of the compute environment.  
Type: String

 ** [computeEnvironmentName](#API_CreateComputeEnvironment_ResponseSyntax) **   <a name="Batch-CreateComputeEnvironment-response-computeEnvironmentName"></a>
The name of the compute environment. It can be up to 128 characters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (\_).  
Type: String

## Errors
<a name="API_CreateComputeEnvironment_Errors"></a>

 ** ClientException **   
These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.  
HTTP Status Code: 400

 ** ServerException **   
These errors are usually caused by a server issue.  
HTTP Status Code: 500

## Examples
<a name="API_CreateComputeEnvironment_Examples"></a>

In the following example or examples, the Authorization header contents (` [authorization-params] `) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_CreateComputeEnvironment_Example_1"></a>

This example creates a managed compute environment with specific C4 instance types that are launched on demand. The compute environment is called `C4OnDemand`.

#### Sample Request
<a name="API_CreateComputeEnvironment_Example_1_Request"></a>

```
POST /v1/createcomputeenvironment HTTP/1.1
Host: batch.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: [content-length]
Authorization: [authorization-params]
X-Amz-Date: 20161128T223128Z
User-Agent: aws-cli/1.11.21 Python/2.7.12 Darwin/16.1.0 botocore/1.4.78

{
  "computeEnvironmentName": "C4OnDemand",
  "state": "ENABLED",
  "type": "MANAGED",
  "computeResources": {
    "subnets": [
      "subnet-220c0e0a",
      "subnet-1a95556d",
      "subnet-978f6dce"
    ],
    "tags": {
      "Name": "Batch Instance - C4OnDemand",
      "Department": "Engineering"
    },
    "desiredvCpus": 48,
    "minvCpus": 0,
    "instanceTypes": [
      "c4.large",
      "c4.xlarge",
      "c4.2xlarge",
      "c4.4xlarge",
      "c4.8xlarge"
    ],
    "securityGroupIds": [
      "sg-cf5093b2"
    ],
    "instanceRole": "ecsInstanceRole",
    "maxvCpus": 128,
    "type": "EC2",
    "ec2KeyPair": "id_rsa"
  },
  "serviceRole": "arn:aws:iam::123456789012:role/AWSBatchServiceRole"
}
```

#### Sample Response
<a name="API_CreateComputeEnvironment_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Mon, 28 Nov 2016 22:31:28 GMT
Content-Type: application/json
Content-Length: [content-length]
Connection: keep-alive
x-amzn-RequestId: [request-id]
X-Amzn-Trace-Id: [trace-id]
X-Cache: Miss from cloudfront
Via: 1.1 7e587c722adb25336835ccb4e5814e4e.cloudfront.net (CloudFront)
X-Amz-Cf-Id: GwQRsxvmiuj1HYwbYq9MAEsQfJpN6BknGQlNX1jAd5qLQFXyHBwOUQ==

{
  "computeEnvironmentName": "C4OnDemand",
  "computeEnvironmentArn": "arn:aws:batch:us-east-1:123456789012:compute-environment/C4OnDemand"
}
```

### Example
<a name="API_CreateComputeEnvironment_Example_2"></a>

This example creates a managed compute environment with the M4 instance type that's launched when the Spot Instance price less than or equal to 20% of the On-Demand price for the instance type. The compute environment is called `M4Spot`.

#### Sample Request
<a name="API_CreateComputeEnvironment_Example_2_Request"></a>

```
POST /v1/createcomputeenvironment HTTP/1.1
Host: batch.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: [content-length]
Authorization: [authorization-params]
X-Amz-Date: 20161128T223813Z
User-Agent: aws-cli/1.11.21 Python/2.7.12 Darwin/16.1.0 botocore/1.4.78

{
  "computeEnvironmentName": "M4Spot",
  "state": "ENABLED",
  "type": "MANAGED",
  "computeResources": {
    "subnets": [
      "subnet-220c0e0a",
      "subnet-1a95556d",
      "subnet-978f6dce"
    ],
    "type": "SPOT",
    "spotIamFleetRole": "arn:aws:iam::123456789012:role/aws-ec2-spot-fleet-role",
    "tags": {
      "Name": "Batch Instance - M4Spot",
      "Department": "Marketing"
    },
    "desiredvCpus": 4,
    "minvCpus": 0,
    "instanceTypes": [
      "m4"
    ],
    "securityGroupIds": [
      "sg-cf5093b2"
    ],
    "instanceRole": "ecsInstanceRole",
    "maxvCpus": 128,
    "bidPercentage": 20,
    "ec2KeyPair": "id_rsa"
  },
  "serviceRole": "arn:aws:iam::123456789012:role/AWSBatchServiceRole"
}
```

#### Sample Response
<a name="API_CreateComputeEnvironment_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Date: Mon, 28 Nov 2016 22:38:16 GMT
Content-Type: application/json
Content-Length: [content-length]
Connection: keep-alive
x-amzn-RequestId: [request-id]
X-Amzn-Trace-Id: [trace-id]
X-Cache: Miss from cloudfront
Via: 1.1 8455edd9286a1292a39c993fdeccce65.cloudfront.net (CloudFront)
X-Amz-Cf-Id: 4mklLyUpygUko86fMNzPgA8_D64lSwPmG6iIKhAZkGpOp2e-3cKg_w==

{
  "computeEnvironmentName": "M4Spot",
  "computeEnvironmentArn": "arn:aws:batch:us-east-1:123456789012:compute-environment/M4Spot"
}
```

## See Also
<a name="API_CreateComputeEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/batch-2016-08-10/CreateComputeEnvironment) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/batch-2016-08-10/CreateComputeEnvironment) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/CreateComputeEnvironment) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/batch-2016-08-10/CreateComputeEnvironment) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/CreateComputeEnvironment) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/batch-2016-08-10/CreateComputeEnvironment) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/batch-2016-08-10/CreateComputeEnvironment) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/batch-2016-08-10/CreateComputeEnvironment) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/CreateComputeEnvironment) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/CreateComputeEnvironment) 