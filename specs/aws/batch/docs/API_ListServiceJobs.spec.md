---
id: "@specs/aws/batch/docs/API_ListServiceJobs"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListServiceJobs"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# ListServiceJobs

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_ListServiceJobs
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListServiceJobs
<a name="API_ListServiceJobs"></a>

Returns a list of service jobs for a specified job queue.

## Request Syntax
<a name="API_ListServiceJobs_RequestSyntax"></a>

```
POST /v1/listservicejobs HTTP/1.1
Content-type: application/json

{
   "filters": [ 
      { 
         "name": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "jobQueue": "{{string}}",
   "jobStatus": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListServiceJobs_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListServiceJobs_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_ListServiceJobs_RequestSyntax) **   <a name="Batch-ListServiceJobs-request-filters"></a>
The filter to apply to the query. Only one filter can be used at a time. When the filter is used, `jobStatus` is ignored with the exception that `SHARE_IDENTIFIER` or `QUOTA_SHARE_NAME` and `jobStatus` can be used together. The results are sorted by the `createdAt` field, with the most recent jobs being first.  
The `SHARE_IDENTIFIER` or `QUOTA_SHARE_NAME` filter and the `jobStatus` field can be used together to filter results.  
JOB\_NAME  
The value of the filter is a case-insensitive match for the job name. If the value ends with an asterisk (\*), the filter matches any job name that begins with the string before the '\*'. This corresponds to the `jobName` value. For example, `test1` matches both `Test1` and `test1`, and `test1*` matches both `test1` and `Test10`. When the `JOB_NAME` filter is used, the results are grouped by the job name and version.  
BEFORE\_CREATED\_AT  
The value for the filter is the time that's before the job was created. This corresponds to the `createdAt` value. The value is a string representation of the number of milliseconds since 00:00:00 UTC (midnight) on January 1, 1970.  
AFTER\_CREATED\_AT  
The value for the filter is the time that's after the job was created. This corresponds to the `createdAt` value. The value is a string representation of the number of milliseconds since 00:00:00 UTC (midnight) on January 1, 1970.  
SHARE\_IDENTIFIER  
The value for the filter is the fairshare scheduling share identifier.  
QUOTA\_SHARE\_NAME  
The value for the filter is the quota management share name.
Type: Array of [KeyValuesPair](API_KeyValuesPair.md) objects  
Required: No

 ** [jobQueue](#API_ListServiceJobs_RequestSyntax) **   <a name="Batch-ListServiceJobs-request-jobQueue"></a>
The name or ARN of the job queue with which to list service jobs.  
Type: String  
Required: No

 ** [jobStatus](#API_ListServiceJobs_RequestSyntax) **   <a name="Batch-ListServiceJobs-request-jobStatus"></a>
The job status used to filter service jobs in the specified queue. If the `filters` parameter is specified, the `jobStatus` parameter is ignored and jobs with any status are returned. The exceptions are the `SHARE_IDENTIFIER` filter and `QUOTA_SHARE_NAME` filter, which can be used with `jobStatus`. If you don't specify a status, only `RUNNING` jobs are returned.  
The `SHARE_IDENTIFIER` filter or `QUOTA_SHARE_NAME` filter can be used with the `jobStatus` field to filter results.
Type: String  
Valid Values: `SUBMITTED | PENDING | RUNNABLE | SCHEDULED | STARTING | RUNNING | SUCCEEDED | FAILED`   
Required: No

 ** [maxResults](#API_ListServiceJobs_RequestSyntax) **   <a name="Batch-ListServiceJobs-request-maxResults"></a>
The maximum number of results returned by `ListServiceJobs` in paginated output. When this parameter is used, `ListServiceJobs` only returns `maxResults` results in a single page and a `nextToken` response element. The remaining results of the initial request can be seen by sending another `ListServiceJobs` request with the returned `nextToken` value. This value can be between 1 and 100. If this parameter isn't used, then `ListServiceJobs` returns up to 100 results and a `nextToken` value if applicable.  
Type: Integer  
Required: No

 ** [nextToken](#API_ListServiceJobs_RequestSyntax) **   <a name="Batch-ListServiceJobs-request-nextToken"></a>
The `nextToken` value returned from a previous paginated `ListServiceJobs` request where `maxResults` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the `nextToken` value. This value is `null` when there are no more results to return.  
Treat this token as an opaque identifier that's only used to retrieve the next items in a list and not for other programmatic purposes.
Type: String  
Required: No

## Response Syntax
<a name="API_ListServiceJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "jobSummaryList": [ 
      { 
         "capacityUsage": [ 
            { 
               "capacityUnit": "string",
               "quantity": number
            }
         ],
         "createdAt": number,
         "jobArn": "string",
         "jobId": "string",
         "jobName": "string",
         "latestAttempt": { 
            "serviceResourceId": { 
               "name": "string",
               "value": "string"
            }
         },
         "quotaShareName": "string",
         "scheduledAt": number,
         "serviceJobType": "string",
         "shareIdentifier": "string",
         "startedAt": number,
         "status": "string",
         "statusReason": "string",
         "stoppedAt": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListServiceJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobSummaryList](#API_ListServiceJobs_ResponseSyntax) **   <a name="Batch-ListServiceJobs-response-jobSummaryList"></a>
A list of service job summaries.  
Type: Array of [ServiceJobSummary](API_ServiceJobSummary.md) objects

 ** [nextToken](#API_ListServiceJobs_ResponseSyntax) **   <a name="Batch-ListServiceJobs-response-nextToken"></a>
The `nextToken` value to include in a future `ListServiceJobs` request. When the results of a `ListServiceJobs` request exceed `maxResults`, this value can be used to retrieve the next page of results. This value is `null` when there are no more results to return.  
Type: String

## Errors
<a name="API_ListServiceJobs_Errors"></a>

 ** ClientException **   
These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.  
HTTP Status Code: 400

 ** ServerException **   
These errors are usually caused by a server issue.  
HTTP Status Code: 500

## Examples
<a name="API_ListServiceJobs_Examples"></a>

In the following example or examples, the Authorization header contents (` [authorization-params] `) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_ListServiceJobs_Example_1"></a>

This example lists all succeeded service jobs from the specified job queue.

#### Sample Request
<a name="API_ListServiceJobs_Example_1_Request"></a>

```
POST /v1/listservicejobs HTTP/1.1
Host: batch.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: [content-length]
Authorization: [authorization-params]
X-Amz-Date: 20250801T103040Z
User-Agent: aws-cli/2.27.33 Python/3.13.4 Darwin/24.3.0

{
  "jobQueue": "sagemaker-training-queue",
  "jobStatus": "SUCCEEDED",
  "maxResults": 10
}
```

#### Sample Response
<a name="API_ListServiceJobs_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: [content-length]
Connection: keep-alive
Date: Fri, 01 Aug 2025 10:30:41 GMT
x-amzn-RequestId: [request-id]
X-Amzn-Trace-Id: [trace-id]
X-Cache: Miss from cloudfront
Via: 1.1 fnhd4k2s8l3n6p9r2t5u8v1w4y7zexample.cloudfront.net (CloudFront)
X-Amz-Cf-Id: mno6pqr9stu2vwx5yz8901defghijklmnopqrstuvexample

{
  "jobSummaryList": [
    {
      "jobId": "a4d6c728-8ee8-4c65-8e2a-9a5e8f4b7c3d",
      "jobName": "sagemaker-training-job-example",
      "jobArn": "arn:aws:batch:us-east-1:123456789012:service-job/a4d6c728-8ee8-4c65-8e2a-9a5e8f4b7c3d",
      "status": "SUCCEEDED",
      "serviceJobType": "SAGEMAKER_TRAINING",
      "createdAt": 1722507600000,
      "startedAt": 1722507660000,
      "stoppedAt": 1722511260000,
      "latestAttempt": {
      "serviceResourceId": {
            "name": "TrainingJobArn",
            "value": "arn:aws:sagemaker:us-east-1:123456789012:training-job/sagemaker-training-job-example"
         }
      }
    },
    {
      "jobId": "b7e9f032-1aa2-4d78-9b3c-8e6f5a4d2c1b",
      "jobName": "image-classification-training",
      "jobArn": "arn:aws:batch:us-east-1:123456789012:service-job/b7e9f032-1aa2-4d78-9b3c-8e6f5a4d2c1b",
      "status": "SUCCEEDED",
      "serviceJobType": "SAGEMAKER_TRAINING",
      "createdAt": 1722495000000,
      "startedAt": 1722495120000,
      "stoppedAt": 1722498720000,
      "latestAttempt": {
      "serviceResourceId": {
            "name": "TrainingJobArn",
            "value": "arn:aws:sagemaker:us-east-1:123456789012:training-job/image-classification-training-example"
         }        
      }
    }
  ]
}
```

## See Also
<a name="API_ListServiceJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/batch-2016-08-10/ListServiceJobs) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/batch-2016-08-10/ListServiceJobs) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/ListServiceJobs) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/batch-2016-08-10/ListServiceJobs) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/ListServiceJobs) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/batch-2016-08-10/ListServiceJobs) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/batch-2016-08-10/ListServiceJobs) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/batch-2016-08-10/ListServiceJobs) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/ListServiceJobs) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/ListServiceJobs) 