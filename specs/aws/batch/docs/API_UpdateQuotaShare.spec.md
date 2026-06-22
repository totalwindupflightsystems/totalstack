---
id: "@specs/aws/batch/docs/API_UpdateQuotaShare"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateQuotaShare"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# UpdateQuotaShare

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_UpdateQuotaShare
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateQuotaShare
<a name="API_UpdateQuotaShare"></a>

Updates a quota share.

## Request Syntax
<a name="API_UpdateQuotaShare_RequestSyntax"></a>

```
POST /v1/updatequotashare HTTP/1.1
Content-type: application/json

{
   "capacityLimits": [ 
      { 
         "capacityUnit": "{{string}}",
         "maxCapacity": {{number}}
      }
   ],
   "preemptionConfiguration": { 
      "inSharePreemption": "{{string}}"
   },
   "quotaShareArn": "{{string}}",
   "resourceSharingConfiguration": { 
      "borrowLimit": {{number}},
      "strategy": "{{string}}"
   },
   "state": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateQuotaShare_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateQuotaShare_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [capacityLimits](#API_UpdateQuotaShare_RequestSyntax) **   <a name="Batch-UpdateQuotaShare-request-capacityLimits"></a>
A list that specifies the quantity and type of compute capacity allocated to the quota share.  
Type: Array of [QuotaShareCapacityLimit](API_QuotaShareCapacityLimit.md) objects  
Required: No

 ** [preemptionConfiguration](#API_UpdateQuotaShare_RequestSyntax) **   <a name="Batch-UpdateQuotaShare-request-preemptionConfiguration"></a>
Specifies the preemption behavior for jobs in a quota share.  
Type: [QuotaSharePreemptionConfiguration](API_QuotaSharePreemptionConfiguration.md) object  
Required: No

 ** [quotaShareArn](#API_UpdateQuotaShare_RequestSyntax) **   <a name="Batch-UpdateQuotaShare-request-quotaShareArn"></a>
The Amazon Resource Name (ARN) of the quota share to update.  
Type: String  
Required: Yes

 ** [resourceSharingConfiguration](#API_UpdateQuotaShare_RequestSyntax) **   <a name="Batch-UpdateQuotaShare-request-resourceSharingConfiguration"></a>
Specifies whether a quota share reserves, lends, or both lends and borrows idle compute capacity.  
Type: [QuotaShareResourceSharingConfiguration](API_QuotaShareResourceSharingConfiguration.md) object  
Required: No

 ** [state](#API_UpdateQuotaShare_RequestSyntax) **   <a name="Batch-UpdateQuotaShare-request-state"></a>
The state of the quota share. If the quota share is `ENABLED`, it is able to accept jobs. If the quota share is `DISABLED`, new jobs won't be accepted but jobs already submitted can finish.  
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: No

## Response Syntax
<a name="API_UpdateQuotaShare_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "quotaShareArn": "string",
   "quotaShareName": "string"
}
```

## Response Elements
<a name="API_UpdateQuotaShare_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [quotaShareArn](#API_UpdateQuotaShare_ResponseSyntax) **   <a name="Batch-UpdateQuotaShare-response-quotaShareArn"></a>
The Amazon Resource Name (ARN) of the quota share.  
Type: String

 ** [quotaShareName](#API_UpdateQuotaShare_ResponseSyntax) **   <a name="Batch-UpdateQuotaShare-response-quotaShareName"></a>
The name of the quota share.  
Type: String

## Errors
<a name="API_UpdateQuotaShare_Errors"></a>

 ** ClientException **   
These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.  
HTTP Status Code: 400

 ** ServerException **   
These errors are usually caused by a server issue.  
HTTP Status Code: 500

## Examples
<a name="API_UpdateQuotaShare_Examples"></a>

In the following example or examples, the Authorization header contents (` [authorization-params] `) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_UpdateQuotaShare_Example_1"></a>

This example updates a quota share to use a reserve strategy and disable in-share preemption.

#### Sample Request
<a name="API_UpdateQuotaShare_Example_1_Request"></a>

```
POST /v1/updatequotashare HTTP/1.1
Host: batch.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: [content-length]
Authorization: [authorization-params]
X-Amz-Date: 20250801T001258Z
User-Agent: aws-cli/2.27.33 Python/3.13.4 Darwin/24.3.0

{
  "quotaShareArn": "arn:aws:batch:us-east-1:123456789012:job-queue/HighPriority/quota-share/TeamAShare",
  "resourceSharingConfiguration": {
    "strategy": "RESERVE"
  },
  "preemptionConfiguration": {
    "inSharePreemption": "DISABLED"
  }
}
```

#### Sample Response
<a name="API_UpdateQuotaShare_Example_1_Response"></a>

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
<a name="API_UpdateQuotaShare_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/batch-2016-08-10/UpdateQuotaShare) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/batch-2016-08-10/UpdateQuotaShare) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/UpdateQuotaShare) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/batch-2016-08-10/UpdateQuotaShare) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/UpdateQuotaShare) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/batch-2016-08-10/UpdateQuotaShare) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/batch-2016-08-10/UpdateQuotaShare) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/batch-2016-08-10/UpdateQuotaShare) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/UpdateQuotaShare) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/UpdateQuotaShare) 