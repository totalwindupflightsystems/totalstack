---
id: "@specs/aws/batch/docs/API_DescribeQuotaShare"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeQuotaShare"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# DescribeQuotaShare

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_DescribeQuotaShare
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeQuotaShare
<a name="API_DescribeQuotaShare"></a>

Returns a description of the specified quota share.

## Request Syntax
<a name="API_DescribeQuotaShare_RequestSyntax"></a>

```
POST /v1/describequotashare HTTP/1.1
Content-type: application/json

{
   "quotaShareArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DescribeQuotaShare_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeQuotaShare_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [quotaShareArn](#API_DescribeQuotaShare_RequestSyntax) **   <a name="Batch-DescribeQuotaShare-request-quotaShareArn"></a>
The Amazon Resource Name (ARN) of the quota share.  
Type: String  
Required: Yes

## Response Syntax
<a name="API_DescribeQuotaShare_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "capacityLimits": [ 
      { 
         "capacityUnit": "string",
         "maxCapacity": number
      }
   ],
   "jobQueueArn": "string",
   "preemptionConfiguration": { 
      "inSharePreemption": "string"
   },
   "quotaShareArn": "string",
   "quotaShareName": "string",
   "resourceSharingConfiguration": { 
      "borrowLimit": number,
      "strategy": "string"
   },
   "state": "string",
   "status": "string",
   "tags": { 
      "string" : "string" 
   }
}
```

## Response Elements
<a name="API_DescribeQuotaShare_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [capacityLimits](#API_DescribeQuotaShare_ResponseSyntax) **   <a name="Batch-DescribeQuotaShare-response-capacityLimits"></a>
A list that specifies the quantity and type of compute capacity allocated to the quota share.  
Type: Array of [QuotaShareCapacityLimit](API_QuotaShareCapacityLimit.md) objects

 ** [jobQueueArn](#API_DescribeQuotaShare_ResponseSyntax) **   <a name="Batch-DescribeQuotaShare-response-jobQueueArn"></a>
The ARN of the job queue associated with the quota share.  
Type: String

 ** [preemptionConfiguration](#API_DescribeQuotaShare_ResponseSyntax) **   <a name="Batch-DescribeQuotaShare-response-preemptionConfiguration"></a>
Specifies the preemption behavior for jobs in a quota share.  
Type: [QuotaSharePreemptionConfiguration](API_QuotaSharePreemptionConfiguration.md) object

 ** [quotaShareArn](#API_DescribeQuotaShare_ResponseSyntax) **   <a name="Batch-DescribeQuotaShare-response-quotaShareArn"></a>
The Amazon Resource Name (ARN) of the quota share.  
Type: String

 ** [quotaShareName](#API_DescribeQuotaShare_ResponseSyntax) **   <a name="Batch-DescribeQuotaShare-response-quotaShareName"></a>
The name of the quota share.  
Type: String

 ** [resourceSharingConfiguration](#API_DescribeQuotaShare_ResponseSyntax) **   <a name="Batch-DescribeQuotaShare-response-resourceSharingConfiguration"></a>
Specifies whether a quota share reserves, lends, or both lends and borrows idle compute capacity.  
Type: [QuotaShareResourceSharingConfiguration](API_QuotaShareResourceSharingConfiguration.md) object

 ** [state](#API_DescribeQuotaShare_ResponseSyntax) **   <a name="Batch-DescribeQuotaShare-response-state"></a>
The state of the quota share.  
Type: String  
Valid Values: `ENABLED | DISABLED` 

 ** [status](#API_DescribeQuotaShare_ResponseSyntax) **   <a name="Batch-DescribeQuotaShare-response-status"></a>
The current status of the quota share.  
Type: String  
Valid Values: `CREATING | VALID | INVALID | UPDATING | DELETING` 

 ** [tags](#API_DescribeQuotaShare_ResponseSyntax) **   <a name="Batch-DescribeQuotaShare-response-tags"></a>
The tags applied to the quota share.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Maximum length of 256.

## Errors
<a name="API_DescribeQuotaShare_Errors"></a>

 ** ClientException **   
These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.  
HTTP Status Code: 400

 ** ServerException **   
These errors are usually caused by a server issue.  
HTTP Status Code: 500

## Examples
<a name="API_DescribeQuotaShare_Examples"></a>

In the following example or examples, the Authorization header contents (` [authorization-params] `) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_DescribeQuotaShare_Example_1"></a>

This example describes the specified quota share.

#### Sample Request
<a name="API_DescribeQuotaShare_Example_1_Request"></a>

```
POST /v1/describequotashare HTTP/1.1
Host: batch.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: [content-length]
Authorization: [authorization-params]
X-Amz-Date: 20250801T001258Z
User-Agent: aws-cli/2.27.33 Python/3.13.4 Darwin/24.3.0

{
  "quotaShareArn": "arn:aws:batch:us-east-1:123456789012:job-queue/HighPriority/quota-share/TeamAShare"
}
```

#### Sample Response
<a name="API_DescribeQuotaShare_Example_1_Response"></a>

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
  "quotaShareArn": "arn:aws:batch:us-east-1:123456789012:job-queue/HighPriority/quota-share/TeamAShare",
  "jobQueueArn": "arn:aws:batch:us-east-1:123456789012:job-queue/HighPriority",
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
  "status": "VALID",
  "tags": {
    "Department": "Engineering"
  }
}
```

## See Also
<a name="API_DescribeQuotaShare_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/batch-2016-08-10/DescribeQuotaShare) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/batch-2016-08-10/DescribeQuotaShare) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/DescribeQuotaShare) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/batch-2016-08-10/DescribeQuotaShare) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/DescribeQuotaShare) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/batch-2016-08-10/DescribeQuotaShare) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/batch-2016-08-10/DescribeQuotaShare) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/batch-2016-08-10/DescribeQuotaShare) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/DescribeQuotaShare) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/DescribeQuotaShare) 