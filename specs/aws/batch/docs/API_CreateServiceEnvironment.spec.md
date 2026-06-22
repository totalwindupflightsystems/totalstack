---
id: "@specs/aws/batch/docs/API_CreateServiceEnvironment"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateServiceEnvironment"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# CreateServiceEnvironment

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_CreateServiceEnvironment
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateServiceEnvironment
<a name="API_CreateServiceEnvironment"></a>

Creates a service environment for running service jobs. Service environments define capacity limits for specific service types such as SageMaker Training jobs.

## Request Syntax
<a name="API_CreateServiceEnvironment_RequestSyntax"></a>

```
POST /v1/createserviceenvironment HTTP/1.1
Content-type: application/json

{
   "capacityLimits": [ 
      { 
         "capacityUnit": "{{string}}",
         "maxCapacity": {{number}}
      }
   ],
   "serviceEnvironmentName": "{{string}}",
   "serviceEnvironmentType": "{{string}}",
   "state": "{{string}}",
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_CreateServiceEnvironment_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateServiceEnvironment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [capacityLimits](#API_CreateServiceEnvironment_RequestSyntax) **   <a name="Batch-CreateServiceEnvironment-request-capacityLimits"></a>
The capacity limits for the service environment. The number of instances a job consumes is the total number of instances requested in the submit training job request resource configuration.  
Type: Array of [CapacityLimit](API_CapacityLimit.md) objects  
Required: Yes

 ** [serviceEnvironmentName](#API_CreateServiceEnvironment_RequestSyntax) **   <a name="Batch-CreateServiceEnvironment-request-serviceEnvironmentName"></a>
The name for the service environment. It can be up to 128 characters long and can contain letters, numbers, hyphens (-), and underscores (\_).  
Type: String  
Required: Yes

 ** [serviceEnvironmentType](#API_CreateServiceEnvironment_RequestSyntax) **   <a name="Batch-CreateServiceEnvironment-request-serviceEnvironmentType"></a>
The type of service environment. For SageMaker Training jobs, specify `SAGEMAKER_TRAINING`.  
Type: String  
Valid Values: `SAGEMAKER_TRAINING`   
Required: Yes

 ** [state](#API_CreateServiceEnvironment_RequestSyntax) **   <a name="Batch-CreateServiceEnvironment-request-state"></a>
The state of the service environment. Valid values are `ENABLED` and `DISABLED`. The default value is `ENABLED`.  
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: No

 ** [tags](#API_CreateServiceEnvironment_RequestSyntax) **   <a name="Batch-CreateServiceEnvironment-request-tags"></a>
The tags that you apply to the service environment to help you categorize and organize your resources. Each tag consists of a key and an optional value. For more information, see [Tagging your AWS Batch resources](https://docs.aws.amazon.com/batch/latest/userguide/using-tags.html).  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Maximum length of 256.  
Required: No

## Response Syntax
<a name="API_CreateServiceEnvironment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "serviceEnvironmentArn": "string",
   "serviceEnvironmentName": "string"
}
```

## Response Elements
<a name="API_CreateServiceEnvironment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [serviceEnvironmentArn](#API_CreateServiceEnvironment_ResponseSyntax) **   <a name="Batch-CreateServiceEnvironment-response-serviceEnvironmentArn"></a>
The Amazon Resource Name (ARN) of the service environment.  
Type: String

 ** [serviceEnvironmentName](#API_CreateServiceEnvironment_ResponseSyntax) **   <a name="Batch-CreateServiceEnvironment-response-serviceEnvironmentName"></a>
The name of the service environment.  
Type: String

## Errors
<a name="API_CreateServiceEnvironment_Errors"></a>

 ** ClientException **   
These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.  
HTTP Status Code: 400

 ** ServerException **   
These errors are usually caused by a server issue.  
HTTP Status Code: 500

## Examples
<a name="API_CreateServiceEnvironment_Examples"></a>

In the following example or examples, the Authorization header contents (` [authorization-params] `) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_CreateServiceEnvironment_Example_1"></a>

This example creates a service environment for SageMaker Training jobs.

#### Sample Request
<a name="API_CreateServiceEnvironment_Example_1_Request"></a>

```
POST /v1/createserviceenvironment HTTP/1.1
Host: batch.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: [content-length]
Authorization: [authorization-params]
X-Amz-Date: 20250801T001258Z
User-Agent: aws-cli/2.27.33 Python/3.13.4 Darwin/24.3.0

{
  "serviceEnvironmentName": "SageMakerTrainingEnv",
  "serviceEnvironmentType": "SAGEMAKER_TRAINING",
  "capacityLimits": [
    {
      "maxCapacity": 50,
      "capacityUnit": "NUM_INSTANCES"
    }
  ]
}
```

#### Sample Response
<a name="API_CreateServiceEnvironment_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: [content-length]
Connection: keep-alive
Date: Fri, 01 Aug 2025 00:12:59 GMT
x-amzn-RequestId: [request-id]
X-Amzn-Trace-Id: [trace-id]
X-Cache: Miss from cloudfront
Via: 1.1 example7k9m3n8q4r2w5x1z6c4vexample.cloudfront.net (CloudFront)
X-Amz-Cf-Id: whn1dX1uTx34Lvao7-7ZdkDXEbCZ_sjn3v3hHVFgbo1ORJtXyexample

{
  "serviceEnvironmentName": "SageMakerTrainingEnv",
  "serviceEnvironmentArn": "arn:aws:batch:us-east-1:123456789012:service-environment/SageMakerTrainingEnv"
}
```

## See Also
<a name="API_CreateServiceEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/batch-2016-08-10/CreateServiceEnvironment) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/batch-2016-08-10/CreateServiceEnvironment) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/CreateServiceEnvironment) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/batch-2016-08-10/CreateServiceEnvironment) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/CreateServiceEnvironment) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/batch-2016-08-10/CreateServiceEnvironment) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/batch-2016-08-10/CreateServiceEnvironment) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/batch-2016-08-10/CreateServiceEnvironment) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/CreateServiceEnvironment) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/CreateServiceEnvironment) 