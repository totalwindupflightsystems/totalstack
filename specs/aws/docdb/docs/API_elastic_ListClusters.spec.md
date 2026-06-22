---
id: "@specs/aws/docdb/docs/API_elastic_ListClusters"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListClusters"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# ListClusters

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_elastic_ListClusters
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListClusters
<a name="API_elastic_ListClusters"></a>

Returns information about provisioned Amazon DocumentDB elastic clusters.

## Request Syntax
<a name="API_elastic_ListClusters_RequestSyntax"></a>

```
GET /clusters?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_elastic_ListClusters_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_elastic_ListClusters_RequestSyntax) **   <a name="documentdb-elastic_ListClusters-request-uri-maxResults"></a>
The maximum number of elastic cluster snapshot results to receive in the response.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_elastic_ListClusters_RequestSyntax) **   <a name="documentdb-elastic_ListClusters-request-uri-nextToken"></a>
A pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond this token, up to the value specified by `max-results`.  
If there is no more data in the responce, the `nextToken` will not be returned.

## Request Body
<a name="API_elastic_ListClusters_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_elastic_ListClusters_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "clusters": [ 
      { 
         "clusterArn": "string",
         "clusterName": "string",
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_elastic_ListClusters_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [clusters](#API_elastic_ListClusters_ResponseSyntax) **   <a name="documentdb-elastic_ListClusters-response-clusters"></a>
A list of Amazon DocumentDB elastic clusters.  
Type: Array of [ClusterInList](API_elastic_ClusterInList.md) objects

 ** [nextToken](#API_elastic_ListClusters_ResponseSyntax) **   <a name="documentdb-elastic_ListClusters-response-nextToken"></a>
A pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond this token, up to the value specified by `max-results`.  
If there is no more data in the responce, the `nextToken` will not be returned.  
Type: String

## Errors
<a name="API_elastic_ListClusters_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
An exception that occurs when there are not sufficient permissions to perform an action.    
 ** message **   
An error message explaining why access was denied.
HTTP Status Code: 403

 ** InternalServerException **   
There was an internal server error.  
HTTP Status Code: 500

 ** ThrottlingException **   
ThrottlingException will be thrown when request was denied due to request throttling.    
 ** retryAfterSeconds **   
The number of seconds to wait before retrying the operation.
HTTP Status Code: 429

 ** ValidationException **   
A structure defining a validation exception.    
 ** fieldList **   
A list of the fields in which the validation exception occurred.  
 ** message **   
An error message describing the validation exception.  
 ** reason **   
The reason why the validation exception occurred (one of `unknownOperation`, `cannotParse`, `fieldValidationFailed`, or `other`).
HTTP Status Code: 400

## See Also
<a name="API_elastic_ListClusters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/docdb-elastic-2022-11-28/ListClusters) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/docdb-elastic-2022-11-28/ListClusters) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-elastic-2022-11-28/ListClusters) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/docdb-elastic-2022-11-28/ListClusters) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-elastic-2022-11-28/ListClusters) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/docdb-elastic-2022-11-28/ListClusters) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/docdb-elastic-2022-11-28/ListClusters) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/docdb-elastic-2022-11-28/ListClusters) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/docdb-elastic-2022-11-28/ListClusters) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-elastic-2022-11-28/ListClusters) 