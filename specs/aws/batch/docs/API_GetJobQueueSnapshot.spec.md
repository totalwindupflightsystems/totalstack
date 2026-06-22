---
id: "@specs/aws/batch/docs/API_GetJobQueueSnapshot"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetJobQueueSnapshot"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# GetJobQueueSnapshot

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_GetJobQueueSnapshot
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetJobQueueSnapshot
<a name="API_GetJobQueueSnapshot"></a>

Provides a snapshot of job queue state, including ordering of `RUNNABLE` jobs, as well as capacity utilization for already dispatched jobs. The first 100 `RUNNABLE` jobs in the job queue are listed in order of dispatch. For job queues with an attached quota-share policy, the first `RUNNABLE` job in each quota share is also listed. Capacity utilization for the job queue is provided, as well as break downs by share for job queues with attached fair-share or quota-share scheduling policies.

## Request Syntax
<a name="API_GetJobQueueSnapshot_RequestSyntax"></a>

```
POST /v1/getjobqueuesnapshot HTTP/1.1
Content-type: application/json

{
   "jobQueue": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetJobQueueSnapshot_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetJobQueueSnapshot_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [jobQueue](#API_GetJobQueueSnapshot_RequestSyntax) **   <a name="Batch-GetJobQueueSnapshot-request-jobQueue"></a>
The job queue’s name or full queue Amazon Resource Name (ARN).  
Type: String  
Required: Yes

## Response Syntax
<a name="API_GetJobQueueSnapshot_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "frontOfQueue": { 
      "jobs": [ 
         { 
            "earliestTimeAtPosition": number,
            "jobArn": "string"
         }
      ],
      "lastUpdatedAt": number
   },
   "frontOfQuotaShares": { 
      "lastUpdatedAt": number,
      "quotaShares": { 
         "string" : [ 
            { 
               "earliestTimeAtPosition": number,
               "jobArn": "string"
            }
         ]
      }
   },
   "queueUtilization": { 
      "fairshareUtilization": { 
         "activeShareCount": number,
         "topCapacityUtilization": [ 
            { 
               "capacityUsage": [ 
                  { 
                     "capacityUnit": "string",
                     "quantity": number
                  }
               ],
               "shareIdentifier": "string"
            }
         ]
      },
      "lastUpdatedAt": number,
      "quotaShareUtilization": { 
         "topCapacityUtilization": [ 
            { 
               "capacityUsage": [ 
                  { 
                     "capacityUnit": "string",
                     "quantity": number
                  }
               ],
               "quotaShareName": "string"
            }
         ]
      },
      "totalCapacityUsage": [ 
         { 
            "capacityUnit": "string",
            "quantity": number
         }
      ]
   }
}
```

## Response Elements
<a name="API_GetJobQueueSnapshot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [frontOfQueue](#API_GetJobQueueSnapshot_ResponseSyntax) **   <a name="Batch-GetJobQueueSnapshot-response-frontOfQueue"></a>
The list of the first 100 `RUNNABLE` jobs in each job queue. For first-in-first-out (FIFO) job queues, jobs are ordered based on their submission time. For job queues with an attached fair-share scheduling (FSS) or quota-share policy, jobs are ordered based on their job priority and share usage.  
Type: [FrontOfQueueDetail](API_FrontOfQueueDetail.md) object

 ** [frontOfQuotaShares](#API_GetJobQueueSnapshot_ResponseSyntax) **   <a name="Batch-GetJobQueueSnapshot-response-frontOfQuotaShares"></a>
The first `RUNNABLE` job in each quota share. Jobs are ordered based on their job priority and share usage.  
Type: [FrontOfQuotaSharesDetail](API_FrontOfQuotaSharesDetail.md) object

 ** [queueUtilization](#API_GetJobQueueSnapshot_ResponseSyntax) **   <a name="Batch-GetJobQueueSnapshot-response-queueUtilization"></a>
The job queue's capacity utilization, including total usage and breakdown per given share.  
Type: [QueueSnapshotUtilizationDetail](API_QueueSnapshotUtilizationDetail.md) object

## Errors
<a name="API_GetJobQueueSnapshot_Errors"></a>

 ** ClientException **   
These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.  
HTTP Status Code: 400

 ** ServerException **   
These errors are usually caused by a server issue.  
HTTP Status Code: 500

## See Also
<a name="API_GetJobQueueSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/batch-2016-08-10/GetJobQueueSnapshot) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/batch-2016-08-10/GetJobQueueSnapshot) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/GetJobQueueSnapshot) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/batch-2016-08-10/GetJobQueueSnapshot) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/GetJobQueueSnapshot) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/batch-2016-08-10/GetJobQueueSnapshot) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/batch-2016-08-10/GetJobQueueSnapshot) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/batch-2016-08-10/GetJobQueueSnapshot) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/GetJobQueueSnapshot) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/GetJobQueueSnapshot) 