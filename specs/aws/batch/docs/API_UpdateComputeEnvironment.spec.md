---
id: "@specs/aws/batch/docs/API_UpdateComputeEnvironment"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateComputeEnvironment"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# UpdateComputeEnvironment

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_UpdateComputeEnvironment
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateComputeEnvironment
<a name="API_UpdateComputeEnvironment"></a>

Updates an AWS Batch compute environment.

## Request Syntax
<a name="API_UpdateComputeEnvironment_RequestSyntax"></a>

```
POST /v1/updatecomputeenvironment HTTP/1.1
Content-type: application/json

{
   "computeEnvironment": "{{string}}",
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
      "subnets": [ "{{string}}" ],
      "tags": { 
         "{{string}}" : "{{string}}" 
      },
      "type": "{{string}}",
      "updateToLatestImageVersion": {{boolean}}
   },
   "context": "{{string}}",
   "serviceRole": "{{string}}",
   "state": "{{string}}",
   "unmanagedvCpus": {{number}},
   "updatePolicy": { 
      "jobExecutionTimeoutMinutes": {{number}},
      "terminateJobsOnUpdate": {{boolean}}
   }
}
```

## URI Request Parameters
<a name="API_UpdateComputeEnvironment_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateComputeEnvironment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [computeEnvironment](#API_UpdateComputeEnvironment_RequestSyntax) **   <a name="Batch-UpdateComputeEnvironment-request-computeEnvironment"></a>
The name or full Amazon Resource Name (ARN) of the compute environment to update.  
Type: String  
Required: Yes

 ** [computeResources](#API_UpdateComputeEnvironment_RequestSyntax) **   <a name="Batch-UpdateComputeEnvironment-request-computeResources"></a>
Details of the compute resources managed by the compute environment. Required for a managed compute environment. For more information, see [Compute Environments](https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html) in the * AWS Batch User Guide*.  
Type: [ComputeResourceUpdate](API_ComputeResourceUpdate.md) object  
Required: No

 ** [context](#API_UpdateComputeEnvironment_RequestSyntax) **   <a name="Batch-UpdateComputeEnvironment-request-context"></a>
Reserved.  
Type: String  
Required: No

 ** [serviceRole](#API_UpdateComputeEnvironment_RequestSyntax) **   <a name="Batch-UpdateComputeEnvironment-request-serviceRole"></a>
The full Amazon Resource Name (ARN) of the IAM role that allows AWS Batch to make calls to other AWS services on your behalf. For more information, see [AWS Batch service IAM role](https://docs.aws.amazon.com/batch/latest/userguide/service_IAM_role.html) in the * AWS Batch User Guide*.  
If the compute environment has a service-linked role, it can't be changed to use a regular IAM role. Likewise, if the compute environment has a regular IAM role, it can't be changed to use a service-linked role. To update the parameters for the compute environment that require an infrastructure update to change, the **AWSServiceRoleForBatch** service-linked role must be used. For more information, see [Updating compute environments](https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html) in the * AWS Batch User Guide*.
If your specified role has a path other than `/`, then you must either specify the full role ARN (recommended) or prefix the role name with the path.  
Depending on how you created your AWS Batch service role, its ARN might contain the `service-role` path prefix. When you only specify the name of the service role, AWS Batch assumes that your ARN doesn't use the `service-role` path prefix. Because of this, we recommend that you specify the full ARN of your service role when you create compute environments.
Type: String  
Required: No

 ** [state](#API_UpdateComputeEnvironment_RequestSyntax) **   <a name="Batch-UpdateComputeEnvironment-request-state"></a>
The state of the compute environment. Compute environments in the `ENABLED` state can accept jobs from a queue and scale in or out automatically based on the workload demand of its associated queues.  
If the state is `ENABLED`, then the AWS Batch scheduler can attempt to place jobs from an associated job queue on the compute resources within the environment. If the compute environment is managed, then it can scale its instances out or in automatically, based on the job queue demand.  
If the state is `DISABLED`, then the AWS Batch scheduler doesn't attempt to place jobs within the environment. Jobs in a `STARTING` or `RUNNING` state continue to progress normally. Managed compute environments in the `DISABLED` state don't scale out.   
Compute environments in a `DISABLED` state may continue to incur billing charges, for example, if they have running instances due to jobs that are still executing or a non-zero `minvCpus` setting. To prevent additional charges, disable and delete the compute environment.
When an instance is idle, the instance scales down to the `minvCpus` value. However, the instance size doesn't change. For example, consider a `c5.8xlarge` instance with a `minvCpus` value of `4` and a `desiredvCpus` value of `36`. This instance doesn't scale down to a `c5.large` instance.  
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: No

 ** [unmanagedvCpus](#API_UpdateComputeEnvironment_RequestSyntax) **   <a name="Batch-UpdateComputeEnvironment-request-unmanagedvCpus"></a>
The maximum number of vCPUs expected to be used for an unmanaged compute environment. Don't specify this parameter for a managed compute environment. This parameter is only used for fair-share scheduling to reserve vCPU capacity for new share identifiers. If this parameter isn't provided for a fair-share job queue, no vCPU capacity is reserved.  
Type: Integer  
Required: No

 ** [updatePolicy](#API_UpdateComputeEnvironment_RequestSyntax) **   <a name="Batch-UpdateComputeEnvironment-request-updatePolicy"></a>
Specifies the updated infrastructure update policy for the compute environment. For more information about infrastructure updates, see [Updating compute environments](https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html) in the * AWS Batch User Guide*.  
Type: [UpdatePolicy](API_UpdatePolicy.md) object  
Required: No

## Response Syntax
<a name="API_UpdateComputeEnvironment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "computeEnvironmentArn": "string",
   "computeEnvironmentName": "string"
}
```

## Response Elements
<a name="API_UpdateComputeEnvironment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [computeEnvironmentArn](#API_UpdateComputeEnvironment_ResponseSyntax) **   <a name="Batch-UpdateComputeEnvironment-response-computeEnvironmentArn"></a>
The Amazon Resource Name (ARN) of the compute environment.  
Type: String

 ** [computeEnvironmentName](#API_UpdateComputeEnvironment_ResponseSyntax) **   <a name="Batch-UpdateComputeEnvironment-response-computeEnvironmentName"></a>
The name of the compute environment. It can be up to 128 characters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (\_).  
Type: String

## Errors
<a name="API_UpdateComputeEnvironment_Errors"></a>

 ** ClientException **   
These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.  
HTTP Status Code: 400

 ** ServerException **   
These errors are usually caused by a server issue.  
HTTP Status Code: 500

## Examples
<a name="API_UpdateComputeEnvironment_Examples"></a>

In the following example or examples, the Authorization header contents (` [authorization-params] `) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_UpdateComputeEnvironment_Example_1"></a>

This example disables the `P3OnDemand` compute environment so it can be deleted.

#### Sample Request
<a name="API_UpdateComputeEnvironment_Example_1_Request"></a>

```
POST /v1/updatecomputeenvironment HTTP/1.1
Host: batch.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: [content-length]
Authorization: AUTHPARAMS
X-Amz-Date: 20161128T194248Z
User-Agent: aws-cli/1.11.21 Python/2.7.12 Darwin/16.1.0 botocore/1.4.78

{
  "computeEnvironment": "P3OnDemand",
  "state": "DISABLED"
}
```

#### Sample Response
<a name="API_UpdateComputeEnvironment_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: [content-length]
Connection: keep-alive
Date: Mon, 28 Nov 2016 19:42:49 GMT
x-amzn-RequestId: [request-id]
X-Amzn-Trace-Id: [trace-id]
X-Cache: Miss from cloudfront
Via: 1.1 7f3f42df8af148df1f9f1ee7175987ad.cloudfront.net (CloudFront)
X-Amz-Cf-Id: uxJn0P7cg_1RTxOs15FkCItWfmCeniKMZdXlFWaOfPfjqATHw3j-AA==

{
  "computeEnvironmentName": "P3OnDemand",
  "computeEnvironmentArn": "arn:aws:batch:us-east-1:123456789012:compute-environment/P3OnDemand"
}
```

## See Also
<a name="API_UpdateComputeEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/batch-2016-08-10/UpdateComputeEnvironment) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/batch-2016-08-10/UpdateComputeEnvironment) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/UpdateComputeEnvironment) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/batch-2016-08-10/UpdateComputeEnvironment) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/UpdateComputeEnvironment) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/batch-2016-08-10/UpdateComputeEnvironment) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/batch-2016-08-10/UpdateComputeEnvironment) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/batch-2016-08-10/UpdateComputeEnvironment) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/UpdateComputeEnvironment) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/UpdateComputeEnvironment) 