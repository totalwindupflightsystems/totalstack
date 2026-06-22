---
id: "@specs/aws/batch/docs/API_ListJobsByConsumableResource"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListJobsByConsumableResource"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# ListJobsByConsumableResource

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_ListJobsByConsumableResource
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListJobsByConsumableResource
<a name="API_ListJobsByConsumableResource"></a>

Returns a list of AWS Batch jobs that require a specific consumable resource.

## Request Syntax
<a name="API_ListJobsByConsumableResource_RequestSyntax"></a>

```
POST /v1/listjobsbyconsumableresource HTTP/1.1
Content-type: application/json

{
   "consumableResource": "{{string}}",
   "filters": [ 
      { 
         "name": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListJobsByConsumableResource_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListJobsByConsumableResource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [consumableResource](#API_ListJobsByConsumableResource_RequestSyntax) **   <a name="Batch-ListJobsByConsumableResource-request-consumableResource"></a>
The name or ARN of the consumable resource.  
Type: String  
Required: Yes

 ** [filters](#API_ListJobsByConsumableResource_RequestSyntax) **   <a name="Batch-ListJobsByConsumableResource-request-filters"></a>
The filters to apply to the job list query. If used, only those jobs requiring the specified consumable resource (`consumableResource`) and that match the value of the filters are listed. The filter names and values can be:  
+ name: `JOB_STATUS` 

  values: `SUBMITTED | PENDING | RUNNABLE | STARTING | RUNNING | SUCCEEDED | FAILED` 
+ name: `JOB_NAME ` 

  The values are case-insensitive matches for the job name. If a filter value ends with an asterisk (\*), it matches any job name that begins with the string before the '\*'.
Type: Array of [KeyValuesPair](API_KeyValuesPair.md) objects  
Required: No

 ** [maxResults](#API_ListJobsByConsumableResource_RequestSyntax) **   <a name="Batch-ListJobsByConsumableResource-request-maxResults"></a>
The maximum number of results returned by `ListJobsByConsumableResource` in paginated output. When this parameter is used, `ListJobsByConsumableResource` only returns `maxResults` results in a single page and a `nextToken` response element. The remaining results of the initial request can be seen by sending another `ListJobsByConsumableResource` request with the returned `nextToken` value. This value can be between 1 and 100. If this parameter isn't used, then `ListJobsByConsumableResource` returns up to 100 results and a `nextToken` value if applicable.  
Type: Integer  
Required: No

 ** [nextToken](#API_ListJobsByConsumableResource_RequestSyntax) **   <a name="Batch-ListJobsByConsumableResource-request-nextToken"></a>
The `nextToken` value returned from a previous paginated `ListJobsByConsumableResource` request where `maxResults` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the `nextToken` value. This value is `null` when there are no more results to return.  
Treat this token as an opaque identifier that's only used to retrieve the next items in a list and not for other programmatic purposes.
Type: String  
Required: No

## Response Syntax
<a name="API_ListJobsByConsumableResource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "jobs": [ 
      { 
         "consumableResourceProperties": { 
            "consumableResourceList": [ 
               { 
                  "consumableResource": "string",
                  "quantity": number
               }
            ]
         },
         "createdAt": number,
         "jobArn": "string",
         "jobDefinitionArn": "string",
         "jobName": "string",
         "jobQueueArn": "string",
         "jobStatus": "string",
         "quantity": number,
         "shareIdentifier": "string",
         "startedAt": number,
         "statusReason": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListJobsByConsumableResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobs](#API_ListJobsByConsumableResource_ResponseSyntax) **   <a name="Batch-ListJobsByConsumableResource-response-jobs"></a>
The list of jobs that require the specified consumable resources.  
Type: Array of [ListJobsByConsumableResourceSummary](API_ListJobsByConsumableResourceSummary.md) objects

 ** [nextToken](#API_ListJobsByConsumableResource_ResponseSyntax) **   <a name="Batch-ListJobsByConsumableResource-response-nextToken"></a>
The `nextToken` value to include in a future `ListJobsByConsumableResource` request. When the results of a `ListJobsByConsumableResource` request exceed `maxResults`, this value can be used to retrieve the next page of results. This value is `null` when there are no more results to return.  
Type: String

## Errors
<a name="API_ListJobsByConsumableResource_Errors"></a>

 ** ClientException **   
These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.  
HTTP Status Code: 400

 ** ServerException **   
These errors are usually caused by a server issue.  
HTTP Status Code: 500

## See Also
<a name="API_ListJobsByConsumableResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/batch-2016-08-10/ListJobsByConsumableResource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/batch-2016-08-10/ListJobsByConsumableResource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/ListJobsByConsumableResource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/batch-2016-08-10/ListJobsByConsumableResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/ListJobsByConsumableResource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/batch-2016-08-10/ListJobsByConsumableResource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/batch-2016-08-10/ListJobsByConsumableResource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/batch-2016-08-10/ListJobsByConsumableResource) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/ListJobsByConsumableResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/ListJobsByConsumableResource) 