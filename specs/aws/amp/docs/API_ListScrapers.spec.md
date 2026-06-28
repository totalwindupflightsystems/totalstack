---
id: "@specs/aws/amp/docs/API_ListScrapers"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListScrapers"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# ListScrapers

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_ListScrapers
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListScrapers
<a name="API_ListScrapers"></a>

The `ListScrapers` operation lists all of the scrapers in your account. This includes scrapers being created or deleted. You can optionally filter the returned list.

## Request Syntax
<a name="API_ListScrapers_RequestSyntax"></a>

```
GET /scrapers?{{filters}}&maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListScrapers_RequestParameters"></a>

The request uses the following URI parameters.

 ** [filters](#API_ListScrapers_RequestSyntax) **   <a name="prometheus-ListScrapers-request-uri-filters"></a>
(Optional) A list of key-value pairs to filter the list of scrapers returned. Keys include `status`, `sourceArn`, `destinationArn`, and `alias`.  
Filters on the same key are `OR`'d together, and filters on different keys are `AND`'d together. For example, `status=ACTIVE&status=CREATING&alias=Test`, will return all scrapers that have the alias Test, and are either in status ACTIVE or CREATING.  
To find all active scrapers that are sending metrics to a specific Amazon Managed Service for Prometheus workspace, you would use the ARN of the workspace in a query:  
 `status=ACTIVE&destinationArn=arn:aws:aps:us-east-1:123456789012:workspace/ws-example1-1234-abcd-56ef-123456789012`   
If this is included, it filters the results to only the scrapers that match the filter.  
Map Entries: Maximum number of 4 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 256.  
Array Members: Minimum number of 1 item. Maximum number of 20 items.  
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [maxResults](#API_ListScrapers_RequestSyntax) **   <a name="prometheus-ListScrapers-request-uri-maxResults"></a>
Optional) The maximum number of scrapers to return in one `ListScrapers` operation. The range is 1-1000.  
If you omit this parameter, the default of 100 is used.  
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nextToken](#API_ListScrapers_RequestSyntax) **   <a name="prometheus-ListScrapers-request-uri-nextToken"></a>
(Optional) The token for the next set of items to return. (You received this token from a previous call.)  
Length Constraints: Minimum length of 0. Maximum length of 1000.

## Request Body
<a name="API_ListScrapers_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListScrapers_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "scrapers": [ 
      { 
         "alias": "string",
         "arn": "string",
         "createdAt": number,
         "destination": { ... },
         "lastModifiedAt": number,
         "roleArn": "string",
         "roleConfiguration": { 
            "sourceRoleArn": "string",
            "targetRoleArn": "string"
         },
         "scraperId": "string",
         "source": { ... },
         "status": { 
            "statusCode": "string"
         },
         "statusReason": "string",
         "tags": { 
            "string" : "string" 
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListScrapers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListScrapers_ResponseSyntax) **   <a name="prometheus-ListScrapers-response-nextToken"></a>
A token indicating that there are more results to retrieve. You can use this token as part of your next `ListScrapers` operation to retrieve those results.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1000.

 ** [scrapers](#API_ListScrapers_ResponseSyntax) **   <a name="prometheus-ListScrapers-response-scrapers"></a>
A list of `ScraperSummary` structures giving information about scrapers in the account that match the filters provided.  
Type: Array of [ScraperSummary](API_ScraperSummary.md) objects

## Errors
<a name="API_ListScrapers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You do not have sufficient access to perform this action.    
 ** message **   
Description of the error.
HTTP Status Code: 403

 ** InternalServerException **   
An unexpected error occurred during the processing of the request.    
 ** message **   
Description of the error.  
 ** retryAfterSeconds **   
Advice to clients on when the call can be safely retried.
HTTP Status Code: 500

 ** ThrottlingException **   
The request was denied due to request throttling.    
 ** message **   
Description of the error.  
 ** quotaCode **   
Service quotas code for the originating quota.  
 ** retryAfterSeconds **   
Advice to clients on when the call can be safely retried.  
 ** serviceCode **   
Service quotas code for the originating service.
HTTP Status Code: 429

 ** ValidationException **   
The input fails to satisfy the constraints specified by an AWS service.    
 ** fieldList **   
The field that caused the error, if applicable.  
 ** message **   
Description of the error.  
 ** reason **   
Reason the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_ListScrapers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amp-2020-08-01/ListScrapers) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amp-2020-08-01/ListScrapers) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/ListScrapers) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amp-2020-08-01/ListScrapers) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/ListScrapers) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amp-2020-08-01/ListScrapers) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amp-2020-08-01/ListScrapers) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amp-2020-08-01/ListScrapers) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amp-2020-08-01/ListScrapers) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/ListScrapers) 