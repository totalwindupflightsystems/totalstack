---
id: "@specs/aws/kendra/docs/API_BatchDeleteDocument"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS BatchDeleteDocument"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# BatchDeleteDocument

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_BatchDeleteDocument
> **target_lang:** meta — documentation tier. ALL sections preserved.



# BatchDeleteDocument
<a name="API_BatchDeleteDocument"></a>

Removes one or more documents from an index. The documents must have been added with the `BatchPutDocument` API.

The documents are deleted asynchronously. You can see the progress of the deletion by using AWS CloudWatch. Any error messages related to the processing of the batch are sent to your AWS CloudWatch log. You can also use the `BatchGetDocumentStatus` API to monitor the progress of deleting your documents.

Deleting documents from an index using `BatchDeleteDocument` could take up to an hour or more, depending on the number of documents you want to delete.

## Request Syntax
<a name="API_BatchDeleteDocument_RequestSyntax"></a>

```
{
   "DataSourceSyncJobMetricTarget": { 
      "DataSourceId": "{{string}}",
      "DataSourceSyncJobId": "{{string}}"
   },
   "DocumentIdList": [ "{{string}}" ],
   "IndexId": "{{string}}"
}
```

## Request Parameters
<a name="API_BatchDeleteDocument_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DataSourceSyncJobMetricTarget](#API_BatchDeleteDocument_RequestSyntax) **   <a name="kendra-BatchDeleteDocument-request-DataSourceSyncJobMetricTarget"></a>
Maps a particular data source sync job to a particular data source.  
Type: [DataSourceSyncJobMetricTarget](API_DataSourceSyncJobMetricTarget.md) object  
Required: No

 ** [DocumentIdList](#API_BatchDeleteDocument_RequestSyntax) **   <a name="kendra-BatchDeleteDocument-request-DocumentIdList"></a>
One or more identifiers for documents to delete from the index.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: Yes

 ** [IndexId](#API_BatchDeleteDocument_RequestSyntax) **   <a name="kendra-BatchDeleteDocument-request-IndexId"></a>
The identifier of the index that contains the documents to delete.  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]*`   
Required: Yes

## Response Syntax
<a name="API_BatchDeleteDocument_ResponseSyntax"></a>

```
{
   "FailedDocuments": [ 
      { 
         "DataSourceId": "string",
         "ErrorCode": "string",
         "ErrorMessage": "string",
         "Id": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchDeleteDocument_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FailedDocuments](#API_BatchDeleteDocument_ResponseSyntax) **   <a name="kendra-BatchDeleteDocument-response-FailedDocuments"></a>
A list of documents that could not be removed from the index. Each entry contains an error message that indicates why the document couldn't be removed from the index.  
Type: Array of [BatchDeleteDocumentResponseFailedDocument](API_BatchDeleteDocumentResponseFailedDocument.md) objects

## Errors
<a name="API_BatchDeleteDocument_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.  
HTTP Status Code: 400

 ** ConflictException **   
A conflict occurred with the request. Please fix any inconsistences with your resources and try again.  
HTTP Status Code: 400

 ** InternalServerException **   
An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact [Support](http://aws.amazon.com/contact-us/) for help.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.  
HTTP Status Code: 400

 ** ThrottlingException **   
The request was denied due to request throttling. Please reduce the number of requests and try again.  
HTTP Status Code: 400

 ** ValidationException **   
The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.  
HTTP Status Code: 400

## See Also
<a name="API_BatchDeleteDocument_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kendra-2019-02-03/BatchDeleteDocument) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kendra-2019-02-03/BatchDeleteDocument) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/BatchDeleteDocument) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kendra-2019-02-03/BatchDeleteDocument) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/BatchDeleteDocument) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kendra-2019-02-03/BatchDeleteDocument) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kendra-2019-02-03/BatchDeleteDocument) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kendra-2019-02-03/BatchDeleteDocument) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kendra-2019-02-03/BatchDeleteDocument) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/BatchDeleteDocument) 