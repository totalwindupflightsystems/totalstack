---
id: "@specs/aws/batch/docs/API_DescribeJobQueues"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeJobQueues"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# DescribeJobQueues

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_DescribeJobQueues
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeJobQueues
<a name="API_DescribeJobQueues"></a>

Describes one or more of your job queues.

## Request Syntax
<a name="API_DescribeJobQueues_RequestSyntax"></a>

```
POST /v1/describejobqueues HTTP/1.1
Content-type: application/json

{
   "jobQueues": [ "{{string}}" ],
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DescribeJobQueues_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeJobQueues_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [jobQueues](#API_DescribeJobQueues_RequestSyntax) **   <a name="Batch-DescribeJobQueues-request-jobQueues"></a>
A list of up to 100 queue names or full queue Amazon Resource Name (ARN) entries.  
Type: Array of strings  
Required: No

 ** [maxResults](#API_DescribeJobQueues_RequestSyntax) **   <a name="Batch-DescribeJobQueues-request-maxResults"></a>
The maximum number of results returned by `DescribeJobQueues` in paginated output. When this parameter is used, `DescribeJobQueues` only returns `maxResults` results in a single page and a `nextToken` response element. The remaining results of the initial request can be seen by sending another `DescribeJobQueues` request with the returned `nextToken` value. This value can be between 1 and 100. If this parameter isn't used, then `DescribeJobQueues` returns up to 100 results and a `nextToken` value if applicable.  
Type: Integer  
Required: No

 ** [nextToken](#API_DescribeJobQueues_RequestSyntax) **   <a name="Batch-DescribeJobQueues-request-nextToken"></a>
The `nextToken` value returned from a previous paginated `DescribeJobQueues` request where `maxResults` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the `nextToken` value. This value is `null` when there are no more results to return.  
Treat this token as an opaque identifier that's only used to retrieve the next items in a list and not for other programmatic purposes.
Type: String  
Required: No

## Response Syntax
<a name="API_DescribeJobQueues_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "jobQueues": [ 
      { 
         "computeEnvironmentOrder": [ 
            { 
               "computeEnvironment": "string",
               "order": number
            }
         ],
         "jobQueueArn": "string",
         "jobQueueName": "string",
         "jobQueueType": "string",
         "jobStateTimeLimitActions": [ 
            { 
               "action": "string",
               "maxTimeSeconds": number,
               "reason": "string",
               "state": "string"
            }
         ],
         "priority": number,
         "schedulingPolicyArn": "string",
         "serviceEnvironmentOrder": [ 
            { 
               "order": number,
               "serviceEnvironment": "string"
            }
         ],
         "state": "string",
         "status": "string",
         "statusReason": "string",
         "tags": { 
            "string" : "string" 
         }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeJobQueues_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobQueues](#API_DescribeJobQueues_ResponseSyntax) **   <a name="Batch-DescribeJobQueues-response-jobQueues"></a>
The list of job queues.  
Type: Array of [JobQueueDetail](API_JobQueueDetail.md) objects

 ** [nextToken](#API_DescribeJobQueues_ResponseSyntax) **   <a name="Batch-DescribeJobQueues-response-nextToken"></a>
The `nextToken` value to include in a future `DescribeJobQueues` request. When the results of a `DescribeJobQueues` request exceed `maxResults`, this value can be used to retrieve the next page of results. This value is `null` when there are no more results to return.  
Type: String

## Errors
<a name="API_DescribeJobQueues_Errors"></a>

 ** ClientException **   
These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.  
HTTP Status Code: 400

 ** ServerException **   
These errors are usually caused by a server issue.  
HTTP Status Code: 500

## Examples
<a name="API_DescribeJobQueues_Examples"></a>

In the following example or examples, the Authorization header contents (` [authorization-params] `) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_DescribeJobQueues_Example_1"></a>

This example describes the `HighPriority` job queue.

#### Sample Request
<a name="API_DescribeJobQueues_Example_1_Request"></a>

```
POST /v1/describejobqueues HTTP/1.1
Host: batch.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: [content-length]
Authorization: [authorization-params]
X-Amz-Date: 20161128T194731Z
User-Agent: aws-cli/1.11.21 Python/2.7.12 Darwin/16.1.0 botocore/1.4.78

{
  "jobQueues": [
    "HighPriority"
  ]
}
```

#### Sample Response
<a name="API_DescribeJobQueues_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Mon, 28 Nov 2016 19:47:32 GMT
Content-Type: application/json
Content-Length: [content-length]
Connection: keep-alive
x-amzn-RequestId: [request-id]
X-Amzn-Trace-Id: [trace-id]
X-Cache: Miss from cloudfront
Via: 1.1 7bfcc2251021d9dc94a87ff179d69731.cloudfront.net (CloudFront)
X-Amz-Cf-Id: dwf7P2pnEYCxN1C3XdApqDtqzLfjpWAjbHvskd9oUqz4OUn9pvtx3Q==

{
  "jobQueues": [{
    "jobQueueName": "HighPriority",
    "jobQueueArn": "arn:aws:batch:us-east-1:123456789012:job-queue/HighPriority",
    "state": "ENABLED",
    "status": "VALID",
    "statusReason": "JobQueue Healthy",
    "priority": 10,
    "computeEnvironmentOrder": [{
      "order": 1,
      "computeEnvironment": "arn:aws:batch:us-east-1:123456789012:compute-environment/C4OnDemand"
    }]
  }]
}
```

## See Also
<a name="API_DescribeJobQueues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/batch-2016-08-10/DescribeJobQueues) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/batch-2016-08-10/DescribeJobQueues) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/DescribeJobQueues) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/batch-2016-08-10/DescribeJobQueues) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/DescribeJobQueues) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/batch-2016-08-10/DescribeJobQueues) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/batch-2016-08-10/DescribeJobQueues) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/batch-2016-08-10/DescribeJobQueues) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/DescribeJobQueues) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/DescribeJobQueues) 