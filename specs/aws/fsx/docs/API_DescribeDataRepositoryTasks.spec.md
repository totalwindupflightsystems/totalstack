---
id: "@specs/aws/fsx/docs/API_DescribeDataRepositoryTasks"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeDataRepositoryTasks"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# DescribeDataRepositoryTasks

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_DescribeDataRepositoryTasks
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeDataRepositoryTasks
<a name="API_DescribeDataRepositoryTasks"></a>

Returns the description of specific Amazon FSx for Lustre or Amazon File Cache data repository tasks, if one or more `TaskIds` values are provided in the request, or if filters are used in the request. You can use filters to narrow the response to include just tasks for specific file systems or caches, or tasks in a specific lifecycle state. Otherwise, it returns all data repository tasks owned by your AWS account in the AWS Region of the endpoint that you're calling.

When retrieving all tasks, you can paginate the response by using the optional `MaxResults` parameter to limit the number of tasks returned in a response. If more tasks remain, a `NextToken` value is returned in the response. In this case, send a later request with the `NextToken` request parameter set to the value of `NextToken` from the last response.

## Request Syntax
<a name="API_DescribeDataRepositoryTasks_RequestSyntax"></a>

```
{
   "Filters": [ 
      { 
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "TaskIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeDataRepositoryTasks_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeDataRepositoryTasks_RequestSyntax) **   <a name="FSx-DescribeDataRepositoryTasks-request-Filters"></a>
(Optional) You can use filters to narrow the `DescribeDataRepositoryTasks` response to include just tasks for specific file systems, or tasks in a specific lifecycle state.  
Type: Array of [DataRepositoryTaskFilter](API_DataRepositoryTaskFilter.md) objects  
Array Members: Maximum number of 3 items.  
Required: No

 ** [MaxResults](#API_DescribeDataRepositoryTasks_RequestSyntax) **   <a name="FSx-DescribeDataRepositoryTasks-request-MaxResults"></a>
The maximum number of resources to return in the response. This value must be an integer greater than zero.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 2147483647.  
Required: No

 ** [NextToken](#API_DescribeDataRepositoryTasks_RequestSyntax) **   <a name="FSx-DescribeDataRepositoryTasks-request-NextToken"></a>
(Optional) Opaque pagination token returned from a previous operation (String). If present, this token indicates from what point you can continue processing the request, where the previous `NextToken` value left off.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$`   
Required: No

 ** [TaskIds](#API_DescribeDataRepositoryTasks_RequestSyntax) **   <a name="FSx-DescribeDataRepositoryTasks-request-TaskIds"></a>
(Optional) IDs of the tasks whose descriptions you want to retrieve (String).  
Type: Array of strings  
Array Members: Maximum number of 50 items.  
Length Constraints: Minimum length of 12. Maximum length of 128.  
Pattern: `^(task-[0-9a-f]{17,})$`   
Required: No

## Response Syntax
<a name="API_DescribeDataRepositoryTasks_ResponseSyntax"></a>

```
{
   "DataRepositoryTasks": [ 
      { 
         "CapacityToRelease": number,
         "CreationTime": number,
         "EndTime": number,
         "FailureDetails": { 
            "Message": "string"
         },
         "FileCacheId": "string",
         "FileSystemId": "string",
         "Lifecycle": "string",
         "Paths": [ "string" ],
         "ReleaseConfiguration": { 
            "DurationSinceLastAccess": { 
               "Unit": "string",
               "Value": number
            }
         },
         "Report": { 
            "Enabled": boolean,
            "Format": "string",
            "Path": "string",
            "Scope": "string"
         },
         "ResourceARN": "string",
         "StartTime": number,
         "Status": { 
            "FailedCount": number,
            "LastUpdatedTime": number,
            "ReleasedCapacity": number,
            "SucceededCount": number,
            "TotalCount": number
         },
         "Tags": [ 
            { 
               "Key": "string",
               "Value": "string"
            }
         ],
         "TaskId": "string",
         "Type": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeDataRepositoryTasks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DataRepositoryTasks](#API_DescribeDataRepositoryTasks_ResponseSyntax) **   <a name="FSx-DescribeDataRepositoryTasks-response-DataRepositoryTasks"></a>
The collection of data repository task descriptions returned.  
Type: Array of [DataRepositoryTask](API_DataRepositoryTask.md) objects  
Array Members: Maximum number of 50 items.

 ** [NextToken](#API_DescribeDataRepositoryTasks_ResponseSyntax) **   <a name="FSx-DescribeDataRepositoryTasks-response-NextToken"></a>
(Optional) Opaque pagination token returned from a previous operation (String). If present, this token indicates from what point you can continue processing the request, where the previous `NextToken` value left off.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$` 

## Errors
<a name="API_DescribeDataRepositoryTasks_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequest **   
A generic error indicating a failure with a client request.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** DataRepositoryTaskNotFound **   
The data repository task or tasks you specified could not be found.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** FileSystemNotFound **   
No Amazon FSx file systems were found based upon supplied parameters.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** InternalServerError **   
A generic error indicating a server-side failure.    
 ** Message **   
A detailed error message.
HTTP Status Code: 500

## Examples
<a name="API_DescribeDataRepositoryTasks_Examples"></a>

### Retrieve Specific Data Repository Task Descriptions
<a name="API_DescribeDataRepositoryTasks_Example_1"></a>

The following request retrieves the descriptions of a specific data repository task by using the TaskIDs request parameter.

#### Sample Request
<a name="API_DescribeDataRepositoryTasks_Example_1_Request"></a>

```
GET /2015-02-01/describe-data-repository-task HTTP/1.1 
Host: fsx.us-east-1.amazonaws.com
x-amz-date: 20140620T221118Z
Authorization: <...>
Content-Type: application/json
Content-Length: 160

{    
    "TaskIds": ["task-0123456789abcdef0"]
}
```

#### Sample Response
<a name="API_DescribeDataRepositoryTasks_Example_1_Response"></a>

```
HTTP/1.1 200 success
x-amzn-RequestId: c3616af3-33fa-40ad-ae0d-d3895a2c3a1f

{
    "DataRepositoryTasks": [
        {
            "TaskId": "task-0123456789abcdef0",
            "TaskType": "EXPORT_TO_REPOSITORY",
            "Lifecycle": "PENDING",
            "FileSystemId": "fs-0123456789abcdef1",
            "Paths": ["/path1", "/path2/file1"],
            "CreationTime": "2019-07-17T18:18:18.000Z",
            "TaskReport": {
                "Path":"s3://amzn-s3-demo-bucket/FSxLustre20191118T225838Z/myreports",
                "Format":"REPORT_CSV_20191124",
                "Enabled":true,
                "Scope":"FAILED_FILES_ONLY"
            },
            "Status": {
                "TotalCount": 100,
                "SucceededCount": 0,
                "FailedCount": 0,
                "LastUpdated": "2019-07-17T18:19:05.003Z"
            },
            "Tags": [{"Key": "MyKey"}, {"Value": "MyValue"}],
            "ClientRequestToken": "1234",
            "ResourceARN": "arn:aws:fsx:us-east-1:123456789012:task:task-123f8cd8e330c1321"
        }
    ]
}
```

## See Also
<a name="API_DescribeDataRepositoryTasks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/DescribeDataRepositoryTasks) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/DescribeDataRepositoryTasks) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/DescribeDataRepositoryTasks) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/DescribeDataRepositoryTasks) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/DescribeDataRepositoryTasks) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/DescribeDataRepositoryTasks) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/DescribeDataRepositoryTasks) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/DescribeDataRepositoryTasks) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/DescribeDataRepositoryTasks) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/DescribeDataRepositoryTasks) 