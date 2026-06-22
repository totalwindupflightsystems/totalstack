---
id: "@specs/aws/batch/docs/API_CreateQuotaShare"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateQuotaShare"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# CreateQuotaShare

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_CreateQuotaShare
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateQuotaShare
<a name="API_CreateQuotaShare"></a>

Creates an AWS Batch quota share. Each quota share operates as a virtual queue with a configured compute capacity, resource sharing strategy, and borrow limits. 

## Request Syntax
<a name="API_CreateQuotaShare_RequestSyntax"></a>

```
POST /v1/createquotashare HTTP/1.1
Content-type: application/json

{
   "capacityLimits": [ 
      { 
         "capacityUnit": "{{string}}",
         "maxCapacity": {{number}}
      }
   ],
   "jobQueue": "{{string}}",
   "preemptionConfiguration": { 
      "inSharePreemption": "{{string}}"
   },
   "quotaShareName": "{{string}}",
   "resourceSharingConfiguration": { 
      "borrowLimit": {{number}},
      "strategy": "{{string}}"
   },
   "state": "{{string}}",
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_CreateQuotaShare_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateQuotaShare_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [capacityLimits](#API_CreateQuotaShare_RequestSyntax) **   <a name="Batch-CreateQuotaShare-request-capacityLimits"></a>
A list that specifies the quantity and type of compute capacity allocated to the quota share.   
Type: Array of [QuotaShareCapacityLimit](API_QuotaShareCapacityLimit.md) objects  
Required: Yes

 ** [jobQueue](#API_CreateQuotaShare_RequestSyntax) **   <a name="Batch-CreateQuotaShare-request-jobQueue"></a>
The AWS Batch job queue associated with the quota share. This can be the job queue name or ARN. A job queue must be in the `VALID` state before you can associate it with a quota share.  
Type: String  
Required: Yes

 ** [preemptionConfiguration](#API_CreateQuotaShare_RequestSyntax) **   <a name="Batch-CreateQuotaShare-request-preemptionConfiguration"></a>
Specifies the preemption behavior for jobs in a quota share.  
Type: [QuotaSharePreemptionConfiguration](API_QuotaSharePreemptionConfiguration.md) object  
Required: Yes

 ** [quotaShareName](#API_CreateQuotaShare_RequestSyntax) **   <a name="Batch-CreateQuotaShare-request-quotaShareName"></a>
The name of the quota share. It can be up to 128 characters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (\_).  
Type: String  
Required: Yes

 ** [resourceSharingConfiguration](#API_CreateQuotaShare_RequestSyntax) **   <a name="Batch-CreateQuotaShare-request-resourceSharingConfiguration"></a>
Specifies whether a quota share reserves, lends, or both lends and borrows idle compute capacity.  
Type: [QuotaShareResourceSharingConfiguration](API_QuotaShareResourceSharingConfiguration.md) object  
Required: Yes

 ** [state](#API_CreateQuotaShare_RequestSyntax) **   <a name="Batch-CreateQuotaShare-request-state"></a>
The state of the quota share. If the quota share is `ENABLED`, it is able to accept jobs. If the quota share is `DISABLED`, new jobs won't be accepted but jobs already submitted can finish. The default state is `ENABLED`.  
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: No

 ** [tags](#API_CreateQuotaShare_RequestSyntax) **   <a name="Batch-CreateQuotaShare-request-tags"></a>
The tags that you apply to the quota share to help you categorize and organize your resources. Each tag consists of a key and an optional value. For more information, see [Tagging your AWS Batch resources](https://docs.aws.amazon.com/batch/latest/userguide/using-tags.html) in * AWS Batch User Guide*.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Maximum length of 256.  
Required: No

## Response Syntax
<a name="API_CreateQuotaShare_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "quotaShareArn": "string",
   "quotaShareName": "string"
}
```

## Response Elements
<a name="API_CreateQuotaShare_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [quotaShareArn](#API_CreateQuotaShare_ResponseSyntax) **   <a name="Batch-CreateQuotaShare-response-quotaShareArn"></a>
The Amazon Resource Name (ARN) of the quota share.  
Type: String

 ** [quotaShareName](#API_CreateQuotaShare_ResponseSyntax) **   <a name="Batch-CreateQuotaShare-response-quotaShareName"></a>
The name of the quota share.  
Type: String

## Errors
<a name="API_CreateQuotaShare_Errors"></a>

 ** ClientException **   
These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.  
HTTP Status Code: 400

 ** ServerException **   
These errors are usually caused by a server issue.  
HTTP Status Code: 500

## Examples
<a name="API_CreateQuotaShare_Examples"></a>

In the following example or examples, the Authorization header contents (` [authorization-params] `) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_CreateQuotaShare_Example_1"></a>

This example creates a quota share called `TeamAShare` associated with the `HighPriority` job queue, with capacity limits of 10 `ml.m5.large` and 5 `ml.m5.xlarge` instances, and a borrow limit of 200%.

#### Sample Request
<a name="API_CreateQuotaShare_Example_1_Request"></a>

```
POST /v1/createquotashare HTTP/1.1
Host: batch.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: [content-length]
Authorization: [authorization-params]
X-Amz-Date: 20250801T001258Z
User-Agent: aws-cli/2.27.33 Python/3.13.4 Darwin/24.3.0

{
  "quotaShareName": "TeamAShare",
  "jobQueue": "HighPriority",
  "capacityLimits": [
    {
      "maxCapacity": 10,
      "capacityUnit": "ml.m5.large"
    },
    {
      "maxCapacity": 5,
      "capacityUnit": "ml.m5.xlarge"
    }
  ],
  "resourceSharingConfiguration": {
    "strategy": "LEND_AND_BORROW",
    "borrowLimit": 200
  },
  "preemptionConfiguration": {
    "inSharePreemption": "ENABLED"
  },
  "state": "ENABLED",
  "tags": {
    "Department": "Engineering"
  }
}
```

#### Sample Response
<a name="API_CreateQuotaShare_Example_1_Response"></a>

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
  "quotaShareName": "TeamAShare",
  "quotaShareArn": "arn:aws:batch:us-east-1:123456789012:job-queue/HighPriority/quota-share/TeamAShare"
}
```

## See Also
<a name="API_CreateQuotaShare_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/batch-2016-08-10/CreateQuotaShare) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/batch-2016-08-10/CreateQuotaShare) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/CreateQuotaShare) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/batch-2016-08-10/CreateQuotaShare) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/CreateQuotaShare) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/batch-2016-08-10/CreateQuotaShare) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/batch-2016-08-10/CreateQuotaShare) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/batch-2016-08-10/CreateQuotaShare) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/CreateQuotaShare) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/CreateQuotaShare) 