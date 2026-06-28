---
id: "@specs/aws/quicksight/docs/API_ListAssetBundleImportJobs"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListAssetBundleImportJobs"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# ListAssetBundleImportJobs

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_ListAssetBundleImportJobs
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListAssetBundleImportJobs
<a name="API_ListAssetBundleImportJobs"></a>

Lists all asset bundle import jobs that have taken place in the last 14 days. Jobs created more than 14 days ago are deleted forever and are not returned. If you are using the same job ID for multiple jobs, `ListAssetBundleImportJobs` only returns the most recent job that uses the repeated job ID.

## Request Syntax
<a name="API_ListAssetBundleImportJobs_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/asset-bundle-import-jobs?max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAssetBundleImportJobs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_ListAssetBundleImportJobs_RequestSyntax) **   <a name="QS-ListAssetBundleImportJobs-request-uri-AwsAccountId"></a>
The ID of the AWS account that the import jobs were executed in.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [MaxResults](#API_ListAssetBundleImportJobs_RequestSyntax) **   <a name="QS-ListAssetBundleImportJobs-request-uri-MaxResults"></a>
The maximum number of results to be returned per request.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListAssetBundleImportJobs_RequestSyntax) **   <a name="QS-ListAssetBundleImportJobs-request-uri-NextToken"></a>
The token for the next set of results, or null if there are no more results.

## Request Body
<a name="API_ListAssetBundleImportJobs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAssetBundleImportJobs_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "AssetBundleImportJobSummaryList": [ 
      { 
         "Arn": "string",
         "AssetBundleImportJobId": "string",
         "CreatedTime": number,
         "FailureAction": "string",
         "JobStatus": "string"
      }
   ],
   "NextToken": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_ListAssetBundleImportJobs_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_ListAssetBundleImportJobs_ResponseSyntax) **   <a name="QS-ListAssetBundleImportJobs-response-Status"></a>
The HTTP status of the response.

The following data is returned in JSON format by the service.

 ** [AssetBundleImportJobSummaryList](#API_ListAssetBundleImportJobs_ResponseSyntax) **   <a name="QS-ListAssetBundleImportJobs-response-AssetBundleImportJobSummaryList"></a>
A list of import job summaries.  
Type: Array of [AssetBundleImportJobSummary](API_AssetBundleImportJobSummary.md) objects

 ** [NextToken](#API_ListAssetBundleImportJobs_ResponseSyntax) **   <a name="QS-ListAssetBundleImportJobs-response-NextToken"></a>
The token for the next set of results, or null if there are no more results.  
Type: String

 ** [RequestId](#API_ListAssetBundleImportJobs_ResponseSyntax) **   <a name="QS-ListAssetBundleImportJobs-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String  
Pattern: `.*\S.*` 

## Errors
<a name="API_ListAssetBundleImportJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 401

 ** InvalidNextTokenException **   
The `NextToken` value isn't valid.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 400

 ** ResourceNotFoundException **   
One or more resources can't be found.    
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **   
Access is throttled.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 429

 ** UnsupportedUserEditionException **   
This error indicates that you are calling an operation on an Amazon Quick Suite subscription where the edition doesn't include support for that operation. Amazon Quick Suite currently has Standard Edition and Enterprise Edition. Not every operation and capability is available in every edition.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 403

## See Also
<a name="API_ListAssetBundleImportJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/ListAssetBundleImportJobs) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/ListAssetBundleImportJobs) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ListAssetBundleImportJobs) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/ListAssetBundleImportJobs) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ListAssetBundleImportJobs) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/ListAssetBundleImportJobs) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/ListAssetBundleImportJobs) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/ListAssetBundleImportJobs) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/ListAssetBundleImportJobs) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ListAssetBundleImportJobs) 