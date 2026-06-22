---
id: "@specs/aws/batch/docs/API_UpdateServiceEnvironment"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateServiceEnvironment"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# UpdateServiceEnvironment

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_UpdateServiceEnvironment
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateServiceEnvironment
<a name="API_UpdateServiceEnvironment"></a>

Updates a service environment. You can update the state of a service environment from `ENABLED` to `DISABLED` to prevent new service jobs from being placed in the service environment.

## Request Syntax
<a name="API_UpdateServiceEnvironment_RequestSyntax"></a>

```
POST /v1/updateserviceenvironment HTTP/1.1
Content-type: application/json

{
   "capacityLimits": [ 
      { 
         "capacityUnit": "{{string}}",
         "maxCapacity": {{number}}
      }
   ],
   "serviceEnvironment": "{{string}}",
   "state": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateServiceEnvironment_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateServiceEnvironment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [capacityLimits](#API_UpdateServiceEnvironment_RequestSyntax) **   <a name="Batch-UpdateServiceEnvironment-request-capacityLimits"></a>
The capacity limits for the service environment. This defines the maximum resources that can be used by service jobs in this environment.  
Type: Array of [CapacityLimit](API_CapacityLimit.md) objects  
Required: No

 ** [serviceEnvironment](#API_UpdateServiceEnvironment_RequestSyntax) **   <a name="Batch-UpdateServiceEnvironment-request-serviceEnvironment"></a>
The name or ARN of the service environment to update.  
Type: String  
Required: Yes

 ** [state](#API_UpdateServiceEnvironment_RequestSyntax) **   <a name="Batch-UpdateServiceEnvironment-request-state"></a>
The state of the service environment.   
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: No

## Response Syntax
<a name="API_UpdateServiceEnvironment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "serviceEnvironmentArn": "string",
   "serviceEnvironmentName": "string"
}
```

## Response Elements
<a name="API_UpdateServiceEnvironment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [serviceEnvironmentArn](#API_UpdateServiceEnvironment_ResponseSyntax) **   <a name="Batch-UpdateServiceEnvironment-response-serviceEnvironmentArn"></a>
The Amazon Resource Name (ARN) of the service environment that was updated.  
Type: String

 ** [serviceEnvironmentName](#API_UpdateServiceEnvironment_ResponseSyntax) **   <a name="Batch-UpdateServiceEnvironment-response-serviceEnvironmentName"></a>
The name of the service environment that was updated.  
Type: String

## Errors
<a name="API_UpdateServiceEnvironment_Errors"></a>

 ** ClientException **   
These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.  
HTTP Status Code: 400

 ** ServerException **   
These errors are usually caused by a server issue.  
HTTP Status Code: 500

## Examples
<a name="API_UpdateServiceEnvironment_Examples"></a>

In the following example or examples, the Authorization header contents (` [authorization-params] `) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_UpdateServiceEnvironment_Example_1"></a>

This example updates a service environment to disable it.

#### Sample Request
<a name="API_UpdateServiceEnvironment_Example_1_Request"></a>

```
POST /v1/updateserviceenvironment HTTP/1.1
Host: batch.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: [content-length]
Authorization: [authorization-params]
X-Amz-Date: 20250801T154520Z
User-Agent: aws-cli/2.27.33 Python/3.13.4 Darwin/24.3.0

{
  "serviceEnvironment": "SageMakerTrainingEnv",
  "state": "DISABLED"
}
```

#### Sample Response
<a name="API_UpdateServiceEnvironment_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: [content-length]
Connection: keep-alive
Date: Fri, 01 Aug 2025 15:45:21 GMT
x-amzn-RequestId: [request-id]
X-Amzn-Trace-Id: [trace-id]
X-Cache: Miss from cloudfront
Via: 1.1 25g84de7k2m5n8p1q4r9s6t3w2xexample.cloudfront.net (CloudFront)
X-Amz-Cf-Id: ghi4jkl7mno0pqr3stu6vwx9yz2345fghijklmnopqrstuexample

{
  "serviceEnvironmentName": "SageMakerTrainingEnv",
  "serviceEnvironmentArn": "arn:aws:batch:us-east-1:123456789012:service-environment/SageMakerTrainingEnv"
}
```

## See Also
<a name="API_UpdateServiceEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/batch-2016-08-10/UpdateServiceEnvironment) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/batch-2016-08-10/UpdateServiceEnvironment) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/UpdateServiceEnvironment) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/batch-2016-08-10/UpdateServiceEnvironment) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/UpdateServiceEnvironment) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/batch-2016-08-10/UpdateServiceEnvironment) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/batch-2016-08-10/UpdateServiceEnvironment) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/batch-2016-08-10/UpdateServiceEnvironment) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/UpdateServiceEnvironment) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/UpdateServiceEnvironment) 