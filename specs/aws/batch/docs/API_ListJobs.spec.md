---
id: "@specs/aws/batch/docs/API_ListJobs"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListJobs"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# ListJobs

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_ListJobs
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListJobs
<a name="API_ListJobs"></a>

Returns a list of AWS Batch jobs.

You must specify only one of the following items:
+ A job queue ID to return a list of jobs in that job queue
+ A multi-node parallel job ID to return a list of nodes for that job
+ An array job ID to return a list of the children for that job

## Request Syntax
<a name="API_ListJobs_RequestSyntax"></a>

```
POST /v1/listjobs HTTP/1.1
Content-type: application/json

{
   "arrayJobId": "{{string}}",
   "filters": [ 
      { 
         "name": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "jobQueue": "{{string}}",
   "jobStatus": "{{string}}",
   "maxResults": {{number}},
   "multiNodeJobId": "{{string}}",
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListJobs_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListJobs_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [arrayJobId](#API_ListJobs_RequestSyntax) **   <a name="Batch-ListJobs-request-arrayJobId"></a>
The job ID for an array job. Specifying an array job ID with this parameter lists all child jobs from within the specified array.  
Type: String  
Required: No

 ** [filters](#API_ListJobs_RequestSyntax) **   <a name="Batch-ListJobs-request-filters"></a>
The filter to apply to the query. Only one filter can be used at a time. When the filter is used, `jobStatus` is ignored with the exception that `SHARE_IDENTIFIER` and `jobStatus` can be used together. The filter doesn't apply to child jobs in an array or multi-node parallel (MNP) jobs. The results are sorted by the `createdAt` field, with the most recent jobs being first.  
The `SHARE_IDENTIFIER` filter and the `jobStatus` field can be used together to filter results.  
JOB\_NAME  
The value of the filter is a case-insensitive match for the job name. If the value ends with an asterisk (\*), the filter matches any job name that begins with the string before the '\*'. This corresponds to the `jobName` value. For example, `test1` matches both `Test1` and `test1`, and `test1*` matches both `test1` and `Test10`. When the `JOB_NAME` filter is used, the results are grouped by the job name and version.  
JOB\_DEFINITION  
The value for the filter is the name or Amazon Resource Name (ARN) of the job definition. This corresponds to the `jobDefinition` value. The value is case sensitive. When the value for the filter is the job definition name, the results include all the jobs that used any revision of that job definition name. If the value ends with an asterisk (\*), the filter matches any job definition name that begins with the string before the '\*'. For example, `jd1` matches only `jd1`, and `jd1*` matches both `jd1` and `jd1A`. The version of the job definition that's used doesn't affect the sort order. When the `JOB_DEFINITION` filter is used and the ARN is used (which is in the form `arn:${Partition}:batch:${Region}:${Account}:job-definition/${JobDefinitionName}:${Revision}`), the results include jobs that used the specified revision of the job definition. Asterisk (\*) isn't supported when the ARN is used.  
BEFORE\_CREATED\_AT  
The value for the filter is the time that's before the job was created. This corresponds to the `createdAt` value. The value is a string representation of the number of milliseconds since 00:00:00 UTC (midnight) on January 1, 1970.  
AFTER\_CREATED\_AT  
The value for the filter is the time that's after the job was created. This corresponds to the `createdAt` value. The value is a string representation of the number of milliseconds since 00:00:00 UTC (midnight) on January 1, 1970.  
SHARE\_IDENTIFIER  
The value for the filter is the fairshare scheduling share identifier.
Type: Array of [KeyValuesPair](API_KeyValuesPair.md) objects  
Required: No

 ** [jobQueue](#API_ListJobs_RequestSyntax) **   <a name="Batch-ListJobs-request-jobQueue"></a>
The name or full Amazon Resource Name (ARN) of the job queue used to list jobs.  
Type: String  
Required: No

 ** [jobStatus](#API_ListJobs_RequestSyntax) **   <a name="Batch-ListJobs-request-jobStatus"></a>
The job status used to filter jobs in the specified queue. If the `filters` parameter is specified, the `jobStatus` parameter is ignored and jobs with any status are returned. The exception is the `SHARE_IDENTIFIER` filter and `jobStatus` can be used together. If you don't specify a status, only `RUNNING` jobs are returned.  
Array job parents are updated to `PENDING` when any child job is updated to `RUNNABLE` and remain in `PENDING` status while child jobs are running. To view these jobs, filter by `PENDING` status until all child jobs reach a terminal state.
Type: String  
Valid Values: `SUBMITTED | PENDING | RUNNABLE | STARTING | RUNNING | SUCCEEDED | FAILED`   
Required: No

 ** [maxResults](#API_ListJobs_RequestSyntax) **   <a name="Batch-ListJobs-request-maxResults"></a>
The maximum number of results returned by `ListJobs` in a paginated output. When this parameter is used, `ListJobs` returns up to `maxResults` results in a single page and a `nextToken` response element, if applicable. The remaining results of the initial request can be seen by sending another `ListJobs` request with the returned `nextToken` value.  
The following outlines key parameters and limitations:  
+ The minimum value is 1. 
+ When `--job-status` is used, AWS Batch returns up to 1000 values. 
+ When `--filters` is used, AWS Batch returns up to 100 values.
+ If neither parameter is used, then `ListJobs` returns up to 1000 results (jobs that are in the `RUNNING` status) and a `nextToken` value, if applicable.
Type: Integer  
Required: No

 ** [multiNodeJobId](#API_ListJobs_RequestSyntax) **   <a name="Batch-ListJobs-request-multiNodeJobId"></a>
The job ID for a multi-node parallel job. Specifying a multi-node parallel job ID with this parameter lists all nodes that are associated with the specified job.  
Type: String  
Required: No

 ** [nextToken](#API_ListJobs_RequestSyntax) **   <a name="Batch-ListJobs-request-nextToken"></a>
The `nextToken` value returned from a previous paginated `ListJobs` request where `maxResults` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the `nextToken` value. This value is `null` when there are no more results to return.  
Treat this token as an opaque identifier that's only used to retrieve the next items in a list and not for other programmatic purposes.
Type: String  
Required: No

## Response Syntax
<a name="API_ListJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "jobSummaryList": [ 
      { 
         "arrayProperties": { 
            "index": number,
            "size": number,
            "statusSummary": { 
               "string" : number 
            },
            "statusSummaryLastUpdatedAt": number
         },
         "capacityUsage": [ 
            { 
               "capacityUnit": "string",
               "quantity": number
            }
         ],
         "container": { 
            "exitCode": number,
            "reason": "string"
         },
         "createdAt": number,
         "jobArn": "string",
         "jobDefinition": "string",
         "jobId": "string",
         "jobName": "string",
         "nodeProperties": { 
            "isMainNode": boolean,
            "nodeIndex": number,
            "numNodes": number
         },
         "scheduledAt": number,
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
<a name="API_ListJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobSummaryList](#API_ListJobs_ResponseSyntax) **   <a name="Batch-ListJobs-response-jobSummaryList"></a>
A list of job summaries that match the request.  
Type: Array of [JobSummary](API_JobSummary.md) objects

 ** [nextToken](#API_ListJobs_ResponseSyntax) **   <a name="Batch-ListJobs-response-nextToken"></a>
The `nextToken` value to include in a future `ListJobs` request. When the results of a `ListJobs` request exceed `maxResults`, this value can be used to retrieve the next page of results. This value is `null` when there are no more results to return.  
Type: String

## Errors
<a name="API_ListJobs_Errors"></a>

 ** ClientException **   
These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.  
HTTP Status Code: 400

 ** ServerException **   
These errors are usually caused by a server issue.  
HTTP Status Code: 500

## Examples
<a name="API_ListJobs_Examples"></a>

In the following example or examples, the Authorization header contents (` [authorization-params] `) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_ListJobs_Example_1"></a>

This example lists the running jobs in the `HighPriority` job queue.

#### Sample Request
<a name="API_ListJobs_Example_1_Request"></a>

```
POST /v1/listjobs HTTP/1.1
Host: batch.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: [content-length]
Authorization: [authorization-params]
X-Amz-Date: 20161129T201622Z
User-Agent: aws-cli/1.11.22 Python/2.7.12 Darwin/16.1.0 botocore/1.4.79

{
  "jobQueue": "HighPriority"
}
```

#### Sample Response
<a name="API_ListJobs_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: [content-length]
Connection: keep-alive
Date: Tue, 29 Nov 2016 20:16:22 GMT
x-amzn-RequestId: [request-id]
X-Amzn-Trace-Id: [trace-id]
X-Cache: Miss from cloudfront
Via: 1.1 7f3f42df8af148df1f9f1ee7175987ad.cloudfront.net (CloudFront)
X-Amz-Cf-Id: idKR5mD8f7Luom03P9DV1bFGXsq_SIFNy_nMrTCOqZrRc0nXgHqZfg==

{
  "jobSummaryList": [{
    "jobId": "e66ff5fd-a1ff-4640-b1a2-0b0a142f49bb",
    "jobName": "example"
  }]
}
```

### Example
<a name="API_ListJobs_Example_2"></a>

This example lists jobs in the `HighPriority` job queue that are in the `SUBMITTED` job status.

#### Sample Request
<a name="API_ListJobs_Example_2_Request"></a>

```
POST /v1/listjobs HTTP/1.1
Host: batch.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: [content-length]
Authorization: [authorization-params]
X-Amz-Date: 20161129T201642Z
User-Agent: aws-cli/1.11.22 Python/2.7.12 Darwin/16.1.0 botocore/1.4.79

{
  "jobQueue": "HighPriority",
  "jobStatus": "SUBMITTED"
}
```

#### Sample Response
<a name="API_ListJobs_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 29 Nov 2016 20:16:42 GMT
Content-Type: application/json
Content-Length: [content-length]
Connection: keep-alive
x-amzn-RequestId: [request-id]
X-Amzn-Trace-Id: [trace-id]
X-Cache: Miss from cloudfront
Via: 1.1 ebc28fb0ad14691ee5d6c1a49f41b878.cloudfront.net (CloudFront)
X-Amz-Cf-Id: Ngsjm0gBg2y4cDFG4uwpAmaKaT6Dejh7oGlVDmewQrUaeW_SPst_Bw==

{
  "jobSummaryList": [{
    "jobId": "68f0c163-fbd4-44e6-9fd1-25b14a434786",
    "jobName": "example"
  }]
}
```

## See Also
<a name="API_ListJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/batch-2016-08-10/ListJobs) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/batch-2016-08-10/ListJobs) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/ListJobs) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/batch-2016-08-10/ListJobs) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/ListJobs) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/batch-2016-08-10/ListJobs) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/batch-2016-08-10/ListJobs) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/batch-2016-08-10/ListJobs) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/ListJobs) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/ListJobs) 