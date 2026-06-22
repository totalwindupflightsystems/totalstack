---
id: "@specs/aws/batch/docs/API_ListQuotaShares"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListQuotaShares"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# ListQuotaShares

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_ListQuotaShares
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListQuotaShares
<a name="API_ListQuotaShares"></a>

Returns a list of AWS Batch quota shares associated with a job queue.

## Request Syntax
<a name="API_ListQuotaShares_RequestSyntax"></a>

```
POST /v1/listquotashares HTTP/1.1
Content-type: application/json

{
   "jobQueue": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListQuotaShares_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListQuotaShares_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [jobQueue](#API_ListQuotaShares_RequestSyntax) **   <a name="Batch-ListQuotaShares-request-jobQueue"></a>
The name or full Amazon Resource Name (ARN) of the job queue used to list quota shares.  
Type: String  
Required: Yes

 ** [maxResults](#API_ListQuotaShares_RequestSyntax) **   <a name="Batch-ListQuotaShares-request-maxResults"></a>
The maximum number of results returned by `ListQuotaShares` in paginated output. When this parameter is used, `ListQuotaShares` only returns `maxResults` results in a single page and a `nextToken` response element. You can see the remaining results of the initial request by sending another `ListQuotaShares` request with the returned `nextToken` value. This value can be between 1 and 100. If this parameter isn't used, `ListQuotaShares` returns up to 100 results and a `nextToken` value if applicable.  
Type: Integer  
Required: No

 ** [nextToken](#API_ListQuotaShares_RequestSyntax) **   <a name="Batch-ListQuotaShares-request-nextToken"></a>
The `nextToken` value that's returned from a previous paginated `ListQuotaShares` request where `maxResults` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the `nextToken` value. This value is `null` when there are no more results to return.  
Treat this token as an opaque identifier that's only used to retrieve the next items in a list and not for other programmatic purposes.
Type: String  
Required: No

## Response Syntax
<a name="API_ListQuotaShares_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "quotaShares": [ 
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
         "status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListQuotaShares_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListQuotaShares_ResponseSyntax) **   <a name="Batch-ListQuotaShares-response-nextToken"></a>
The `nextToken` value to include in a future `ListQuotaShares` request. When the results of a `ListQuotaShares` request exceed `maxResults`, this value can be used to retrieve the next page of results. This value is `null` when there are no more results to return.  
Type: String

 ** [quotaShares](#API_ListQuotaShares_ResponseSyntax) **   <a name="Batch-ListQuotaShares-response-quotaShares"></a>
A list of quota shares that match the request.  
Type: Array of [QuotaShareDetail](API_QuotaShareDetail.md) objects

## Errors
<a name="API_ListQuotaShares_Errors"></a>

 ** ClientException **   
These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.  
HTTP Status Code: 400

 ** ServerException **   
These errors are usually caused by a server issue.  
HTTP Status Code: 500

## Examples
<a name="API_ListQuotaShares_Examples"></a>

In the following example or examples, the Authorization header contents (` [authorization-params] `) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_ListQuotaShares_Example_1"></a>

This example lists the quota shares associated with the `HighPriority` job queue.

#### Sample Request
<a name="API_ListQuotaShares_Example_1_Request"></a>

```
POST /v1/listquotashares HTTP/1.1
Host: batch.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: [content-length]
Authorization: [authorization-params]
X-Amz-Date: 20250801T001258Z
User-Agent: aws-cli/2.27.33 Python/3.13.4 Darwin/24.3.0

{
  "jobQueue": "HighPriority"
}
```

#### Sample Response
<a name="API_ListQuotaShares_Example_1_Response"></a>

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
  "quotaShares": [
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
    },
    ...
  ]
}
```

## See Also
<a name="API_ListQuotaShares_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/batch-2016-08-10/ListQuotaShares) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/batch-2016-08-10/ListQuotaShares) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/ListQuotaShares) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/batch-2016-08-10/ListQuotaShares) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/ListQuotaShares) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/batch-2016-08-10/ListQuotaShares) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/batch-2016-08-10/ListQuotaShares) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/batch-2016-08-10/ListQuotaShares) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/ListQuotaShares) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/ListQuotaShares) 